#!/usr/bin/env python3
"""Read-only public alias contract checks. Python stdlib + strict curl; no secrets."""
import argparse
import concurrent.futures
import datetime as dt
import json
import subprocess
import time
from pathlib import Path
from urllib.parse import urljoin

QUERY = '?zion_monitor=public%20check&probe=1&probe=2'
REDIRECTS = {301, 302, 303, 307, 308}


def request(url, method):
    # -q disables user curl config. No cookies, proxy, credentials or automatic redirects.
    args = ['curl', '-q', '--silent', '--noproxy', '*', '--proto', '=https',
            '--connect-timeout', '3', '--max-time', '6', '--output', '/dev/null',
            '--write-out', '%{http_code}\n%{redirect_url}', '--user-agent', 'ZionPublicAliasObserver/1.0']
    if method == 'HEAD':
        args.append('--head')
    for attempt in range(2):
        try:
            result = subprocess.run(args + [url], capture_output=True, text=True, timeout=7)
        except subprocess.TimeoutExpired:
            result = None
        code = result.returncode if result else 28
        if code not in {6, 7, 28, 52, 56} or attempt:
            break
        time.sleep(0.25)
    if code:
        return {'error': 'dns' if code == 6 else 'tls' if code in {35, 51, 58, 60, 77, 83, 90, 91} else 'transport', 'curl_code': code}
    status, _, location = result.stdout.partition('\n')
    return {'status': int(status), 'location': location}


def probe(entry, method='GET', query='', fetch=request):
    current = entry['url'] + query
    expected = entry['canonical'] + query
    seen, chain = set(), []
    for hop in range(3):
        if current in seen:
            return {'error': 'redirect_loop', 'chain': chain}
        seen.add(current)
        response = fetch(current, method)
        # Never retain arbitrary Location, response body, cookies or server error text.
        chain.append({'step': hop, **{k: response[k] for k in ('status', 'error', 'curl_code') if k in response}})
        if response.get('error'):
            return {'error': response['error'], 'chain': chain}
        if response['status'] in REDIRECTS:
            target = urljoin(current, response.get('location', ''))
            if target in seen:
                return {'error': 'redirect_loop', 'chain': chain}
            if hop >= 1:
                return {'error': 'redirect_limit', 'chain': chain}
            if response['status'] != entry.get('redirect_status'):
                return {'error': 'redirect_status', 'chain': chain}
            if target != expected:
                return {'error': 'redirect_destination_or_query', 'chain': chain}
            current = target
        else:
            error = None if response['status'] == 200 and current == expected else 'status_or_destination'
            return {'error': error, 'chain': chain}
    return {'error': 'redirect_limit', 'chain': chain}


def classify(entry, result, now):
    issue = entry.get('known_issue')
    if not result['error']:
        return 'RECOVERY_REVIEW' if issue else 'HEALTHY'
    if issue and result['error'] == issue['error']:
        return 'KNOWN_FAILURE_OVERDUE' if now >= dt.datetime.fromisoformat(issue['review_by']) else 'KNOWN_FAILURE'
    return 'FAILURE'


def observe(entry):
    now = dt.datetime.now(dt.timezone.utc)
    checks = []
    for method in ('GET', 'HEAD'):
        for query in ('', QUERY):
            result = probe(entry, method, query)
            checks.append({'method': method, 'query_probe': bool(query), 'state': classify(entry, result, now), **result})
    return {'name': entry['name'], 'url': entry['url'], 'canonical': entry['canonical'], 'known_issue': entry.get('known_issue'), 'checks': checks}


def exit_code(rows):
    states = {c['state'] for row in rows for c in row['checks']}
    if states & {'FAILURE', 'KNOWN_FAILURE_OVERDUE'}:
        return 1
    return 2 if states & {'KNOWN_FAILURE', 'RECOVERY_REVIEW'} else 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default='alias-report')
    args = parser.parse_args()
    entries = json.loads((Path(__file__).resolve().parents[1] / 'monitoring/approved-roots.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(observe, entries))
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    code = exit_code(rows)
    payload = {'checked_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'exit_code': code, 'results': rows}
    (output / 'report.json').write_text(json.dumps(payload, indent=2) + '\n')
    lines = ['# Public alias observations', '', 'Transport and routing only; not proof of app functionality.', '', '| Alias | GET/HEAD and query checks | Review deadline |', '|---|---|---|']
    for row in rows:
        states = ', '.join(sorted({c['state'] for c in row['checks']}))
        lines.append(f"| {row['name']} | {states} | {(row['known_issue'] or {}).get('review_by', '—')} |")
    lines += ['', 'Exit 0: all healthy; 1: failure/overdue issue; 2: known failure or recovery requiring review.', 'Known failures are not healthy and deliberately fail the workflow.']
    markdown = '\n'.join(lines) + '\n'
    (output / 'report.md').write_text(markdown)
    print(markdown)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
