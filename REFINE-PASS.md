# Beautique Bar — Refine Pass (editorial preview)

**Date:** 2026-09-17 (America/Toronto)  
**Scope:** In-place refine only — `index.html`, `locations/yonge/index.html`, `nails/manicure-pedicure/index.html`, `styles.css` (spacing/type/placeholder polish).  
**Not touched:** live beautiquebar.com, new pages, stub pages (`about.html`, `gallery.html`, `pricing.html`, `services.html`, `locations/index.html`).

---

## Copy changes (before → after)

### Homepage (`index.html`)

| Area | Before | After |
|------|--------|-------|
| Hero H1 | Careful hands. Quiet confidence. | Your beauty ritual, refined. |
| Hero lead | Nails, lashes, and skin — done well, without the noise. … | Nails, lashes, and skin — thoughtfully done at two Beautique Bar studios across Toronto. |
| Hero CTAs | Book / Explore services | Book Appointment / Explore Services |
| Hero photo | Visible “Replace with Beautique Bar professional photography” | Empty gradient block (`data-photo="hero-home"`) |
| Signature head | What we do + “Four pillars. Photography-led, service-first.” | What we do best (no pillars / design note) |
| Signature CTA | View all services | View All Services |
| Experience H2 / lead | Unhurried, considered, yours. / …not overdone. | Beauty, thoughtfully done. / Skilled technicians, careful detail, calm room… |
| Experience list | 3 items (consultation / clean / same standard) | 4 concise: detail, clean+comfort, results, dual-studio standard |
| Featured Work | Featured work / From the studios / “Real client work to replace placeholders.” / View gallery | Gallery / Recent work / short muted line / View Our Work |
| Yonge block | Beautique Bar on Yonge + muted street-level blurb | Destination: BEAUTIQUE BAR + Yonge & York Mills + address/hours/phone + Book Yonge / Explore Yonge / Get Directions |
| Reviews | “Placeholder quote” labels + replace-with-review body | 3 first-name quotes (Sarah, Michelle, Jessica) · Google · ★★★★★ · “From Google reviews” · Read Google Reviews link |
| Instagram | “Secondary feed — swap in live embeds…” | Heading only; empty photo cells |
| Final CTA | Book your chair / Book online | Book your appointment / Book Appointment |

### Yonge page (`locations/yonge/index.html`)

| Area | Before | After |
|------|--------|-------|
| Hero | Beautique Bar on Yonge / Book Yonge | Beautique Bar + On Yonge / Book Appointment |
| Intro H2 | A calm chair on Yonge | Your chair on Yonge |
| Experience lead | …not a rush job, not an oversell. | …finished — careful detail, clean stations, calm atmosphere. |
| Signature | Popular on this floor | Popular here + Explore Services |
| Gallery | Yonge studio (no CTA) | Recent work + View Our Work |
| Reviews | Placeholder quote / replace copy | Amanda, Priya, Emily · Google · Read Google Reviews |
| Pricing note | Sample ranges for preview — confirm live Fresha… | Starting points — confirm exact prices when you book on Fresha. / View Pricing |
| Photos | Visible replace text | Empty `photo-ph` blocks with `data-photo` keys |
| Book CTA | Book on Fresha | Book Appointment |

### Service page (`nails/manicure-pedicure/index.html`)

| Area | Before | After |
|------|--------|-------|
| Hero CTAs | Book / View pricing | Book Appointment / View Pricing |
| Intro H2 / lead | Hands and feet, done properly. / …not rushed colour. | Manicure & pedicure / Hands and feet, done with care… |
| Pricing note | Findable ranges — **not a spreadsheet**. Exact prices… | Easy starting points — exact prices by location when you book on Fresha. |
| Related Bio Gel desc | …(see Bio Gel menu) | Strengthening overlay |
| Bridlewood card | Included “Path: /locations/warden/” design note | Removed; studio name + Book Bridlewood only |
| Final CTA | Choose location | Book Appointment |
| Photos | Visible replace text | Empty placeholders |

---

## Intentionally unchanged

- Homepage section **order**: Hero → Trust → Signature → Experience → Featured Work → Yonge → Reviews → Social → Final CTA  
- Signature categories exactly: **Nails / Pedicures / Lashes / Skin** (no extra categories)  
- Visual system: ivory/cream/taupe/espresso/champagne; Cormorant + Inter  
- Dual-location model; Yonge Fresha URL; Bridlewood Fresha `book-now` URL in sheet  
- NAP: 3430 Yonge St M4N 2M9; `tel:+14164847788`; `sms:+14374344884`; hours Mon–Fri 10–8 · Sat 10–7 · Sun 10–6  
- Mobile sticky Call / Book  
- Yonge page architecture/order (hero → intro → experience → signature → gallery → reviews → pricing → visit → book)  
- Price rows still use `from $—` until live Fresha figures are locked  
- Stub/routing pages not expanded  
- No stock/AI salon image fills  

---

## Remaining photo placeholders

All photography cells are empty tasteful gradient blocks (`.ph.photo-ph`). Track via `data-photo`:

### Homepage (19)
`hero-home`, `sig-nails`, `sig-pedicures`, `sig-lashes`, `sig-skin`, `experience-home`, `work-1`…`work-6`, `yonge-feature`, `ig-1`…`ig-6`

### Yonge (12)
`yonge-hero`, `yonge-experience`, `yonge-sig-mani`, `yonge-sig-biogel`, `yonge-sig-lashes`, `yonge-sig-skin`, `yonge-gal-1`…`yonge-gal-6`

### Mani/Pedi (2)
`mani-hero`, `mani-detail`

**No customer-facing “replace with…” copy.** Internal: HTML comments / `data-photo` / class names only.

---

## Decisions still needed

1. **Real Google reviews** — swap editorial sample quotes (first names) for verified Yonge/Bridlewood Google text; confirm Google Business Profile deep link vs search URL.  
2. **Live prices** — replace `from $—` with Fresha menu figures (or “from $X”) for mani/pedi and Yonge highlights.  
3. **Professional photography** — assign real BB interiors + nail/lash/skin work to `data-photo` slots; logo SVG if replacing BB mark.  
4. **Instagram** — embed handle / feed vs static recent posts; confirm @ account.  
5. **Featured Work heading** — currently **Recent work**; alternate approved option was **The Beautique Edit**.  
6. **Bridlewood NAP** — full address/hours/phone on homepage Yonge note and service cards when ready (path lock `/locations/warden/` remains a build decision, not page copy).  
7. **Review star display** — keep ★★★★★ as editorial; do not invent aggregate review counts until confirmed.  

---

## CSS notes (`styles.css`)

- Placeholders: empty gradient blocks; spans hidden if present.  
- Slightly tighter section / hero / final-CTA padding on mobile; generous on desktop.  
- Added `.loc-name` / `.loc-place`, `.review-more`; restyled `.review-label` as quiet attribution (unused on home; section muted used instead).  

---

## Success checklist

- [x] Files updated in place  
- [x] Design-note / placeholder-as-copy removed from customer-facing text  
- [x] CTAs standardized (Book Appointment, Explore Services, View Pricing, View Our Work, Explore Yonge, Get Directions, Read Google Reviews, Book Yonge, View All Services)  
- [x] Fresha / NAP retained  
- [x] This `REFINE-PASS.md` written  
