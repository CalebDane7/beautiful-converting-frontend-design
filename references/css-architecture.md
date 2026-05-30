# CSS Architecture Reference

Loaded during Phase 4 (Build). All CSS decisions flow from this file.

Default accessibility target: **WCAG 2.2 AA**.

---

## 1. HARD RULE: Zero Inline CSS

Never use `style=` in HTML. Never use `element.style.xxx` in JS (except CSS custom properties via `setProperty`).

| Instead of...              | Do this...                                                        |
|----------------------------|-------------------------------------------------------------------|
| `style="color: red"`       | `.error-text { color: var(--accent-red); }`                       |
| `element.style.transform`  | `element.classList.add('active')` + CSS transition                |
| `style="display: none"`    | `.hidden { display: none; }` + toggle class                      |
| Dynamic per-item styles    | `data-*` attributes + CSS `[data-variant="primary"]`              |
| Computed JS values         | CSS custom properties via `setProperty`                           |
| Per-item computed styles   | Inject `<style>` block into `<head>`                              |

---

## 2. Modular File Structure (ITCSS-Inspired)

```
css/
  variables.css    — CSS custom properties (THE source of truth)
  base.css         — Reset, *, body, html, semantic elements
  typography.css   — @font-face, heading scales, .gradient-text
  components.css   — Buttons, cards, nav, modals (reusable blocks)
  layout.css       — Grid, containers, section spacing, bento
  animations.css   — @keyframes, transition classes, reduced-motion
  utilities.css    — .hidden, .sr-only, .visually-hidden
  [page].css       — Per-page overrides (keep minimal)
```

React/Vue/Svelte: CSS Modules or scoped styles per component + shared `variables.css`.

---

## 3. The CSS Variable Contract

All visual values live in `variables.css`. Components NEVER hardcode colors, spacing, or fonts.

```css
/* GOOD */
.cta-btn { background: var(--gradient-button); border-radius: var(--radius-pill); }

/* BAD */
.cta-btn { background: linear-gradient(135deg, #ff2d55, #9b30ff); border-radius: 50px; }
```

Changing theme = editing ONE file. Changing component = editing ONE file.

---

## 4. Dynamic Styles Without Inline CSS

```javascript
/* CSS custom properties on element — CSS handles styling */
element.style.setProperty('--mouse-x', x + '%');
element.style.setProperty('--mouse-y', y + '%');

/* Per-item computed styles — inject <style> block */
var style = document.createElement('style');
style.textContent = items.map(function(_, i) {
  return '.stagger-child:nth-child(' + (i+1) + ') { transition-delay: ' + (i * 0.1) + 's; }';
}).join('\n');
document.head.appendChild(style);
```

---

## 4b. Layout Integrity Rules (Build-Time)

These are structural defaults for avoiding broken "premium" layouts.

### Layout safety defaults

Every component must survive desktop and mobile without text escaping boxes or boxes colliding.

```css
* {
  box-sizing: border-box;
}

.surface,
.panel,
.card,
.button,
.badge,
.input,
.chart-shell {
  min-width: 0;
  max-width: 100%;
}

.button,
.badge,
.chip,
.nav-item {
  white-space: normal;
  overflow-wrap: anywhere;
}

.media-frame,
.chart-shell,
.tile {
  contain: layout paint;
}
```

Use stable dimensions for fixed-format elements:

```css
.icon-button {
  inline-size: 44px;
  block-size: 44px;
  flex: 0 0 44px;
}

.metric-tile {
  min-block-size: 9rem;
}

.chart-shell {
  min-block-size: clamp(220px, 32vw, 380px);
}
```

Never hide overflow to mask a broken layout. If overflow is used, it must be part of a deliberate scroll/preview pattern.

### Default to intrinsic sizing

Start with content-driven layout before adding equal heights or stretch behavior.

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  align-items: start; /* NOT stretch by default */
}

.card {
  height: auto;
  min-height: 0;
}
```

**Why:** `align-items: stretch` plus mismatched content lengths is a common cause of giant dead zones inside cards.

### Do not clamp meaningful body copy by default

```css
/* GOOD: full readable copy */
.card__body {
  overflow: visible;
  display: block;
}

/* ONLY when brief explicitly wants teaser cards */
.card__excerpt {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}
```

If the user did not ask for teaser cards, narrative content should stay readable.

### Prefer max-width centering for shells

```css
.app-shell__main {
  width: min(100%, 1200px);
  margin-inline: auto;
}
```

Do not "center" a layout indirectly with arbitrary left padding or by eyeballing card positions while the shell itself is off-center.

### Equal-height components require proof

Only force equal-height cards when ALL are true:
- the layout visually benefits from uniform rows
- content lengths are genuinely comparable
- the tallest state still looks intentional
- the shortest state does not produce empty dead space

If any of those fail, use content-driven height instead.

---

## 4c. Material Craft Defaults

Use CSS tokens for the fine details that stop a page from feeling cheap.

```css
.section-band {
  border-block: 2px solid var(--border-section, rgba(255,255,255,0.18));
  background:
    linear-gradient(180deg, rgba(255,255,255,0.045), rgba(255,255,255,0.015)),
    var(--bg-section);
}

