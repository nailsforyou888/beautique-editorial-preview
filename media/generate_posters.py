#!/usr/bin/env python3
"""Generate original cinematic salon stills for Beautique preview posters.

Abstract studio lighting only — no restaurant photography, no Nomé marks,
no stock photos, no on-image labels.
"""

from __future__ import annotations

import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops

OUT = os.path.dirname(os.path.abspath(__file__))


def mix(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def gradient(w, h, top, bot, diagonal=0.12):
    img = Image.new("RGB", (w, h))
    px = img.load()
    # Horizontal strips + cheap diagonal — one inner loop over width only via frombytes
    lines = []
    for y in range(h):
        t = y / max(1, h - 1)
        c = mix(top, bot, t)
        # slight left-right shift
        row = bytearray()
        for x in range(0, w, 8):
            t2 = (x / max(1, w - 1) - 0.5) * diagonal
            cc = mix(c, bot, max(0.0, min(1.0, t2 + 0.5)) * 0.15)
            row.extend(bytes(cc) * min(8, w - x))
        lines.append(bytes(row[: w * 3]))
    img.frombytes(b"".join(lines))
    return img


def radial_layer(size, cx, cy, radius, color, strength=0.7):
    """Soft radial glow as an RGBA layer."""
    w, h = size
    # Work at half-res then upscale
    sw, sh = max(2, w // 2), max(2, h // 2)
    scx, scy, sr = cx * 0.5, cy * 0.5, radius * 0.5
    layer = Image.new("L", (sw, sh), 0)
    # Draw concentric ellipses
    d = ImageDraw.Draw(layer)
    steps = 28
    for i in range(steps, 0, -1):
        t = i / steps
        a = int(255 * strength * ((1 - t) ** 1.7))
        r = sr * t
        d.ellipse([scx - r, scy - r, scx + r, scy + r], fill=a)
    layer = layer.resize((w, h), Image.Resampling.LANCZOS)
    layer = layer.filter(ImageFilter.GaussianBlur(radius=max(8, radius / 18)))
    tint = Image.new("RGB", (w, h), color)
    return tint, layer


def apply_glow(img, cx, cy, radius, color, strength=0.65):
    tint, mask = radial_layer(img.size, cx, cy, radius, color, strength)
    return Image.composite(tint, img, mask)


def vignette(img, amount=0.55):
    w, h = img.size
    mask = Image.new("L", (max(2, w // 2), max(2, h // 2)), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([-mask.size[0] * 0.05, -mask.size[1] * 0.08, mask.size[0] * 1.05, mask.size[1] * 1.08], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(40))
    mask = mask.resize((w, h), Image.Resampling.LANCZOS)
    # invert amount: darken edges
    edge = Image.new("RGB", (w, h), (0, 0, 0))
    # reduce mask so center stays
    mask = ImageEnhance.Brightness(mask).enhance(1.0)
    # amount controls how much black shows at edges
    black_mask = ImageChops.invert(mask)
    black_mask = ImageEnhance.Brightness(black_mask).enhance(amount * 1.4)
    return Image.composite(edge, img, black_mask)


def grain(img, amount=16, seed=1):
    rng = random.Random(seed)
    w, h = img.size
    sw, sh = max(2, w // 2), max(2, h // 2)
    noise = Image.new("L", (sw, sh))
    noise.putdata([rng.randint(128 - amount, 128 + amount) for _ in range(sw * sh)])
    noise = noise.resize((w, h), Image.Resampling.BILINEAR)
    noise_rgb = Image.merge("RGB", (noise, noise, noise))
    return Image.blend(img, noise_rgb, 0.08)


def stone(img, cx, cy, rw, rh, fill, highlight):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse([cx - rw, cy - rh, cx + rw, cy + rh], fill=fill)
    d.ellipse(
        [cx - rw * 0.5, cy - rh * 0.75, cx + rw * 0.12, cy - rh * 0.12],
        fill=highlight,
    )
    d.ellipse(
        [cx + rw * 0.15, cy + rh * 0.05, cx + rw * 0.62, cy + rh * 0.5],
        fill=(255, 255, 255, 32),
    )
    blur = max(6, int(min(rw, rh) / 10))
    layer = layer.filter(ImageFilter.GaussianBlur(radius=blur))
    out = img.convert("RGBA")
    out.alpha_composite(layer)
    return out.convert("RGB")


def crescent(img, cx, cy, r, color, rot=0.8, thick=0.22):
    mask = Image.new("L", img.size, 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=220)
    ox = math.cos(rot) * r * thick * 2.1
    oy = math.sin(rot) * r * thick * 2.1
    d.ellipse([cx - r + ox, cy - r + oy, cx + r + ox, cy + r + oy], fill=0)
    mask = mask.filter(ImageFilter.GaussianBlur(10))
    tint = Image.new("RGB", img.size, color[:3])
    return Image.composite(tint, img, ImageEnhance.Brightness(mask).enhance(color[3] / 255 if len(color) > 3 else 0.2))


def finish(img, seed, vig=0.48, contrast=1.1, color=1.06):
    img = grain(img, seed=seed)
    img = vignette(img, vig)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Color(img).enhance(color)
    img = ImageEnhance.Sharpness(img).enhance(1.12)
    return img


def compose(w, h, top, bot, lights, stones, curves, seed, vig=0.48):
    img = gradient(w, h, top, bot)
    for cx, cy, rad, col, strength in lights:
        img = apply_glow(img, cx * w, cy * h, rad * min(w, h), col, strength)
    for s in stones:
        img = stone(
            img,
            s["cx"] * w,
            s["cy"] * h,
            s["rw"] * w,
            s["rh"] * h,
            s["fill"],
            s["hi"],
        )
    for c in curves:
        img = crescent(
            img,
            c["cx"] * w,
            c["cy"] * h,
            c["r"] * min(w, h),
            c["fill"],
            c.get("rot", 0.7),
            c.get("thick", 0.2),
        )
    return finish(img, seed, vig)


def save(img, name, quality=88):
    path = os.path.join(OUT, name)
    img.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    print("wrote", name, img.size)


def main():
    save(
        compose(
            1920,
            1080,
            (16, 10, 9),
            (6, 4, 4),
            [
                (0.62, 0.38, 0.72, (196, 154, 118), 0.58),
                (0.28, 0.72, 0.5, (92, 42, 40), 0.42),
                (0.5, 0.18, 0.4, (230, 210, 190), 0.22),
            ],
            [
                {"cx": 0.72, "cy": 0.42, "rw": 0.18, "rh": 0.28, "fill": (210, 168, 140, 150), "hi": (255, 236, 214, 90)},
                {"cx": 0.24, "cy": 0.68, "rw": 0.14, "rh": 0.10, "fill": (88, 36, 38, 130), "hi": (200, 120, 110, 50)},
            ],
            [{"cx": 0.38, "cy": 0.48, "r": 0.42, "fill": (180, 130, 100, 48), "rot": 0.9}],
            11,
        ),
        "hero-desktop.jpg",
    )
    save(
        compose(
            1080,
            1920,
            (14, 9, 8),
            (5, 3, 3),
            [
                (0.5, 0.36, 0.7, (196, 154, 118), 0.52),
                (0.3, 0.72, 0.45, (80, 36, 36), 0.38),
                (0.7, 0.18, 0.35, (230, 210, 190), 0.2),
            ],
            [{"cx": 0.58, "cy": 0.4, "rw": 0.28, "rh": 0.18, "fill": (200, 160, 132, 140), "hi": (255, 236, 214, 80)}],
            [{"cx": 0.42, "cy": 0.55, "r": 0.48, "fill": (160, 110, 90, 40), "rot": 1.1}],
            12,
        ),
        "hero-mobile.jpg",
    )
    save(
        compose(
            1920,
            1080,
            (32, 20, 18),
            (12, 8, 8),
            [
                (0.5, 0.45, 0.85, (214, 176, 156), 0.5),
                (0.15, 0.2, 0.4, (240, 220, 200), 0.26),
                (0.85, 0.75, 0.4, (90, 40, 38), 0.34),
            ],
            [
                {"cx": 0.78, "cy": 0.55, "rw": 0.16, "rh": 0.24, "fill": (186, 122, 108, 140), "hi": (255, 220, 200, 70)},
                {"cx": 0.2, "cy": 0.38, "rw": 0.12, "rh": 0.08, "fill": (230, 200, 176, 110), "hi": (255, 244, 230, 70)},
            ],
            [],
            21,
        ),
        "bridge.jpg",
    )
    save(
        compose(
            1920,
            1080,
            (8, 8, 10),
            (4, 4, 6),
            [
                (0.7, 0.4, 0.7, (210, 214, 220), 0.44),
                (0.3, 0.65, 0.45, (70, 48, 40), 0.3),
                (0.55, 0.25, 0.3, (255, 250, 246), 0.18),
            ],
            [
                {"cx": 0.68, "cy": 0.48, "rw": 0.22, "rh": 0.14, "fill": (190, 196, 204, 150), "hi": (255, 255, 255, 100)},
                {"cx": 0.32, "cy": 0.62, "rw": 0.1, "rh": 0.16, "fill": (48, 36, 34, 160), "hi": (160, 140, 130, 50)},
            ],
            [{"cx": 0.55, "cy": 0.5, "r": 0.38, "fill": (220, 220, 228, 36), "rot": 0.4}],
            31,
            0.42,
        ),
        "service-moment.jpg",
    )
    save(
        compose(
            1920,
            1080,
            (10, 8, 12),
            (6, 5, 6),
            [
                (0.5, 0.35, 0.9, (70, 42, 36), 0.48),
                (0.22, 0.2, 0.28, (240, 210, 170), 0.3),
                (0.8, 0.25, 0.22, (240, 200, 150), 0.24),
            ],
            [],
            [{"cx": 0.48, "cy": 0.52, "r": 0.55, "fill": (90, 50, 40, 40), "rot": 1.4}],
            41,
        ),
        "atmosphere.jpg",
    )
    save(
        compose(
            1920,
            1080,
            (18, 20, 26),
            (6, 6, 8),
            [
                (0.35, 0.28, 0.35, (230, 220, 200), 0.3),
                (0.7, 0.55, 0.7, (50, 44, 40), 0.42),
                (0.15, 0.7, 0.35, (30, 28, 32), 0.32),
            ],
            [{"cx": 0.8, "cy": 0.42, "rw": 0.08, "rh": 0.2, "fill": (200, 188, 168, 80), "hi": (255, 244, 220, 40)}],
            [],
            51,
            0.58,
        ),
        "yonge.jpg",
    )
    save(
        compose(
            1920,
            1080,
            (22, 14, 12),
            (8, 6, 6),
            [
                (0.55, 0.4, 0.75, (160, 96, 72), 0.42),
                (0.25, 0.25, 0.3, (236, 214, 186), 0.24),
                (0.8, 0.75, 0.4, (40, 22, 20), 0.34),
            ],
            [{"cx": 0.28, "cy": 0.58, "rw": 0.14, "rh": 0.1, "fill": (140, 80, 60, 100), "hi": (230, 180, 140, 50)}],
            [],
            61,
        ),
        "bridlewood.jpg",
    )
    for name, seed, top, side in (
        ("story-edge-a.jpg", 71, (244, 236, 224), "a"),
        ("story-edge-b.jpg", 72, (236, 226, 210), "b"),
        ("story-edge-c.jpg", 73, (232, 218, 200), "c"),
    ):
        save(
            compose(
                900,
                1200,
                top,
                (220, 200, 184),
                [
                    (0.5, 0.4, 0.7, (210, 160, 130), 0.36),
                    (0.3, 0.7, 0.4, (180, 90, 80), 0.22),
                ],
                [{"cx": 0.55, "cy": 0.42, "rw": 0.28, "rh": 0.18, "fill": (200, 150, 120, 110), "hi": (255, 230, 210, 70)}],
                [],
                seed,
                0.22,
            ),
            name,
        )
    tiles = [
        ("social-1.jpg", 81, (16, 12, 12), (8, 6, 6), (200, 160, 140)),
        ("social-2.jpg", 82, (20, 16, 14), (10, 8, 8), (180, 120, 90)),
        ("social-3.jpg", 83, (12, 12, 16), (6, 6, 8), (210, 210, 220)),
        ("social-4.jpg", 84, (18, 10, 10), (8, 4, 4), (160, 70, 70)),
        ("social-5.jpg", 85, (14, 12, 10), (6, 5, 4), (220, 190, 150)),
        ("social-6.jpg", 86, (10, 10, 12), (4, 4, 6), (190, 196, 204)),
        ("social-7.jpg", 87, (22, 16, 12), (8, 6, 5), (170, 100, 70)),
        ("social-8.jpg", 88, (12, 10, 12), (5, 4, 5), (200, 170, 160)),
    ]
    for name, seed, top, bot, glow in tiles:
        save(
            compose(
                800,
                1000,
                top,
                bot,
                [
                    (0.5, 0.42, 0.7, glow, 0.5),
                    (0.2, 0.75, 0.35, mix(glow, (20, 12, 10), 0.5), 0.3),
                ],
                [{"cx": 0.58, "cy": 0.46, "rw": 0.22, "rh": 0.16, "fill": (*glow, 90), "hi": (255, 240, 220, 60)}],
                [],
                seed,
            ),
            name,
            quality=84,
        )


if __name__ == "__main__":
    main()
