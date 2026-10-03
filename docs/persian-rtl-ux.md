# Persian RTL UX

## When to use it

Audit or patch a Persian interface, especially mixed Persian/Latin text, inputs, responsive layout and locale choices. Give framework/platform, source or runtime access and any calendar/currency requirements.

## Request and synthetic example

```text
با $persian-rtl-ux فایل before.html را بررسی کن.
شناسهٔ سفارش و شمارهٔ تماس باید خوانا و قابل کپی بمانند.
بین ایراد قابل مشاهده در کد و رفتار تست‌نشده فرق بگذار.
```

The original [before page](../examples/rtl/before.html) has no semantic language/direction, uses physical spacing and leaves its visible label unassociated with the input. The [after page](../examples/rtl/after.html) demonstrates document semantics, identifier isolation, logical spacing and input label association.

| Change | Purpose |
|---|---|
| lang=fa, dir=rtl | Semantic Persian document boundary |
| bdi dir=ltr around order ID | Isolate identifier display without changing its value |
| label for / input id | Associate label and field |
| Logical spacing and wrapping | Adapt layout to direction and target widths |
| LTR phone input | Preserve useful entry/display direction for the fixture |

The demo is not connected to a backend. Open both pages in a browser and use the [test corpus](../skills/persian-rtl-ux/references/test-cases.md) to compare behavior. Actual verification results belong in [evaluation records](../evals/README.md); the example alone is not a runtime claim.

The 2026-10-03 [actual verification](../evals/results/review-2026-10-03.md) passed the demo checks at 390/1024 pixels in headless Edge, including labels, keyboard order, identifier preservation and overflow. [Mobile screenshot](../evals/results/browser-2026-10-03/after-390.png). Screen-reader speech, OS clipboard, native mobile keyboard and backend behavior remain untested.

## It is working if

Each finding has a location and input case; fixes preserve identifiers/values. The report names actual checks and remaining keyboard, clipboard, screen-reader or platform checks. Locale choices are explicit.

## Common limits

RTL does not choose a calendar, timezone or rial/toman display. Search normalization should not mutate source content. Source review cannot prove assistive-technology behavior. Native platforms require their own implementation guidance.

## Local form and state contracts

Test Latin, Persian and Arabic-Indic digits under each field contract; preserve leading zeroes. Choose language, region, calendar and timezone separately. The [RTL reference](../skills/persian-rtl-ux/references/rtl-localization.md) adds address eligibility, named timezone handling, font fallback and pending-payment states; the [corpus](../skills/persian-rtl-ux/references/test-cases.md) supplies synthetic cases. These additions have behavioral plan evaluations; they do not expand the previously measured demo runtime coverage.
