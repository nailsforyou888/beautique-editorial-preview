# Beautique Bar — Restore Pass (editorial preview)

**Date:** 2026-09-17 (America/Toronto)  
**Goal:** Keep previous visual design; apply new copy only. Undo visual redesign from refine pass `8aac6f9`.

**Policy:** PREVIOUS VISUAL = KEEP | NEW COPY = APPLY | NEW VISUAL REDESIGN = DO NOT APPLY

---

## Restored from commit `091382f`

| Asset | Action |
|-------|--------|
| `styles.css` | Fully restored from `091382f` — byte-identical; **no** `8aac6f9` CSS kept |
| `index.html` | Markup/classes restored from `091382f`, then copy-only text edits |
| `locations/yonge/index.html` | Same |
| `nails/manicure-pedicure/index.html` | Same |

**Not touched:** live production, stub pages (`about.html`, `gallery.html`, `pricing.html`, `services.html`, `locations/index.html`), logo/BB mark, section order, layout wrappers.

**Git:** Working tree left dirty for parent review — **no commit / no push** from this pass.

---

## CSS fully restored

- `diff` of working `styles.css` vs `git show 091382f:styles.css` → **identical**
- Removed all refine-pass visual changes, including:
  - `.photo-ph` companion rules
  - `.loc-name` / `.loc-place`
  - `.review-more` and restyled `.review-label`
  - padding / min-height / gradient tweaks from `8aac6f9`

---

## Copy-only edits applied

### Homepage (`index.html`)

- Hero → “Your beauty ritual, refined.” + thoughtfully-done lead; CTAs **Book Appointment** / **Explore Services**
- Signature → “What we do best”; dropped “Four pillars…”; **View All Services**; kept Nails / Pedicures / Lashes / Skin blurbs
- Experience → “Beauty, thoughtfully done.” + warm concrete lead + concise list (no “not overdone”)
- Featured work → heading **Recent work**; muted gallery line; **View Our Work**
- Yonge block → destination copy via existing `eyebrow` / `h2` / `muted` / `loc-details` (Beautique Bar · Yonge & York Mills · address/hours); CTAs **Book Yonge** / **Explore Yonge** / **Get Directions**
- Reviews → 3 first-name quotes (Sarah, Michelle, Jessica) · Google · stars; **Read Google Reviews**; no “Placeholder quote”
- Instagram → heading only (removed internal “Secondary feed…” note)
- Final CTA → “Book your appointment” / **Book Appointment**
- Photo cells → kept `091382f` `.ph` / `.ph-hero` / `.ph-tall` markup; removed inner “Replace with…” `<span>` text (empty tasteful blocks)

### Yonge (`locations/yonge/index.html`)

- Hero lead + **Book Appointment**; intro “Your chair on Yonge”; experience lead without “oversell”
- Signature “Popular here” + **Explore Services**; gallery **Recent work** + **View Our Work**
- Reviews → Amanda, Priya, Emily · Google · **Read Google Reviews**
- Pricing note + **View Pricing**; visit **Get Directions**; book **Book Appointment**
- Photo cells emptied the same way (`.ph` only)

### Service (`nails/manicure-pedicure/index.html`)

- CTAs → **Book Appointment** / **View Pricing** throughout
- Intro → clear manicure & pedicure copy; dropped “not a spreadsheet”
- Bio Gel desc shortened; Bridlewood card dropped visible “Path: /locations/warden/” note
- Photo cells emptied (`.ph` only)

---

## Confirmation: no redesign classes kept

Verified absent from HTML + CSS:

- `.loc-name`
- `.loc-place`
- `.photo-ph`
- `.review-more`

Class set on pages matches `091382f` except intentional removal of unused `review-label` spans (were “Placeholder quote” labels only).

---

## Verification

```text
diff styles.css vs 091382f:styles.css  → identical
rg forbidden internal/old phrases      → no matches
rg loc-name|loc-place|photo-ph|review-more → no matches
```

**Success:** Previous visual mock restored; new copy applied; redesign CSS/classes not applied; `RESTORE-PASS.md` written; tree ready for parent push after review.
