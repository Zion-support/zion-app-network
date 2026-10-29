# Approved public alias observer

Owner/review contact: Zion-support (Kleber). Observation only: no auto-fix,
DNS changes, deployment, issues, emails, forms, POST requests or new credentials.
`approved-roots.json` is the explicit reviewable target inventory and documents
canonical destinations. Do not turn it into a crawler or accept arbitrary URLs
from workflow inputs. Only root GET/HEAD routes are covered; other paths and app
functionality are outside this guarantee.

## Run and interpret

```
python3 -m unittest discover -s scripts -p 'test_observe_aliases.py' -v
python3 scripts/observe_aliases.py
```

Python standard library plus system curl; no install required. Four workers,
three-second connection timeout, six-second request timeout, seven-second child
process watchdog, at most one retry for transient DNS/connection/timeout errors.
Strict system CA/hostname verification is mandatory. DNS resolution is tested
by curl (code 6 identifies resolution failure); this does not verify CNAME
ownership, authoritative zone contents or propagation from all regions.

Each alias gets GET and HEAD with and without a fixed non-sensitive synthetic
query (repeated keys and encoded space). Exactly one 302 to the declared canonical
URL is required for redirect aliases, then HTTP 200. Unexpected destinations are
reported without being fetched. Loops, downgrades, extra hops, wrong status and
query changes fail. tools requires direct HTTPS 200, but remains under known-issue
review. Reports retain only static URLs and status/error codes, never bodies,
cookies, credentials, IP addresses, arbitrary Locations or raw stderr.

Exit codes: 0 all healthy; 1 unexpected failure or overdue known issue; 2 known
failure or apparent recovery awaiting human review. Both 1 and 2 fail Actions.
Tools' known TLS failure must be reviewed by **2026-10-30 18:00 UTC**, a review
deadline rather than a promise of provider recovery. If it starts working, the
state becomes RECOVERY_REVIEW, never silently HEALTHY. Verify recovery and remove
the known_issue field in a reviewed change. Do not extend the deadline blindly.
JSON and Markdown are generated locally; Actions prints JSON and puts Markdown
in the run summary even when observation fails. A cancelled/timed-out run is
incomplete evidence, never healthy.

## Inventory and scheduling decision (2026-10-29)

Inspected all nine registered workflows in this public repository (eight YAML
workflows plus Pages), open PRs including #16, #17 and #18, and the main site's
registered workflow inventory. No CODEOWNERS file exists here; open PR authors
are Zion-support. No ownership or review assignment was changed.

- `scoped-release-qa.yml`: weekly multilingual content/source/link QA plus manual
  and release triggers. Its apex Discovery content checks are complementary;
  it does not assert these alias roots or exact query-preserving redirects.
- `workflow-supply-chain-guard.yml`: reusable security guard, left unchanged.
- Main site `public-tls-certificate-expiry.yml`: apex/www expiry checks twice weekly.
- Main site `public-site-smoke-check.yml`: daily apex page status checks.
- Main site `production-health-monitor.yml`: apex routes every six hours with
  issue writes; not reused because this observer must remain read-only.
- Main site `cert-monitor.yml`: weekly certificate job with issue/Telegram side
  effects and failure suppression. Do not copy those side effects here.

No existing workflows or main-site PRs are modified. This new workflow is
**manual only**. No recurring monitoring is active through this PR. After review,
merge and one validated default-branch run, propose either integrating this
contract into an existing read-only cadence or adding `17 */6 * * *` (UTC) here,
never both. Recheck overlap and owner workload then. GitHub scheduling can delay
runs and is not an uptime SLA. No workflow has been dispatched by this change.

## Cost and resource bounds

Verified repository API visibility: **public**, default branch main on 2026-10-29.
GitHub documents standard hosted runners as free for public repositories:
https://docs.github.com/en/actions/reference/runners/github-hosted-runners
The workflow uses standard `ubuntu-24.04`, not larger or self-hosted runners,
with six-minute timeout, one concurrent job, no dependency installation/cache,
and actions pinned to the same full SHAs as the existing secure workflow.
Proposed cadence would be four runs/day, at most 24 runner-minutes/day.

Storage is a separate shared account allowance; account storage headroom was
not established. Therefore artifact upload defaults **off**. JSON remains in
run logs and Markdown in the summary; no artifact/cache storage is added by
default. Optional report upload requires deliberate manual input, retains only
three days, and should be used only after checking storage allowance. No purchase
or billing-setting change is authorized or performed. See current billing terms:
https://docs.github.com/en/billing/concepts/product-billing/github-actions
Recheck pricing and visibility if this repository becomes private.
