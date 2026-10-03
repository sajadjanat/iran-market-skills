# Task-based benchmark method

## Observation record

Capture product, source URL or artifact ID, observed date, device/viewport, version if known, task, observed steps, exact visible evidence, interpretation, confidence and implication. Record source conditions such as locale, account state and whether the page was static or interactive.

Convenience examples include [Digikala](https://www.digikala.com/), [Divar](https://divar.ir/), [Snapp](https://snapp.ir/), [Cafe Bazaar](https://cafebazaar.ir/) and [Myket](https://myket.ir/). These are candidate products, not a verified current comparison, ranking or representative sample. Open relevant flows during the task.

## Dimensions and judgments

| Dimension | Look for | What static artifacts cannot establish |
|---|---|---|
| Findability | Search, category labels, applied filters, empty states | Search relevance or recovery without interaction |
| Decision support | Offer detail, currency, comparison basis, eligibility | Actual stock, historical price or seller quality |
| Risk information | Published delivery, returns, payment and support terms | Fulfillment or conversion quality |
| Interaction | Input/error/loading states, keyboard, target width | Focus or assistive-technology behavior without testing |
| Voice | Clear labels and actions fitting the task | Audience preference without user evidence |

Use categorical descriptions when sufficient. If scoring is requested, define anchored criteria before assessing products and apply them consistently. Treat unobserved as missing, not zero; avoid a single overall score hiding incomparability. Even a tested task-completion count measures this sample, not market adoption.

## Report shape

| Product/state | Observation and artifact | Interpretation | Confidence/limit | Target-product action |
|---|---|---|---|---|

Each action must explain why it fits the target audience and what still needs testing. Keep public-product screenshots local unless reuse rights support publication.

### Synthetic example

Two fictional supplied mobile screens: A labels a price with no unit; B explicitly says تومان. Observation: B exposes the currency unit. Interpretation: B reduces this particular ambiguity. Limit: neither screenshot establishes checkout success, trust or conversion. Action: display explicit currency in the target product, then check comprehension in its actual flow.

## Local transaction and service conditions

For Iranian commerce/service tasks, include only dimensions relevant to the target flow:

| State | Capture | Target check |
|---|---|---|
| Service area | Selected city/address and shown eligibility | Distinguish unavailable area from generic error; preserve entered details |
| Offer/checkout | Amount, unit, tax/delivery/fee inclusion, seller and options | Compare full cost on the same basis; unsupported payment methods remain unknown |
| Gateway return | Visible pending/success/failed status and source of that status | Return URL or screenshot does not establish server-confirmed payment |
| Delivery/return | Published conditions, cutoff dates, exceptions and source freshness | Merchant policy is not evidence of actual fulfillment |
| Support/trust | Identity/contact, terms, badges and their inspectable destination | A badge's presence does not establish validity, user trust or delivery quality |
| Interrupted task | Loading, timeout, back navigation and retry if authorized | Check state preservation and duplicate-action prevention; never initiate a real payment for this audit |

Use the selected provider's official documentation for payment interpretation. [Zarinpal currency](https://www.zarinpal.com/docs/paymentGateway/moreFeatures/currency) documents IRR/IRT for its request API; [connection guide](https://www.zarinpal.com/docs/paymentGateway/connectToGateway) separates callback and verification. Read on 2026-10-03; no visible publication date. These are provider-specific, and request/verify unit wording must be reconciled against the actual integration rather than generalized.

Choose recovery or low-bandwidth tests because the brief, research or task risk warrants them, and record the simulated conditions. They do not prove that every Iranian user has unreliable connectivity. Observe whether the target segment understands city eligibility, total cost, a pending payment and the next recovery step; local brand popularity cannot answer those questions.
