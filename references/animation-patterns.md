# Animation Patterns Reference

Loaded during **Phase 5 (Animate)** of the beautiful-converting-frontend-design skill.
All patterns are production-tested on erebora-umbrella. Use `var` (not `const`/`let`)
for broadest compatibility in inline `<script>` blocks.

---

## 1. CDN Setup

Add to `<head>` or before closing `</body>`. Order matters: GSAP before ScrollTrigger,
Lenis before GSAP (so the scroll sync works).

```html
<!-- Lenis Smooth Scroll -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lenis@1.3.18/dist/lenis.css">
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.18/dist/lenis.min.js" defer></script>

<!-- GSAP + ScrollTrigger -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/ScrollTrigger.min.js" defer></script>

<!-- SplitType (character-level text animations) -->
<script src="https://cdn.jsdelivr.net/npm/split-type@0.3.4/umd/index.min.js" defer></script>

<!-- Three.js (WebGL hero animations, optional — use importmap for ES modules) -->
<script type="importmap">
{ "imports": {
  "three": "https://cdn.jsdelivr.net/npm/three@0.183.2/build/three.module.js",
  "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.183.2/examples/jsm/"
}}
</script>

<!-- BarbaJS (multi-page transitions, optional) -->
<script src="https://unpkg.com/@barba/core" defer></script>
```

**CDN preference:** jsdelivr > unpkg > cdnjs. jsdelivr has better caching and version pinning.

---

## 2. Lenis Smooth Scroll Init

From erebora-umbrella production. Creates buttery-smooth inertia scrolling and
syncs the scroll position with GSAP ScrollTrigger so scrub-based animations
track correctly.

```javascript
var lenis = new Lenis({
  duration: 1.2,
  easing: function(t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
  smoothWheel: true
});

// Sync Lenis with GSAP ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add(function(time) { lenis.raf(time * 1000); });
gsap.ticker.lagSmoothing(0);

// Anchor scroll with nav offset
document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
  anchor.addEventListener('click', function(e) {
    var target = document.querySelector(this.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    var navHeight = document.querySelector('.nav')
      ? document.querySelector('.nav').offsetHeight
      : 0;
    lenis.scrollTo(target, { offset: -(navHeight + 16) });
  });
});

// Stop/start for modals and menus
// lenis.stop();  — call when opening an overlay
// lenis.start(); — call when closing an overlay
```

---

## 3. GSAP ScrollTrigger Patterns (data-gsap Attribute System)

### How it works

1. Add `data-gsap="animation-type"` to any HTML element.
2. CSS hides it: `[data-gsap] { opacity: 0; }`.
3. GSAP reveals it when ScrollTrigger fires.

### Reduced-motion guard

Always run this first. Users who prefer reduced motion see all content
immediately with no animation.

```javascript
gsap.registerPlugin(ScrollTrigger);

var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  document.querySelectorAll('[data-gsap]').forEach(function(el) {
    el.style.opacity = '1';
  });
}
```

### Animation types

Wrap everything below in `if (!prefersReducedMotion) { ... }`.

#### fade-up (most common -- use for paragraphs, cards, sections)

```javascript
gsap.utils.toArray('[data-gsap="fade-up"]').forEach(function(el) {
  gsap.from(el, {
    y: 40,
    opacity: 0,
    duration: 0.8,
    ease: 'power3.out',
    scrollTrigger: {
      trigger: el,
      start: 'top 85%',
      toggleActions: 'play none none none'
    }
  });
});
```

#### reveal-3d (hero sections, key cards -- adds perspective rotation)

```javascript
gsap.utils.toArray('[data-gsap="reveal-3d"]').forEach(function(el) {
  gsap.from(el, {
    y: 60,
    rotateX: 8,
    opacity: 0,
    duration: 1,
    ease: 'power3.out',
    transformPerspective: 1200,
    scrollTrigger: {
      trigger: el,
      start: 'top 85%',
      toggleActions: 'play none none none'
    }
  });
});
```

#### stagger (feature grids, card lists -- children animate sequentially)

```javascript
gsap.utils.toArray('[data-gsap="stagger"]').forEach(function(container) {
  gsap.from(container.children, {
    y: 40,
    opacity: 0,
    duration: 0.6,
    stagger: 0.1,
    ease: 'power3.out',
    scrollTrigger: {
      trigger: container,
      start: 'top 85%',
      toggleActions: 'play none none none'
    }
  });
});
```

#### fade-in (subtle, no Y movement -- background elements, dividers)

