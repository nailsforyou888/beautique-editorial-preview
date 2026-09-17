# Beautique Bar — Editorial Preview Report (static HTML)

**Date:** 2026-09-17  
**Path:** `/workspace/beautique-studio-audit/v2-preview/site/`  
**Brief:** `STEVEN-VISUAL-MOCKUP-BRIEF.md`  
**Status:** Static backup / fast path — **not** live production (`beautiquebar.com` untouched)

---

## 1. Preview URL

**TBD** — open files locally, or serve this folder (e.g. `python -m http.server` from `site/`) when a public preview URL is assigned.

Local entry: `index.html`

---

## 2–3. Screenshots

Desktop / mobile homepage screenshots: **not captured in this pass** (static file build only). Capture when preview URL is live.

---

## 4. What changed (vs live / prior direction)

- New **editorial** visual system: ivory/cream surfaces, espresso ink, champagne-bronze accents — no pink, no gold gradients.
- Homepage rebuilt to brief **exact section order** (hero → trust → 4 categories → experience → featured work → Yonge feature → reviews → Instagram → final CTA).
- Yonge location page rebuilt to brief **exact order** (hero → intro → experience → signature → gallery → reviews → pricing → visit/NAP → book CTA).
- Service sample: manicure-pedicure with category nav, professional copy, findable pricing (not spreadsheet).
- Homepage **Book** opens location sheet (Yonge vs Bridlewood Fresha); Yonge page **Book → Yonge Fresha only**.
- Mobile sticky **Call | Book**.
- Footer: builder / RapidWebLaunch branding **dropped**.
- No “over a decade” / tenure marketing claim.
- Bio Gel (not Bio Bel); Snug (not Smug) where refill naming appears.
- Dual location preserved (Yonge featured; Bridlewood linked, path lock `/locations/warden/` noted).

---

## 5. Fonts used

| Role | Family | Source |
|------|--------|--------|
| Display / headlines | **Cormorant Garamond** (400/500/600 + italic) | Google Fonts |
| UI / body / nav / buttons / pricing | **Inter** (400/500/600) | Google Fonts |

---

## 6. HEX palette

| Token | HEX | Use |
|-------|-----|-----|
| Ivory | `#FAF7F2` | Page background |
| Cream | `#F3EEE6` | Alternating sections |
| Off-white | `#FFFEFB` | Cards / panels |
| Beige | `#E8DFD4` | Soft fields / placeholder base |
| Taupe soft | `#C9BDB0` | Muted chrome on dark |
| Taupe | `#A89888` | Secondary muted |
| Line | `#E5DCD0` | Borders |
| Espresso | `#2C241C` | Primary ink, CTAs, header book |
| Espresso soft | `#4A4038` | Body text |
| Muted | `#6B6158` | Secondary copy |
| Champagne | `#B8976A` | Accent CTAs / brows |
| Champagne deep | `#9A7B52` | Hover / eyebrow |
| Star (reviews only) | `#C9A227` | Rating glyphs |

---

## 7. Retained vs replace images

| Asset | Status |
|-------|--------|
| All photography in this preview | **Placeholders** with exact text: `Replace with Beautique Bar professional photography` |
| Logo | Typographic BB mark + wordmark (no live SVG pulled) — swap for real `/logo.svg` later |
| Real BB interiors / nail / lash work | **Replace** placeholders before client-facing share |

---

## 8. Rewritten copy notes

- Shorter above-the-fold; avoided stacking “luxury / premium / exclusive / best”.
- Hero: “Careful hands. Quiet confidence.” — boutique-calm, not discount or flashy.
- Trust strip: walk-ins, book ahead, two studios — no invented awards/ratings.
- Reviews: labeled **Placeholder quote** until real Google quotes are inserted.
- Service page: professional mani/pedi description; SEO substance kept (classic/gel/spa, both locations).
- Pricing: “from $—” placeholders pointing to Fresha for live numbers.

---

## 9. Removed / reorganized sections

- Demoted / omitted from this home: large blog grid, long service-card walls, builder chrome.
- Instagram kept **secondary** (below reviews).
- Yonge is a destination feature on home; Bridlewood not erased (footer + sheet + locations stub).
- Stub-only: `services.html`, `pricing.html`, `gallery.html`, `about.html`, `locations/index.html`.

---

## 10. What must NOT change (and why)

| Lock | Why |
|------|-----|
| Live `beautiquebar.com` | Preview only — no production deploy |
| Yonge NAP: 3430 Yonge St, M4N 2M9 · 416-484-7788 · text 437-434-4884 | Accuracy / local SEO |
| Yonge hours Mon–Fri 10–8 · Sat 10–7 · Sun 10–6 | FAQ-locked |
| Yonge Fresha URL | Booking path |
| Bridlewood Fresha URL + path `/locations/warden/` | Path lock / dual-shop booking |
| No decade tenure claim | Brief + conversion audit |
| Dual locations exist | Must not erase Bridlewood |

---

## 11. Preview coverage

| Page | Path | Status |
|------|------|--------|
| Homepage | `site/index.html` | Full editorial |
| Yonge location | `site/locations/yonge/index.html` | Full editorial |
| Service (mani/pedi) | `site/nails/manicure-pedicure/index.html` | Full editorial |
| Shared CSS | `site/styles.css` | System |
| Stubs | services, pricing, gallery, about, locations | Minimal |

---

## File tree

```
site/
  index.html
  styles.css
  PREVIEW-REPORT.md
  services.html
  pricing.html
  gallery.html
  about.html
  locations/index.html
  locations/yonge/index.html
  nails/manicure-pedicure/index.html
```

## NAP / Fresha (wired)

- **Yonge book:** `https://www.fresha.com/a/beautique-bar-on-yonge-toronto-3430-yonge-street-e0fzhnga/booking?menu=true`
- **Bridlewood book:** `https://www.fresha.com/book-now/nails-for-you-m7weksrj/all-offer?share&pId=32159`
- **Yonge call:** `tel:+14164847788`
- **Yonge text:** `sms:+14374344884`
