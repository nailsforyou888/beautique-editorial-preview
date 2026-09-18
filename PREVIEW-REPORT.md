# Beautique Bar — Fora-dark preview report

**Date:** 2026-09-18 (polish pass)  
**Repo:** https://github.com/nailsforyou888/beautique-editorial-preview  
**Status:** Static GitHub Pages preview only — **not** live production (`beautiquebar.com` untouched)

---

## 1. Live Pages URL

**https://nailsforyou888.github.io/beautique-editorial-preview/**

After this branch merges to `main`, Pages (source: `main` / root) will serve the Fora-dark homepage.

Relative asset paths from each HTML file (`styles.css`, `../../styles.css`) — no `<base>` tag, so the project site path `/beautique-editorial-preview/` keeps working.

---

## 2. HEX palette (from fora.so audit)

| Token | HEX | Use |
|-------|-----|-----|
| Page root | `#000912` | `html` / alternating sections |
| Section black | `#000000` | Major content bands |
| Warm ivory | `#FFF3F0` | H1, key labels |
| White | `#FFFFFF` | H2 / primary body |
| Text 80% | `#FFFFFFCC` | Supporting copy, nav |
| Text 65% | `#FFFFFFA6` | Meta / small labels |
| Line 10% | `#FFFFFF1A` | Quiet borders |
| Line 25% | `#FFFFFF40` | Stronger edges |
| Card | `#0F0F0F` @ 85% | Translucent surfaces |
| Card raised | `#171717` @ 85% | Showcase / sheet |
| Card active | `#262626` @ 85% | Hover / raised |
| Primary CTA fill | `#FFFFFFCC` | Pill buttons, dark text |
| Secondary pill | `#FFFFFF1A` | Ghost pills |
| Hero wash | `#1B2228 → #353F44 → #D39794` | Radial hero / closing CTA |

No teal product accent, no Fora logo, no SaaS pricing tiers.

---

## 3. Fonts

| Role | Family | Source |
|------|--------|--------|
| Body / nav / UI | **Inter** variable (`opsz` 14–32, weight 100–900) | Google Fonts |
| Display / H1 / H3 | **Inter Display** name in the stack; optical size of variable Inter at large `opsz` | Google Fonts Inter (Display as a separate family is not always listed; optical sizing is the fallback) |

H1: clamp 44–64px / ~1.18, weight 400, letter-spacing −0.042em (Fora-scale display).  
H2: ~40 / 1.28, weight 500, letter-spacing −0.04em.  
Hero lead / body: 14 / 21, max ~42ch.  
Eyebrow / kickers: 12–13px, #FFFFFFA6.

---

## 4a. Polish pass (2026-09-18) — vs first Fora-dark draft

Steven QA: first dark preview still read as a placeholder template, not the same family as fora.so. This pass targets the ranked gaps:

| Gap | What changed |
|-----|----------------|
| 1. Hero visual | Removed “Replace with…” labels and soft blobs. Composed stage: `art/horizon.svg` desert/rose landscape + glass booking chrome overlay |
| 2. Hero atmosphere | Full-bleed `#1B2228 → #353F44 → #D39794` radial **behind the headline**, plus grain. Not a flat `#000912` field |
| 3. Type | Larger display H1, tighter lead (42ch), quieter eyebrow, H2 vs body contrast |
| 4. Nav + CTAs | Filled ivory mark (not outlined B), 32px nav link gaps, 48px primary / 36px nav pills, shared hover language |
| 5. Cards + density | Tonal `#0F0F0F` surfaces with inner highlight, tighter padding, locations fade out of the hero charcoal instead of a hard navy/black band |
| Services / quotes | Same horizon art (hue-shifted per tab) + caption bar; quote cards share the card surface |
| Preview badge | Quiet 10px, 28% white, no pill chrome |

Photography is still original SVG art (no Unsplash, no stock). Swap `art/horizon.svg` for real BB photography later.

---

## 4. What changed vs the prior editorial preview

