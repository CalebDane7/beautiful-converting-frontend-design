# Premium 3D Buttons — Tactile, High-Class, Animated

Buttons are the most-touched object on a page. On premium/expressive surfaces they must feel like
**real, physical, high-tech controls** — visible depth, a hover that lifts and catches light, and a
**tactile press that slams down**. Flat fills with a color-change hover read cheap. This reference
gives the recipes and the timing that make buttons feel expensive.

## When to apply
- **Apply** to primary CTAs, hero actions, mode toggles, and any key interactive button on dark
  luxury / fintech / product / campaign surfaces.
- **Skip** (keep flat/quiet) for dense toolbars, table-row actions, tertiary text links, and
  disabled/utility chrome where depth would add noise.

## The core idea (3 states, asymmetric timing)
1. **Rest** — the button is raised and shows a **3D edge/rim** (a hard colored shadow below it).
2. **Hover** — it **lifts** (`translateY`), **brightens**, a **specular glare** sweeps, the rim grows.
3. **Press (`:active`)** — it **slams down** fast and the rim **collapses** → a real tactile click.

**The tactile secret is asymmetric timing:** a lightning press (~34ms), a springy hover rise
(~220ms with overshoot), and a leisurely settle (~600ms). Same speed everywhere = lifeless.

```css
:root {
  --ease-press:        cubic-bezier(0.3, 0.7, 0.4, 1);    /* grounded settle */
  --ease-press-spring: cubic-bezier(0.3, 0.7, 0.4, 1.5);  /* hover overshoot */
}
```

## Technique A — Single-element chunky hard-3D push (RECOMMENDED default)
Upgrades a plain `<button class="btn">` with **no extra markup**. The "rim" is a hard colored
`box-shadow`; the press is a `translateY` that collapses the rim. Token-driven so it re-themes.

```css
.btn {
  position: relative;
  border: none;
  border-radius: 12px;
  padding: 12px 28px;
  font-weight: 700;
  cursor: pointer;
  transform: translateY(0);
  transition: transform .12s var(--ease-press), box-shadow .12s var(--ease-press), filter .2s ease;
  will-change: transform;
}
.btn-primary {
  color: #fff;
  background: var(--brand-gradient, linear-gradient(120deg, #ff3b5c, #a855f7 50%, #3b82f6));
  box-shadow:
    inset 0 2px 0 rgba(255,255,255,.5),       /* top bevel highlight */
    inset 0 -3px 7px rgba(0,0,0,.28),         /* inner bottom shade */
    0 7px 0 var(--btn-rim, #3a1d6b),          /* THE 3D RIM (hard, darker) */
    0 12px 24px rgba(168,85,247,.45),         /* colored glow */
    0 16px 32px rgba(0,0,0,.5);               /* ground shadow */
}
.btn:hover  { transform: translateY(-2px); filter: brightness(1.08);
  transition: transform .22s var(--ease-press-spring), box-shadow .22s var(--ease-press-spring), filter .2s ease; }
.btn-primary:hover {                           /* rim grows, glow intensifies */
  box-shadow: inset 0 2px 0 rgba(255,255,255,.6), inset 0 -3px 7px rgba(0,0,0,.28),
    0 9px 0 var(--btn-rim,#3a1d6b), 0 16px 34px rgba(168,85,247,.6), 0 20px 40px rgba(0,0,0,.55); }
.btn:active { transform: translateY(5px); transition: transform 34ms ease, box-shadow 34ms ease; }
.btn-primary:active {                          /* rim COLLAPSES → tactile slam */
  box-shadow: inset 0 2px 0 rgba(255,255,255,.4), inset 0 -2px 5px rgba(0,0,0,.3),
    0 1px 0 var(--btn-rim,#3a1d6b), 0 4px 10px rgba(168,85,247,.4), 0 5px 12px rgba(0,0,0,.45); }
.btn:focus-visible { outline: 3px solid var(--focus-ring, #a855f7); outline-offset: 3px; }
```

