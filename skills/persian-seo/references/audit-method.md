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

## Local services, brands and seasonal intent

Record country/service area separately from Persian language. Build intent hypotheses from actual query/support data: service + city/area, formal and colloquial phrasing, Persian/Latin brand names or transliterations. Preserve spelling in source evidence; combine only semantically equivalent variants. No data means no volume estimate or claim of preferred spelling.

For a city landing page require real service availability and decision-useful local facts such as covered areas, applicable offer/fees, operational contact and booking conditions. A headquarters address is not proof of branches or coverage in every city. Prefer one accurate coverage page over fabricated addresses or city-name swaps; regional pages need distinct utility. This applies [Google doorway and scaled-content policies](https://developers.google.com/search/docs/essentials/spam-policies), read 2026-10-03, rather than a Persian-specific ranking formula.

Check current regional/product eligibility before recommending local-business/search features; Persian content alone does not establish availability of a platform feature. Mark this check unresolved without current official feature guidance.

For Nowruz, school/calendar or weather-linked queries, distinguish date/season hypotheses from actual search evidence. Validate calendar/year, target geography, dated offer and service cutoffs; compare relevant seasonal windows rather than claiming holiday uplift from one spike. Updating a year in a title must accompany actually updated content. For prices, availability and delivery statements, record who maintains the information and when it was checked. Do not invent deadlines, discounts, review counts or city operations for SEO.

## Iranian commerce and local-page checks

- **Price consistency:** compare visible price/unit, final-cost qualifications and machine-readable offers. Under the conventional example contract, a visible 250,000 toman corresponds to 2,500,000 rial. If emitting IRR structured data, use the converted rial value; never pair 250,000 with IRR merely because the label says toman. Do not use a gateway's IRT token as an assumed ISO currency code. Validate the actual supported schema, offer eligibility and current engine requirements; markup is not an eligibility/ranking guarantee. [Google product snippet guidance](https://developers.google.com/search/docs/appearance/structured-data/product-snippet), read 2026-10-03, requires supported currency/value semantics.
- **Persian queries:** research relevant spelling, ی/ک, half-space, colloquial versus formal wording, price units and city/neighborhood variants using actual query evidence. Preserve original evidence and group by intent. Do not create near-identical URLs for each spelling or claim local search volume without data.
- **Local service pages:** show only real coverage, contact route, request process, available shipping/visit options and useful local differences. A city name in a footer does not prove an office/service there; do not invent map listings, locations, reviews or opening hours. Test address-dependent serviceability where access allows; otherwise label it unverified.
- **Commerce facts:** align delivery cost, payment methods, installment eligibility, return terms and seller support with current owner/provider facts. A famous merchant's policy is not a template for every Iranian business. Avoid marking synthetic prices/reviews as live offers.
- **Calendar/season:** when an Iranian calendar is selected, make campaign year, cutoff date, timezone and holiday support clear to readers while retaining the machine-readable format required by the schema. Do not put localized Jalali numerals into an ISO date field. Confirm dates with a maintained library and owner schedule; no automatic assumptions about weekends or holiday demand.
- **Mobile/accessibility:** ensure crawled/rendered useful content and contact/recovery instructions remain available when permitted resources are slow or scripts fail. Check RTL, mixed identifiers and input labels as actual page evidence; source-only checks cannot establish SMS, backend or screen-reader behavior.

Synthetic offer: visible «۲۵۰٬۰۰۰ تومان», eligible IRR offer value 2500000. Shipping remains separately disclosed according to its actual terms. Compare structured data with visible content after conversion, not by comparing raw numbers with different units. Real search-result eligibility remains unverified without the appropriate engine evidence.
