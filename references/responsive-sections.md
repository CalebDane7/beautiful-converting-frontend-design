# Responsive Section Architecture (Universal)

Reference for building section-based pages that snap into full view on ANY device. Every section must fit within one viewport height. The primary CTA must be visible without scrolling on ANY screen size.

---

## 1. Viewport Height Units (ALL DEVICES)

Every section MUST use the two-line `min-height` pattern: a `100vh` fallback followed by `100svh`. This is non-negotiable.

On desktop, `svh` equals `vh` because there is no browser chrome that appears/disappears, so the fallback is harmless. On mobile, `100vh` includes the area behind the browser's address bar and bottom toolbar, meaning content overflows the visible area. `100svh` accounts for chrome being visible and gives you the actual usable height.

```css
.section {
  min-height: 100vh; /* Fallback for older browsers */
  min-height: 100svh; /* Safe: accounts for browser chrome on mobile */
}
```

### Viewport unit comparison

| Unit | Meaning | When Chrome Visible | Use For |
|------|---------|-------------------|---------|
| `vh` | Large viewport | Overflows (100vh > visible area) | NEVER for layout heights |
| `svh` | Small viewport (chrome visible) | Fits perfectly | Section heights, hero |
| `dvh` | Dynamic (animates with chrome) | Causes reflow jank | NEVER for layout |
| `lvh` | Large viewport (chrome hidden) | Same as `vh` | NEVER for layout |

**Why NOT `dvh`?** When the user scrolls on mobile, the browser chrome animates in and out. `dvh` changes value continuously during that animation, causing the section height to reflow on every frame. This produces visible jank (content jumping, layout shifts). `svh` picks the smallest safe value and stays fixed.

**Why NOT `vh`?** On mobile Chrome and Safari, `100vh` is taller than the visible area when the address bar is showing. A CTA at the bottom of a `100vh` section is hidden behind the browser toolbar. `svh` guarantees the section fits the visible area.

**Browser support:** `svh` is supported in Chrome 108+, Safari 15.4+, Firefox 101+, Samsung Internet 21+. The `100vh` fallback covers everything older. This two-line pattern is safe to ship today.

---

## 2. Scroll-Snap for Section-Based Pages — CONDITIONAL

Scroll-snap forces the browser to align sections to viewport boundaries after the user finishes scrolling. When it works, the user NEVER sees a half-section. But snap only works when ALL snapping sections fit within the viewport height. **Snap is conditional, not automatic.**

### Decision tree: Should this page use scroll-snap?

1. **New build (designing from scratch)?** Design each section to fit one viewport at ALL breakpoints (desktop 1280x800, tablet 768x1024, android-narrow 360x780, android-worst 360x668). If ALL sections fit → use `scroll-snap-type: y mandatory`. This delivers the best UX.

2. **Pre-existing site / variable-height content?** Measure every section at every breakpoint. If ANY section exceeds viewport height at ANY breakpoint → **DO NOT use snap globally.** Snap on tall sections traps users — they physically cannot scroll past the section because snap keeps pulling them back.

