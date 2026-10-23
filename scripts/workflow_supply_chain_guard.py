#!/usr/bin/env python3
"""Dependency-free guard for pinned Actions and explicitly reviewed write scopes.

Scans step-level and reusable-job uses declarations. It skips shell block
scalars so fake uses: strings inside run: | do not produce false alarms.
"""
from pathlib import Path
import re
import sys

ROOT = Path('.github/workflows')
WRITE_ALLOWLIST = {
    'consolidate-communications.yml': {'contents'},
    'insurance-catalog-consistency.yml': {'contents'},
    'sync-finance-discovery-catalog.yml': {'contents'},
}
WRITE_SCOPES = {
    'actions', 'attestations', 'checks', 'contents', 'deployments', 'discussions',
    'id-token', 'issues', 'models', 'packages', 'pages', 'pull-requests',
    'repository-projects', 'security-events', 'statuses',
}
USES_RE = re.compile(r'^(?:-\s+)?uses\s*:\s*(.+?)\s*$')
PERM_RE = re.compile(r'^([a-z-]+)\s*:\s*[\'\"]?write[\'\"]?\s*$', re.I)
PIN_RE = re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_./-]+)?@[0-9a-fA-F]{40}$')
DOCKER_DIGEST_RE = re.compile(r'^docker://[^\s@]+@sha256:[0-9a-fA-F]{64}$')
BLOCK_RE = re.compile(r'^(?:-\s+)?[A-Za-z_-][\w-]*\s*:\s*[|>][-+]?\s*(?:#.*)?$')
WRITE_ALL_RE = re.compile(r'^permissions\s*:\s*[\'\"]?write-all[\'\"]?\s*$', re.I)
INLINE_PERMISSIONS_RE = re.compile(r'^permissions\s*:\s*\{(.*)\}\s*(?:#.*)?$', re.I)


def yaml_structure_lines(text):
    """Yield non-comment lines outside YAML literal/folded scalar bodies."""
    scalar_indent = None
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(' '))
        if scalar_indent is not None:
            if not stripped or indent > scalar_indent:
                continue
            scalar_indent = None
        if not stripped or stripped.startswith('#'):
            continue
        if BLOCK_RE.match(stripped):
            scalar_indent = indent
            continue
        yield number, stripped


def extract_reference(raw):
    # Separate a YAML comment without accidentally modifying a quoted SHA.
    return re.split(r'\s+#', raw.strip(), maxsplit=1)[0].strip().strip('\'\"')


def scan_workflows(root=ROOT, allowlist=WRITE_ALLOWLIST):
    errors = []
    paths = sorted(list(root.glob('*.yml')) + list(root.glob('*.yaml')))
    if not paths:
        return ['No workflow YAML files found; supply-chain audit cannot pass.']
    for path in paths:
        scopes = set()
        text = path.read_text(encoding='utf-8')
        for number, line in yaml_structure_lines(text):
            match = USES_RE.match(line)
            if match:
                ref = extract_reference(match.group(1))
                if not ref.startswith('./') and not PIN_RE.fullmatch(ref) and not DOCKER_DIGEST_RE.fullmatch(ref):
                    errors.append(f'{path}:{number}: external step/job action is not pinned to a full SHA/digest: {ref}')
            if WRITE_ALL_RE.fullmatch(line):
                errors.append(f'{path}:{number}: permissions write-all is forbidden')
            perm = PERM_RE.fullmatch(line)
            if perm and perm.group(1).lower() in WRITE_SCOPES:
                scopes.add(perm.group(1).lower())
            inline = INLINE_PERMISSIONS_RE.fullmatch(line)
            if inline:
                for scope in WRITE_SCOPES:
                    if re.search(r'(?<![\w-])' + re.escape(scope) + r'\s*:\s*[\'\"]?write[\'\"]?(?:\s*,|\s*$)', inline.group(1), re.I):
                        scopes.add(scope)
        expected = allowlist.get(path.name, set())
        for scope in sorted(scopes - expected):
            errors.append(f'{path}: {scope}: write is not in the reviewed allowlist')
        for scope in sorted(expected - scopes):
            errors.append(f'{path}: expected reviewed {scope}: write declaration is missing')
    return errors


def main():
    errors = scan_workflows()
    if errors:
        for problem in errors:
            print('ERROR: ' + problem)
        return 1
    print('Workflow supply-chain guard: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
