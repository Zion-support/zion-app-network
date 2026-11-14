import atexit, base64, json, os, subprocess, tempfile

REPOS = {
    "zion-governance-evidence-pack": "Copy-ready evidence packs (AI readiness, compliance, audit) assembled from the Governance, Risk & Compliance suite. Part of the Zion AI App Network.",
    "zion-ai-risk-evaluator": "Consolidated AI risk scoring matrix (safety, governance, readiness, compliance) for board-level review. Part of the Zion AI App Network.",
}

def put_contents(owner, repo, path, message, content, branch="main"):
    b64 = base64.b64encode(content.encode()).decode()
    body = {"message": message, "content": b64, "branch": branch}
    fd, p = tempfile.mkstemp(suffix=".json")
    os.write(fd, json.dumps(body).encode()); os.close(fd)
    atexit.register(os.remove, p)
    cmd = ["gh", "api", "-X", "PUT", f"/repos/{owner}/{repo}/contents/{path}", "--input", p]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("CMD:", " ".join(cmd)); print("ERR:", r.stderr); raise SystemExit(1)
    return json.loads(r.stdout)

for name in REPOS:
    readme = (
        "# " + name + "\n\n"
        "Part of the [Zion AI App Network](https://ziontechgroup.com/zion-app-network/).\n\n"
        "- [Network hub](https://ziontechgroup.com/zion-app-network/)\n"
        "- [Free AI Discovery](https://ziontechgroup.com/discovery/)\n"
    )
    fh = put_contents("Zion-support", name, "README.md", f"Add README for {name}", readme)
    print(f"{name}: README uploaded ({fh.get('commit', {}).get('sha', '?')})")
print("done")
