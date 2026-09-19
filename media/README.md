# Higgsfield drop-in slots

Steven supplies short clips. Drop files here with these **exact names**. The preview already points `<video>` tags at them. Until a file exists, the matching poster JPEG shows (no on-page “missing video” label).

Do not commit huge uncompressed masters. Prefer H.264 `.mp4`, muted-friendly (no required audio), 8–15s loops.

| File | Aspect | Used on | Notes |
|------|--------|---------|--------|
| `hero-desktop.mp4` | 16:9 landscape | Homepage hero (desktop) | Muted autoplay loop, no controls, `object-fit: cover`. Pair with `hero-desktop.jpg`. |
| `hero-mobile.mp4` | 9:16 vertical | Homepage hero (≤767px) | Same behavior. Desktop file is hidden on small screens and vice versa. |
| `service-moment.mp4` | 16:9 | “Chrome & colour” band | Optional. Poster `service-moment.jpg` until present. |
| `atmosphere.mp4` | 16:9 | “The studio” band | Optional. Poster `atmosphere.jpg`. |
| `yonge.mp4` | 16:9 | Yonge location panel + `/locations/yonge/` | Optional venue loop. Poster `yonge.jpg`. |
| `bridlewood.mp4` | 16:9 | Bridlewood location panel + `/locations/warden/` | Optional. Poster `bridlewood.jpg`. Label stays **Beautique / Bridlewood**. |

## Already in this folder (posters / stills)

Original abstract studio stills — not Nomé photography, not stock salon photos:

- `hero-desktop.jpg` / `hero-mobile.jpg`
- `bridge.jpg`
- `service-moment.jpg` / `atmosphere.jpg`
- `yonge.jpg` / `bridlewood.jpg`
- `story-edge-a.jpg` `story-edge-b.jpg` `story-edge-c.jpg`
- `social-1.jpg` … `social-8.jpg`

Regenerate stills (optional): `python3 generate_posters.py`

## Behavior

- All wired videos: `muted` `loop` `playsinline` `controls` omitted.
- `prefers-reduced-motion: reduce` pauses video and leaves the poster visible.
- A 404 on the `.mp4` hides that `<video>` so the poster stays elegant.

## Suggested Higgsfield content (not required)

Hands, polish glide, chrome reveal, lash application, studio room — no restaurant plates, no Nomé koi mark.
