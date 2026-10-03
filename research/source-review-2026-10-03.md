# Primary-source review, 2026-10-03

Retrieval date: **2026-10-03**, Asia/Tehran. This is a source-access and claim-scope review, not a market dataset or a claim that every linked document was read. Source publication/update dates are recorded separately below. `Not observed` means no date was verified, not that the source is undated. Access errors describe this research environment only: they do not prove a site is unavailable to everyone, a URL is permanently dead, a source claim is false, or reuse is permitted.

## Scope and method

Opened the URLs in the four existing reference files using the research browser; inspected returned content/status for relevant claims. Also checked the informal orthography PDF cited by the older pilot note and a more specific Android RTL source. No AGENTS.md or CLAUDE.md was present in the repository at initial inspection. Followed the research skill's primary-source and single-note approach; this note is the background research artifact. No private properties, account data, or bulk datasets accessed.

## Market sources

| Source checked | Access result on retrieval date | Source date verified | Safe use and correction |
|---|---|---|---|
| [Statistical Center of Iran](https://www.amar.org.ir/) | Research browser fetch timed out; reported 400/timeout | Not observed | Keep as a starting point with access unverified. A directory URL cannot support a numerical claim; obtain the exact report/table, period and definitions before using figures. |
| [Central Bank of Iran](https://www.cbi.ir/) | Readable first-party homepage | Homepage has item-specific dates; no single publication date assigned here | Its navigation exposes publications, statistics, accounts and time-series resources. Cite a specific publication for macro figures; the homepage does not establish demand for a product. |
| [E-commerce development portal](https://ecommerce.gov.ir/fa) | Research browser returned 403 Forbidden | Not observed | Record access blocked in this environment. Do not describe the linked annual report as verified from this URL, substitute invented figures, or infer scraping permission. |

The earlier pilot note links an annual report hosted on ecomotive.ir. This review did not reopen or verify that mirrored PDF; its prior claims remain separately attributed to that earlier review. Publisher identity and file hosting identity should be recorded separately if a mirror is used. Prefer the exact official publication page when accessible.

## Persian writing

| Source checked | Access result | Source date verified | Safe use and correction |
|---|---|---|---|
| [Academy formal orthography PDF](https://apll.ir/wp-content/uploads/2023/07/Dastour-e-Khat-17.04.1402.pdf) | Fetch timed out; reported 400/timeout | Not observed; filename/upload path is not a verified publication date | Keep as candidate official reference, mark content verification pending. Do not claim the manual was read during this review. It cannot establish marketing tone. |
| [Academy informal orthography page](https://apll.ir/1403/02/26/%D9%86%D8%B3%D8%AE%DB%80-%D9%BE%DB%8C%D8%B4%D9%86%D9%87%D8%A7%D8%AF%DB%8C-%D8%AF%D8%B3%D8%AA%D9%88%D8%B1-%D8%AE%D8%B7-%D9%88-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A7%D9%85%D9%84%D8%A7%DB%8C%DB%8C-%D9%81/) | Tool returned internal error without readable document or specific HTTP status | Not observed; date-shaped URL is not verified page metadata | Existing label says proposed; retain that cautious label but mark current verification pending. Do not upgrade it to a binding or final standard. |
| [Academy informal PDF](https://apll.ir/wp-content/uploads/2024/05/dasture-gheyrerasmi-2.pdf) | Tool returned internal error without readable content or specific HTTP status | Not observed | Previously linked in pilot note; not independently verified here. |
| [Unicode CLDR Persian guidance](https://cldr.unicode.org/translation/language-specific/persian) | Readable content | Not observed | Supports Persian kaf U+06A9, ye U+06CC, digits U+06F0–U+06F9, decimal U+066B and grouping U+066C. Apply conventions to localized presentation; distinguish identifiers, numeric storage, search normalization and verbatim user content. Does not prescribe brand voice. |

Domain-restricted Academy searches returned no results in this tool. That is not evidence that the documents do not exist. Obtain an accessible official copy or owner-provided excerpt before making detailed manual-specific spelling claims.

## RTL and localization

| Source checked | Access result | Source version/date verified | Implication |
|---|---|---|---|
| [W3C ALReq](https://www.w3.org/TR/alreq/) | Readable content | **Group Draft Note, 2025-10-02** | Existing draft status/date is accurate. It is work in progress, not an endorsed W3C Recommendation. Covers Standard Arabic and Persian script layout; use implementation docs for framework behavior. |
| [W3C structural markup and RTL](https://www.w3.org/International/questions/qa-html-dir) | Readable content | Not observed | Supports semantic `dir` at document/changed boundaries, separate `lang`, and `dir=auto` for unknown direction. `auto` is first-strong-character inference with edge cases; test mixed strings rather than promising it solves every case. |
| [Unicode UAX #9](https://www.unicode.org/reports/tr9/) | Readable content | **Unicode 18.0.0, revision 52, 2026-09-01** | Text stays in logical memory order; bidi determines display. Use platform support rather than reversing stored strings. Runtime Unicode support may differ from latest specification. |
| [Android localization](https://developer.android.com/guide/topics/resources/localization) | Readable content | **Last updated 2026-09-22 UTC** | Good general resource/locale reference. |
| [Android language/culture and RTL support](https://developer.android.com/training/basics/supporting-devices/languages) | Readable content | Not recorded | Add as the more direct Android RTL implementation reference when relevant; verify target API/framework and test on device. |
| [Apple HIG RTL](https://developer.apple.com/design/human-interface-guidelines/right-to-left) | Title and JavaScript-required shell only; recommendation body unavailable | Not observed | URL is a usable candidate, but no specific mirroring rule was verified from it here. Mark body verification pending and open it in a normal browser before applying platform-specific claims. |

An attempted Apple documentation JSON fallback was also inaccessible in the research browser. No platform instructions were inferred from that failed request. The versioned CLDR date-chart URL in the older pilot note was not reopened in this review; use current runtime locale data and explicit product calendar/timezone choices instead of claiming all Persian products must share one display policy.

## Google SEO references

| Source checked | Access result | Source date verified | Implication |
|---|---|---|---|
| [Developer SEO guide](https://developers.google.com/search/docs/fundamentals/get-started-developers) | Readable content | **Last updated 2025-12-10 UTC** | Supports crawlable links, accessible textual content and inspection. No indexing/ranking guarantee. |
| [Helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Readable content | **Last updated 2026-10-01 UTC** | Supports original useful content, clear sourcing and honest authorship. Google says no preferred word count, and E-E-A-T is not itself a specific ranking factor. Avoid a keyword-density or fixed-word-count recipe. |
| [Multi-regional/multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites) | Readable content | **Last updated 2025-12-10 UTC** | Current path works. Apply only to actual language/region variants; use this path instead of the older advanced/crawling URL in the pilot note. |
| [Search Console overview](https://search.google.com/search-console/about) | Readable public overview | Not observed | Public product page does not expose a site's private performance data. Use authorized connection or owner-supplied exports. |
| [Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en) | Readable content | Not observed | Confirms sampled, normalized 0–100 relative interest, low-volume zeros and non-poll status. It also describes statistical noise and possible isolated low-volume spikes: do not treat them as proof of actual demand. Compare within a recorded query/window/geography; never convert index points into monthly search counts. |

The international localized-versions URL and RFC 9309 in the older pilot note were outside the four current reference lists and were not independently checked here. Existing references should not imply that all of the old pilot's links received fresh verification.

## Actionable maintenance changes

1. Replace blanket verification language with a dated access-status link to this note, especially for Academy, SCI, e-commerce portal and Apple. Distinguish a linked starting point from a read and verified source.
2. Keep a source record's `published_or_updated_at`, `retrieved_at`, and `access_status` separate. Figures also need report period, units, scope and metric definition. Store `unknown` where not observed.
3. Keep ALReq explicitly a 2025-10-02 Group Draft Note. Pin a version when reproducibility matters; a latest-version link can change after this review.
4. Add the specific Android RTL resource alongside general localization if supporting Android. Separate platform verification from web RTL guidance.
5. Add Trends noise/low-volume limitations to keyword-demand reporting. Preserve query/window/geography and distinguish observation from hypothesis.
6. Obtain readable official Academy sources before manual-specific rule claims; keep product voice decisions in the brief and validate them with the target audience.
7. Reopen changing documentation and report sources during actual execution. This review is not a permanent certification, nor permission to redistribute linked manuals or data.