| Prior (ivory / editorial) | This pass (Fora-dark) |
|---------------------------|------------------------|
| Ivory `#FAF7F2`, cream, espresso, champagne bronze | Near-black canvas, warm ivory type, translucent charcoal cards |
| Cormorant Garamond display + Inter UI | Inter + Inter Display optical sizing only |
| Sharp 2px buttons, uppercase tracking | Full pills, 14px labels, quiet hover |
| Sticky ivory header | Sticky **transparent** nav (blur only after scroll) |
| Hero split + photo placeholder | Centered cinematic hero + rose–charcoal radial + booking-feel panel |
| Trust strip, experience, featured work, Instagram grid | Removed from homepage (not in this brief) |
| Category **grid** of four services | **Tabbed** Nails / Pedicures / Lashes / Skin showcase |
| Placeholder ★★★★★ review cards | **Live homepage quotes only** — no star counts |
| Yonge featured; Bridlewood stub-only | Dual location Book strip + full `/locations/warden/` page |
| Global Book → chooser only | Dual Fresha CTAs on hero, strip, closing CTA; nav Book still opens chooser |
| Editorial section order from Steven v2 brief | Brief order: nav → hero → dual Book strip → tabs → quotes → closing CTA → footer |

Production `beautiquebar.com` was not edited. GTM was not added on this preview.

---

## 5. Pages shipped

| Page | Path | Notes |
|------|------|--------|
| Homepage | `index.html` | Full Fora-dark landing |
| Shared CSS / JS | `styles.css`, `script.js` | Mobile-first + 1080px column |
| Yonge | `locations/yonge/index.html` | NAP + Yonge Fresha only |
| Bridlewood (path lock) | `locations/warden/index.html` | Labeled Beautique / Bridlewood — **not** Nails For You |
| Locations chooser | `locations/index.html` | Dual cards |
| Continuity stubs | `services.html`, `about.html`, `gallery.html`, `pricing.html`, `privacy.html`, `terms.html`, `nails/manicure-pedicure/index.html` | Dark chrome so old links do not fall back to ivory |

---

## 6. Booking CTAs (exact)

- **Yonge:** `https://www.fresha.com/a/beautique-bar-on-yonge-toronto-3430-yonge-street-e0fzhnga/booking?menu=true`
- **Bridlewood:** `https://www.fresha.com/book-now/nails-for-you-m7weksrj/all-offer?share&pId=32159`  
  UI label: **Beautique at Bridlewood Mall** / **Book Bridlewood**

---

## 7. Photography

Original SVG landscape (`art/horizon.svg`) — dusk dunes / rose bloom, used as the hero stage and hue-shifted in the service showcase. No Unsplash, no hotlinked stock, no “replace with photography” labels on the page. Real Beautique photography can replace the SVG later without changing layout.

---

## 8. Open decisions

| Item | Status |
|------|--------|
| **Bridlewood hours** | Unknown — page says call 647-770-5232 |
| **Bridlewood Fresha canonical** | Preview uses live `book-now/nails-for-you-…pId=32159`; FAQ alternate `a/nails-for-you-beautique-bar-…` not used |
| **Yonge postal `M4N 2M9`** | Shown (documented); missing from some live homepage schema |
| **Yonge hours** | Shown as FAQ-documented Mon–Fri 10–8 / Sat 10–7 / Sun 10–6 — confirm with Steven before production |
| **Per-shop Google review URLs** | Generic Google search until GBP links are supplied |
| **Hero photography** | SVG horizon is art-directed for this preview; replace with BB photos when available |
| **Licence / decade brand claims** | Omitted. Client quote from Sangeetha J about *her* two decades of visits is reused as-is from the live homepage |
| **`/locations/bridlewood/`** | Still a broken alias on live — not used here |
| **Pages serve from `main`** | Merge this PR so the public preview URL updates |

---

## 9. Copy hygiene

- No invented metrics, awards, or star averages
- No “over a decade” brand tenure line
- Bio Gel spelling preserved
- Title/meta keep existing live “top-rated” language only
- Quotes: Reem Abdali, Victoria Huang, Sangeetha J, Samantha C, Marcus Duncan, Mariam Clarke, Valerie, Jessica Cimino

---

## 10. URL locks preserved

`/` · `/locations/` · `/locations/yonge/` · `/locations/warden/`

Public name **Bridlewood**; folder stays **`warden`**.
