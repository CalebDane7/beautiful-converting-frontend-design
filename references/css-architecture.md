# CSS Architecture Reference

Loaded during Phase 4 (Build). All CSS decisions flow from this file.

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

## 11. Responsive Breakpoints (Mobile-First)

```css
/* Base = mobile */
@media (min-width: 768px) { /* Tablet: 2-col, larger type */ }
@media (min-width: 1024px) { /* Desktop: 3-col, full animations */ }
@media (min-width: 1440px) { /* Wide: max container, larger spacing */ }
```

Mobile adjustments: Reduce particles (60 to 30), remove cursor effects, simplify glass, stack grids, 44px touch targets.
