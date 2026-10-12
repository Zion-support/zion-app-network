# Supplier workbench — runtime verification / verificação / verificación / vérification / Prüfung

[App network](https://ziontechgroup.com/zion-app-network/) · [Supplier coverage](https://ziontechgroup.com/zion-app-network/supplier-coverage.html) · [Coverage authority](TRANSLATIONS-STATUS.md)

This record preserves the existing published supplier release. It does not create another calculator, replace translated pages or duplicate homepage promotions.

## Verified editions

| Language | Local workbench | Review guidance | Homepage promotion |
|---|---|---|---|
| English | [Open](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.html) | [Review](https://ziontechgroup.com/apps/supplier-quote-review-guide.html) | [Homepage](https://ziontechgroup.com/en/#supplier-comparison) |
| Português brasileiro | [Abrir](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.pt-br.html) | [Revisão](https://ziontechgroup.com/apps/supplier-quote-review-guide.pt-br.html) | [Página inicial](https://ziontechgroup.com/#supplier-comparison) |
| Español | [Abrir](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.es.html) | [Revisión](https://ziontechgroup.com/apps/supplier-quote-review-guide.es.html) | [Inicio](https://ziontechgroup.com/es/#supplier-comparison) |
| Français | [Ouvrir](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.fr.html) | [Revue](https://ziontechgroup.com/apps/supplier-quote-review-guide.fr.html) | [Accueil](https://ziontechgroup.com/fr/#supplier-comparison) |
| Deutsch | [Öffnen](https://ziontechgroup.com/apps/supplier-quote-evidence-workbench.de.html) | [Prüfung](https://ziontechgroup.com/apps/supplier-quote-review-guide.de.html) | [Startseite](https://ziontechgroup.com/de/#supplier-comparison) |

## English — try the local example

Load the fictional example. Complete cost 130, 40% markup gives a selling price of 182 before client tax; illustrative 10% tax gives 18.20 and total 200.20. The margin is 28.57%, not 40%. Declarations reset and the report remains HOLD. Download the internal report, then edit a cost: the old download must be disabled until recalculation. A report and checked boxes do not authorize a purchase, reservation or dispatch.

## Português brasileiro — teste o exemplo local

Carregue o exemplo fictício. Custo completo 130, acréscimo de 40% gera preço 182 antes do imposto do cliente; imposto ilustrativo de 10% gera 18,20 e total 200,20. A margem é 28,57%, não 40%. As declarações são desmarcadas e o relatório permanece AGUARDAR. Baixe o relatório interno e altere um custo: o download anterior deve ficar desativado até recalcular. Relatório e caixas marcadas não autorizam compra, reserva nem mobilização.

## Español — pruebe el ejemplo local

Cargue el ejemplo ficticio. Coste completo 130, recargo del 40% produce precio 182 antes del impuesto del cliente; impuesto ilustrativo del 10% produce 18,20 y total 200,20. El margen es 28,57%, no 40%. Las declaraciones se desmarcan y el informe queda EN ESPERA. Descargue el informe interno y cambie un coste: la descarga anterior debe desactivarse hasta recalcular. El informe y las casillas marcadas no autorizan compra, reserva ni desplazamiento.

## Français — essayez l’exemple local

Chargez l’exemple fictif. Coût complet 130, majoration de 40% donne un prix de 182 avant taxe client ; taxe illustrative de 10% donne 18,20 et total 200,20. La marge est 28,57%, non 40%. Les déclarations sont décochées et le rapport reste EN ATTENTE. Téléchargez le rapport interne, puis modifiez un coût : le téléchargement précédent doit être désactivé jusqu’au recalcul. Le rapport et les cases cochées n’autorisent ni achat, ni réservation, ni intervention.

## Deutsch — lokales Beispiel prüfen

Laden Sie das fiktive Beispiel. Vollständige Kosten 130 und 40% Aufschlag ergeben einen Preis von 182 vor Kundensteuer; beispielhafte 10% Steuer ergeben 18,20 und insgesamt 200,20. Die Marge beträgt 28,57%, nicht 40%. Die Erklärungen werden zurückgesetzt; der Bericht bleibt ZURÜCKHALTEN. Laden Sie den internen Bericht herunter und ändern Sie einen Kostenwert: Der alte Download muss bis zur Neuberechnung deaktiviert bleiben. Bericht und Häkchen erteilen keine Kauf-, Reservierungs- oder Einsatzfreigabe.

## Engineering evidence and limits

- [Website guard commit](https://github.com/Zion-support/zion-support.github.io/commit/c9a62d56db90be65aec32d64add07535be01ff6c) changes exactly two test files; no page, runtime, recipient, price or workflow definition changes.
- [Runtime guard source](https://github.com/Zion-support/zion-support.github.io/blob/c9a62d56db90be65aec32d64add07535be01ff6c/scripts/test-supplier-evidence-runtime.cjs) supports offline artifact checks and GET-only `--live` checks.
- 255 assertions passed on five freshly downloaded page/script editions and offline fixtures. Coverage: arithmetic, localized validation/status/filenames, report/download equality, example declaration reset, two-supplier state, stale-download blocking, literal alias text, and validation recovery.
- Five mutation/metadata negative cases failed as expected. Eight existing arithmetic/privacy tests and the 15-page worked-comparison verifier passed, including 31 negative fixture cases. A separate 27-route check verified exact reciprocal blocks on 20 pages, five field guides, the stylesheet and supplier coverage index.
- Build chain: field-evidence quality renderer → supplier release renderer → supplier locale tests → new synchronous runtime guard. Errors prevent artifact publication. Existing workflow definitions and all previously published promotions are preserved.
- [Production verification run](https://github.com/Zion-support/zion-support.github.io/actions/runs/38190326648): consult this link for the current deployment result; this document does not infer success from dispatch acceptance.

Synthetic DOM checks are not visual/mobile/browser, native-language editorial, screen-reader or whole-network certification. No actual form submission, email, supplier booking, purchase or dispatch occurred. Inputs remain local; retain written client confirmation, applicable PO and separate Zion authorization before any commitment.
