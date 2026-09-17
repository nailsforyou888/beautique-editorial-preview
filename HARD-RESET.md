# Hard reset vs 091382f (copy text only)

**Baseline visual:** commit `091382f` (same look as initial `3c86d7c`)
**Method:** `git checkout 091382f --` for index, yonge, mani/pedi, styles.css → then text-node replacements only.
**CSS diff vs 091382f:** 0 lines (identical)

## Structural/visual deltas remaining vs 091382f
None in classes, wrappers, or CSS. Only text content inside existing elements changed, plus:
- Photo `<span>` text emptied (tags kept) so “Replace with…” is not customer-facing
- Review label text “Placeholder quote” → “Google” (same `review-label` class)

## Copy applied (text only)
- Hero → Your beauty ritual, refined. / thoughtfully done…
- Removed Four pillars line
- Experience → Beauty, thoughtfully done.
- Featured → Recent work; cleaned placeholder language
- CTAs → Book Appointment, Explore Services, View All Services, View Our Work, Read Google Reviews
- Yonge/service pages: removed oversell / spreadsheet language; Book Appointment

## If it still “looks wrong”
Likely causes to confirm with Steven (not CSS drift):
1. Empty photo placeholders vs remembered filled images
2. Browser cache of an older Pages build
3. A specific section (hero / signature cards / yonge block / reviews)
