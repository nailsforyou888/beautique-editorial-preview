# Beautique Bar — Nomé-format preview report

**Date:** 2026-09-19  
**Repo:** https://github.com/nailsforyou888/beautique-editorial-preview  
**Status:** Static GitHub Pages preview only — **not** live production (`beautiquebar.com` untouched)

---

## 1. Live Pages URL

**https://nailsforyou888.github.io/beautique-editorial-preview/**

After this branch merges to `main`, Pages (source: `main` / root) serves the Nomé-format homepage.

Relative asset paths from each HTML file (`styles.css`, `../../styles.css`, `media/…`) — no `<base>` tag, so the project site path `/beautique-editorial-preview/` keeps working.

---

## 2. What changed vs the Fora-dark preview

Steven moved the format reference from **fora.so** (dark SaaS landing: centered Inter hero, glass booking card, tabbed services, quote grid) to **https://nomeizakaya.com/** (immersive full-bleed media, oversized geometric sans, sequential location panels).

| Fora-dark (superseded) | This pass (Nomé format) |
|------------------------|-------------------------|
| Near-black SaaS canvas, Inter, pill chrome, 1080px column | Full-viewport media sections, Oswald display + Montserrat, edge-to-edge |
| Centered “Your beauty ritual, refined.” + mock booking card | Muted autoplay **video slots** + rotating NAILS / LASHES / SKIN / PEDICURES / YOUR RITUAL |
| Dual location **cards** in a 2-col grid | Sequential full-bleed panels: **Yonge**, then **Bridlewood** |
| Tabbed Nails / Pedicures / Lashes / Skin showcase | Story → service moment → atmosphere (Higgsfield-ready) |
| Quote card grid | Instagram-style 4-col reel strip with play icons |
| Fora rose–charcoal radial + `art/horizon.svg` | Abstract studio posters in `media/` (no restaurant photos, no Nomé koi) |
| Sticky translucent navy header | Transparent nav over hero → **solid black** on scroll |

Production `beautiquebar.com` was not edited. GTM was not added on this preview.

---

## 3. Homepage section order (Nomé rhythm)

1. Full-bleed hero + rotating all-caps words + primary **BOOK** (studio chooser)
2. Visual bridge — “SEE SERVICES” / Book
3. Cream story — **EXPERIENCE BEAUTIQUE** + tightened live about copy
4. Dark service moment — **CHROME & COLOUR** + Book
5. Atmosphere — **THE STUDIO** + Book
6. Location panel — **YONGE** · 3430 Yonge St. · outlined Book → Yonge Fresha
7. Location panel — **BRIDLEWOOD** · 2900 Warden Ave. · outlined Book → Bridlewood Fresha (UI label Beautique, never Nails For You)
8. Loyalty band — **YOUR NEXT SET STARTS HERE** (modest; no fake free-appetizer clone)
9. Instagram strip — `beautiquebar88`, 8 tiles, play affordances, sourced quote fragments only
10. Dark patterned footer — two NAP columns + Book

---

## 4. Higgsfield video slots

Wired now. Drop files using the names in `media/README.md`. Until then, cinematic posters show and a failed `.mp4` hides the `<video>` element.

| Slot | Markup | Poster until file exists |
|------|--------|--------------------------|
| Hero desktop 16:9 | `media/hero-desktop.mp4` | `media/hero-desktop.jpg` |
| Hero mobile 9:16 | `media/hero-mobile.mp4` | `media/hero-mobile.jpg` |
| Service moment | `media/service-moment.mp4` | `media/service-moment.jpg` |
| Atmosphere | `media/atmosphere.mp4` | `media/atmosphere.jpg` |
| Yonge | `media/yonge.mp4` | `media/yonge.jpg` |
| Bridlewood | `media/bridlewood.mp4` | `media/bridlewood.jpg` |

All loops: `muted` `autoplay` `loop` `playsinline`, no controls.  
`prefers-reduced-motion: reduce` pauses video and leaves the poster.

---

## 5. Booking CTAs (exact)

- **Yonge:** `https://www.fresha.com/a/beautique-bar-on-yonge-toronto-3430-yonge-street-e0fzhnga/booking?menu=true`
- **Bridlewood:** `https://www.fresha.com/book-now/nails-for-you-m7weksrj/all-offer?share&pId=32159`  
  UI label: **Beautique at Bridlewood Mall** / **Bridlewood** — never Nails For You on the page.

Global header **Book** opens a two-studio Fresha sheet. Location panels deep-link that shop only.

---

## 6. Pages shipped

| Page | Path |
|------|------|
| Homepage | `index.html` |
| Shared CSS / JS | `styles.css`, `script.js` |
| Yonge | `locations/yonge/index.html` |
| Bridlewood (path lock) | `locations/warden/index.html` |
| Locations chooser | `locations/index.html` |
| Media + Higgsfield README | `media/` |
| Continuity stubs | `services.html`, `about.html`, `gallery.html`, `pricing.html`, `privacy.html`, `terms.html`, `nails/manicure-pedicure/index.html` |

---

## 7. Typography & palette

| Role | Choice |
|------|--------|
| Display | **Oswald** 700, uppercase (Futura-like condensed) |
| Body / nav | **Montserrat** |
| Black / white | `#000000` / `#FFFFFF` |
| Story field | cream `#F3EEE6` |
| Active Home / accent | champagne `#C4A07A` (not Nomé restaurant red) |
| Club band | deep rose `#5C2A30` |

---

## 8. Copy hygiene

- No invented metrics, awards, or star averages
- No “over a decade” brand tenure line
- Bio Gel spelling preserved
- Title/meta keep existing live “top-rated” language only
- Social captions reuse live homepage quotes (first names) or service labels
- Loyalty band does **not** clone Nomé’s free-appetizer / $1 oyster offer

---

## 9. URL locks preserved

`/` · `/locations/` · `/locations/yonge/` · `/locations/warden/`

Public name **Bridlewood**; folder stays **`warden`**.

---

## 10. Open decisions

| Item | Status |
|------|--------|
| **Higgsfield clips** | Slots wired; files not in repo yet |
| **Bridlewood hours** | Unknown — page says call 647-770-5232 |
| **Bridlewood Fresha canonical** | Preview uses live `book-now/nails-for-you-…pId=32159`; FAQ alternate not used |
| **Yonge postal `M4N 2M9`** | Shown in footer / detail page; homepage panel matches Nomé (street only) |
| **Yonge hours** | Detail page only; FAQ-documented Mon–Fri 10–8 / Sat 10–7 / Sun 10–6 — confirm before production |
| **Per-shop Google review URLs** | Not on this homepage (IG strip instead) |
| **Beautique Club** | Soft ask-in-studio line only — no invented perks or join form |
| **`/locations/bridlewood/`** | Still a broken alias on live — not used here |
| **Pages serve from `main`** | Merge this PR so the public preview URL updates |

---

## 11. Out of scope

- Production DNS / RapidWebLaunch Astro site
- NFY downstairs site
- Invented prices or Warden hours
