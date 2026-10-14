# Batch 75 five-language catalog review — 14 October 2026

Status: DRAFT ONLY. No merge or deployment authorized/executed by this batch.

## Scope
Thirteen existing catalog resources now share one responsive card pattern and 65 localized descriptions (EN, pt-BR, ES, FR, DE). Names remain product names. Copy describes suggested review activities, not verified AI functionality. Underlying app pages/repositories have not been translated or functionality-certified by this change.

`index.html` replaces only the marker-bounded legacy Batch 75 section through `_includes/batch75_cards.html` and `_data/batch75_review.json`. Missing/nonunique markers preserve the prior output. Existing links remain available; no forms, recipient logic, homepage pipeline, workflows or commercial terms changed. Language anchors, per-card related-resource returns, localized homepage/Discovery links, wrapping cards and visible focus outlines are included. No new JavaScript or tracking.

## Live GET evidence
Browser navigation on 14 October 2026 returned HTTP 200 for eleven legacy app routes. `https://ziontechgroup.com/gdpr-dsar-autopilot/` and `https://ziontechgroup.com/legal-contract-analyzer/` returned HTTP 404; these legacy links are preserved and explicitly marked unavailable in every locale, with repository alternatives. Do not claim the missing routes are fixed or that HTTP 200 proves app functionality. Observations may age; repeat before release.

## Local tests
Python Liquid smoke renderer (include filenames quoted for compatibility; NOT full Jekyll): five locale sections, 65 cards, unique IDs, all original hrefs retained, internal fragment resolution, exact script/form preservation, two 404 warnings per locale, unrelated suffix preservation, and missing-marker fail-closed behavior: 9/9 PASS. Rendered fixture retained locally. Full GitHub Pages/Jekyll build, visual/mobile/assistive-tech and native-language editorial QA remain release gates.

## Release gates / continuity
Fresh base main `30084d38b56a837afe136f05423b02075a49f294`. Branch `review/batch75-five-language-grew-20261014`. Preserve concurrent hub PRs and website release hold. Require current-head build/provider checks, reviewer signoff and separate merge/deploy confirmation. No automatic trigger or CI weakening. Existing routes are live evidence; the new cards are NOT published yet.

Next: verify draft bytes and PR diff; investigate the two missing app routes in a separately scoped repair; recheck bounded coverage, then coordinate production release with the existing Website QA owner. Free Discovery dual-inbox receipt is not proven by GET checks.