```javascript
gsap.utils.toArray('[data-gsap="fade-in"]').forEach(function(el) {
  gsap.from(el, {
    opacity: 0,
    duration: 1,
    ease: 'power2.out',
    scrollTrigger: {
      trigger: el,
      start: 'top 85%',
      toggleActions: 'play none none none'
    }
  });
});
```

#### scale-up (logos, icons, avatars)

```javascript
gsap.utils.toArray('[data-gsap="scale-up"]').forEach(function(el) {
  gsap.from(el, {
    scale: 0.8,
    opacity: 0,
    duration: 0.8,
    ease: 'back.out(1.7)',
    scrollTrigger: {
      trigger: el,
      start: 'top 85%',
      toggleActions: 'play none none none'
    }
  });
});
```

#### slide-left / slide-right (split layouts, before/after)

```javascript
gsap.utils.toArray('[data-gsap="slide-left"]').forEach(function(el) {
  gsap.from(el, {
    x: -60, opacity: 0, duration: 0.8, ease: 'power3.out',
    scrollTrigger: { trigger: el, start: 'top 85%', toggleActions: 'play none none none' }
  });
});

gsap.utils.toArray('[data-gsap="slide-right"]').forEach(function(el) {
  gsap.from(el, {
    x: 60, opacity: 0, duration: 0.8, ease: 'power3.out',
    scrollTrigger: { trigger: el, start: 'top 85%', toggleActions: 'play none none none' }
  });
});
```

---

## 4. Counter Animation (stats, numbers)

Animates a number from 0 to `data-target`. Use on stat sections, social proof.

**HTML:** `<span data-counter data-target="97">0</span>%`

```javascript
document.querySelectorAll('[data-counter]').forEach(function(el) {
  var target = parseInt(el.getAttribute('data-target'), 10);
  if (isNaN(target)) return;
  el.textContent = '0';
  var obj = { value: 0 };
  gsap.to(obj, {
    value: target,
    duration: 2,
    ease: 'power2.out',
    scrollTrigger: {
      trigger: el,
      start: 'top 85%',
      toggleActions: 'play none none none'
    },
    onUpdate: function() {
      el.textContent = Math.round(obj.value);
    }
  });
});
```

---

## 5. Parallax Patterns

From erebora-umbrella production. Different scroll speeds on layered elements
create a sense of depth.

### Hero background elements

```javascript
var heroElements = document.querySelectorAll('[data-parallax]');
var speeds = [-0.3, -0.2, -0.15];

heroElements.forEach(function(el, i) {
  gsap.to(el, {
    y: function() { return speeds[i % speeds.length] * window.innerHeight; },
    ease: 'none',
    scrollTrigger: {
      trigger: '.hero',
      start: 'top top',
      end: 'bottom top',
      scrub: 1
    }
  });
});
```

### Product screenshots (subtle y-shift within frames)

```javascript
gsap.utils.toArray('.product-frame img').forEach(function(img) {
  gsap.fromTo(img,
    { y: -20 },
    {
      y: 20,
      ease: 'none',
      scrollTrigger: {
        trigger: img.closest('.product-section') || img,
        start: 'top bottom',
        end: 'bottom top',
        scrub: 1
      }
    }
  );
});
```

---

## 6. Nav State on Scroll

Adds/removes a `.scrolled` class on the nav when the user scrolls past the hero.
Style `.nav.scrolled` in CSS with background blur, border, shadow, etc.

```javascript
var nav = document.querySelector('.nav');
var hero = document.querySelector('.hero');

if (nav && hero) {
  ScrollTrigger.create({
    trigger: hero,
    start: 'top top',
    end: 'bottom top',
    onLeave: function() { nav.classList.add('scrolled'); },
    onEnterBack: function() { nav.classList.remove('scrolled'); }
  });
}
```

---

## 7. Cursor Following Effects

From erebora-umbrella production. Skipped entirely on touch devices.

```javascript
if (!('ontouchstart' in window) && navigator.maxTouchPoints === 0) {
  var hero = document.querySelector('.hero');
  var ticking = false;

  // Hero cursor glow
  if (hero) {
    hero.addEventListener('mousemove', function(e) {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function() {
        var rect = hero.getBoundingClientRect();
        hero.style.setProperty('--mouse-x',
          ((e.clientX - rect.left) / rect.width) * 100 + '%');
        hero.style.setProperty('--mouse-y',
          ((e.clientY - rect.top) / rect.height) * 100 + '%');
        ticking = false;
      });
    });
  }

  // Card cursor glow
  document.querySelectorAll('[data-cursor-glow]').forEach(function(card) {
    card.addEventListener('mousemove', function(e) {
      var rect = card.getBoundingClientRect();
      card.style.setProperty('--card-mouse-x', (e.clientX - rect.left) + 'px');
      card.style.setProperty('--card-mouse-y', (e.clientY - rect.top) + 'px');
    });
    card.addEventListener('mouseleave', function() {
      card.style.removeProperty('--card-mouse-x');
      card.style.removeProperty('--card-mouse-y');
    });
  });
}
```

