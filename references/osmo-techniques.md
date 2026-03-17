# OSMO-Level Animation Techniques

> Premium animation catalog for Awwwards-quality sites. Loaded during Phase 5 (Animate).
> Reference: osmo.supply aesthetic. Each technique includes difficulty, performance rating, and production-ready code.

---

## Category 1: Scroll-Driven Animations

### Horizontal Scroll Section

Transform vertical scroll into horizontal movement for gallery/showcase sections.

- **Difficulty:** Medium
- **Performance:** Good (GPU composited)
- **Use case:** Portfolio showcases, timeline sections, product galleries

```javascript
var section = document.querySelector('.horizontal-section');
var wrapper = section.querySelector('.horizontal-wrapper');
gsap.to(wrapper, {
  x: function() { return -(wrapper.scrollWidth - window.innerWidth); },
  ease: 'none',
  scrollTrigger: {
    trigger: section,
    start: 'top top',
    end: function() { return '+=' + (wrapper.scrollWidth - window.innerWidth); },
    scrub: 1,
    pin: true,
    anticipatePin: 1
  }
});
```

```css
.horizontal-section { overflow: hidden; }
.horizontal-wrapper { display: flex; flex-wrap: nowrap; width: fit-content; }
```

### Scroll-Linked Progress Bar

Thin progress indicator showing scroll depth. Subtle but expected on premium sites.

- **Difficulty:** Easy
- **Performance:** Excellent

```javascript
gsap.to('.progress-bar', {
  scaleX: 1,
  ease: 'none',
  scrollTrigger: { trigger: 'body', start: 'top top', end: 'bottom bottom', scrub: 0.3 }
});
```

### Section Pin + Reveal

Pin a section in place while content reveals inside it. Creates a storytelling effect.

- **Difficulty:** Medium
- **Performance:** Good

```javascript
ScrollTrigger.create({
  trigger: '.pinned-section',
  start: 'top top',
  end: '+=200%',
  pin: true
});
gsap.to('.reveal-content', {
  opacity: 1, y: 0,
  scrollTrigger: { trigger: '.pinned-section', start: 'top top', end: '+=100%', scrub: 1 }
});
```

---

## Category 2: Page Transitions (Barba.js)

### Fade + Slide

Smooth directional transition between pages. The baseline for SPA-like multi-page sites.

- **Difficulty:** Medium
- **Performance:** Good
- **Dependency:** Barba.js v2+

```javascript
barba.init({
  transitions: [{
    name: 'slide-fade',
    leave: function(data) {
      return gsap.to(data.current.container, { opacity: 0, x: -50, duration: 0.4, ease: 'power2.in' });
    },
    enter: function(data) {
      return gsap.from(data.next.container, { opacity: 0, x: 50, duration: 0.4, ease: 'power2.out' });
    },
    after: function() {
      ScrollTrigger.getAll().forEach(function(t) { t.kill(); });
      initAnimations();
      window.scrollTo(0, 0);
    }
  }]
});
```

### Clip-Path Reveal Transition

Cinematic circular reveal between pages. High visual impact.

- **Difficulty:** Hard
- **Performance:** Good (GPU composited clip-path)

```javascript
barba.init({
  transitions: [{
    name: 'clip-reveal',
    leave: function(data) {
      return gsap.to(data.current.container, { clipPath: 'circle(0% at 50% 50%)', duration: 0.6, ease: 'power2.in' });
    },
    enter: function(data) {
      gsap.set(data.next.container, { clipPath: 'circle(0% at 50% 50%)' });
      return gsap.to(data.next.container, { clipPath: 'circle(150% at 50% 50%)', duration: 0.8, ease: 'power2.out' });
    }
  }]
});
```

---

## Category 3: Cursor Interactions

### Magnetic Button

Button that pulls toward the cursor when nearby. Signature OSMO micro-interaction.

- **Difficulty:** Medium
- **Performance:** Good
- **Note:** Skip on touch devices

```javascript
document.querySelectorAll('[data-magnetic]').forEach(function(btn) {
  btn.addEventListener('mousemove', function(e) {
    var rect = btn.getBoundingClientRect();
    var x = e.clientX - rect.left - rect.width / 2;
    var y = e.clientY - rect.top - rect.height / 2;
    gsap.to(btn, { x: x * 0.3, y: y * 0.3, duration: 0.3, ease: 'power2.out' });
  });
  btn.addEventListener('mouseleave', function() {
    gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.3)' });
  });
});
```

### Custom Cursor

Replace default cursor with a smooth-following custom element. Defines the premium feel.

