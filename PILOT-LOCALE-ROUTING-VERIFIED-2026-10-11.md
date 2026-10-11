# Native Planner locale routing — live verification

Final readback: 11 October 2026, 16:51 UTC. This supersedes the deployment-pending snapshot in [the five-language release notes](PILOT-LOCALE-ROUTING-2026-10-11.md).

## Published and working within scope
- Website commit [0dee0f22](https://github.com/Zion-support/zion-support.github.io/commit/0dee0f22cd228731f680d41494ea3b644222a41c) changed four existing renderer/test files only.
- Independent read-only checks passed on 15 routes: five pilot guides, five canonical homepages and five native Planner interfaces. They check localized destinations, link lang/hreflang, single owned blocks, alternate metadata and non-alias native Planner pages.
- Fresh manifest at https://ziontechgroup.com/apps/pilot-tool-paths-publication.json showed `plannerRouting: locale-native-2026-10-11`, five Planner routes and `emailSubmitted: false` at 16:50:02 UTC.
- At 16:51:07 UTC the exact failed workflow command, `node scripts/render-discovery-pilot-backlinks.cjs --live`, passed independently using the committed entrypoint and repaired modules. That chain covers benefits/workflow backlinks, guide/homepage navigation, native destinations and localized guide bodies.
- The English guide's Portuguese summary keeps its Portuguese Planner link. Other English-resource disclosures, existing styles, forms, scripts, recipients, checkout links, runtime and workflows remain unchanged.

## CI caveat — do not claim all green
[Run 38156838964](https://github.com/Zion-support/zion-support.github.io/actions/runs/38156838964), job114521454044, is COMPLETED/FAILURE. The Pages publication step succeeded at16:49:13 UTC. Its immediate live pilot-backlink step failed at16:49:16 UTC with `Planner destination es`; the final field-guide consistency step was skipped. Later independent 15-route and full-chain checks passed. These observations are consistent with publication propagation timing but do not prove the cause. No workflow rerun, cancel, error suppression or second dispatch was performed.

The next CI improvement is a reviewed, bounded retry/backoff contract that still fails persistently wrong content. It is not implemented by this batch. Preserve the published repair rather than reverting working locale navigation merely to rewrite run history.

## Verification links
[English Planner](https://ziontechgroup.com/automation-pilot-planner/en/) · [Português](https://ziontechgroup.com/automation-pilot-planner/) · [Español](https://ziontechgroup.com/automation-pilot-planner/es/) · [Français](https://ziontechgroup.com/automation-pilot-planner/fr/) · [Deutsch](https://ziontechgroup.com/automation-pilot-planner/de/)

[English guide](https://ziontechgroup.com/apps/free-discovery-to-pilot-guide.html) · [Portuguese guide](https://ziontechgroup.com/pt/apps/free-discovery-to-pilot-guide.html) · [Spanish guide](https://ziontechgroup.com/es/apps/free-discovery-to-pilot-guide.html) · [French guide](https://ziontechgroup.com/fr/apps/free-discovery-to-pilot-guide.html) · [German guide](https://ziontechgroup.com/de/apps/free-discovery-to-pilot-guide.html)

HTTP and markup checks do not certify all app interactions, whole-network translations, accessibility, native-speaker quality or paired email delivery. Historical homepage and benefits/workflow Planner-anchor repairs remain a separate backlog.