### CSS for cursor glow

```css
/* Hero-level glow — large, ambient, follows cursor */
.hero__cursor-glow {
  position: absolute;
  inset: 0;
  background: radial-gradient(
    var(--cursor-glow-size, 1200px) circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
    var(--cursor-glow-color, rgba(155, 48, 255, 0.12)),
    transparent 60%
  );
  pointer-events: none;
}

/* Card-level glow — smaller, tighter, reveals on hover */
[data-cursor-glow]::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    400px circle at var(--card-mouse-x) var(--card-mouse-y),
    rgba(255, 255, 255, 0.06),
    transparent 60%
  );
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s ease;
}
[data-cursor-glow]:hover::after {
  opacity: 1;
}
```

---

## 8. CSS Animation States

### GSAP initial state

```css
/* Hidden until ScrollTrigger fires */
[data-gsap] {
  opacity: 0;
}
```

### Reduced motion override

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  [data-gsap] {
    opacity: 1 !important;
    transform: none !important;
  }
}
```

---

## 9. BarbaJS Page Transitions (multi-page sites)

Only include if the site has multiple HTML pages. Single-page sites skip this.

```javascript
barba.init({
  transitions: [{
    name: 'fade',
    leave: function(data) {
      return gsap.to(data.current.container, {
        opacity: 0,
        y: -20,
        duration: 0.4,
        ease: 'power2.in'
      });
    },
    enter: function(data) {
      return gsap.from(data.next.container, {
        opacity: 0,
        y: 20,
        duration: 0.4,
        ease: 'power2.out'
      });
    },
    after: function() {
      // Kill old ScrollTriggers and re-initialize on new page
      ScrollTrigger.getAll().forEach(function(t) { t.kill(); });
      initAnimations(); // Re-run your animation setup function
      window.scrollTo(0, 0);
    }
  }]
});
```

---

## 10. SplitType Text Reveals

Character-by-character or word-by-word reveals for headlines. Requires the
SplitType CDN script.

```javascript
var heading = new SplitType('.hero__headline', { types: 'chars' });

gsap.from(heading.chars, {
  opacity: 0,
  y: 20,
  rotateX: -90,
  stagger: 0.02,
  duration: 0.5,
  ease: 'back.out(1.7)',
  scrollTrigger: {
    trigger: '.hero__headline',
    start: 'top 80%'
  }
});
```

---

## 11. Performance Rules

These are non-negotiable. Violating them causes jank, layout thrash, and
poor Lighthouse scores.

### Only animate composited properties
- **DO:** `transform` (translate, scale, rotate) and `opacity`
- **NEVER:** `width`, `height`, `top`, `left`, `margin`, `padding`, `border-width`

### GPU hints
- Apply `will-change: transform` only on elements that are actively animating
- Remove it after the animation completes (GSAP does this automatically)

### Canvas and particles
- Use `requestAnimationFrame` only -- never `setInterval` or `setTimeout`
- Pause off-screen with `IntersectionObserver`
- Reduce particle count on mobile (e.g., 60 down to 30)

### Containment
- Add `contain: layout style paint` on animated containers to limit browser
  reflow scope

### Event listeners
- Always use `{ passive: true }` on scroll and touch listeners
- Throttle mousemove with `requestAnimationFrame` (see cursor glow pattern above)

### ScrollTrigger specifics
- Use `toggleActions: 'play none none none'` for one-shot reveals (most common)
- Use `scrub: 1` for parallax effects tied to scroll position
- Batch similar animations where possible to reduce ScrollTrigger instances

---

## 12. Per-Section Unique Animations (Anti-Template Pattern)

Premium sites like Linear, Cursor, Stripe use DIFFERENT animations per section.
Uniform fade-up everywhere looks AI-generated. Each section should have a unique
entrance direction, timing, and ease.

```javascript
/* Pain cards: stagger from left + scale */
gsap.fromTo('.pain-card',
  { autoAlpha: 0, x: -50, scale: 0.95 },
  { autoAlpha: 1, x: 0, scale: 1, duration: 0.8, stagger: 0.15, ease: 'power3.out',
    scrollTrigger: { trigger: '.pain-grid', start: 'top 80%' } }
);

