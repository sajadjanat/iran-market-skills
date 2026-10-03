# Persian RTL and localization references

Sources checked 2026-10-03. Recheck platform documentation when framework or OS behavior matters.

| Source | Use | Status or boundary |
|---|---|---|
| [W3C Arabic & Persian Layout Requirements](https://www.w3.org/TR/alreq/) | Script layout, direction, bidirectional text, shaping, punctuation, and numerals | W3C Group Draft Note, published 2025-10-02; work in progress, not an endorsed Recommendation |
| [W3C: Structural markup and right-to-left text](https://www.w3.org/International/questions/qa-html-dir) | Semantic direction in HTML and mixed-direction content | Check examples against current HTML and browser support |
| [Unicode CLDR: Persian](https://cldr.unicode.org/translation/language-specific/persian) | Persian locale characters, digits, separators, and date conventions | Locale data guidance; not a mandate for every product display decision |
| [Unicode Bidirectional Algorithm, UAX #9](https://www.unicode.org/reports/tr9/) | Formal handling of mixed-direction text | Use platform bidi support; do not manually reverse stored text |
| [Android localization](https://developer.android.com/guide/topics/resources/localization) | Android locale and resource implementation | Android-specific guidance; verify current APIs |
| [Apple Human Interface Guidelines: Right to Left](https://developer.apple.com/design/human-interface-guidelines/right-to-left) | Native Apple interface direction and mirroring | Apple-platform guidance; verify current recommendations |

## Review checklist

- Use semantic `lang` and `dir` values at the correct boundary; isolate embedded Latin text or identifiers when needed.
- Prefer logical CSS properties and direction-aware components. Mirror directional controls only when their meaning changes with reading direction.
- Test strings that mix Persian with Latin brand names, URLs, phone numbers, prices, parentheses, and punctuation.
- Check Persian `ی` and `ک` and the expected Persian digit set. Define separate handling for searchable text, numeric values, and copyable identifiers.
- Decide calendar, timezone, and currency presentation with the product owner. Do not infer these choices from RTL alone.
- Verify input, copy/paste, screen readers, keyboard navigation, validation, and responsive layouts in the actual target framework.