### Specular glare (catches the light on hover)
```css
.btn-primary::after {
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(118deg, transparent 32%, rgba(255,255,255,.5) 50%, transparent 68%);
  background-size: 230% 100%; background-position: 150% 0; mix-blend-mode: screen;
  transition: background-position .6s cubic-bezier(.22,1,.36,1);
}
.btn-primary:hover::after { background-position: -50% 0; }   /* glare sweeps across */
```

## Technique B — Josh-Comeau layered (front / edge / shadow)
Max polish when you control the markup. Three layers; the shadow moves OPPOSITE the front.
Source: joshwcomeau.com/animation/3d-button.

```html
<button class="pushable"><span class="shadow"></span><span class="edge"></span><span class="front">Push me</span></button>
```
```css
.pushable { position: relative; border: none; background: transparent; padding: 0; cursor: pointer; }
.shadow, .edge { position: absolute; inset: 0; border-radius: 12px; }
.shadow { background: hsl(0 0% 0% / .25); transform: translateY(2px); transition: transform .6s var(--ease-press); }
.edge   { background: linear-gradient(to left, hsl(266 70% 22%), hsl(266 70% 40%) 8%, hsl(266 70% 40%) 92%, hsl(266 70% 22%)); }
.front  { display: block; position: relative; padding: 12px 42px; border-radius: 12px;
          background: hsl(266 85% 58%); color: #fff; transform: translateY(-4px); transition: transform .6s var(--ease-press); will-change: transform; }
.pushable:hover { filter: brightness(1.1); }
.pushable:hover .front  { transform: translateY(-6px); transition: transform .25s var(--ease-press-spring); }
.pushable:hover .shadow { transform: translateY(4px);  transition: transform .25s var(--ease-press-spring); }
.pushable:active .front  { transform: translateY(-2px); transition: transform 34ms; }
.pushable:active .shadow { transform: translateY(1px);  transition: transform 34ms; }
```

## Technique C — Neumorphic press (soft, calm, least aggressive)
For wellness/utility surfaces. Dual-shadow emboss; press = inset.
```css
.neu-btn { background: var(--neu-bg,#e0e5ec); border-radius: 14px; padding: 12px 28px; border: none; cursor: pointer;
  box-shadow: 6px 6px 12px rgba(0,0,0,.18), -6px -6px 12px rgba(255,255,255,.7); transition: box-shadow .12s ease, transform .12s ease; }
.neu-btn:active { box-shadow: inset 4px 4px 8px rgba(0,0,0,.2), inset -4px -4px 8px rgba(255,255,255,.7); transform: translateY(1px); }
```

## Accessibility + reduced-motion (REQUIRED)
- Always a real `<button>` (or `<a>` for navigation) — never a styled `<div>`.
- Visible `:focus-visible` ring; **touch target ≥ 44×44px**.
- `box-shadow` rims are NOT clipped by `overflow: hidden`, so the rim shows even on clipped buttons.
- Animate only `transform`, `box-shadow`, `filter`, `background-position` — never `width/height/top/left`.
```css
@media (prefers-reduced-motion: reduce) {
  .btn, .btn:hover, .btn:active { transition: box-shadow .1s ease, filter .1s ease; }
  .btn:hover { transform: none; }
  .btn:active { transform: translateY(3px); }   /* keep a small press for feedback */
}
```

## Anti-patterns
- **Flat lifeless button on a premium/expressive surface** (the #1 cheap tell). Give it real depth.
- Symmetric timing (same duration for press + hover + return) — kills the tactile feel.
- Animating `box-shadow` blur on large elements (jank) — use the hard-rim + `transform` approach.
- Replacing `<button>` with a `<div>` (breaks keyboard, focus, semantics).
- A glow with no edge: glow alone reads like a halo, not a physical button. The **rim** is what sells depth.
```
