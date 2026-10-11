# Field Guide → matching-language Pilot Planner

Implementation: [602a539](https://github.com/Zion-support/zion-support.github.io/commit/602a539a722f1664d81bde6be714102a0ffbcf95)

A prominent, translated primary action connects each Field Evidence Guide to the same-language Planner. Portuguese compatibility destinations remain; existing tools and guide-return links are preserved.

| Language | Field Guide | Planner |
|---|---|---|
| English | [Guide](https://ziontechgroup.com/apps/field-service-evidence-guide.html) | [Planner](https://ziontechgroup.com/automation-pilot-planner/en/) |
| Português | [Guia](https://ziontechgroup.com/apps/field-service-evidence-guide.pt-br.html) | [Planejador](https://ziontechgroup.com/automation-pilot-planner/) |
| Español | [Guía](https://ziontechgroup.com/apps/field-service-evidence-guide.es.html) | [Planificador](https://ziontechgroup.com/automation-pilot-planner/es/) |
| Français | [Guide](https://ziontechgroup.com/apps/field-service-evidence-guide.fr.html) | [Planificateur](https://ziontechgroup.com/automation-pilot-planner/fr/) |
| Deutsch | [Leitfaden](https://ziontechgroup.com/apps/field-service-evidence-guide.de.html) | [Planer](https://ziontechgroup.com/automation-pilot-planner/de/) |

Four localized guide aliases receive complete copies during the final artifact pass. Planner source links now identify [the multilingual artifact renderer](https://github.com/Zion-support/zion-support.github.io/blob/main/scripts/render-pilot-planner-locales.cjs), not the raw Portuguese reference file.

Offline tests passed two runs on all five current guide pages: head metadata, forms and scripts unchanged; exact matching primary language; single owned block; source correction; idempotence. Production status is recorded separately in the [CEO Release Board](https://app.notion.com/p/3f4b94b0eaf7819fbb04ed6612856bc3). Do not infer publication from a Git commit alone.

Planning only, browser-local: no email, booking, order, system execution or guaranteed savings. This is a nine-guide navigation increment, not a full-network localization claim.

[App network](https://ziontechgroup.com/zion-app-network/) · [Planner language directory](https://ziontechgroup.com/zion-app-network/pilot-planner-languages.html) · [Homepage](https://ziontechgroup.com/)
