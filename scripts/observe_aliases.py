#!/usr/bin/env python3
"""Read-only public alias contract checks. Python stdlib + strict curl; no secrets."""
import argparse
import concurrent.futures
import datetime as dt
import json
import subprocess
import time
from pathlib import Path
from urllib.parse import urljoin, urlsplit

QUERY = '?zion_monitor=public%20check&probe=1&probe=2'
REDIRECTS = {301, 302, 303, 307, 308}


PLANNED_PROBES = {(method, query) for method in ('GET', 'HEAD') for query in (False, True)}
MANIFEST = Path(__file__).resolve().parents[1] / 'monitoring/approved-roots.json'


def validate_inventory(entries):
    """Reject bad configuration before any request; never silently skip an entry."""
    if not isinstance(entries, list) or not entries:
        raise ValueError('Inventory must be a nonempty list')
    names, urls = set(), set()
    for entry in entries:
        if not isinstance(entry, dict) or not {'name', 'url', 'canonical'} <= entry.keys():
            raise ValueError('Missing required inventory fields')
        if entry.keys() - {'name', 'url', 'canonical', 'redirect_status', 'known_issue'}:
            raise ValueError('Unknown inventory field')
        name = entry['name']
        if not isinstance(name, str) or not name or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in name):
            raise ValueError('Invalid alias name')
        for key in ('url', 'canonical'):
            if not isinstance(entry[key], str):
                raise ValueError('URL must be a string')
            parsed = urlsplit(entry[key])
            if (parsed.scheme != 'https' or parsed.username or parsed.password or parsed.port
                    or parsed.query or parsed.fragment or not parsed.path.startswith('/')
                    or any(c.isspace() for c in entry[key])):
                raise ValueError('Only clean HTTPS URLs are allowed')
        if entry['url'] != f'https://{name}.ziontechgroup.com/':
            raise ValueError('Alias URL must match its approved root name')
        if name in names or entry['url'] in urls:
            raise ValueError('Duplicate inventory entry')
        names.add(name)
        urls.add(entry['url'])
        if entry['canonical'] == entry['url']:
            if 'redirect_status' in entry:
                raise ValueError('Direct root cannot declare a redirect')
        elif urlsplit(entry['canonical']).netloc != 'ziontechgroup.com' or entry.get('redirect_status') != 302:
            raise ValueError('Redirect requires canonical apex and status 302')
        if 'known_issue' in entry:
            issue = entry['known_issue']
            if (not isinstance(issue, dict) or set(issue) != {'error', 'review_by', 'reason'}
                    or issue['error'] != 'tls' or not isinstance(issue['reason'], str) or not issue['reason'].strip()
                    or not isinstance(issue['review_by'], str)):
                raise ValueError('Invalid known issue')
            deadline = dt.datetime.fromisoformat(issue['review_by'])
            if deadline.tzinfo is None or deadline.utcoffset() is None:
                raise ValueError('Review deadline needs timezone')
    return entries


def load_inventory():
    return validate_inventory(json.loads(MANIFEST.read_text()))


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


def exit_code(rows, entries=None):
    """Success requires the full configured inventory and every planned probe."""
    try:
        entries = load_inventory() if entries is None else validate_inventory(entries)
        if not isinstance(rows, list) or len(rows) != len(entries):
            return 1
        expected = {entry['name']: entry for entry in entries}
        seen, states = set(), set()
        for row in rows:
            entry = expected[row['name']]
            if row['name'] in seen or any(row.get(k) != entry.get(k) for k in ('url', 'canonical', 'known_issue')):
                return 1
            seen.add(row['name'])
            checks = row['checks']
            if not isinstance(checks, list) or len(checks) != len(PLANNED_PROBES):
                return 1
            probes = set()
            for check in checks:
                if type(check['query_probe']) is not bool:
                    return 1
                pair = (check['method'], check['query_probe'])
                if pair not in PLANNED_PROBES or pair in probes:
                    return 1
                probes.add(pair)
                if 'error' not in check or not isinstance(check['chain'], list) or not check['chain']:
                    return 1
                state = check['state']
                if state not in {'HEALTHY', 'KNOWN_FAILURE', 'RECOVERY_REVIEW', 'FAILURE', 'KNOWN_FAILURE_OVERDUE'}:
                    return 1
                if state == 'HEALTHY' and (check['error'] is not None or entry.get('known_issue') or check['chain'][-1].get('status') != 200):
                    return 1
                if state in {'KNOWN_FAILURE', 'KNOWN_FAILURE_OVERDUE', 'RECOVERY_REVIEW'} and not entry.get('known_issue'):
                    return 1
                states.add(state)
        if seen != set(expected) or states & {'FAILURE', 'KNOWN_FAILURE_OVERDUE'}:
            return 1
        return 2 if states & {'KNOWN_FAILURE', 'RECOVERY_REVIEW'} else 0
    except (KeyError, TypeError, ValueError, OSError):
        return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default='alias-report')
    args = parser.parse_args()
    try:
        entries = load_inventory()
    except (ValueError, TypeError, OSError):
        print('CONFIGURATION_FAILURE: invalid or unreadable inventory; no probes executed.')
        return 1
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(observe, entries))
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    code = exit_code(rows, entries)
    payload = {'checked_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'exit_code': code, 'results': rows}
    (output / 'report.json').write_text(json.dumps(payload, indent=2) + '\n')
    lines = ['# Public alias observations', '', 'Transport and routing only; not proof of app functionality.', '', '| Alias | GET/HEAD and query checks | Review deadline |', '|---|---|---|']
    for row in rows:
        states = ', '.join(sorted({c['state'] for c in row['checks']}))
        lines.append(f"| {row['name']} | {states} | {(row['known_issue'] or {}).get('review_by', '—')} |")
    lines += ['', 'Exit 0: complete coverage and all healthy; 1: failure/incomplete coverage/overdue issue; 2: known failure or recovery requiring review.', 'Known failures are not healthy and deliberately fail the workflow.']
    markdown = '\n'.join(lines) + '\n'
    (output / 'report.md').write_text(markdown)
    print(markdown)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
