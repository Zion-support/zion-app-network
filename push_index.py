import base64, json, os, subprocess, tempfile

INDEX_TEMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — Zion AI App Network</title>
<link rel="canonical" href="https://ziontechgroup.com/{name}/">
<meta name="description" content="Part of the Zion AI App Network — the {short} suite. Explore {short}, governance, risk, and compliance tools at ziontechgroup.com/zion-app-network/.">
<link rel="alternate" hreflang="en" href="https://ziontechgroup.com/{name}/">
<link rel="alternate" hreflang="pt" href="https://ziontechgroup.com/{name}/">
<link rel="alternate" hreflang="es" href="https://ziontechgroup.com/{name}/">
<link rel="alternate" hreflang="fr" href="https://ziontechgroup.com/{name}/">
<link rel="alternate" hreflang="de" href="https://ziontechgroup.com/{name}/">
<link rel="alternate" hreflang="x-default" href="https://ziontechgroup.com/{name}/">
</head>
<body>
<header><a href="https://ziontechgroup.com/zion-app-network/">← Zion AI App Network</a></header>
<main>
<h1>{name}</h1>
<p>Part of the Zion AI App Network — the Governance, Risk &amp; Compliance (GRC) and AI Trust &amp; Safety suite. {desc}</p>
<p><a href="https://ziontechgroup.com/zion-app-network/app/network-governance-trust-2026.html">Explore the Governance &amp; AI Trust suite (5 languages) →</a></p>
</main>
<footer>© 2026 Zion Tech Group · <a href="https://ziontechgroup.com">ziontechgroup.com</a></footer>
</body>
</html>
"""

FILES = {
    "zion-governance-evidence-pack": {
        "name": "zion-governance-evidence-pack",
        "short": "Governance Evidence Pack",
        "desc": "This repository ships copy-ready evidence packs (AI readiness, compliance, audit) assembled from the Governance, Risk &amp; Compliance suite.",
    },
    "zion-ai-risk-evaluator": {
        "name": "zion-ai-risk-evaluator",
        "short": "AI Risk Evaluator",
        "desc": "This repository ships a consolidated AI risk scoring matrix (safety, governance, readiness, compliance) for board-level review.",
    },
}

def put(owner, repo, path, content, message, branch="main"):
    b64 = base64.b64encode(content.encode()).decode()
    body = {"message": message, "content": b64, "branch": branch}
    fd, p = tempfile.mkstemp(suffix=".json"); os.write(fd, json.dumps(body).encode()); os.close(fd)
    cmd = ["gh", "api", "-X", "PUT", "--input", p, f"/repos/{owner}/{repo}/contents/{path}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR", repo, r.stderr); raise SystemExit(1)
    d = json.loads(r.stdout)
    print(f"  {repo}/{path} -> {d.get('commit', {}).get('sha', '?')[:10]}")

for repo, meta in FILES.items():
    content = INDEX_TEMPL.format(**meta)
    put("Zion-support", repo, "index.html", content, f"Add index page for {repo}")
print("done")
