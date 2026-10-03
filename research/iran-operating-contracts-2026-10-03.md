# Iranian operating-contract expansion — 2026-10-03

Scope: the five existing skill packages and the Sepehra page. No new skill, scheduled automation, legal-rule certification or marketplace release.

## Sources and actual access

| Source | What was checked | Limit |
|---|---|---|
| [Zarinpal currency](https://www.zarinpal.com/docs/paymentGateway/moreFeatures/currency) | Official page read; explicit provider IRR/IRT request semantics | API token is provider-specific; verify actual SDK/version and conversion boundary |
| [Zarinpal connection](https://www.zarinpal.com/docs/paymentGateway/connectToGateway) | Official page read; callback and subsequent verification documented | Request/verify unit labels need reconciliation with the chosen implementation; no live charge attempted |
| [ITU Iran index](https://www.itu.int/oth/T0202000066/en) | Index read; current attachment links listed | Attachment body not read; no new operator-prefix allocation claims |
| [Unicode Persian](https://cldr.unicode.org/translation/language-specific/persian) | Official locale guidance reopened | Does not choose audience, region, business calendar or payment contract |
| [IANA Asia data](https://data.iana.org/time-zones/tzdb/asia) | Official source reopened | Use maintained runtime data; no fixed-offset calendar implementation prescribed |
| [Google product snippets](https://developers.google.com/search/docs/appearance/structured-data/product-snippet) | Official structured-data guidance reopened | Eligibility/indexing/traffic not measured |
| [Google merchant listings](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) | Official guidance reopened | No claim that this project's fictional offers qualify |
| [Dona failed-payment help](https://help.doona.ai/hc/articles/68/rd-kht-n-mofk-mblgh-z-hs-bm-sr-shd-h-nm) | Merchant's 72-hour unsuccessful-payment and support guidance read | Merchant policy, not a nationwide or all-transaction legal deadline |
| [GNAF](https://gnaf.post.ir/) | Attempted direct access | Timeout; detailed postal format/address-validation rules not verified |

Earlier reviewed Torob, Digikala, Achareh and Khedmat Az Ma pages are category/context examples, not rankings, endorsements or customer-behavior evidence. Conventional example arithmetic (1 toman = 10 rial) is an explicitly supplied product contract; any unit migration/provider change requires rechecking the current implementation, not relabeling stored historical money.

## Change and verification boundaries

Each skill's existing task reference contains its own relevant operating checks; entrypoints route to them. All runtime links stay within the installed skill. Human docs carry a 16-topic coverage map. Original names, audience, source evidence and user scope are preserved.

Five new synthetic evaluation requests cover currency/state/phone/calendar/address/recovery and local search. They are not fresh-session model results. Prior evaluation outputs are historical and not rescored or presented as validation of this expansion. Browser, packaging and manual artifact checks are recorded separately from model quality.

## Actual checks

- Repository validator: pass, five self-contained packages, metadata/local links/resources/docs/cases.
- Existing nine unittest regression checks: all pass, including independent-copy links/license and reproducible safe ZIP contents.
- Original synthetic RTL demo: pass at 390/1024 in headless installed Edge 154.0.4258.53. Checks: labels/focus/tab order, mixed identifier, phone string/leading zero and overflow. Artifacts in ignored dist/verification/rtl/. OS clipboard, screen reader, native keyboard and backend remain unverified.
- New five model scenarios: not independently run; no new model-quality score. The expansion adds reference detail and routing, preserving the workflow and prior records.