/* Before/after terminals: opposite-side slides */
gsap.fromTo('.terminal-bad',
  { autoAlpha: 0, x: -60 },
  { autoAlpha: 1, x: 0, duration: 0.9, ease: 'power3.out',
    scrollTrigger: { trigger: '#comparison', start: 'top 70%' } }
);
gsap.fromTo('.terminal-good',
  { autoAlpha: 0, x: 60 },
  { autoAlpha: 1, x: 0, duration: 0.9, delay: 0.2, ease: 'power3.out',
    scrollTrigger: { trigger: '#comparison', start: 'top 70%' } }
);

/* Price: elastic pop from center */
gsap.fromTo('.price-value',
  { autoAlpha: 0, scale: 0.5 },
  { autoAlpha: 1, scale: 1, duration: 1, ease: 'elastic.out(1, 0.4)',
    scrollTrigger: { trigger: '.price-block', start: 'top 80%' } }
);

/* Innovation cards: back.out scale (feels like they "pop" into place) */
gsap.fromTo('.innovation-card',
  { autoAlpha: 0, scale: 0.85, y: 30 },
  { autoAlpha: 1, scale: 1, y: 0, duration: 0.7, stagger: 0.12, ease: 'back.out(1.4)',
    scrollTrigger: { trigger: '.innovations-grid', start: 'top 75%' } }
);
```

**Key principle:** Each section communicates a different emotion, so each
animation should match that emotion (left-slide = progression, elastic = surprise,
scale = importance, right-slide = contrast).

---

## 13. Per-Section Color Themes (CSS Pseudo-Elements)

Subconscious color coding guides emotional response. Use `::before` radial
gradients at 0.04-0.08 alpha — visible in aggregate but not garish.

```css
section::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: -1;
}

/* Warm red for pain/danger sections */
#pain::before {
  background: radial-gradient(ellipse at 30% 50%, rgba(255,45,85, 0.06), transparent 60%);
}

/* Split red/teal for comparison sections */
#comparison::before {
  background:
    radial-gradient(ellipse at 20% 50%, rgba(255,45,85, 0.05), transparent 50%),
    radial-gradient(ellipse at 80% 50%, rgba(77,217,192, 0.05), transparent 50%);
}

/* Purple for value/prestige sections */
#value::before {
  background: radial-gradient(ellipse at 50% 40%, rgba(155,48,255, 0.07), transparent 55%);
}

/* Teal for trust/safety sections */
#trust::before {
  background: radial-gradient(ellipse at 50% 50%, rgba(77,217,192, 0.05), transparent 55%);
}
```

---

## 14. 3D Card Tilt on Hover (Desktop Only)

Subtle perspective transforms create depth. Max 5deg prevents motion sickness.
Skip on touch devices (no hover) and reduced-motion users.

```javascript
if (!noHover && !prefersReducedMotion) {
  document.querySelectorAll('.tilt-card').forEach(function(card) {
    card.addEventListener('mousemove', function(e) {
      var rect = card.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      var rotateX = ((y - rect.height / 2) / (rect.height / 2)) * -5;
      var rotateY = ((x - rect.width / 2) / (rect.width / 2)) * 5;
      card.style.transform = 'perspective(800px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg)';
    });
    card.addEventListener('mouseleave', function() {
      card.style.transform = 'perspective(800px) rotateX(0) rotateY(0)';
      card.style.transition = 'transform 0.4s ease-out';
      setTimeout(function() { card.style.transition = ''; }, 400);
    });
  });
}
```

---

## 15. Magnetic CTA Buttons (Desktop Only)

Button shifts toward cursor on hover, springs back elastically. Creates a
"the button wants you to click" micro-interaction.

```javascript
if (!noHover && !prefersReducedMotion) {
  document.querySelectorAll('.btn-cta').forEach(function(btn) {
    btn.addEventListener('mousemove', function(e) {
      var rect = btn.getBoundingClientRect();
      var x = e.clientX - rect.left - rect.width / 2;
      var y = e.clientY - rect.top - rect.height / 2;
      gsap.to(btn, { x: x * 0.15, y: y * 0.15, duration: 0.3, ease: 'power2.out' });
    });
    btn.addEventListener('mouseleave', function() {
      gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.3)' });
    });
  });
}
```

---

## 16. Animated Gradient Borders (CSS @property)

Rotating conic gradient border. GPU-accelerated angle interpolation, no JS needed.

```css
@property --border-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.gradient-border {
  --border-angle: 0deg;
  border: 2px solid transparent;
  background-origin: border-box;
  background-clip: padding-box, border-box;
  background-image:
    linear-gradient(var(--bg-surface), var(--bg-surface)),
    conic-gradient(from var(--border-angle), #9b30ff, #ff2d55, #4dd9c0, #3366ff, #9b30ff);
  animation: rotateBorder 4s linear infinite;
}

@keyframes rotateBorder {
  to { --border-angle: 360deg; }
}
```

**Note:** Disable animation on mobile (static gradient is fine). `@property` is
supported in all modern browsers but not Firefox <128.

---

## 17. Section Divider Draw-on-Scroll

Replace static `<hr>` with animated line that draws itself as you scroll past.

**HTML:** `<div class="section-divider"><span class="divider-line"></span></div>`

```css
.section-divider { display: flex; justify-content: center; overflow: hidden; }
.divider-line {
  display: block;
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(155,48,255, 0.25),
    rgba(77,217,192, 0.2), transparent);
  transform: scaleX(0);
  transform-origin: center;
}
```

```javascript
gsap.utils.toArray('.divider-line').forEach(function(line) {
  gsap.fromTo(line,
    { scaleX: 0 },
    { scaleX: 1, duration: 1.2, ease: 'power2.inOut',
      scrollTrigger: { trigger: line, start: 'top 90%' } }
  );
});
```

---

## 18. Hero Entrance Timeline

Orchestrate hero elements with a GSAP timeline instead of independent animations.
This ensures elements appear in the right order and overlap naturally.

```javascript
var heroTl = gsap.timeline({ delay: 0.3 });

