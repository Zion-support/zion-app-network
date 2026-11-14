import atexit, base64, json, os, subprocess, tempfile, time

OWNER = "Zion-support"
REPOS = {
    "zion-governance-evidence-pack": "Copy-ready evidence packs (AI readiness, compliance, audit) assembled from the Governance, Risk & Compliance suite. Part of the Zion AI App Network.",
    "zion-ai-risk-evaluator": "Consolidated AI risk scoring matrix (safety, governance, readiness, compliance) for board-level review. Part of the Zion AI App Network.",
}

def gh(method, path, body=None, body_file=None):
    cmd = ["gh", "api", "-X", method, f"/repos/{OWNER}/{path}"]
    if body_file:
        cmd += ["--input", body_file]
    elif body is not None:
        fd, path2 = tempfile.mkstemp(suffix=".json")
        os.write(fd, json.dumps(body).encode())
        os.close(fd)
        cmd += ["--input", path2]
        atexit.register(os.remove, path2)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("CMD:", " ".join(cmd))
        print("ERR:", r.stderr)
        raise SystemExit(1)
    return json.loads(r.stdout)

def raw_body(obj):
    fd, p = tempfile.mkstemp(suffix=".json")
    os.write(fd, json.dumps(obj).encode())
    os.close(fd)
    atexit.register(os.remove, p)
    return p

for name, desc in REPOS.items():
    # 1) create repo
    body = {"name": name, "description": desc, "private": "false", "auto_init": "true"}
    repo = gh("PUT", name, body_file=raw_body(body))
    default_branch = repo.get("default_branch", "main")
    print(f"created {repo['html_url']} (default branch: {default_branch})")
    time.sleep(1)

    # 2) upload README.md
    readme = "# " + name + "\n\nPart of the [Zion AI App Network](https://ziontechgroup.com/zion-app-network/).\n\n- [Network hub](https://ziontechgroup.com/zion-app-network/)\n- [Free AI Discovery](https://ziontechgroup.com/discovery/)\n"
    body = {"message": f"Add README for {name}", "content": base64.b64encode(readme.encode()).decode(), "branch": default_branch}
    fh = gh("PUT", f"{name}/contents/README.md", body_file=raw_body(body))
    print(f"  uploaded README.md ({fh.get('commit', {}).get('sha', '?')})")
    time.sleep(1)

print("done")
