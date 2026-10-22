from pathlib import Path
import re
import sys

ROOT = Path(".github/workflows")
WRITE_ALLOWLIST = {
    "consolidate-communications.yml",
    "insurance-catalog-consistency.yml",
    "sync-finance-discovery-catalog.yml",
}
USE_RE = re.compile(r"^\s*-\s+uses:\s*([^#\s]+)")
PIN_RE = re.compile(r"^[^@]+@[0-9a-fA-F]{40}$")


def main() -> int:
    errors = []
    paths = sorted(ROOT.glob("*.yml")) + sorted(ROOT.glob("*.yaml"))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), 1):
            match = USE_RE.match(line)
            if not match:
                continue
            ref = match.group(1).strip()
            if ref.startswith("./"):
                continue
            if not PIN_RE.match(ref):
                errors.append(
                    f"{path}:{number}: external action is not pinned to a 40-char SHA: {ref}"
                )

        has_contents_write = bool(
            re.search(r"(?m)^\s{2}contents:\s*write\s*$", text)
        )
        if has_contents_write and path.name not in WRITE_ALLOWLIST:
            errors.append(f"{path}: contents write is not in the reviewed allowlist")
        if path.name in WRITE_ALLOWLIST and not has_contents_write:
            errors.append(f"{path}: expected reviewed contents write declaration is missing")

    if errors:
        for item in errors:
            print(f"ERROR: {item}")
        return 1

    print("Workflow supply-chain guard: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