3. **Mixed situation (most sections fit, 1-2 don't)?** Two options:
   - Exempt tall sections with `scroll-snap-align: none` on those specific sections. Adjacent sections still snap normally.
   - Use `scroll-snap-type: y proximity` instead of `mandatory` — snaps only when close to a boundary, doesn't trap users in tall sections.

4. **GSAP-pinned sections?** Sections using GSAP ScrollTrigger `pin: true` MUST be exempted from snap (`scroll-snap-align: none`). The pin extends the section's scroll range far beyond viewport height — snap would fight the pin.

### When ALL sections fit (use snap):

```css
html {
  scroll-snap-type: y mandatory;
  overflow-y: scroll;
  scroll-behavior: smooth;
}

section {
  scroll-snap-align: start;
  scroll-snap-stop: always;
  min-height: 100vh;
  min-height: 100svh;
}
```

### When sections DON'T all fit (NO snap):

```css
/* No scroll-snap-type on html */
/* No scroll-snap-align on sections */
/* Sections use natural flow — no min-height forced */

section {
  padding: clamp(4rem, 10vh, 8rem) 0;
  /* Content determines height naturally */
}
```

### Key properties (when snap IS used)

- **`scroll-snap-type: y mandatory`** on `html`: forces snap after every scroll. Only use when ALL sections fit viewport.
- **`scroll-snap-type: y proximity`**: snaps only when close to a boundary. Fallback when most sections fit but 1-2 don't.
- **`scroll-snap-align: start`** on each `<section>`: top edge aligns with viewport top.
- **`scroll-snap-stop: always`**: prevents fast swipes from skipping sections.
- **`overflow-y: scroll`**: MUST be on snap container or browser ignores snap entirely.
- **`scroll-snap-align: none`** on individual sections: exempts them from snapping (for pinned or tall sections).

### Anti-patterns

- **NEVER add snap to a page with variable-height sections without verifying fit at every breakpoint.** This is the #1 cause of broken mobile scroll.
- **NEVER use `mandatory` snap with GSAP-pinned sections.** Pin extends scroll range → snap traps users.
- **NEVER retrofit snap onto an existing site without measuring every section.** If the content wasn't designed for snap, snap will break the scroll experience.

### Cross-browser notes

Scroll-snap is a CSS-only, compositor-thread feature. It does not require JavaScript, has no jank (no main-thread blocking), and works on all modern browsers. It is the correct snapping mechanism for mobile devices — but ONLY when sections are designed to fit.

---

## 3. GSAP ScrollTrigger + Scroll-Snap Coexistence (ALL DEVICES)

### The conflict

GSAP's `ScrollTrigger.snap` and CSS `scroll-snap-type` both try to control scroll position after the user stops scrolling. If both are active, they fight: CSS snap jumps to one position, GSAP tweens to another, CSS snap reacts to the tween, and the page oscillates or locks up. They are mutually exclusive snapping mechanisms.

### The strategy: split by device

- **Desktop (769px+):** Use GSAP `ScrollTrigger.snap` for smooth, eased, animated snapping. Disable CSS `scroll-snap-type` via media query. GSAP snap runs on the main thread but desktop has enough CPU headroom.
- **Mobile (<=768px):** Use CSS `scroll-snap-type: y mandatory` for compositor-thread snapping (zero jank, zero CPU cost). Keep GSAP ScrollTrigger for entrance animations (fade-in, slide-up) but do NOT use GSAP's `snap` property. The result is the same user experience — sections snap into view — but the mechanism differs by platform.

```css
/* Mobile: CSS scroll-snap (compositor thread, zero jank) */
html {
  scroll-snap-type: y mandatory;
}

/* Desktop: disable CSS snap, let GSAP handle it */
@media (min-width: 769px) {
  html {
    scroll-snap-type: none;
  }
}
```

```js
const isMobile = window.matchMedia('(max-width: 768px)').matches;

// GSAP snap on desktop ONLY
if (!isMobile) {
  ScrollTrigger.create({
    snap: 1 / (sections.length - 1),
    duration: 0.5,
    ease: 'power2.inOut',
  });
}

// Entrance animations on ALL devices (not snap, just animations)
sections.forEach(section => {
  gsap.from(section.children, {
    scrollTrigger: {
      trigger: section,
      start: 'top 85%',
      toggleActions: 'play none none none',
    },
    opacity: 0,
    y: 40,
    stagger: 0.1,
    duration: 0.8,
  });
});
```

### Why `start: 'top 85%'`?

On mobile with CSS snap, the viewport jumps directly to a section boundary. If the trigger start is `top center` (50%), the animation fires when the section top crosses the viewport center — but with mandatory snap, the section top is almost immediately at `top top` (0%). Setting `start: 'top 85%'` means the animation fires as soon as the section enters the viewport from below, which is the only scroll position you reliably hit during a snap transition.

---

## 4. Lenis Configuration (DESKTOP vs MOBILE)

Lenis provides smooth, lerped scrolling that feels premium on desktop. However, Lenis intercepts native scroll events and does not support CSS `scroll-snap-type`. On mobile, where CSS scroll-snap is the snapping mechanism, Lenis must be disabled entirely.

```js
if (window.matchMedia('(min-width: 769px)').matches) {
  const lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((time) => lenis.raf(time * 1000));
  gsap.ticker.lagSmoothing(0);
}
// Mobile: native scroll + CSS scroll-snap. No Lenis.
```

### Desktop pipeline

1. User scrolls (wheel/trackpad)
2. Lenis intercepts the scroll event and applies lerped smooth scrolling
3. Lenis fires `scroll` events that update GSAP ScrollTrigger
4. GSAP ScrollTrigger handles snapping via its `snap` property
5. GSAP ScrollTrigger fires entrance animations via individual triggers

### Mobile pipeline

1. User swipes (touch)
2. Browser handles scroll natively (compositor thread)
3. CSS `scroll-snap-type: y mandatory` snaps to section boundaries
4. GSAP ScrollTrigger fires entrance animations (no snap, just `toggleActions`)

### Why `lagSmoothing(0)`?

GSAP's default lag smoothing can cause Lenis's scroll position to desync from ScrollTrigger's internal position. Disabling it ensures 1:1 sync.

---

## 5. Above-Fold CTA Content Budget (ALL DEVICES)

The primary call-to-action button MUST be visible without scrolling on EVERY viewport size. This is the single most important conversion constraint.

### Available space by device

- **Desktop (1280x800):** 800px viewport height. Subtract 60-80px nav. ~720px available. CTA easily above fold.
- **Tablet portrait (768x1024):** 1024px viewport height. Even more space than desktop.
- **Android standard (412x915):** 915px viewport. Subtract 56px chrome top + 56px chrome bottom + 60px nav = ~743px. Comfortable.
- **Android worst case (360x668):** This is a 360px-wide phone (Galaxy S series, etc.) with Chrome address bar AND bottom toolbar visible. 780px viewport - 56px top chrome - 56px bottom chrome = 668px CSS pixels. Subtract 60px nav = **608px** for hero content.

Design the hero to fit at 360x668. All larger viewports automatically have surplus space.

```css
.hero {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  min-height: 100svh;
  padding: var(--nav-height, 60px) clamp(1rem, 5vw, 2rem) 2rem;
}

.hero__content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 1rem;
}

.hero__cta {
  margin-top: auto; /* Pins CTA to bottom of hero if needed */
}

.hero__headline {
  font-size: clamp(2rem, 6vw, 3.5rem);
  line-height: 1.1;
}

.hero__subhead {
  font-size: clamp(1rem, 2.5vw, 1.25rem);
  line-height: 1.4;
}
```

### Content budget at 360x668

- Nav: 60px
- Top padding: 16px
- Headline (2rem, 2 lines): ~70px
- Gap: 16px
- Subhead (1rem, 3 lines): ~67px
- Gap: 16px
- CTA button: 48px
- Bottom padding: 32px
- **Total: ~325px** — fits in 608px with 283px to spare for imagery/spacing

### Body text minimum

All body text must be at least **16px** (`1rem`). Below 16px, iOS Safari auto-zooms when the user taps an input field inside or near the text. This breaks the layout and disorients the user. 16px is the threshold that prevents auto-zoom.

---

## 6. Section Content Must Fit Viewport (ALL DEVICES)

The fundamental constraint of section-based design: each `<section>` must have ALL its content visible within one viewport height. If the user has to scroll within a section, the snap behavior fights them.

### Design principles

- Use `min-height: 100svh` (not fixed `height: 100svh`) so sections CAN expand if content overflows. `min-height` is a safety valve — it prevents content from being clipped.
- **Desktop sections:** side-by-side layouts (2-3 columns) keep content vertically compact. A 3-column feature grid fits in one viewport. A 2-column pricing comparison fits in one viewport.
- **Mobile sections:** single-column stacked layouts. Content must be condensed or split across multiple sections. A 3-column feature grid becomes a single-column list or a swipeable carousel.
- **Test at these viewports:**
  - Desktop: 1280x800
  - Tablet portrait: 768x1024
  - Android standard: 412x915
  - Android narrow: 360x780
  - Android worst case: 360x668

### When content exceeds the viewport

If a section's content is taller than the viewport at a specific breakpoint, you have two options:

1. **Reduce content** for that breakpoint: collapse lists into accordions, replace grids with carousels, shorten copy, hide secondary elements.
2. **Switch snap behavior** for that section: add `scroll-snap-align: none` on that specific section (see Section 13).

Option 1 is always preferred. Option 2 is the escape hatch.

---

## 7. Android-Specific CSS Patterns

Android devices represent the tightest width constraints. 360px CSS width is the narrowest modern flagship screen. All horizontal sizing must account for this.

### Key Android CSS viewport sizes

| Device | Width | Height | DPR |
|--------|-------|--------|-----|
| Galaxy S24/S23/S22/A15 | 360 | 780 | 3.0 |
| Galaxy S23+/S21 Ultra | 384 | 824 | 3.0 |
| Pixel 5/4a, Galaxy Z Flip6 | 393 | 851 | 2.75 |
| Pixel 8/7/6, Galaxy A54/A53 | 412 | 915 | 2.625 |

### Browser chrome steals vertical space

- Chrome address bar: **56px**
- Chrome bottom toolbar: **56px**
- Worst case usable height: 780 - 56 - 56 = **668px**

This is why `100svh` exists — it equals 668px when chrome is visible, not 780px.

### Horizontal layout rules

- **Container padding:** `clamp(1rem, 5vw, 2rem)` — at 360px this yields 18px per side, leaving 324px content width. At 412px, it yields 20.6px per side.
- **Never use 2-column grid below 412px.** At 360px with padding, each column would be ~150px wide — too narrow for readable text + a card component.
- **Single column is mandatory below 412px** unless items are very narrow (icons, avatar thumbnails).

### CSS patterns for Android

```css
/* Container */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding-inline: clamp(1rem, 5vw, 2rem);
}

/* Aspect ratio for responsive media (replaces padding-bottom hack) */
.media-container {
  aspect-ratio: 16 / 9;
  width: 100%;
  overflow: hidden;
}

/* Font sizing that floors at readable on 360px */
.heading {
  font-size: clamp(1.75rem, 5vw, 3rem);
}

.body-text {
  font-size: clamp(1rem, 2.5vw, 1.125rem);
}
```

### `aspect-ratio` vs padding-bottom hack

The old technique for responsive containers was `padding-bottom: 56.25%` (for 16:9). The modern replacement is `aspect-ratio: 16 / 9`. It is supported in all browsers that support `svh`. Use `aspect-ratio` exclusively.

---

## 7b. Heading Word-Wrap Safety (MANDATORY)

Headings must NEVER break mid-word. Different browsers have different font metrics — a word that fits in desktop Chromium may not fit on a real Android phone with the same CSS. The ONLY safe approach is to prevent mid-word breaks entirely.

```css
h1, h2, h3, h4, h5, h6 {
  overflow-wrap: normal;  /* NEVER break words mid-word */
  word-break: normal;
  hyphens: none;
}
```

### Why `overflow-wrap: normal` (not `break-word`)?

`overflow-wrap: break-word` tells the browser: "If a word doesn't fit on the current line, you MAY break it mid-word." This sounds harmless on desktop where words usually fit. But on a 360px Android screen with different font rendering, the browser calculates that "mistakes." is too wide and splits it as "mi" / "stakes." — a critical visual defect.

With `overflow-wrap: normal`, the browser NEVER splits words. If a word doesn't fit, it overflows (which is visible and fixable) rather than silently breaking mid-word (which looks broken and is hard to detect in testing).

### Rules

- **Headings (h1-h6):** Always `overflow-wrap: normal; word-break: normal; hyphens: none;`
- **Body text (p, li, td):** Can use `overflow-wrap: break-word` — mid-word breaks in paragraphs are acceptable for long URLs or technical strings.
- **If a heading overflows at narrow viewports:** Fix the design (reduce font-size via `clamp()`, shorten text, use `<br class="mobile-only">` for explicit break points). NEVER enable `break-word` on headings.
- **Non-breaking spaces (`&nbsp;`):** NEVER use `&nbsp;` in headings. Use `<span style="white-space:nowrap">words to keep together</span>` instead. `&nbsp;` creates unbreakable units that can exceed viewport width, forcing mid-word breaks as a last resort.

### SplitType and text-splitting libraries (CRITICAL)

SplitType, GSAP SplitText, and similar libraries split text into individual `<div>` or `<span>` elements. When `types: 'chars'` is used, each character becomes a separate `display: inline-block` element. The browser breaks between ANY two — `overflow-wrap: normal` has zero effect because the word no longer exists as a single text node.

**Mandatory rules:**
1. Use `types: 'words, chars'` (NOT just `'chars'`) — wraps chars in word-level containers, preventing mid-word breaks DURING animation
2. ALWAYS call `split.revert()` after animation — but use the RIGHT method depending on context

**For timeline animations with stagger:**
```js
// CORRECT — timeline.call() fires exactly ONCE at calculated position:
var split = new SplitType(heading, { types: 'words, chars' });
tl.fromTo(split.chars,
  { opacity: 0, y: 20 },
  { opacity: 1, y: 0, duration: 0.6, stagger: 0.025,
    ease: 'power3.out'
  }, 0
);
var revertTime = 0.6 + 0.025 * (split.chars.length - 1) + 0.3;
tl.call(function() { split.revert(); }, null, revertTime);

// WRONG — onComplete in staggered timeline tweens may fire per-element:
tl.fromTo(split.chars, {}, { stagger: 0.025,
  onComplete: function() { split.revert(); }  // fires after FIRST char, destroys all mid-animation
});
```

**For ScrollTrigger animations (per-element forEach):**
```js
// CORRECT — onEnter + delayedCall:
titles.forEach(function(title) {
  var split = new SplitType(title, { types: 'words' });
  var wordCount = split.words.length;
  gsap.fromTo(split.words,
    { autoAlpha: 0, y: 24 },
    { autoAlpha: 1, y: 0, duration: 0.5, stagger: 0.04, ease: 'power3.out',
      scrollTrigger: {
        trigger: title, start: 'top 85%',
        onEnter: function() {
          gsap.delayedCall(0.5 + 0.04 * wordCount + 0.3, function() { split.revert(); });
        }
      }
    }
  );
});

// WRONG — no revert, word elements persist forever:
gsap.fromTo(split.words, { opacity: 0 }, { opacity: 1 });
// split.revert() never called
```

This applies to ALL text-splitting libraries. If you split text for animation, you MUST revert after.

---

## 8. Content Adaptation by Breakpoint

Different viewport sizes require different content strategies, not just different layouts. Features that enhance desktop experience actively harm mobile performance and usability.

### Breakpoint strategy

- **Desktop (1024px+):** Full animations, cursor-follow effects, particle backgrounds, parallax, side-by-side section layouts (2-3 columns), hover states.
- **Tablet (768-1023px):** Reduced particle count, no cursor effects, 2-column where appropriate, simplified animations.
- **Mobile (<768px):** Maximum 25 particles, no cursor-follow effects, maximum 3 glass/blur elements (GPU cost), single-column stacked, simplified animations (fade + slide only).

### Cursor-dependent features

Use `@media (hover: hover)` to gate features that require a mouse cursor. Touch devices report `hover: none`. This is more reliable than width-based media queries for this purpose.

```css
@media (hover: hover) {
  .cursor-follower { display: block; }
  .card:hover { transform: translateY(-4px); }
}

@media (max-width: 767px) {
  .features-grid { grid-template-columns: 1fr; }
  .glass-card:nth-child(n+4) .glass-effect { display: none; }
}
```

### Mobile content patterns

Desktop components often cannot fit in a mobile viewport without adaptation:

- **Feature grid (3-4 items):** becomes a swipeable horizontal carousel or a vertical list with icons.
- **FAQ section (6+ items):** becomes an accordion. Only one item open at a time. This collapses ~600px of content into ~300px.
- **Pricing table (3 columns):** becomes a swipeable card stack or a tabbed interface showing one plan at a time.
- **Team grid (6+ members):** becomes a horizontal scroll strip with small avatars, tapping for detail.
- **Testimonials (3 cards):** becomes an auto-playing carousel with dots.

### GPU budget on mobile

Glass/blur effects (`backdrop-filter: blur()`) are expensive on mobile GPUs. Each glass element creates a separate compositing layer. Limit to 3 glass elements visible simultaneously on mobile. Hide glass effects on elements beyond the third:

```css
@media (max-width: 767px) {
  .glass-card:nth-child(n+4) .glass-effect {
    display: none;
  }
}
```

---

## 9. Sticky Nav Height Subtraction (ALL DEVICES)

Every section-based page has a navigation bar, typically 60-80px tall. This nav bar sits on top of the first section and can overlap content if not accounted for.

### The problem

`min-height: 100svh` means the section fills the viewport. But if a fixed/sticky nav sits on top of the section, the section's content area is actually `100svh - nav_height`. The bottom of the section's content extends behind the nav of the next section or below the viewport fold.

### Fixed nav vs sticky nav

- **Fixed nav** (`position: fixed`): the nav stays at the top at all times. EVERY section needs `min-height: calc(100svh - var(--nav-height))` because the nav always overlaps.
- **Sticky nav that scrolls away** (`position: sticky` on a wrapper, or the nav scrolls with the first section): only the hero needs the subtraction. Subsequent sections occupy the full viewport because the nav is no longer visible.

```css
:root {
  --nav-height: 60px;
}

/* If nav is fixed/sticky and always visible */
.section {
  min-height: calc(100vh - var(--nav-height));
  min-height: calc(100svh - var(--nav-height));
}

/* If nav scrolls away, only hero needs subtraction */
.hero {
  min-height: calc(100vh - var(--nav-height));
  min-height: calc(100svh - var(--nav-height));
}
.section:not(.hero) {
  min-height: 100vh;
  min-height: 100svh;
}
```

### Padding-top approach

An alternative to `calc()` subtraction is adding `padding-top: var(--nav-height)` to each section. This keeps `min-height: 100svh` unchanged but pushes content down below the nav. The downside: the section is now taller than the viewport by `nav-height`, which can cause scroll-snap to show a sliver of the next section. The `calc()` approach is more reliable.

### Testing

At 360x668 (worst case mobile), the hero content area with a 60px nav is 668 - 60 = **608px**. Verify that headline + subhead + CTA + padding fit within 608px. If they don't, the CTA is below the fold on the smallest supported device.

---

## 10. Scroll-to-Anchor + Snap Coexistence

Section-based pages typically have internal navigation links (`#pricing`, `#features`, `#contact`). Clicking these while scroll-snap is active can cause conflicts if the anchor target is not aligned with a snap point.

### The rule

The `id` attribute MUST be on the `<section>` element itself, NOT on a child element inside the section.

**Correct:** the anchor scrolls to the section top, which is a snap point. The browser snaps cleanly.

```html
<section id="pricing" class="snap-section">
  <h2>Pricing</h2>
  ...
</section>
```

**Incorrect:** the anchor scrolls to the `<h2>` inside the section, which is NOT a snap point. The browser scrolls to the `<h2>`, then snap kicks in and pulls the viewport to the nearest snap point (the section top), causing a visible jump.

```html
<section>
  <h2 id="pricing">Pricing</h2>
  ...
</section>
```

### Smooth scrolling

`scroll-behavior: smooth` on `html` enables smooth programmatic scrolling. When the user clicks `<a href="#pricing">`, the browser smoothly scrolls to `#pricing`, and snap takes over at the end to align precisely. This produces a polished experience.

```css
html {
  scroll-behavior: smooth;
  scroll-snap-type: y mandatory;
  overflow-y: scroll;
}
```

### JavaScript navigation

If using JavaScript to scroll to sections (e.g., a custom nav component), use `element.scrollIntoView({ behavior: 'smooth' })`. The browser's scroll-snap will finalize the position after the smooth scroll completes.

```js
document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(anchor.getAttribute('href'));
    target.scrollIntoView({ behavior: 'smooth' });
  });
});
```

Because the `id` is on the `<section>` (which has `scroll-snap-align: start`), `scrollIntoView` and scroll-snap agree on the target position. No conflict.

---

## 11. GSAP ScrollTrigger Animation Timing with CSS Snap (MOBILE)

On mobile, CSS `scroll-snap-type: y mandatory` causes the viewport to jump directly from one section boundary to the next. This is fundamentally different from the smooth, continuous scrolling on desktop (with or without Lenis). GSAP ScrollTrigger animations must be configured to work with this jump behavior.

### The problem

GSAP ScrollTrigger calculates animation progress based on continuous scroll position. A trigger with `start: 'top center'` and `end: 'bottom center'` expects the scroll position to pass through every pixel between start and end. With CSS snap, the viewport jumps from section N to section N+1 in one frame. If the trigger range is narrow, the animation fires and completes in one frame — no visible transition.

### The solution

Use `toggleActions: 'play none none none'` with an early trigger start. This fires the animation as a discrete event (play once) rather than scrubbing through it based on scroll position.

```js
// Mobile-safe animation pattern
ScrollTrigger.create({
  trigger: section,
  start: 'top 85%',
  toggleActions: 'play none none none',
  onEnter: () => gsap.to(section.children, {
    opacity: 1, y: 0, stagger: 0.1, duration: 0.6
  })
});
```

### Why `start: 'top 85%'`?

When the user swipes to a new section, the browser starts scrolling, and at some point CSS snap accelerates the viewport to the section boundary. The animation trigger must fire during that transition, not after the snap completes. `top 85%` means "fire when the section top enters the bottom 15% of the viewport" — early enough that it triggers mid-snap on most devices.

### Parallax on mobile

Parallax effects (elements moving at different scroll speeds) depend on continuous scroll position. With CSS snap jumping between sections, parallax produces abrupt jumps instead of smooth motion. On mobile, replace parallax with simple fade-in + slide-up entrance animations.

### Desktop behavior

On desktop with GSAP snap (no CSS snap), scroll position changes continuously (Lenis lerps it). ScrollTrigger animations work normally — scrub-based timelines, parallax, and all continuous effects function as expected.

---

## 12. Safe Area Insets (Notched/Rounded Devices)

Modern phones have notches (iPhone), hole-punch cameras (Samsung), rounded display corners, and gesture bars at the bottom. Content placed at the very edges of the screen can be obscured by these hardware features.

### Viewport meta tag

The viewport meta tag MUST include `viewport-fit=cover` to extend the page into the safe area. Without this, the browser adds black bars around the content on notched devices, wasting screen real estate.

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

### Safe area CSS

Use `env(safe-area-inset-*)` to add padding where hardware features might obscure content.

```css
.page-container {
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

.sticky-cta, .fixed-nav {
  padding-bottom: env(safe-area-inset-bottom);
}
```

### Where to apply insets

- **Left/right insets:** Apply to the outermost page container. These protect against rounded corners and landscape notches. Values: 0px on most portrait phones, up to 44px in landscape on iPhones with notch.
- **Bottom inset:** Apply to any fixed or sticky element at the bottom of the screen (CTAs, bottom navs, cookie banners). The gesture bar on modern iPhones is ~34px tall. Without `env(safe-area-inset-bottom)`, a fixed CTA button sits behind the gesture bar and is difficult to tap.
- **Top inset:** Usually handled by the browser's status bar. Rarely needed in CSS unless you have a fullscreen app.

### Fallback behavior

On devices without notches, rounded corners, or gesture bars, all `env(safe-area-inset-*)` values resolve to `0`. The padding has no visual impact. This makes it safe to include universally.

### Combining with existing padding

```css
.fixed-cta {
  padding-bottom: calc(1rem + env(safe-area-inset-bottom));
}
```

This ensures at least `1rem` of padding on non-notched devices, plus the safe area offset on notched devices.

---

## 13. Sections Taller Than Viewport -- Escape Hatch

Not every section can fit within one viewport height at every breakpoint. FAQ sections, detailed pricing tables, and team grids are common offenders. This section defines the decision tree for handling overflow.

### Decision tree

1. **Can the content be condensed?** Use an accordion for FAQ, tabs for pricing plans, a carousel for team members. This is the PREFERRED approach. It keeps `mandatory` snap and maintains the section-based experience.

2. **Still too tall after condensing?** Apply `scroll-snap-align: none` on THAT specific section. This exempts the section from snapping — the user can scroll through it freely, and the next snap point is the following section.

3. **Alternative: split into sub-sections.** Break a long section into two snap-aligned sections. For example, a "Features" section with 6 features becomes "Features Part 1" (3 features) and "Features Part 2" (3 features), each fitting one viewport.

### Code

```css
.section--tall {
  scroll-snap-align: none;
  min-height: auto; /* Remove both snap AND min-height */
}
```

When `scroll-snap-align: none` is used, also remove `min-height: 100svh`. The section should be as tall as its content — forcing it to at least one viewport height when it's already too tall makes no sense.

### Detection

A visual QA script can flag sections that exceed the viewport:

```js
// Flag sections taller than 110% of viewport height
document.querySelectorAll('section').forEach(section => {
  const ratio = section.scrollHeight / window.innerHeight;
  if (ratio > 1.1) {
    console.warn(
      `Section "${section.id || section.className}" is ${Math.round(ratio * 100)}% of viewport height. ` +
      `Consider condensing content or adding scroll-snap-align: none.`
    );
  }
});
```

The 110% threshold allows for minor overflow (padding, borders) without triggering false positives. Anything beyond 110% means the user cannot see all content within one snap stop.

### Both fixes are valid

- Condensing content preserves the section-based snap experience (preferred).
- `scroll-snap-align: none` breaks the snap pattern for that section but keeps the page functional (acceptable fallback).

Choose based on the content: if the section's content is integral and cannot be hidden behind tabs/accordions, use the escape hatch.

---

## 14. Landscape Orientation

Landscape on mobile phones dramatically reduces viewport height (typically 360-412px CSS height on a phone rotated sideways). This makes section-based `mandatory` snap impractical — most sections' content cannot fit in that height.

### Strategy: graceful degradation

Landscape on mobile phones is NOT a primary design target for section-based landing pages. Users who rotate their phone to landscape are a small minority and usually doing so for video content. The strategy is graceful degradation, not a complete redesign.

### Switch to `proximity` snap

```css
@media (orientation: landscape) and (max-height: 500px) {
  html {
    scroll-snap-type: y proximity;
  }
}
```

`proximity` snap means the browser only snaps if the user stops scrolling close to a snap point. If they're in the middle of a tall section, the scroll stops where they left it. This prevents the jarring experience of `mandatory` snap forcing users into sections they can't see all of.

### CTA above fold in landscape

The CTA is NOT guaranteed to be above the fold in landscape on small phones. At 360px viewport height minus browser chrome, usable height can be as low as ~280px. A headline + subhead + CTA likely exceeds this. This is acceptable — landscape is not the primary orientation for landing pages, and users can scroll to the CTA.

### What to preserve in landscape

- Readability: text remains legible, images remain proportional.
- Navigation: the nav bar still works, links still function.
- Content order: the logical flow of sections is unchanged.

### What to accept in landscape

- Sections may require scrolling within them.
- Snap is `proximity` instead of `mandatory`.
- CTA may be below the fold.
- Some visual polish (particle effects, large hero images) may be cropped.

---

## 15. `prefers-reduced-motion` Accessibility

Users who enable "Reduce motion" in their OS settings have told the browser they are sensitive to animation. This includes people with vestibular disorders, motion sickness, and certain cognitive disabilities. Respecting this preference is both an accessibility requirement and legally relevant (WCAG 2.1 SC 2.3.3).

### What to disable

- Smooth scroll behavior (scroll jumps instantly to target)
- GSAP entrance animations (elements appear immediately, no fade/slide)
- Parallax effects
- Particle animations
- Cursor-follow effects
- Auto-playing carousels (stop on current slide)

### What to KEEP

- Scroll-snap (it is positioning/navigation, not animation)
- Layout and content (everything is still visible and accessible)
- Color transitions on hover (subtle, not motion-based)

### CSS

```css
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }

  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Setting `animation-duration` and `transition-duration` to near-zero (not zero, to avoid breaking animation-end event listeners) effectively disables all CSS animations and transitions globally.

### JavaScript

```js
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReducedMotion) {
  // Initialize GSAP timelines and animations
  initAnimations();

  // Initialize particle effects
  initParticles();

  // Initialize cursor-follow effects
  initCursorEffects();
}

// Scroll-snap stays active regardless — it's navigation, not decoration
```

### Why scroll-snap stays

Scroll-snap aligns the viewport to section boundaries. It is a navigation aid, not a decorative animation. Disabling it would make the page harder to use, not easier. The snap itself is instantaneous (or near-instantaneous with `scroll-behavior: auto`), which is the behavior reduced-motion users prefer — immediate response without animation.

### Dynamic detection

The user can change their motion preference while the page is open (e.g., toggling "Reduce motion" in system settings). Listen for changes:

```js
window.matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change', (e) => {
  if (e.matches) {
    // Kill running GSAP animations
    gsap.globalTimeline.clear();
    ScrollTrigger.getAll().forEach(st => st.kill());
  } else {
    // Re-initialize animations
    initAnimations();
  }
});
```

This ensures the page responds immediately without requiring a reload.
