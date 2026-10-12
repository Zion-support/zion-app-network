# Supplier keyboard navigation — 12 October 2026

Release: `supplier-keyboard-2026-10-12-v1`.

## Status

Website code is committed as [7586816](https://github.com/Zion-support/zion-support.github.io/commit/7586816495d22696320ffaa466fded372f4b6920). [Static deployment 38190447029](https://github.com/Zion-support/zion-support.github.io/actions/runs/38190447029) was dispatched; deployment and live keyboard verification are pending at this record's creation. This is not yet a LIVE certification.

Exactly three website scripts changed: new `render-supplier-keyboard.cjs`, new `test-supplier-keyboard.cjs`, and a narrow final extension to `render-supplier-release.cjs`. Existing production hook: `render-field-evidence-quality.cjs` → `render-supplier-release.cjs`. No workflow, homepage source, calculator form, runtime, price, recipient or delivery-code modification.

## Scope and checks

The generated workbenches receive two translated skip links, focusable calculator/report targets and keyboard/confidential-report guidance. The five locale editions share the same structure. Original calculator forms/scripts and canonical/alternate links are preserved. No new AI capability, upload, storage, order, booking or dispatch is added.

97 structural, idempotence, preservation and fail-closed checks passed against production fixtures and after the existing wrapper. Tests copy only the five fixture pages. The wrapper and subsequent supplier-pilot/comparison passes preserved all five additions. Immutable committed blob hashes matched the locally tested files. Original eight arithmetic/privacy tests and 50 checks against downloaded runtime scripts had passed in the prior continuation; they are not substitutes for real keyboard testing.

## Verify the five locale editions

- [English: keyboard guidance](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.html#supplier-keyboard-help)
- [Português: orientação de teclado](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.pt-br.html#supplier-keyboard-help)
- [Español: navegación con teclado](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.es.html#supplier-keyboard-help)
- [Français: navigation au clavier](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.fr.html#supplier-keyboard-help)
- [Deutsch: Tastaturnavigation](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.de.html#supplier-keyboard-help)

[Publication manifest](https://ziontechgroup.com/apps/supplier-keyboard-publication.json) · [Existing five-language supplier/field/pilot coverage](https://ziontechgroup.com/zion-app-network/supplier-coverage.html) · [Master app network](https://ziontechgroup.com/zion-app-network/) · [Homepage](https://ziontechgroup.com/) · [Canonical historical translation coverage](TRANSLATIONS-STATUS.md).

## Release gates

Require completed/success deployment, fresh HTTP200 and exact translated help/navigation markers, unchanged calculator forms/scripts, and real Tab/activation checks before marking publication complete. Native editorial review, full screen-reader/Safari/accessibility certification and whole-network translations/interlinks remain unfinished. No actual external form submission, email, purchase or supplier commitment is included.
