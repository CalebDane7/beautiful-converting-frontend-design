# Performance Reference

Loaded during Phase 4 (Build). Every technique here is mandatory — beautiful animations are worthless if users bounce.

---

## Core Web Vitals Targets (MANDATORY)

| Metric | Target | What It Measures |
|--------|--------|-----------------|
| **LCP** | < 2.5s | Time to render biggest visible element |
| **INP** | < 200ms | Responsiveness — click/tap to visual update |
| **CLS** | < 0.1 | Visual stability — elements shouldn't jump |

Target: 90+ PageSpeed Insights score.

---

## Critical Rendering Path

```html
<head>
  <!-- 1. Preconnect to font CDN -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

  <!-- 2. Critical CSS inline (above-fold, under 14KB) -->
  <style>/* hero, nav, above-fold layout */</style>

  <!-- 3. External CSS -->
  <link rel="stylesheet" href="css/variables.css">
  <link rel="stylesheet" href="css/base.css">

  <!-- 4. Non-critical CSS deferred -->
  <link rel="stylesheet" href="css/animations.css" media="print" onload="this.media='all'">

  <!-- 5. Fonts with display=swap -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;700;800&display=swap">

  <!-- 6. Preload hero image -->
  <link rel="preload" as="image" href="hero.webp" fetchpriority="high">
</head>
<body>
  <!-- content -->

  <!-- 7. ALL JS at end of body with defer -->
  <script src="js/lenis.min.js" defer></script>
  <script src="js/gsap.min.js" defer></script>
  <script src="js/ScrollTrigger.min.js" defer></script>
  <script src="js/main.js" defer></script>
</body>
```

---

## Image Optimization

- WebP (25-34% smaller than JPEG), AVIF (50% smaller) with fallback
- Hero/LCP image: `fetchpriority="high"`, NO `loading="lazy"`
- Below-fold: `loading="lazy"`
- Always set `width` + `height` to prevent CLS
- Responsive: `srcset` + `sizes`
- Decorative SVGs: inline. Complex SVGs: external file.

---

## Font Performance

- Max 2 font families preloaded
- `font-display: swap` — shows fallback instantly
- Subset to latin — 100KB+ → under 20KB
- `size-adjust` on fallback prevents text reflow:

```css
@font-face {
  font-family: 'Geist Fallback';
  src: local('Arial');
  size-adjust: 100.5%;
  ascent-override: 96%;
}
```

- Self-host when possible (eliminates DNS lookup)

---

## Animation Performance Rules

| Safe (GPU composited) | NEVER Animate (triggers layout) |
|---|---|
| `transform` (translate, scale, rotate) | `width`, `height` |
| `opacity` | `top`, `left`, `right`, `bottom` |
| `filter` (sparingly) | `margin`, `padding` |
| `clip-path` | `font-size`, `border-width` |

- `will-change: transform` only on actively animating elements
- `contain: layout style paint` on animated containers
- Canvas: `requestAnimationFrame` only, never `setInterval`
- Pause canvas/particles off-screen (IntersectionObserver)
- Reduce particles on mobile (60 → 30)

---

## Motion Budgets By Mode

Pick a budget before implementing. If the concept does not fit the budget, lower the motion mode or simplify the effect.

| Motion Mode | Typical Site Type | Max Simultaneous Animated Planes | Heavy Blur Zones | WebGL | Notes |
|---|---|---:|---:|---|---|
| 0 | app/dashboard/docs | 1-2 | 0-1 | avoid | prioritize state clarity and responsiveness |
| 1 | SaaS/product/editorial | 2-3 | 1-2 | optional hero only | default mode for most projects |
| 2 | portfolio/campaign | 3-4 | 2-3 | allowed if justified | wow moment should stay localized |
| 3 | experimental microsite | 4 | 3 max | primary system allowed | only if perf is still credible on real hardware |

### Hard limits

- One WebGL scene per page is the default maximum.
- One shader-heavy hero is acceptable; shader-heavy sections repeated down the page are not.
- If FPS drops materially on mobile, remove the effect instead of keeping a degraded gimmick.
- Large `backdrop-filter` zones count as heavy effects. Budget them the same way you budget WebGL.

---

## Mobile / Low-Power Fallback Rules

- Detect `prefers-reduced-motion` and degrade before initializing expensive effects.
- Reduce particle counts, blur radii, and parallax travel on mobile.
- Disable pointer-reactive effects on coarse pointers and touch devices.
- If using Spline/Three.js, cap DPR aggressively and offer a static poster or CSS fallback.
- Dense app screens should remove ornamental continuous motion entirely on mobile.

---

## JavaScript Performance

- Passive event listeners: `{ passive: true }` for scroll/touch
- Break long tasks: `scheduler.yield()` or `setTimeout(0)`
- No synchronous layout reads in animation loops
- Minify: 30-50% size reduction
- Purge unused CSS (DevTools Coverage tab)

---

## Lazy Initialization

```javascript
var observer = new IntersectionObserver(function(entries) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting) {
      initParticleCanvas();
      observer.unobserve(entry.target);
    }
  });
}, { rootMargin: '200px' });
observer.observe(document.getElementById('hero-canvas'));
```

---

## Glass Performance

- 3-5 glass elements: negligible impact
- 10+: noticeable lag on mobile
- NEVER animate `backdrop-filter`
- Animate `opacity` or `transform` instead
- Extended blur zone: height 200% + mask-image
- Always `-webkit-` prefix for Safari

---

## Production Checklist

- [ ] Inline critical CSS (under 14KB)
- [ ] All JS `defer`, end of `<body>`
- [ ] Fonts: `display=swap`, preconnect, max 2, subset latin
- [ ] Hero image: WebP, preloaded, `fetchpriority="high"`, NOT lazy
- [ ] Below-fold images: `loading="lazy"`, explicit dimensions
- [ ] Animations: `transform`/`opacity` only
- [ ] Canvas: paused off-screen, reduced on mobile
- [ ] Motion mode selected and budget respected
- [ ] Heavy effects removed or downgraded on mobile / low-power devices
- [ ] No fake custom cursor / no forced intro loader
- [ ] Run Lighthouse — target 90+