/* Character reveal on headline (SplitType) */
if (typeof SplitType !== 'undefined') {
  var headline = document.querySelector('.hero-headline');
  if (headline) {
    headline.style.visibility = 'visible';
    var split = new SplitType(headline, { types: 'chars' });
    heroTl.fromTo(split.chars,
      { autoAlpha: 0, y: 30, rotateX: -40 },
      { autoAlpha: 1, y: 0, rotateX: 0, duration: 0.6, stagger: 0.025,
        ease: 'power3.out',
        onStart: function() { headline.style.perspective = '600px'; }
      }, 0
    );
  }
}

/* Badge bounces in */
heroTl.fromTo('.hero-badge',
  { autoAlpha: 0, scale: 0.8, y: -20 },
  { autoAlpha: 1, scale: 1, y: 0, duration: 0.7, ease: 'back.out(1.7)' }, 0.1
);

/* Sub text and CTA stagger in after headline */
heroTl.fromTo('.hero-sub',
  { autoAlpha: 0, y: 20 },
  { autoAlpha: 1, y: 0, duration: 0.8, ease: 'power2.out' }, 0.5
);

heroTl.fromTo('.hero-cta',
  { autoAlpha: 0, scale: 0.9 },
  { autoAlpha: 1, scale: 1, duration: 0.6, ease: 'back.out(2)' }, 0.9
);
```

---

## 19. Three.js WebGL Hero Animations

For premium hero visuals (particle flows, fluid simulations, abstract scenes).
Use `<script type="module">` with the importmap from section 1.

### Key patterns:
- **InstancedMesh** for particles (single draw call, handles 10,000+ at 60fps)
- **OrthographicCamera** for 2D particle systems (simpler than perspective)
- **ShaderMaterial** for per-instance color/alpha via instanced attributes
- **AdditiveBlending** for glow-through effect on dark backgrounds
- **IntersectionObserver** to pause render loop when off-screen

### Shader gotcha:
`gl_PointCoord` only works with `GL_POINTS`. For InstancedMesh with geometry
(CircleGeometry, PlaneGeometry), use `vUv` from the vertex shader instead.

```glsl
// WRONG — only works with points
float glow = 1.0 - smoothstep(0.0, 0.5, length(gl_PointCoord - vec2(0.5)));

// RIGHT — works with InstancedMesh geometry
varying vec2 vUv;  // set vUv = uv in vertex shader
float dist = length(vUv - vec2(0.5)) * 2.0;
float glow = 1.0 - smoothstep(0.0, 1.0, dist);
```

### Instanced attributes pattern:
```javascript
var colorAttr = new Float32Array(COUNT * 3);
var alphaAttr = new Float32Array(COUNT);
geo.setAttribute('instanceColor', new THREE.InstancedBufferAttribute(colorAttr, 3));
geo.setAttribute('instanceAlpha', new THREE.InstancedBufferAttribute(alphaAttr, 1));

