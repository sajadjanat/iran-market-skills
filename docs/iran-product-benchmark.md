# Iran product benchmark

## When to use it

Compare local products for one task and use the observations to choose target-product patterns. Supply products/artifacts, task, device and audience. Different categories may need substitutes rather than a false like-for-like ranking.

## Request and synthetic example

```text
با $iran-product-benchmark این دو صفحهٔ ساختگی موبایل را
برای انتخاب پیشنهاد خدمات مقایسه کن. فقط تصاویر/توصیف‌ها موجودند؛
ورود و پرداخت را مشاهده‌شده حساب نکن.
```

Using the original [screen descriptions](../evals/fixtures/benchmark-screens.json):

| Artifact | Observed | Inference | Unknown |
|---|---|---|---|
| Fictional A | Price has no unit | Currency meaning is ambiguous | Checkout behavior |
| Fictional B | Price explicitly says تومان | This ambiguity is reduced | Actual delivery/support quality |

Implication: explicit currency fits the target offer comparison. This does not establish conversion improvement or an overall product ranking.

## It is working if

Findings have date/conditions and artifact references, interpretations are separate, and recommendations explain target-task fit. Hidden states remain unobserved. Any score uses an explicit criterion and handles missing data.

## Common limits

A screenshot cannot establish keyboard behavior, checkout completion or fulfillment. Public examples are a convenience sample. Publish observation links and original examples; keep third-party screenshots local unless rights permit reuse.