.panel,
.card,
.media-frame {
  border: 1px solid var(--border-subtle);
  box-shadow: var(--shadow-md), inset 0 1px 0 rgba(255,255,255,0.08);
}

.hero-object,
.primary-cta,
.is-active {
  box-shadow: var(--outline-glow);
}

.texture-layer {
  opacity: var(--texture-opacity, 0.04);
  pointer-events: none;
}
```

Rules:
- Use thicker section dividers or high-contrast bands when adjacent sections blend together.
- Dark premium surfaces usually need visible rim light, border contrast, or glow. Flat dark cards with invisible borders fail.
- Keep body text solid and crisp. Apply glow/sheen to containers, icons, CTAs, display headings, or major numbers.
- Dense operational UI uses quieter borders and focus rings, not theatrical glow everywhere.

---

## 4d. Accessibility Baselines (Build-Time)

Premium UI still has to be operable. These are defaults, not optional extras.

### Focus visibility is mandatory

```css
:focus-visible {
  outline: 2px solid var(--focus-ring, #2563eb);
  outline-offset: 3px;
}

:focus:not(:focus-visible) {
  outline: none;
}
```

Do not remove focus styles without replacing them with a clearly visible alternative.

### Hover is additive, not required

- If a card reveals essential content on hover, provide the same access on focus and touch.
- If a button relies on color shift alone, add shape, underline, border, icon, or motion cue.

### Minimum target sizing

- Primary buttons, nav items, toggles, and icon controls should be comfortably tappable.
- Do not shrink important controls to preserve a visual composition. Fix the layout instead.

### Semantic-first components

- Use `<button>` for actions, `<a>` for navigation, `<label>` for form labels, and real heading levels in order.
- Icon-only buttons need an accessible name.
- Decorative images should be ignored by assistive tech; meaningful images need alt text.

### Contrast in real states

- Check default, hover, focus, disabled, and overlay states.
- Glass, gradients, textures, and image overlays frequently lower effective contrast. Judge the rendered result, not the raw token values.

---

## 5. Glassmorphism — Selective Use Only

Glass ON: Navigation bars, CTA buttons, modal overlays, 2-3 key feature cards, pricing cards.
Glass NOT ON: Every card, body text, backgrounds, footers, form fields.

**Dark theme glass:**
```css
.glass-panel {
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(12px) saturate(140%);
  -webkit-backdrop-filter: blur(12px) saturate(140%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-md);
}
```

**Light theme glass:**
```css
.glass-panel {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px) saturate(120%);
  -webkit-backdrop-filter: blur(20px) saturate(120%);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: var(--radius-md);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
}
```

**Glass CTA button (dark):**
```css
.glass-cta {
  background: rgba(155, 48, 255, 0.2);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(155, 48, 255, 0.3);
  box-shadow: 0 0 30px rgba(155, 48, 255, 0.15);
  transition: all 0.3s ease;
}
.glass-cta:hover {
  background: rgba(155, 48, 255, 0.35);
  box-shadow: 0 0 50px rgba(155, 48, 255, 0.25);
  transform: translateY(-2px);
}
```

**Glass nav (scrolled state — from erebora-umbrella):**
```css
.nav.scrolled {
  background: var(--glass-bg-heavy);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  box-shadow: var(--shadow-sm);
  border-bottom: 1px solid var(--border-light);
}
```

Performance: 3-5 glass elements = negligible. 10+ = lag on mobile. Never animate backdrop-filter. Always add `-webkit-` prefix.

---

## 6. Multi-Layer Interactive Backgrounds

### Layer 1: Cursor-Following Gradient

JS sets CSS vars, CSS does the styling.

```css
.hero-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
    rgba(155, 48, 255, 0.12),
    transparent 60%
  );
  pointer-events: none;
}
```

### Layer 2: Grid/Dot Patterns

```css
/* Grid pattern */
.grid-bg {
  background-image:
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 40px 40px;
}