// In animation loop:
colorAttr[i * 3] = color.r;
colorAttr[i * 3 + 1] = color.g;
colorAttr[i * 3 + 2] = color.b;
alphaAttr[i] = alpha;
geo.attributes.instanceColor.needsUpdate = true;
geo.attributes.instanceAlpha.needsUpdate = true;
```

### Performance:
- Cap pixel ratio: `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`
- Reduce particle count on mobile (80 vs 150)
- Pause with IntersectionObserver when hero scrolls off-screen
- ~170KB for Three.js — justified for hero centerpiece, not for secondary elements

---

## 20. Enhanced Particle Systems (Canvas 2D)

For ambient background particles. Add sine-wave pulsing so particles feel "alive"
instead of static noise.

```javascript
function createParticle() {
  return {
    x: Math.random() * w, y: Math.random() * h,
    vx: (Math.random() - 0.5) * 0.3, vy: (Math.random() - 0.5) * 0.3,
    baseRadius: Math.random() * 2.5 + 1,   // bigger than typical 0.5-1.5
    baseAlpha: Math.random() * 0.3 + 0.1,   // bolder than typical 0.05-0.2
    phase: Math.random() * Math.PI * 2,
    pulseSpeed: 0.8 + Math.random() * 1.2,
    color: colors[Math.floor(Math.random() * colors.length)]
  };
}

// In draw loop:
var pulse = Math.sin(time * p.pulseSpeed + p.phase);
p.radius = p.baseRadius * (0.7 + 0.3 * pulse);
p.alpha = p.baseAlpha * (0.6 + 0.4 * pulse);
```

Desktop: 60 particles. Mobile: 25. Connection lines at 0.08 alpha (not 0.04).

---

## 21. React + Lightweight Charts Animation Patterns

For React/Next.js apps using TradingView's Lightweight Charts library. Learned from
building cinematic trading bot animations on Erebora Trades. These patterns apply to
any chart-based animation, product demo, or data visualization replay.

### 3-Layer Architecture

```
Layer 3: HUD Overlay (React + Framer Motion)
  └── AnimatePresence, motion.div — declarative enter/exit/physics
Layer 2: Canvas Annotations (Lightweight Charts ISeriesPrimitive)
  └── Custom primitives with updateOptions() for progress/opacity
Layer 1: Candlestick Chart (Lightweight Charts native)
  └── series.update() — candles appear one by one
```

**Why 3 layers:** Each rendering technology handles what it's best at. LC renders
authentic financial candles (no fake SVG needed). Custom primitives draw directly on
the chart canvas (trend lines, zones). React/Framer Motion handles DOM overlays
(gauges, checklists, badges) with declarative state management.

### Variable-Speed Animation Segments

For cinematic replay that speeds up and slows down (e.g., fast scanning → slow
analysis → trade placement):

```typescript
interface SpeedSegment { name: string; candles: number; duration: number; }

const SPEED_SEGMENTS: SpeedSegment[] = [
  { name: "scan",    candles: 60, duration: 20 },  // 3/sec FAST
  { name: "analyze", candles: 15, duration: 18 },  // 0.83/sec SLOW
  { name: "entry",   candles: 3,  duration: 5 },   // 0.6/sec VERY SLOW
  { name: "active",  candles: 20, duration: 15 },  // 1.33/sec MEDIUM
];

const TOTAL_DURATION = SPEED_SEGMENTS.reduce((s, seg) => s + seg.duration, 0);

