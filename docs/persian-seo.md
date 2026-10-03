# Persian SEO

## When to use it

Prioritize technical/content improvements for specific Persian pages and a named search engine. Supply URLs/artifacts and, when relevant, authorized Search Console exports.

## Request and synthetic example

```text
با $persian-seo این HTML ساختگی را فقط از روی کد بررسی کن.
دادهٔ HTTP یا Search Console نداریم؛ وضعیت ایندکس و ترافیک را حدس نزن.
```

The original [HTML fixture](../evals/fixtures/seo-page.html) has noindex and a self-canonical on an intended public landing.

| Finding | Evidence | Action | Limit |
|---|---|---|---|
| Publishing intent conflicts with noindex | Supplied meta directive | Confirm owner intent; adjust directive if authorized | Live headers and engine state unknown |
| Canonical does not cancel noindex | Both declarations present | Inspect actual directives and target | Declared canonical is not selected canonical |

This is an offline review, not proof of current index status. The [audit method](../skills/persian-seo/references/audit-method.md) explains evidence and prioritization.

## It is working if

Recommendations identify URLs and evidence, separate technical facts from demand hypotheses and name post-change checks. Persian query variants are handled by meaning, not invented volume. Measurement needs a real baseline.

## Common limits

Trends values are normalized relative signals and can contain low-volume noise. A Persian-only site does not need invented language variants. Unicode slugs are not inherently defective. Structured data and metadata do not guarantee rankings.

## Local and seasonal pages

A city page needs actual coverage and useful local facts; neither a city-name swap nor a fictional branch helps the user. The [audit method](../skills/persian-seo/references/audit-method.md) adds Persian/Latin brand intent, regional feature eligibility, offer freshness and comparable seasonal measurement.
