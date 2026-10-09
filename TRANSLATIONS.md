# Translation policy

Supported locales: en, pt-BR, es, fr, de; x-default points to English. Product names may remain unchanged; descriptions, navigation, CTAs and limitations must be translated.

Every translated static page must have its own canonical, reciprocal five-locale hreflang set and working language switcher. Hub convention: `app-network-batchNN-date[-pt|-es|-fr|-de].html`. Website conventions may differ; inspect the production renderer before changing routes.

The homepage repository publishes `public/**` plus artifact-only renderers. Root-level website HTML is not automatically published. The separate zion-app-network GitHub Pages repository serves its own pages.

## Single coverage authority

Use [TRANSLATIONS-STATUS.md](TRANSLATIONS-STATUS.md) for coverage evidence. This policy no longer contains a competing status table. Older status claims were inconsistent and are not proof of current publication. Distinguish source existence, HTTP publication, translated body, link validation and actual functionality. A 200 response alone is insufficient.

Full-network translation is NOT complete. Verify release-specific routes and continue the paginated repository/route inventory. Do not renumber colliding batches or infer a suite identity from a filename.
