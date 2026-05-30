# Premium Typography — Gradient Text, Metallic Sheens & Spotlight Effects

Full CSS code, GSAP patterns, color palettes, and anti-patterns for making display typography feel like illuminated metallic surfaces — "golden palace" premium without being literally gold.

---

## Foundation: `background-clip: text`

All gradient text effects rely on three CSS properties working together:

```css
.gradient-text {
  background: [gradient-value];
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  color: #f5f5f0; /* WHY: Fallback for browsers without background-clip: text support */
}
```

**Browser support (2026):** `background-clip: text` is supported in all modern browsers. The `-webkit-` prefix is still required for Chrome, Safari, and Edge. Always include `color` fallback.

```css
/* WHY: Feature detection ensures graceful degradation */
@supports not (background-clip: text) {
  .gradient-text {
    background: none;
    -webkit-text-fill-color: unset;
    color: #f5f5f0;
    text-shadow: 0 0 15px rgba(247, 231, 206, 0.3);
  }
}
```

---

## Layer 1: Warm Metallic Gradient (Base Effect)

The foundation of premium typography. Multi-stop linear gradient simulating light reflecting off a metallic surface.

### Warm White Metallic (THE default for dark themes)

```css
/* WHY: Symmetrical dark→light→dark gradient mimics how light reflects off engraved metal.
   Peak at 50% = light hitting the text face-on. Warm white (#f8f8f4) has subtle warmth
   without reading as yellow/gold. Against #050508 background: 18:1 contrast ratio. */
.kai-display-gradient {
  background: linear-gradient(
    90deg,
    #3a3a38 0%,       /* Dark brown shadow edge */
    #8a8a7e 20%,      /* Mid-dark warm gray */
    #d4d4c8 40%,      /* Warm silver approach */
    #f8f8f4 50%,      /* Peak: warm white (R248 G248 B244 — red slightly higher = warmth) */
    #d4d4c8 60%,      /* Descending warm silver */
    #8a8a7e 80%,      /* Mid-dark return */
    #3a3a38 100%      /* Shadow edge return */
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

### Champagne Luxury (Warmer, more gold presence)

```css
/* WHY: Champagne (#f7e7ce) is elegant warm gold without looking cheap like pure #ffd700.
   Use for hero numbers, revenue figures, or "money shot" moments. */
