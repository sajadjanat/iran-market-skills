# Persian SEO audit method

## Evidence per finding

Record URL/artifact, capture date, access method (HTML, rendered browser, response headers or supplied export), exact observation, effect, severity, confidence, fix and post-change check. Label a blocked check separately from a confirmed failure.

| Check | Evidence needed | Common inference to avoid |
|---|---|---|
| Response / redirects | Actual response and redirect chain | Page screenshot proves HTTP 200 |
| Crawl / indexing directives | Robots file, meta/header directives as applicable | robots disallow is equivalent to noindex |
| Canonical | Declared absolute target and response/indexability | Declared target proves Google's selected canonical |
| Content / internal links | Source and rendered page where needed | JS content is always invisible or always indexed |
| Language variants | Actual alternate pages, reciprocal annotations | Every Persian page needs hreflang |
| Structured data | Supported feature, visible facts, valid schema values | Markup guarantees a rich result |
| Performance | Owner-supplied equivalent-window data | Public observation proves traffic declined |

## Persian intent and normalization

Keep query evidence verbatim. Group variants such as کفش/كفش and نیم‌فاصله/space only where meaning is equivalent; do not claim how Google normalizes a particular variant without evidence. Local search normalization is a product decision separate from search-engine ranking.

Review readable titles, clear descriptions and intent coverage. Avoid fixed keyword density and content length targets. Distinguish formal/conversational phrases by audience and observed query data. With no query data, label clusters hypotheses.

Persian Unicode slugs are not inherently defects. Inspect encoding, links, redirects and canonical consistency; URL changes need an authorized migration plan. Calendar/year and rial/toman labels must match the offer, not be inserted as speculative ranking tricks.

## Prioritization and measurement

Use impact/severity, confidence and effort with explicit reasons, not invented traffic forecasts. Fix confirmed crawl/indexability blockers before speculative editorial expansion when relevant. For content, name the actual information missing for the user's decision.

Set baseline, comparable post-change period, page/query set and confounders. Proposed windows are a plan until data exist. Record indexability checks separately from business conversion measurement.

### Synthetic example

Supplied HTML contains noindex and a self-canonical on a intended public product page. Static conclusion: conflicting publishing intent needs review; canonical does not cancel noindex. Unknown: live response headers, robots access and engine index state. Next step: confirm owner intent, inspect runtime directives, then verify the authorized change.