/* Masked grid (fades at edges — from erebora-umbrella) */
.hero__grid-bg {
  background-image:
    linear-gradient(var(--hero-grid-color) 1px, transparent 1px),
    linear-gradient(90deg, var(--hero-grid-color) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(ellipse 70% 50% at 50% 50%, black 20%, transparent 70%);
  -webkit-mask-image: radial-gradient(ellipse 70% 50% at 50% 50%, black 20%, transparent 70%);
}

/* Dot pattern */
.dot-bg {
  background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
  background-size: 24px 24px;
}
```

### Layer 3: SVG Grain Overlay (CSS-Only, Zero Perf Impact)

```css
.grain-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
  opacity: 0.03;
  z-index: 9999;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

---

## 7. Visual Details & Texture

**Circuit/node aesthetic:**
```css
.circuit-card::before {
  content: '';
  position: absolute;
  top: -3px; left: -3px;
  width: 6px; height: 6px;
  background: var(--accent-secondary);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--accent-secondary);
}
```

**Radial spotlight:**
```css
.hero-spotlight {
  position: absolute;
  width: 800px; height: 800px;
  background: radial-gradient(ellipse at center, rgba(155, 48, 255, 0.12) 0%, rgba(51, 102, 255, 0.06) 40%, transparent 70%);
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  filter: blur(60px);
}
```

**Animated border (Linear-style rotating gradient):**
```css
.highlight-card {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
}
.highlight-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(var(--border-angle, 0deg), transparent 40%, rgba(155, 48, 255, 0.5) 50%, transparent 60%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: border-rotate 4s linear infinite;
}
@keyframes border-rotate {
  to { --border-angle: 360deg; }
}
```

---

## 8. Aurora Keyframes (From erebora-umbrella)

```css
@keyframes aurora-drift-1 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  25% { transform: translate(30px, -20px) scale(1.05); }
  50% { transform: translate(-20px, 15px) scale(0.95); }
  75% { transform: translate(15px, 25px) scale(1.02); }
}

@keyframes aurora-drift-2 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  20% { transform: translate(-25px, 20px) scale(1.03); }
  40% { transform: translate(20px, -15px) scale(0.97); }
  60% { transform: translate(-15px, -25px) scale(1.05); }
  80% { transform: translate(25px, 10px) scale(0.98); }
}
```

Blobs: `position: absolute; border-radius: 50%; filter: blur(80px); animation: aurora-drift-N 15-25s ease-in-out infinite;`

---

## 9. Hover & Interaction States

```css
/* Card lift with glow */
.feature-card { transition: transform 0.3s ease, box-shadow 0.3s ease; }
.feature-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(155, 48, 255, 0.2); }

/* Button gradient shift */
.cta-btn {
  background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
  background-size: 200% 200%;
  transition: background-position 0.4s ease, transform 0.2s ease;
}
.cta-btn:hover { background-position: right center; transform: translateY(-2px); }

/* Arrow link animation */
.arrow-link::after { content: '\2192'; display: inline-block; transition: transform 0.2s ease; }
.arrow-link:hover::after { transform: translateX(4px); }
```

---

## 10. Spatial Composition

- **Z-pattern** for landing pages (logo top-left, nav top-right, content diagonal, CTA bottom-right)
- **Bento grids** -- varied-size for feature showcases, not uniform card grids
- **Section spacing**: `clamp(4rem, 8vw, 8rem)` padding
- **Container max**: 1100px for layouts, 700px for text content
- **CTA isolation**: Always 2rem+ margin around CTAs, highest contrast element

---

## 11. Responsive & Section Architecture

### Breakpoints (Mobile-First)

```css
/* Base = mobile */
@media (min-width: 768px) { /* Tablet: 2-col, larger type */ }
@media (min-width: 1024px) { /* Desktop: 3-col, full animations */ }
@media (min-width: 1440px) { /* Wide: max container, larger spacing */ }
```

### Universal Patterns (ALL Viewports)

These apply to desktop, tablet, AND mobile — not just phones:

```css
/* Section-based scroll architecture */
html {
  scroll-snap-type: y mandatory;
  overflow-y: scroll;
  scroll-behavior: smooth;
}

section {
  scroll-snap-align: start;
  scroll-snap-stop: always;
  min-height: 100vh; /* Fallback */
  min-height: 100svh; /* Safe: accounts for browser chrome */
}

/* Nav-height subtraction (fixed/sticky nav) */
:root { --nav-height: 60px; }
.hero { min-height: calc(100vh - var(--nav-height)); min-height: calc(100svh - var(--nav-height)); }
```

- **`svh` > `vh`**: `100vh` overflows when mobile browser chrome is visible. `100svh` = small viewport (safe). Always use `100vh` fallback + `100svh` override.
- **Scroll-snap**: ensures user NEVER sees a half-section on ANY device.
- **CTA above fold**: primary CTA must be visible without scrolling at ALL viewports, including worst-case 360x668 (Android + Chrome bars).
- **Section content must fit viewport**: each section designed to fit one viewport height. Use `min-height` (not fixed `height`) so sections CAN expand.

### Mobile-Specific Patterns (<768px)

```css
/* Disable CSS snap on desktop (GSAP handles it), enable on mobile */
@media (min-width: 769px) {
  html { scroll-snap-type: none; }
}

@media (max-width: 767px) {
  .features-grid { grid-template-columns: 1fr; }
}

@media (hover: hover) {
  .cursor-follower { display: block; }
}
```

- Reduce particles: 60 → 25 max
- Remove cursor effects: `@media (hover: hover)` gate
- Simplify glass: max 3 elements on mobile
- Stack grids: single column below 412px
- Touch targets: 44px minimum
- Disable Lenis on mobile (incompatible with CSS scroll-snap)
- Disable GSAP `snap` on mobile (CSS scroll-snap handles it on compositor thread)
- Safe area insets: `viewport-fit=cover` meta + `env(safe-area-inset-*)` padding

**Deep detail**: See `references/responsive-sections.md` for 15-section comprehensive guide covering GSAP+snap conflict resolution, nav-height subtraction, anchor-snap alignment, landscape degradation, and `prefers-reduced-motion`.
