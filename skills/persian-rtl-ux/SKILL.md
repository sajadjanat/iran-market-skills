---
name: persian-rtl-ux
description: Design, implement, or audit Persian-language web and mobile interfaces for right-to-left layout, bidirectional text, typography, numbers, dates, and locale behavior. Use for Persian UI reviews or localization work.
---

# Persian Rtl Ux

Use this skill when a product has Persian-language UI or mixed Persian and Latin content. Treat language direction, locale formatting, and product choices as related but distinct decisions.

## Workflow

1. Identify the platform, framework, supported languages, and whether the interface is Persian-only or multilingual. Check the existing locale and design-system conventions before proposing changes.
2. Set semantic language and direction at the correct document or component boundary. Prefer logical layout properties and the platform's bidirectional-text behavior over manually reversing content.
3. Review Persian characters, mixed-direction strings, punctuation, phone numbers, URLs, identifiers, currency, numeric input, date/time formatting, and copy/paste behavior. Preserve raw user input when normalizing a separate search or comparison value.
4. Make calendar, digit, currency, and timezone decisions explicit product requirements. Use Persian locale data where it fits; keep codes and identifiers legible and copyable.
5. Verify layouts at narrow and wide widths, keyboard use, screen-reader labels, and representative mixed-script examples. Use the platform's current official guidance when implementation details may have changed.

## Completion

Provide an actionable audit or patch with affected components, observed examples, and decisions requiring product input. Read [Persian RTL references](references/rtl-localization.md) for the standards and platform documentation, including each source's status.
