# Persian RTL reference

Access review: 2026-10-03, research browser. Verify the actual target framework/version when applying these sources.

| Source | Application | Review status and boundary |
|---|---|---|
| [W3C Arabic & Persian Layout Requirements](https://www.w3.org/TR/alreq/) | Script layout and shaping context | Read; Group Draft Note 2025-10-02, not a W3C Recommendation |
| [W3C structural markup and RTL](https://www.w3.org/International/questions/qa-html-dir) | Semantic HTML direction, boundaries and unknown-direction content | Read; lang and dir serve distinct purposes |
| [Unicode CLDR Persian](https://cldr.unicode.org/translation/language-specific/persian) | Persian letters, display digits and separators | Read; does not prescribe product calendar/currency choices |
| [Unicode UAX #9](https://www.unicode.org/reports/tr9/) | Logical text storage and bidi display | Read; revision 52, Unicode 18.0.0, 2026-09-01; runtime support may differ |
| [Android localization](https://developer.android.com/guide/topics/resources/localization) | Resources and locale handling | Read; platform-specific |
| [Android language and RTL support](https://developer.android.com/training/basics/supporting-devices/languages) | Direction-aware native layouts | Read; verify target APIs and test on device |
| [Apple HIG RTL](https://developer.apple.com/design/human-interface-guidelines/right-to-left) | Candidate native Apple guidance | Partial: JavaScript shell only; recommendation body unverified here |

## Web decisions

- Put `lang="fa"` and `dir="rtl"` at the Persian document boundary. A multilingual subtree can have its own language/direction. CSS direction alone does not replace semantic markup.
- Use logical properties such as margin-inline-start, padding-inline and text-align:start. Preserve logical DOM order so reading and keyboard order follow content meaning.
- Known LTR identifiers can use a direction-isolating element such as `<bdi dir="ltr">`. For unknown-direction user content, choose isolation/dir=auto suited to context and test first-strong-character edge cases.
- Keep phone/email/URL inputs usable and labels Persian. Decide input direction and parsed representation per field; Persian display digits are not a requirement to rewrite identifiers.
- Preserve explicit amount units. An IRR amount represents rial; a toman display requires explicit conversion and product agreement. Avoid formatting a toman value as IRR.
- Store timestamps as instants/appropriate domain values. Select display timezone/calendar deliberately; a Persian locale alone must not silently change a scheduling contract.
- Mirror reading-direction controls where meaning requires it. Review each icon; do not mirror brand marks or arbitrary images by blanket CSS transforms.

## Locale, form and transaction boundaries

Separate Persian language from regional behavior. Choose locale variants, numbering system and calendar with the product contract; CLDR is locale data, not a mandate that all Persian users share Iran's operating terms. For Tehran scheduling use the named zone Asia/Tehran when selected, with maintained runtime timezone data. [IANA Asia source](https://data.iana.org/time-zones/tzdb/asia), read 2026-10-03, records historical rule changes; adding a fixed offset is not a general timezone conversion algorithm.

For numeric entry, decide per field whether Latin 0123456789, Persian ۰۱۲۳۴۵۶۷۸۹ and Arabic-Indic ٠١٢٣٤٥٦٧٨٩ are accepted. When allowed, parse a separate canonical value at the field boundary. Keep leading zeroes for OTPs, phones, postal codes and identifiers; these are strings, not arithmetic numbers. Preserve free text, names, passwords and original evidence. A visual digit substitution is not validation.

For a phone field define accepted domestic/international forms and normalization with the backend; inputmode is a keyboard hint, not proof of validity. Permit editing/paste according to that contract. For an address choose fields based on fulfillment area and actual provider requirements; Iranian examples should not force +98 or an Iranian postal contract on other Persian locales.

Keep display amount, stored amount and gateway request unit explicit. [Zarinpal currency](https://www.zarinpal.com/docs/paymentGateway/moreFeatures/currency) and [connection guide](https://www.zarinpal.com/docs/paymentGateway/connectToGateway), read 2026-10-03, illustrate IRR/IRT requests and separate payment verification. IRT here is a provider API value, not a general ISO/schema currency code. Confirm the chosen API/SDK's request and verify contracts, especially where documentation labels differ; do not guess conversion or default units.

Map UI states to the backend's actual payment/order states: pending confirmation, confirmed, canceled/failed and unresolved. Preserve order/reference identifiers and use an existing safe status-check action before offering another payment. Callback arrival alone is not success. Report backend behavior unverified when unavailable; this UX skill does not authorize building or executing a new payment integration.

Test the selected fonts for Persian shaping, ی/ک, half-space, combining marks, digit legibility, line height and fallback under loading/zoom. Match typography to the existing brand and target readability; do not mandate one font or a universal point size.