- **Difficulty:** Medium
- **Performance:** Good (use gsap.ticker, not mousemove for rendering)

```javascript
var cursor = document.querySelector('.custom-cursor');
var cursorX = 0, cursorY = 0;
document.addEventListener('mousemove', function(e) {
  cursorX = e.clientX;
  cursorY = e.clientY;
});
gsap.ticker.add(function() {
  gsap.to(cursor, { x: cursorX, y: cursorY, duration: 0.5, ease: 'power3.out' });
});

// Scale on hover over interactive elements
document.querySelectorAll('a, button').forEach(function(el) {
  el.addEventListener('mouseenter', function() { gsap.to(cursor, { scale: 2, duration: 0.3 }); });
  el.addEventListener('mouseleave', function() { gsap.to(cursor, { scale: 1, duration: 0.3 }); });
});
```

```css
.custom-cursor {
  position: fixed;
  top: 0;
  left: 0;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--accent-primary);
  pointer-events: none;
  z-index: 10000;
  mix-blend-mode: difference;
}
```

---

## Category 4: Text Effects (SplitType)

### Character Reveal

Individual characters animate in with rotation. High-impact hero text treatment.

- **Difficulty:** Easy
- **Performance:** Good (cache SplitType result)

```javascript
var text = new SplitType('.reveal-text', { types: 'chars' });
gsap.from(text.chars, {
  opacity: 0, y: 20, rotateX: -90,
  stagger: 0.02, duration: 0.5, ease: 'back.out(1.7)',
  scrollTrigger: { trigger: '.reveal-text', start: 'top 80%' }
});
```

### Typewriter Effect

Characters appear one by one. Best for taglines and short statements.

- **Difficulty:** Easy
- **Performance:** Excellent

```javascript
var text = new SplitType('.typewriter', { types: 'chars' });
gsap.from(text.chars, {
  opacity: 0,
  stagger: 0.03,
  duration: 0.1,
  ease: 'none',
  scrollTrigger: { trigger: '.typewriter', start: 'top 80%' }
});
```

### Word-by-Word Reveal

Words highlight progressively as user scrolls. Ideal for long-form storytelling sections.

- **Difficulty:** Easy
- **Performance:** Good

```javascript
var text = new SplitType('.word-reveal', { types: 'words' });
gsap.from(text.words, {
  opacity: 0.1,
  stagger: 0.05,
  scrollTrigger: { trigger: '.word-reveal', start: 'top 80%', end: 'top 20%', scrub: 1 }
});
```

---

## Category 5: Interactive Grids

### Bento Grid with Stagger

Grid items animate in with cascading stagger. The modern layout entrance.

- **Difficulty:** Easy
- **Performance:** Good

```javascript
gsap.from('.bento-item', {
  y: 60, opacity: 0, scale: 0.95,
  stagger: { each: 0.08, from: 'start' },
  duration: 0.8, ease: 'power3.out',
  scrollTrigger: { trigger: '.bento-grid', start: 'top 80%' }
});
```

### Card Tilt on Hover (3D Perspective)

Cards tilt toward the cursor creating depth. Adds tactile quality to grid layouts.

- **Difficulty:** Medium
- **Performance:** Good
- **Note:** Skip on touch devices

```javascript
document.querySelectorAll('[data-tilt]').forEach(function(card) {
  card.addEventListener('mousemove', function(e) {
    var rect = card.getBoundingClientRect();
    var x = (e.clientX - rect.left) / rect.width - 0.5;
    var y = (e.clientY - rect.top) / rect.height - 0.5;
    gsap.to(card, { rotateY: x * 10, rotateX: -y * 10, transformPerspective: 1000, duration: 0.3 });
  });
  card.addEventListener('mouseleave', function() {
    gsap.to(card, { rotateY: 0, rotateX: 0, duration: 0.5, ease: 'power2.out' });
  });
});
```

---

## Category 6: Loading & Preloader

### Preloader with Counter

Animated percentage counter with reveal. Sets the tone before the page loads.

- **Difficulty:** Medium
- **Performance:** N/A (runs once)
- **Rule:** Max 3 seconds. Skip on cached visits.

```javascript
var counter = { value: 0 };
gsap.to(counter, {
  value: 100, duration: 2, ease: 'power2.inOut',
  onUpdate: function() {
    document.querySelector('.preloader-count').textContent = Math.round(counter.value) + '%';
  },
  onComplete: function() {
    gsap.to('.preloader', {
      yPercent: -100, duration: 0.8, ease: 'power4.inOut',
      onComplete: function() { document.querySelector('.preloader').remove(); }
    });
  }
});
```

