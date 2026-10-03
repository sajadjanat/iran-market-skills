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