.kai-display-champagne {
  background: linear-gradient(
    90deg,
    #050508 0%,        /* Blends into dark background */
    #8b6f47 15%,       /* Dark warm gold */
    #cb9b51 30%,       /* Mid champagne */
    #f7e7ce 50%,       /* Peak: champagne highlight */
    #cb9b51 70%,       /* Descending */
    #8b6f47 85%,
    #050508 100%
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

### Platinum Sheen (Cool premium, no warmth)

```css
/* WHY: Platinum is pure cool metallic — no yellow/warm undertones. Use for secondary
   headings or when warmth would clash with the section's accent color. */
.kai-display-platinum {
  background: linear-gradient(
    90deg,
    #2a2a28 0%,
    #6a6a68 20%,
    #b0b0ae 40%,
    #f0f0ee 50%,      /* Peak: cool near-white */
    #b0b0ae 60%,
    #6a6a68 80%,
    #2a2a28 100%
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

### Violet-to-Cyan Brand Metallic (KAI-specific, brand-matched)

```css
/* WHY: Uses the KAI brand gradient (#8B5CF6 → #06B6D4) through a metallic lens.
   Still reads as metallic due to the dark→bright→dark structure, but with brand color. */
.kai-display-brand {
  background: linear-gradient(
    135deg,
    #1a0a30 0%,        /* Deep violet-black */
    #8B5CF6 25%,       /* Violet peak */
    #f5f5f0 50%,       /* Central white flash */
    #06B6D4 75%,       /* Cyan peak */
    #0a1a20 100%       /* Deep cyan-black */
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

---

## Layer 2: Animated Sheen Sweep (Light Moving Across Text)

A bright band sweeps left-to-right across the text, simulating a moving light source.

### Standard Sheen (2.5-3.5s cycle — the "premium" timing zone)

```css
/* WHY: background-size: 300% creates space for the gradient to travel across.
   ease-in-out makes the sweep feel like natural light, not mechanical.
   3s is the sweet spot — faster feels cheesy, slower feels sluggish. */
.kai-display-sheen {
  background: linear-gradient(
    90deg,
    #3a3a38 0%,
    #8a8a7e 15%,
    #f8f8f4 35%,       /* Bright band leading edge */
    #ffffff 50%,        /* Peak intensity */
    #f8f8f4 65%,       /* Bright band trailing edge */
    #8a8a7e 85%,
    #3a3a38 100%
  );
  background-size: 300% 100%;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: kai-premium-sheen 3s ease-in-out infinite;
  will-change: background-position;
}

@keyframes kai-premium-sheen {
  0% {
    background-position: 200% 0;
  }
  100% {
    background-position: -200% 0;
  }
}
```

### Pause-and-Sweep (More Dramatic — Light Hits Then Rests)

```css
/* WHY: The 60% pause at the end creates a "light hits, rests, then sweeps again" rhythm.
   More dramatic than continuous motion. Good for hero headings. */
@keyframes kai-spotlight-sweep {
  0% {
    background-position: 200% 0;
  }
  40% {
    background-position: -200% 0;
  }
  100% {
    background-position: -200% 0;   /* Hold position for 60% of duration */
  }
}

.kai-display-spotlight {
  /* ... same gradient as sheen ... */
  animation: kai-spotlight-sweep 5s ease-in-out infinite;
}
```

### Two-Tone Sweep (Brand Colors in the Light Band)

```css
/* WHY: The sweep carries the brand gradient (violet→cyan) through the metallic text.
   The base text is warm metallic, but the moving light has brand color. */
.kai-display-brand-sweep {
  background:
    linear-gradient(
      90deg,
      transparent 0%,
      rgba(139, 92, 246, 0.4) 20%,     /* Violet tint */
      rgba(255, 255, 255, 0.6) 50%,     /* White peak */
      rgba(6, 182, 212, 0.4) 80%,       /* Cyan tint */
      transparent 100%
    ),
    linear-gradient(
      90deg,
      #3a3a38 0%,
      #8a8a7e 25%,
      #f8f8f4 50%,
      #8a8a7e 75%,
      #3a3a38 100%
    );
  background-size: 200% 100%, 100% 100%;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: kai-brand-sweep 4s ease-in-out infinite;
}

@keyframes kai-brand-sweep {
  0% { background-position: 200% 0, 0% 0; }
  100% { background-position: -200% 0, 0% 0; }
}
```

---

## Layer 3: Spotlight / Light Beam Effect (Directional Light on Text)

Makes text look like a spotlight is hitting it from a specific direction.

### Static Radial Spotlight (CSS Only)

```css
/* WHY: The ellipse positioned at 35% 30% simulates overhead-left light hitting the text.
   Off-center placement is key — centered light looks flat/artificial.
   The radial gradient overlays the linear metallic base for depth. */
.kai-display-lit {
  background:
    radial-gradient(
      ellipse 400px 200px at 35% 30%,
      rgba(255, 255, 255, 0.35) 0%,    /* Bright focal point */
      rgba(247, 231, 206, 0.15) 30%,   /* Warm falloff */
      transparent 70%                    /* Fades to nothing */
    ),
    linear-gradient(
      90deg,
      #3a3a38 0%,
      #8a8a7e 25%,
      #f8f8f4 50%,
      #8a8a7e 75%,
      #3a3a38 100%
    );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

### Interactive Spotlight (Follows Cursor via CSS Custom Properties)

```css
/* WHY: CSS custom properties updated by JS give a "light following the viewer" effect.
   Uses GSAP quickTo for smooth interpolation, no jank. */
.kai-display-interactive {
  --spot-x: 50%;
  --spot-y: 30%;

  background:
    radial-gradient(
      circle 250px at var(--spot-x) var(--spot-y),
      rgba(255, 255, 255, 0.4) 0%,
      rgba(247, 231, 206, 0.2) 30%,
      transparent 60%
    ),
    linear-gradient(
      90deg,
      #3a3a38 0%,
      #8a8a7e 25%,
      #f8f8f4 50%,
      #8a8a7e 75%,
      #3a3a38 100%
    );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

```javascript
// WHY: GSAP quickTo smoothly interpolates the spotlight position without tween spam.
// Pointer events on the section container, not the text element itself.
const heading = document.querySelector('.kai-display-interactive');
const container = heading.closest('section');

container.addEventListener('pointermove', (e) => {
  const rect = heading.getBoundingClientRect();
  const x = ((e.clientX - rect.left) / rect.width) * 100;
  const y = ((e.clientY - rect.top) / rect.height) * 100;
  heading.style.setProperty('--spot-x', `${x}%`);
  heading.style.setProperty('--spot-y', `${y}%`);
});

// WHY: Reset to center when pointer leaves — avoids stuck spotlight at edge
container.addEventListener('pointerleave', () => {
  heading.style.setProperty('--spot-x', '50%');
  heading.style.setProperty('--spot-y', '30%');
});
```

---

## Layer 4: Warm Glow Halo (Text Shadow for "Illuminated from Within")

```css
/* WHY: Subtle glow behind the text creates "illuminated" feeling. Two shadow layers:
   - Tight (20px): sharp glow directly behind text
   - Wide (50px): ambient warmth that bleeds into space around the heading
   Keep blur ≤50px — heavier glows look cheap/neon. */
.kai-display-glow {
  text-shadow:
    0 0 20px rgba(247, 231, 206, 0.25),     /* Tight champagne glow */
    0 0 50px rgba(245, 245, 240, 0.10);      /* Wide warm ambient */
}

/* WHY: Mode-specific glow colors tie the heading to the active UI accent */
.mode-analytics .kai-display-glow {
  text-shadow:
    0 0 20px rgba(163, 230, 53, 0.20),       /* Lime accent */
    0 0 50px rgba(163, 230, 53, 0.08);
}

.mode-inbox .kai-display-glow {
  text-shadow:
    0 0 20px rgba(6, 182, 212, 0.25),        /* Cyan accent */
    0 0 50px rgba(6, 182, 212, 0.08);
}

.mode-content .kai-display-glow {
  text-shadow:
    0 0 20px rgba(251, 113, 133, 0.20),      /* Coral accent */
    0 0 50px rgba(251, 113, 133, 0.08);
}
```

---

## Layer 5: Holographic / Conic Gradient (Special Moments Only)

For premium reveal moments — achievement unlocks, hero numbers, the "$1,774" royalty display.

```css
/* WHY: @property enables GPU-accelerated angle interpolation for smooth rotation.
   Conic gradient creates a rotating metallic reflection effect. Use SPARINGLY —
   max 1-2 elements per page. */
@property --holo-angle {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: false;
}

.kai-display-holo {
  background: conic-gradient(
    from var(--holo-angle) at 50% 50%,
    #f5f5f0 0deg,
    #f7e7ce 72deg,
    #e0e0e0 144deg,
    #f7e7ce 216deg,
    #f5f5f0 288deg,
    #f7e7ce 360deg
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: holo-rotate 8s linear infinite;
}

@keyframes holo-rotate {
  to { --holo-angle: 360deg; }
}
```

---

## Color Palette: "Golden Palace" Warm Premium

### Recommended Colors (on `#050508` dark background)

| Color | Hex | Role | Contrast vs #050508 |
|-------|-----|------|---------------------|
| Warm White (peak) | `#f8f8f4` | Primary gradient highlight | 18.5:1 ✓ |
| Champagne | `#f7e7ce` | Warm accent gradient stop | 16.8:1 ✓ |
| Warm Silver | `#d4d4c8` | Mid-tone metallic | 12.2:1 ✓ |
| Dark Warm Gray | `#8a8a7e` | Shadow gradient stop | 5.3:1 ✓ |
| Deep Shadow | `#3a3a38` | Darkest gradient edge | 1.8:1 (decorative) |
| Platinum Cool | `#e0e0e0` | Cool accent (no warmth) | 14.1:1 ✓ |
| Gold Hint | `#d4af37` | Accent ONLY, never primary | 8.3:1 ✓ |

### Colors to AVOID

| Color | Hex | Why It Fails |
|-------|-----|-------------|
| Pure Gold | `#ffd700` | Reads as "cheap costume," not luxury |
| Pure Yellow | `#ffff00` | Jarring high-energy, wrong mood |
| Warm Beige | `#deb887` | Too muted, loses shine |
| Clinical White | `#ffffff` | Cold, no warmth, no character |
| Neon Gold | `#ff9f00` | Feels Vegas, not palace |
| Desaturated Olive | `#808000` | Muddy, no premium feeling |

---

## Application Rules: When to Use What

### By Element Type

| Element | Treatment | Animated? |
|---------|-----------|-----------|
| **Hero h1** (one per page) | Full metallic gradient + sheen sweep + glow | Yes — sheen sweep |
| **Section h2** | Metallic gradient (no animation) + subtle glow | No |
| **Large stat numbers** ($1,774, scores) | Champagne luxury gradient OR holographic | Optional — holographic for reveals |
| **Tile headings** (inside bento) | Static gradient, no glow | No |
| **Nav brand** | Subtle gradient + slow sweep | Yes — slow sweep |
| **Body text** | **NEVER gradient** — solid `#FAFAFA` | No |
| **Button text** | **NEVER gradient** — solid color | No |
| **Labels/overlines** | **NEVER gradient** — solid secondary color | No |
| **Subheading / h3+** | Static gradient if 24px+, solid if smaller | No |

### Size Threshold

```
≥ 48px (display/hero) → Full gradient + animation + glow
32-47px (section heading) → Gradient, optional glow, no animation
24-31px (card heading) → Subtle gradient, no glow, no animation
< 24px → NEVER use gradient text. Solid color only.
```

### Gradient Intensity by Hierarchy

```
Primary heading:   Full metallic (dark→light→dark, 7+ color stops)
Secondary heading: Reduced metallic (3-5 stops, smaller range)
Tertiary heading:  Barely-there gradient (white→warm white, 2-3 stops)
Stat numbers:      Champagne or brand gradient (contextual)
```

---

## Combining With 3D Spatial Depth

When using premium typography INSIDE a 3D spatial layout (see `references/3d-spatial-depth.md`):

```css
/* WHY: Text on a glassmorphism tile at translateZ(25px) needs the gradient to respect
   the 3D transform. Ensure the text element doesn't flatten the 3D context. */
.bento-tile {
  transform: translateZ(25px);
  transform-style: preserve-3d; /* WHY: Let children exist in 3D space */
}

.bento-tile .kai-display-gradient {
  /* Gradient text works normally inside 3D-transformed parents.
     No special treatment needed — background-clip: text is independent of transforms. */
}

/* WHY: Text glow (text-shadow) renders in 3D space when the parent has preserve-3d.
   The glow appears at the same Z-depth as the text, creating natural depth. */
.bento-tile .kai-display-glow {
  text-shadow:
    0 0 20px rgba(247, 231, 206, 0.25),
    0 0 50px rgba(245, 245, 240, 0.10);
}
```

---

## Performance Rules

| Rule | Why |
|------|-----|
| `will-change: background-position` only on animated text | Promotes to GPU layer; wasting memory on static elements |
| Max 3 animated gradient headings per page | Each animated gradient is a separate GPU layer |
| Use `@keyframes` not JS for sheen sweep | CSS animations run on compositor thread, JS on main thread |
| `text-shadow` max 2 layers, max 50px blur | More layers/blur = more GPU compositing |
| No gradient text inside `overflow: hidden` with `backdrop-filter` parent | Stacking context conflicts can cause rendering glitches |
| Test on mobile at 2x DPI | Gradient text rendering quality varies — ensure no banding |

---

## Accessibility

### Contrast

All gradient text passes WCAG AA at its **lightest** stop:
- `#f8f8f4` on `#050508` = 18.5:1 (AAA at all sizes) ✓
- `#f7e7ce` on `#050508` = 16.8:1 (AAA at all sizes) ✓
- `#d4d4c8` on `#050508` = 12.2:1 (AAA at all sizes) ✓

The darkest stops (`#3a3a38`, `#8a8a7e`) are decorative gradient edges that pass through quickly — the readable text portions maintain high contrast.

### Reduced Motion

```css
/* WHY: Disable all sheen/sweep/rotation animations. Keep the static gradient visible —
   the metallic look comes from the gradient stops, not the motion. */
@media (prefers-reduced-motion: reduce) {
  .kai-display-sheen,
  .kai-display-spotlight,
  .kai-display-brand-sweep,
  .kai-display-holo {
    animation: none !important;
    background-position: 50% 0 !important;
  }

  .kai-display-interactive {
    --spot-x: 50% !important;
    --spot-y: 30% !important;
  }
}
```

### Fallback

```css
@supports not (background-clip: text) {
  [class*="kai-display-"] {
    background: none !important;
    -webkit-text-fill-color: unset !important;
    color: #f5f5f0;
    text-shadow: 0 0 15px rgba(247, 231, 206, 0.3);
  }
}
```

---

## Anti-Patterns

1. **Gradient on body text** — Illegible under 24px. Looks noisy, not premium.
2. **Pure gold `#ffd700` as primary** — Reads as "MySpace era." Champagne (`#f7e7ce`) is the correct warm accent.
3. **Animation faster than 2.5s** — Feels cheap/flashy. Premium = slow, confident light.
4. **More than 3 animated headings per page** — Competing animations cancel each other out.
5. **text-shadow blur > 50px** — Goes from "glow" to "neon sign."
6. **Gradient on button text** — Buttons need solid contrast for action clarity.
7. **Same gradient everywhere** — Use different intensities for hierarchy (see Application Rules).
8. **Conic/holographic on more than 2 elements** — Special moments stop being special.
9. **Missing `color` fallback** — Older browsers show nothing without the fallback color property.
10. **Animating gradient text inside scrolling containers** — Janky on mobile due to scroll+animation compositing conflict.

---

## Quality Gate Checklist

```
[ ] TYPO-GRADIENT — If premium gradient typography is chosen, display headings (48px+) have metallic depth, not flat white?
[ ] TYPO-SHEEN — If hero heading is the focal premium moment, sheen sweep exists and timing is 2.5-3.5s?
[ ] TYPO-GLOW — Dark/luminous premium display text has warm controlled glow? ≤50px blur?
[ ] TYPO-HIERARCHY — Gradient intensity decreases with heading level (h1 > h2 > h3)?
[ ] TYPO-BODY — Body text, labels, buttons are solid color (NO gradient)?
[ ] TYPO-CONTRAST — Lightest gradient stop passes WCAG AA against background?
[ ] TYPO-FALLBACK — `color` fallback set? `@supports` query for old browsers?
[ ] TYPO-MOTION — Reduced-motion disables sweep/rotation but keeps static gradient?
[ ] TYPO-WARM — Colors feel warm/premium, not cold/clinical or cheap/neon?
[ ] TYPO-PALETTE — No pure gold #ffd700, no pure yellow, no neon? Champagne/platinum palette?
```