function getCandleIndex(elapsed: number) {
  const t = elapsed % TOTAL_DURATION;
  let cumTime = 0, cumCandles = 0;
  for (const seg of SPEED_SEGMENTS) {
    if (t < cumTime + seg.duration) {
      const progress = (t - cumTime) / seg.duration;
      return {
        index: cumCandles + Math.floor(progress * seg.candles),
        phase: seg.name,
        phaseProgress: progress
      };
    }
    cumTime += seg.duration;
    cumCandles += seg.candles;
  }
  return { index: 0, phase: "scan", phaseProgress: 0 };
}
```

### Seeded PRNG for Deterministic Chart Data

Use mulberry32 with a fixed seed so candle data is identical every render.
No external data dependency, no API calls, no randomness between sessions.

```typescript
function mulberry32(seed: number) {
  return function() {
    seed |= 0; seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// Use target prices at structural points to guide the random walk
// so the chart hits key levels (support, entry, TP) naturally.
const ALL_CANDLES = generateCandles(42); // Same output every time
```

### CRITICAL: Loop Reset Pattern

When looping a chart animation, reset ALL refs to initial values and return early
from the reset frame. **Never partially reset** — the second loop must start with
identical state to the first loop.

```typescript
// ✗ WRONG — partial reset causes freeze after one cycle
if (loopCount > lastLoopRef.current) {
  lastLoopRef.current = loopCount;     // grows forever (1, 2, 3...)
  series.setData([ALL_CANDLES[0]]);    // initial was empty series
  lastCandleRef.current = 0;           // initial was -1
  // Missing: startRef, lastHudRef, setHud, early return
}

// ✓ CORRECT — full reset makes loop 2+ identical to loop 1
if (loopCount > lastLoopRef.current) {
  startRef.current = now;              // elapsed restarts from 0
  lastLoopRef.current = 0;             // allows next loop trigger (0→1)
  lastCandleRef.current = 0;           // ready for first update
  lastHudRef.current = INITIAL_HUD;    // forces HUD comparison
  series.setData([ALL_CANDLES[0]]);    // clean chart state
  chart.timeScale().fitContent();
  resetPrimitives();
  setHud(INITIAL_HUD);                 // force React state reset
  rafRef.current = requestAnimationFrame(animate);
  return;                              // skip rest of frame
}
```

**Why `series.setData([firstCandle])` not `series.setData([])`:** LC has documented
issues with empty arrays (github.com/tradingview/lightweight-charts/issues/267).
Always provide at least one data point.

### Selective React State in RAF

At 60fps, calling setState every frame causes unnecessary re-renders. Use a ref to
track the last HUD state and only trigger a React update when something visually
changes.

```typescript
const lastHudRef = useRef<HudState>(INITIAL_HUD);

// Inside RAF callback:
const last = lastHudRef.current;
if (
  newHud.phase !== last.phase ||
  newHud.confidence !== last.confidence ||
  // ... other visual-change checks
  Math.abs(newHud.profit - last.profit) > 2
) {
  lastHudRef.current = newHud;
  setHud(newHud);
}
```

### Never Try-Catch in RAF Loops

Silent error swallowing in `requestAnimationFrame` callbacks masks bugs. If an error
occurs during the loop, you WANT the animation to stop and the error to appear in
the console. A try-catch that logs to `window.__animError` makes debugging nearly
impossible because the loop keeps running in a broken state.

### Framer Motion in React (replaces GSAP for DOM)

For React/Next.js apps, Framer Motion replaces GSAP for DOM animations:
- `AnimatePresence` handles conditional enter/exit (GSAP can't without ref cleanup)
- `motion.div` with variants handles staggered orchestration declaratively
- Spring physics via `type: "spring"` for organic HUD element appearances
- GSAP still preferred for vanilla HTML/JS pages (no React virtual DOM conflict)

### Docker Deployment Gotcha

Always use `docker compose build --no-cache` when deploying frontend changes.
Docker layer caching can serve stale builds even when source files changed. This
wastes debugging time chasing "bugs" that are actually stale cached code.

### Custom Lightweight Charts Primitives

Extend `ISeriesPrimitive<Time>` with an `updateOptions()` method for animatable
properties (progress, opacity). The RAF loop calls `updateOptions()` each frame to
drive the animation, and the primitive's renderer reads the current values.

```typescript
class AnimatedTrendLinePrimitive implements ISeriesPrimitive<Time> {
  private _options: TrendLineOptions;

  updateOptions(opts: Partial<TrendLineOptions>) {
    Object.assign(this._options, opts);
    this.requestUpdate(); // triggers LC to repaint
  }

  paneViews() {
    return [new TrendLinePaneView(this._options)];
  }
}
```

### prefers-reduced-motion

Always provide a static fallback. Show the completed state (all candles, all
annotations visible, HUD at 100% confidence) with no animation.

```typescript
if (prefersReduced) {
  series.setData(ALL_CANDLES);
  chart.timeScale().fitContent();
  trendLine.updateOptions({ progress: 1, opacity: 1 });
  setHud({ phase: "tp_hit", confidence: 100, ... });
  return; // No RAF loop
}
```

### 21.11 Horizontal Panning via `setVisibleLogicalRange()`

**The TradingView bar replay pattern**: Load ALL candles upfront with `series.setData()`,
then animate the viewport by calling `setVisibleLogicalRange({ from, to })` in the RAF
loop. This creates the horizontal scrolling effect where the chart pans left.

**Critical difference from the old approach**: The old method used `series.update()` to add
candles one-by-one and `scrollToRealTime()` to follow the latest candle. This looked like
"candles appearing at the right edge" — not like a replay. The new approach loads everything
first, then moves a fixed-size viewport window across the data.

```typescript
// Load once at mount
series.setData(ALL_CANDLES);

// In RAF loop — pan viewport
const VIEWPORT_BEHIND = 25;
const VIEWPORT_AHEAD = 5;
chart.timeScale().setVisibleLogicalRange({
  from: currentIdx - VIEWPORT_BEHIND,
  to: currentIdx + VIEWPORT_AHEAD,
});
```

Smoothness comes from ~60fps RAF calls, NOT from any LC animation parameter. There is no
`animation` option on `setVisibleLogicalRange()`.

### 21.12 Multi-Trade Cycle Pattern

Define trades as data structures with setupStart/entry/exit candle indices. Each trade has
phases (scan → analyze → entry → trade_active → exit) with different speeds:

```typescript
interface SpeedSegment {
  name: string;       // "scan" | "analyze" | "entry" | "trade_active" | "exit"
  fromCandle: number;
  toCandle: number;
  duration: number;   // seconds
  tradeIdx?: number;
}
```

Speed control: `getCandleIndex(elapsed)` walks the segment array and interpolates. Fast
scan = 4 candles/sec (~15s for 60 candles). Slow analyze = 1.25/sec. Entry = 0.75/sec.
Trade active speeds back up = 2.5/sec. Exit slows again = 0.75/sec.

**Reuse a single set of primitives** — reconfigure positions/options when each trade
becomes active instead of creating N×5 primitives. Fade out between trades, reconfigure,
fade in.

```typescript
function configurePrimitivesForTrade(tradeIdx: number) {
  const trade = TRADE_TEMPLATES[tradeIdx];
  trendLine.updateOptions({
    startTime: ALL_CANDLES[trade.setupStartIdx].time,
    endTime: ALL_CANDLES[trade.entryIdx].time,
    startPrice: trade.supportPrice,
    endPrice: trade.resistancePrice,
    progress: 0, opacity: 0,
  });
  // Similarly for zone, entryLine, slLine, tpLine, target
}
```

### 21.13 Canvas Primitives for Text and Target Icons

Use `ISeriesPrimitive<Time>` to render text labels and target circles directly on the
Lightweight Charts canvas at specific price/time coordinates.

**AnimatedTargetPrimitive** — pulsing circle at entry candle:
- Outer glow ring (strokeStyle with alpha) + inner center dot (fillStyle)
- `pulsePhase` oscillates radius via `Math.sin()` for breathing effect
- Color: `#ff4757` (red) for target icon

**AnimatedTextPrimitive** — text label at price/time:
- Background pill via `ctx.roundRect()` with glass-like fill
- Text with optional glow via `ctx.shadowColor`
- Configurable: fontSize, bold, offsetY, background color

Both use `timeScale().timeToCoordinate()` and `priceToCoordinate()` to convert
data-space positions to pixel coordinates. Return `null` from coordinate functions
when the element is off-screen (viewport has scrolled past).

### 21.14 Descriptive Overlays as Conversion Tool

The animation IS the product demo. Text overlays that explain bot reasoning convert
visitors by building understanding and trust. Structure:

1. **Confluence panel** (bottom-left): Staggered checklist items explaining WHY the bot
   is interested — "Trend: Overbought reversal signal", "Resistance zone: 1.0935-1.0948"
2. **Direction badge** (center): "LONG" (green) or "SHORT ENTRY" (red) — replaces generic
   "BUY" badge
3. **Entry description** (center): "Entering short — double top resistance rejection"
4. **Profit counter** (center, large): "$102,672" ticking up during trade_active phase
5. **Exit flash** (center): "TAKE PROFIT REACHED" with celebration animation

**High-leverage profit display**: For motivational impact, show realistic high-leverage
profits ($80K-$350K). Format with `toLocaleString("en-US")` for comma separators.
Numbers should feel real and exciting — this is what converts visitors.

### 21.15 Seamless Loop for Multi-Trade Animations

After the last trade exits, the animation must loop back to the beginning without a
visible jump. Key technique:

```typescript
const TOTAL_DURATION = segments.reduce((s, seg) => s + seg.duration, 0);
const elapsed = ((performance.now() - startRef.current) / 1000) % TOTAL_DURATION;
```

When looping, reset ALL state: primitive opacity to 0, HUD to scanning defaults,
confluence lines cleared. The `%` modulo handles the wrap naturally — no special
"loop transition" code needed. The viewport jumps back to candle 0, which looks
natural because the scan phase starts fast anyway.

### 21.16 Selective setState in RAF Loops

React re-renders from `setState` inside RAF can kill performance. Solution: keep a
`lastHudRef` and only call `setHudState()` when values meaningfully change.

```typescript
const last = lastHudRef.current;
const needsUpdate =
  newHud.phase !== last.phase ||
  newHud.confidence !== last.confidence ||
  newHud.activeTrade !== last.activeTrade ||
  Math.abs(newHud.profit - last.profit) > 500;

if (needsUpdate) {
  setHudState(newHud);
  lastHudRef.current = newHud;
}
```

This throttles React renders to ~2-5/sec instead of 60/sec while the RAF loop
continues updating chart viewport and primitives at full 60fps via direct
Lightweight Charts API calls (no React involvement).