---

## Category 7: Background Effects

### Animated Gradient Mesh

Slow-moving gradient background. Adds life without distraction.

- **Difficulty:** Easy
- **Performance:** Excellent (CSS-driven)

```javascript
gsap.to('.gradient-mesh', {
  backgroundPosition: '400% 400%',
  duration: 20,
  ease: 'none',
  repeat: -1
});
```

```css
.gradient-mesh {
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
  background-size: 400% 400%;
}
```

### Floating Particles (CSS-Only, Lightweight)

Ambient particles rising through the viewport. Zero JS, pure CSS.

- **Difficulty:** Easy
- **Performance:** Excellent

```css
.particle {
  position: absolute;
  width: var(--size, 4px);
  height: var(--size, 4px);
  border-radius: 50%;
  background: var(--color, rgba(155, 48, 255, 0.3));
  animation: float-up var(--duration, 10s) var(--delay, 0s) infinite;
}
@keyframes float-up {
  0%   { transform: translateY(100vh) translateX(0); opacity: 0; }
  10%  { opacity: 0.6; }
  90%  { opacity: 0.2; }
  100% { transform: translateY(-100vh) translateX(var(--drift, 20px)); opacity: 0; }
}
```

---

## Category 8: Micro-Interactions

### Button Ripple Effect

Material-inspired ripple originating from click position.

- **Difficulty:** Easy
- **Performance:** Excellent

```javascript
document.querySelectorAll('[data-ripple]').forEach(function(btn) {
  btn.addEventListener('click', function(e) {
    var rect = btn.getBoundingClientRect();
    var ripple = document.createElement('span');
    ripple.className = 'ripple';
    ripple.style.setProperty('--ripple-x', (e.clientX - rect.left) + 'px');
    ripple.style.setProperty('--ripple-y', (e.clientY - rect.top) + 'px');
    btn.appendChild(ripple);
    gsap.to(ripple, { scale: 4, opacity: 0, duration: 0.6, onComplete: function() { ripple.remove(); } });
  });
});
```

### Toggle Switch Animation

Playful toggle with elastic bounce. Small detail, big polish.

- **Difficulty:** Easy
- **Performance:** Excellent

```javascript
document.querySelectorAll('[data-toggle]').forEach(function(toggle) {
  toggle.addEventListener('click', function() {
    var isActive = toggle.classList.toggle('active');
    gsap.to(toggle.querySelector('.toggle-thumb'), {
      x: isActive ? 24 : 0, duration: 0.3, ease: 'back.out(1.7)'
    });
  });
});
```

---

## Category 9: Media & Video

### Video Play on Scroll

Autoplay video when visible, pause when out of view. Saves bandwidth.

- **Difficulty:** Easy
- **Performance:** Good

```javascript
var video = document.querySelector('.scroll-video');
ScrollTrigger.create({
  trigger: video,
  start: 'top 80%',
  end: 'bottom 20%',
  onEnter: function() { video.play(); },
  onLeave: function() { video.pause(); },
  onEnterBack: function() { video.play(); },
  onLeaveBack: function() { video.pause(); }
});
```

### Image Reveal with Clip-Path

Image slides into view with a wipe effect. Adds editorial quality to image sections.

- **Difficulty:** Easy
- **Performance:** Good (GPU composited)

```javascript
gsap.from('.image-reveal', {
  clipPath: 'inset(0 100% 0 0)',
  duration: 1.2,
  ease: 'power4.inOut',
  scrollTrigger: { trigger: '.image-reveal', start: 'top 75%' }
});
```

---

## Performance Guidelines for Advanced Techniques

| Technique | Constraint | Reason |
|---|---|---|
| Horizontal scroll | Max 3x viewport length for pinned section | Excessive pin length causes scroll jank |
| SplitType | Call once per element, cache the result | Re-splitting causes layout thrash |
| Custom cursor | Render via `gsap.ticker`, not `mousemove` | Ticker syncs to 60fps; mousemove fires irregularly |
| Magnetic buttons | Skip on touch devices | No hover on mobile; wastes event listeners |
| Clip-path animations | Safe to use freely | GPU composited in all modern browsers |
| Preloaders | Max 3 seconds; skip on cached visits | Users abandon after 3s wait |
| All techniques | Wrap in `if (!prefersReducedMotion)` | Accessibility requirement; respect user OS settings |

### Reduced Motion Check (Required)

```javascript
var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReducedMotion) {
  // Initialize all OSMO-level animations here
}
```
