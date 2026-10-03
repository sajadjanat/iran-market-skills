# Persian interface test corpus

Select cases relevant to the component. Record runtime/browser/device, viewport, input, expected behavior, actual result and verification method. These strings are synthetic fixtures, not user data.

| Case | Sample | Expected invariant |
|---|---|---|
| Mixed brand/model | گوشی Samsung Galaxy S24 (نسخهٔ 256GB) | Words, model and parentheses retain meaning |
| Phone | +98 912 000 0000 | Digit/sign order and copied value remain intact |
| Email | support@example.com | Latin order, editable input and copy/paste preserved |
| URL | https://example.com/product?id=42 | Delimiters and query order stay usable |
| Order identifier | سفارش AB-123/45 | Identifier remains intact within Persian prose |
| Amount | ۱٬۲۵۰٬۰۰۰ تومان | Explicit unit; numeric value unaffected by display formatting |
| Decimal | ۱۲٫۵ | Parser/display behavior matches specified locale |
| Letter variants | كي / کی | Search may normalize a separate key; original stored content remains intact |
| Half-space | می‌روم / میروم / می روم | Search policy can compare variants; names/free text stay verbatim |
| Untrusted user text | Alice گفت: (سلام) | Content is rendered safely and isolated appropriately |
| Long content | A long Persian title with SKU AB-123 | Wraps without hiding actions or changing identifier meaning |
| Date/time | A known supplied instant near midnight | Agreed timezone/calendar; machine value remains the same |

## Interaction checks

- At narrow/wide target widths, check overflow, truncation, action order and readable long content.
- Tab through interactive controls; inspect focus, label/error association and semantic DOM order. A visual RTL position alone does not dictate reversed tab order.
- Enter Persian and Latin digits in numeric fields where supported; check validation, editing, selection and copied values. Preserve leading zeroes on identifiers.
- Exercise screen-reader labels when a reader is available; otherwise label them statically reviewed and runtime untested.
- For bilingual products switch language and repeat affected cases.
- Capture failures before changes and rerun the same cases after. Mark a source-only review as source-only.

## Small web pattern

```html
<html lang="fa" dir="rtl">
  <p>سفارش <bdi dir="ltr">AB-123/45</bdi></p>
  <label for="phone">شمارهٔ تماس</label>
  <input id="phone" type="tel" dir="ltr" autocomplete="tel">
</html>
```

This pattern demonstrates boundaries; it is not a complete application or a tested guarantee for every browser. Keep the app's existing validation, security and locale contract.
