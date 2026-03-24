# Visual Styles Reference

Premium visual design techniques beyond the standard glassmorphism + gradient + grain stack.
Select based on brand identity and project brief. Each technique includes copy-paste CSS/JS recipes.

**When to use which:**
- Neumorphism → utility apps, wellness, fintech (soft, approachable)
- Glitch → tech, gaming, crypto, streetwear (edgy, dynamic)
- Brutalist Typography → fashion, music, editorial (bold, distinctive)
- 3D Product → e-commerce, product launches, hardware (immersive, premium)
- Product-as-Hero → beauty, food, consumer electronics (product-centered)
- Luxury Dark → fashion houses, premium brands, high-end goods (cinematic, exclusive)

**Rules:**
- Never combine more than 2 styles in one project
- Neumorphism and glassmorphism are mutually exclusive (pick one)
- Glitch effects: max 2-3 instances per page (overuse = cheap)
- Brutalist type requires generous whitespace to avoid chaos

---

## 1. Neumorphism (Soft UI)

Neumorphism creates the illusion of elements extruding from or pressed into
the background surface. It relies on dual box-shadows (one light, one dark)
on a background that matches the element color. LIGHTER than glassmorphism --
no `backdrop-filter`. Use on non-critical UI (toggles, cards, dials, clocks)
-- NOT on CTAs (contrast too low for reliable click targets).

Best for: wellness apps, fintech dashboards, boutique SaaS, alarm/utility apps.

**Accessibility:** Always test contrast ratios between interactive and
non-interactive elements. Neumorphic buttons need a subtle border or color
shift on hover/focus to be distinguishable.

### Neumorphic Design Tokens

```css
:root {
  /* Light neumorphism */
  --neu-bg: #E0E0E0;
  --neu-shadow-distance: 6px;
  --neu-blur: 12px;
  --neu-light-shadow: rgba(255, 255, 255, 0.8);
  --neu-dark-shadow: rgba(163, 163, 163, 0.6);
  --neu-radius: 20px;

  /* Dark neumorphism */
  --neu-dark-bg: #2D2D2D;
  --neu-dark-light-shadow: rgba(62, 62, 62, 0.7);
  --neu-dark-dark-shadow: rgba(18, 18, 18, 0.8);
}
```

### Light Neumorphism -- Raised Element (Convex)

```css
.neu-raised {
  background: var(--neu-bg);
  border-radius: var(--neu-radius);
  box-shadow:
    calc(var(--neu-shadow-distance) * -1) calc(var(--neu-shadow-distance) * -1) var(--neu-blur) var(--neu-light-shadow),
    var(--neu-shadow-distance) var(--neu-shadow-distance) var(--neu-blur) var(--neu-dark-shadow);
  padding: 2rem;
  border: none;
}
```

### Inset / Pressed Variant (Active State)

```css
.neu-pressed {
  background: var(--neu-bg);
  border-radius: var(--neu-radius);
  box-shadow:
    inset calc(var(--neu-shadow-distance) * -1) calc(var(--neu-shadow-distance) * -1) var(--neu-blur) var(--neu-light-shadow),
    inset var(--neu-shadow-distance) var(--neu-shadow-distance) var(--neu-blur) var(--neu-dark-shadow);
  padding: 2rem;
}
```

### Dark Neumorphism Variant

```css
.neu-dark-raised {
  background: var(--neu-dark-bg);
  border-radius: var(--neu-radius);
  color: #BDBDBD;
  box-shadow:
    calc(var(--neu-shadow-distance) * -1) calc(var(--neu-shadow-distance) * -1) var(--neu-blur) var(--neu-dark-light-shadow),
    var(--neu-shadow-distance) var(--neu-shadow-distance) var(--neu-blur) var(--neu-dark-dark-shadow);
  padding: 2rem;
}

.neu-dark-pressed {
  background: var(--neu-dark-bg);
  border-radius: var(--neu-radius);
  color: #BDBDBD;
  box-shadow:
    inset calc(var(--neu-shadow-distance) * -1) calc(var(--neu-shadow-distance) * -1) var(--neu-blur) var(--neu-dark-light-shadow),
    inset var(--neu-shadow-distance) var(--neu-shadow-distance) var(--neu-blur) var(--neu-dark-dark-shadow);
  padding: 2rem;
}
```

### Circular Controls -- Clock Dial / Rotary Selector

```css
.neu-clock {
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: var(--neu-bg);
  box-shadow:
    -8px -8px 20px var(--neu-light-shadow),
    8px 8px 20px var(--neu-dark-shadow),
    inset -2px -2px 6px var(--neu-light-shadow),
    inset 2px 2px 6px var(--neu-dark-shadow);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Hour markers -- position 12 markers around the dial */
.neu-clock__marker {
  position: absolute;
  width: 4px;
  height: 16px;
  background: #999;
  border-radius: 2px;
  top: 16px;
  left: 50%;
  transform-origin: 50% 124px; /* half clock height minus top offset */
}

/* Apply rotation per marker: .neu-clock__marker:nth-child(1) { transform: translateX(-50%) rotate(30deg); } etc. */
/* Or generate with JS: */
```

```javascript
var clock = document.querySelector('.neu-clock');
for (var i = 0; i < 12; i++) {
  var marker = document.createElement('div');
  marker.className = 'neu-clock__marker';
  marker.style.transform = 'translateX(-50%) rotate(' + (i * 30) + 'deg)';
  if (i % 3 === 0) {
    marker.style.height = '24px';
    marker.style.width = '5px';
    marker.style.background = '#666';
  }
  clock.appendChild(marker);
}
```

### Neumorphic Card

```css
.neu-card {
  background: var(--neu-bg);
  border-radius: 24px;
  padding: 2rem;
  box-shadow:
    -6px -6px 14px var(--neu-light-shadow),
    6px 6px 14px var(--neu-dark-shadow);
  transition: box-shadow 0.3s ease;
}

.neu-card:hover {
  box-shadow:
    -8px -8px 18px var(--neu-light-shadow),
    8px 8px 18px var(--neu-dark-shadow);
}
```

### Toggle Switch

```css
.neu-toggle {
  width: 64px;
  height: 32px;
  border-radius: 16px;
  background: var(--neu-bg);
  box-shadow:
    inset -3px -3px 8px var(--neu-light-shadow),
    inset 3px 3px 8px var(--neu-dark-shadow);
  position: relative;
  cursor: pointer;
  transition: background 0.3s ease;
}

.neu-toggle__thumb {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--neu-bg);
  box-shadow:
    -3px -3px 6px var(--neu-light-shadow),
    3px 3px 6px var(--neu-dark-shadow);
  position: absolute;
  top: 3px;
  left: 3px;
  transition: transform 0.3s ease;
}

.neu-toggle.active .neu-toggle__thumb {
  transform: translateX(32px);
}

.neu-toggle.active {
  background: #B0D4B8; /* subtle green tint for "on" state */
}
```

---

## 2. Glitch / Distortion Effects

All CSS-only, GPU-composited via `transform` and `clip-path`. Safe for mobile.
Renders on the compositor thread -- no layout thrashing, no paint storms.

Best for: tech brands, gaming, creative agencies, streetwear, crypto.

### RGB Channel Split Text

Three layers: original text, `::before` (red channel), `::after` (cyan channel).
`mix-blend-mode: screen` on dark backgrounds blends the channels naturally.

```css
.glitch-text {
  position: relative;
  font-size: clamp(3rem, 10vw, 8rem);
  font-weight: 900;
  color: #FFFFFF;
  letter-spacing: 0.05em;
}

.glitch-text::before,
.glitch-text::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  mix-blend-mode: screen;
}

.glitch-text::before {
  color: #FF0000;
  animation: glitch-shift-red 3s infinite linear alternate-reverse;
  clip-path: polygon(0 0, 100% 0, 100% 45%, 0 45%);
}

.glitch-text::after {
  color: #00FFFF;
  animation: glitch-shift-cyan 3s infinite linear alternate-reverse;
  clip-path: polygon(0 55%, 100% 55%, 100% 100%, 0 100%);
}

@keyframes glitch-shift-red {
  0%, 80% { transform: translate(0); }
  82% { transform: translate(-3px, 1px); }
  84% { transform: translate(2px, -1px); }
  86%, 100% { transform: translate(0); }
}

@keyframes glitch-shift-cyan {
  0%, 80% { transform: translate(0); }
  82% { transform: translate(3px, -2px); }
  84% { transform: translate(-2px, 1px); }
  86%, 100% { transform: translate(0); }
}
```

HTML: `<h1 class="glitch-text" data-text="GLITCH">GLITCH</h1>` on a dark (`#0A0A0A`) background.

### Scan Line Overlay

```css
.scanlines {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9998;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0, 0, 0, 0.1) 2px,
    rgba(0, 0, 0, 0.1) 4px
  );
}
```

### Full Glitch Animation Keyframes

Irregular timing creates the sense of digital corruption. Use on text, images,
or containers.

```css
@keyframes glitch {
  0% {
    clip-path: polygon(0 2%, 100% 2%, 100% 5%, 0 5%);
    transform: translate(0);
    filter: hue-rotate(0deg);
  }
  15% {
    clip-path: polygon(0 15%, 100% 15%, 100% 15.5%, 0 15.5%);
    transform: translate(-3px, 0);
    filter: hue-rotate(40deg);
  }
  16% {
    clip-path: polygon(0 10%, 100% 10%, 100% 30%, 0 30%);
    transform: translate(3px, 0);
    filter: hue-rotate(0deg);
  }
  49% {
    clip-path: polygon(0 33%, 100% 33%, 100% 33.5%, 0 33.5%);
    transform: translate(0);
    filter: hue-rotate(0deg);
  }
  50% {
    clip-path: polygon(0 44%, 100% 44%, 100% 60%, 0 60%);
    transform: translate(-2px, 0);
    filter: hue-rotate(-60deg);
  }
  65% {
    clip-path: polygon(0 60%, 100% 60%, 100% 70%, 0 70%);
    transform: translate(4px, 0);
    filter: hue-rotate(30deg);
  }
  66% {
    clip-path: polygon(0 75%, 100% 75%, 100% 76%, 0 76%);
    transform: translate(-1px, 0);
    filter: hue-rotate(0deg);
  }
  100% {
    clip-path: polygon(0 85%, 100% 85%, 100% 90%, 0 90%);
    transform: translate(0);
    filter: hue-rotate(0deg);
  }
}

/* Apply to an element */
.glitch-element {
  position: relative;
}

.glitch-element::before {
  content: '';
  position: absolute;
  inset: 0;
  background: inherit;
  animation: glitch 2s infinite steps(1);
  opacity: 0.8;
}
```

### Transition Glitch -- Between Screen State Changes

Trigger the glitch effect for 500ms during state transitions, then remove.

```css
.glitch-transition {
  animation: glitch-burst 0.5s steps(1) forwards;
}

@keyframes glitch-burst {
  0% { transform: translate(0); filter: none; }
  10% { transform: translate(-5px, 2px); filter: hue-rotate(90deg); }
  20% { transform: translate(3px, -3px); filter: hue-rotate(-45deg) saturate(2); }
  30% { transform: translate(-2px, 1px); filter: hue-rotate(180deg); }
  40% { transform: translate(4px, -1px); filter: hue-rotate(-90deg) brightness(1.5); }
  50% { transform: translate(-3px, 3px); filter: hue-rotate(45deg); }
  60% { transform: translate(2px, -2px); filter: hue-rotate(-180deg) saturate(1.5); }
  70% { transform: translate(-1px, 1px); filter: hue-rotate(90deg); }
  80% { transform: translate(1px, -1px); filter: hue-rotate(0deg); }
  100% { transform: translate(0); filter: none; }
}
```

```javascript
/* Trigger on state change */
function triggerGlitch(element) {
  element.classList.add('glitch-transition');
  setTimeout(function() {
    element.classList.remove('glitch-transition');
  }, 500);
}

/* Example: page transition */
var transitionTarget = document.querySelector('.page-content');
document.querySelectorAll('.nav-link').forEach(function(link) {
  link.addEventListener('click', function() {
    triggerGlitch(transitionTarget);
  });
});
```

### Image Glitch -- RGB Split on Images

```css
.glitch-image {
  position: relative;
  overflow: hidden;
}

.glitch-image img {
  display: block;
  width: 100%;
}

.glitch-image::before,
.glitch-image::after {
  content: '';
  position: absolute;
  inset: 0;
  background: inherit;
  background-size: cover;
  mix-blend-mode: screen;
  pointer-events: none;
}

.glitch-image::before {
  background-color: rgba(255, 0, 0, 0.3);
  animation: glitch-shift-red 4s infinite linear alternate-reverse;
  clip-path: polygon(0 0, 100% 0, 100% 40%, 0 40%);
}

.glitch-image::after {
  background-color: rgba(0, 255, 255, 0.3);
  animation: glitch-shift-cyan 4s infinite linear alternate-reverse;
  clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
}
```

For images, set the same `background-image` on the container and the pseudo-elements:
```css
.glitch-image,
.glitch-image::before,
.glitch-image::after {
  background-image: url('product.jpg');
  background-size: cover;
  background-position: center;
}
```

---

## 3. Brutalist Typography

Bold, deliberately raw type compositions. Requires generous whitespace around
the heavy elements to avoid visual chaos.

Best for: fashion, streetwear, music, creative agencies, editorial.

**Font recommendations:** Bebas Neue, Impact, Archivo Black, Oswald,
Dharma Gothic, Anton, Passion One.

### Oversized Headings

```css
.brut-heading {
  font-family: 'Bebas Neue', 'Impact', sans-serif;
  font-size: clamp(4rem, 15vw, 12rem);
  line-height: 0.85;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  margin: 0;
  padding: 0;
}
```

### Rotated Text

```css
/* Horizontal text rotated 90 degrees -- sidebar label style */
.brut-rotated {
  font-family: 'Archivo Black', sans-serif;
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  transform: rotate(-90deg);
  transform-origin: left top;
  position: absolute;
  left: 2rem;
  top: 50%;
  white-space: nowrap;
}

/* Alternative: vertical writing mode (flows naturally in layout) */
.brut-vertical {
  writing-mode: vertical-lr;
  text-orientation: mixed;
  font-family: 'Archivo Black', sans-serif;
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.2em;
}
```

### Overlapping / Stacked Text

```css
.brut-stacked {
  position: relative;
}

.brut-stacked__line {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(4rem, 12vw, 10rem);
  line-height: 0.85;
  text-transform: uppercase;
  position: relative;
}

/* Negative margin pulls lines into overlap */
.brut-stacked__line:nth-child(2) {
  margin-top: -0.15em;
  z-index: 2;
  color: var(--accent-primary, #FF3333);
}

.brut-stacked__line:nth-child(3) {
  margin-top: -0.15em;
  z-index: 3;
}
```

### Mixed Weight in Single Line

```css
.brut-mixed-weight {
  font-family: 'Oswald', sans-serif;
  font-size: clamp(2rem, 6vw, 5rem);
  text-transform: uppercase;
}

.brut-mixed-weight .heavy {
  font-weight: 900;
}

.brut-mixed-weight .light {
  font-weight: 300;
  opacity: 0.7;
}
```

HTML: `<h2 class="brut-mixed-weight"><span class="heavy">Break</span> <span class="light">the</span> <span class="heavy">Rules</span></h2>`

### Outline Text (Hollow Lettering)

```css
.brut-outline {
  font-family: 'Anton', sans-serif;
  font-size: clamp(4rem, 14vw, 11rem);
  text-transform: uppercase;
  -webkit-text-stroke: 2px currentColor;
  color: transparent;
  line-height: 0.9;
}

/* Outline with fill on hover */
.brut-outline-interactive {
  font-family: 'Anton', sans-serif;
  font-size: clamp(4rem, 14vw, 11rem);
  text-transform: uppercase;
  -webkit-text-stroke: 2px currentColor;
  color: transparent;
  transition: color 0.3s ease;
  cursor: pointer;
}

.brut-outline-interactive:hover {
  color: currentColor;
}
```

### Condensed + Expanded Contrast

Pair a super-condensed font with an expanded or wide font in the same heading
to create dramatic visual contrast.

```css
.brut-contrast-pair {
  text-transform: uppercase;
  line-height: 0.9;
}

.brut-contrast-pair .condensed {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(5rem, 15vw, 12rem);
  display: block;
  letter-spacing: 0.05em;
}

.brut-contrast-pair .expanded {
  font-family: 'Oswald', sans-serif;
  font-weight: 200;
  font-size: clamp(1.5rem, 4vw, 3rem);
  letter-spacing: 0.4em;
  display: block;
}
```

HTML:
```html
<h1 class="brut-contrast-pair">
  <span class="condensed">Fashion</span>
  <span class="expanded">Forward</span>
</h1>
```

### Text as Texture -- Repeating Background Text

```css
.brut-text-texture {
  position: relative;
  overflow: hidden;
}

.brut-text-texture::before {
  content: '';
  position: absolute;
  inset: 0;
  opacity: 0.04;
  pointer-events: none;
  /* SVG text pattern as background -- replace TEXT with your word */
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='40'%3E%3Ctext x='0' y='30' font-family='Impact,sans-serif' font-size='32' fill='white' letter-spacing='0.1em'%3EDESIGN%20DESIGN%20%3C/text%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 300px 40px;
}
```

---

## 4. 3D Product Integration

### Spline Embed -- Iframe Approach (Simplest)

```html
<div class="spline-container" style="width:100%;height:80vh;position:relative;">
  <iframe
    src="https://my.spline.design/YOUR-SCENE-ID/"
    frameborder="0"
    width="100%"
    height="100%"
    loading="lazy"
    title="3D product viewer"
  ></iframe>
</div>
```

### Spline Embed -- Runtime JS Approach

```html
<canvas id="spline-canvas" style="width:100%;height:80vh;"></canvas>
<script type="module">
  import { Application } from 'https://unpkg.com/@splinetool/runtime@1.9.82/build/runtime.js';

  var canvas = document.getElementById('spline-canvas');
  var app = new Application(canvas);
  app.load('https://prod.spline.design/YOUR-SCENE-ID/scene.splinecode');
</script>
```

### Three.js Product Viewer

Minimal GLTF model viewer with orbit controls, auto-rotate, and proper lighting.

```html
<div id="product-viewer" style="width:100%;height:80vh;"></div>

<script type="module">
  import * as THREE from 'three';
  import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
  import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

  var container = document.getElementById('product-viewer');
  var width = container.clientWidth;
  var height = container.clientHeight;

  /* Scene */
  var scene = new THREE.Scene();
  scene.background = null; /* transparent -- inherits page background */

  /* Camera */
  var camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
  camera.position.set(0, 1.5, 4);

  /* Renderer */
  var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.2;
  container.appendChild(renderer.domElement);

  /* Lighting */
  var ambient = new THREE.AmbientLight(0xffffff, 0.6);
  scene.add(ambient);

  var directional = new THREE.DirectionalLight(0xffffff, 1.2);
  directional.position.set(5, 8, 5);
  directional.castShadow = true;
  scene.add(directional);

  var fillLight = new THREE.DirectionalLight(0xffffff, 0.4);
  fillLight.position.set(-5, 2, -3);
  scene.add(fillLight);

  /* Controls */
  var controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  controls.autoRotate = true;
  controls.autoRotateSpeed = 1.5;
  controls.enablePan = false;
  controls.minDistance = 2;
  controls.maxDistance = 8;

  /* Load Model */
  var loader = new GLTFLoader();
  loader.load('product.glb', function(gltf) {
    var model = gltf.scene;
    /* Center the model */
    var box = new THREE.Box3().setFromObject(model);
    var center = box.getCenter(new THREE.Vector3());
    model.position.sub(center);
    scene.add(model);
  });

  /* Animate */
  function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }
  animate();

  /* Resize */
  window.addEventListener('resize', function() {
    var w = container.clientWidth;
    var h = container.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  });
</script>
```

### CSS-Only Floating Effect

```css
.product-float {
  animation: float 4s ease-in-out infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(2deg);
  }
}
```

### Product Shadow (Synced with Float)

A blurred ellipse shadow beneath the floating product that scales and fades
with the float animation.

```css
.product-float-wrapper {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.product-float-wrapper .product-image {
  animation: float 4s ease-in-out infinite;
  position: relative;
  z-index: 2;
}

.product-float-wrapper .product-shadow {
  width: 60%;
  height: 20px;
  background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.25) 0%, transparent 70%);
  border-radius: 50%;
  animation: shadow-pulse 4s ease-in-out infinite;
  margin-top: -10px;
  z-index: 1;
}

@keyframes shadow-pulse {
  0%, 100% {
    transform: scaleX(1);
    opacity: 0.6;
  }
  50% {
    transform: scaleX(0.75);
    opacity: 0.3;
  }
}
```

### GSAP Scroll-Linked Product Rotation

Pin the product in the viewport and rotate it as the user scrolls through
a content section.

```javascript
/* Requires GSAP + ScrollTrigger (see animation-patterns.md for CDN setup) */
gsap.registerPlugin(ScrollTrigger);

var productModel = document.querySelector('.product-3d');

gsap.to(productModel, {
  rotateY: 360,
  ease: 'none',
  scrollTrigger: {
    trigger: '.product-scroll-section',
    start: 'top top',
    end: 'bottom bottom',
    pin: '.product-pin-container',
    scrub: 1
  }
});
```

```css
/* CSS for the pinned scroll section */
.product-scroll-section {
  height: 300vh; /* 3x viewport = the scroll runway for rotation */
  position: relative;
}

.product-pin-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-3d {
  will-change: transform;
}
```

Best for: e-commerce, product launches, tech hardware, beauty/skincare.

---

## 5. Immersive Product-as-Hero Layouts

The product IS the design. Everything else (text, UI, navigation) is
subordinate to the product image. Remove visual clutter ruthlessly.

Best for: beauty, food/beverage, consumer electronics, fashion accessories.

### Product-Centered Composition

Product fills 60%+ of the viewport. Text overlays are minimal.

```css
.hero-product-centered {
  display: grid;
  place-items: center;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
}

.hero-product-centered__image {
  max-height: 80vh;
  max-width: 90vw;
  object-fit: contain;
  position: relative;
  z-index: 2;
}

.hero-product-centered__overlay-text {
  position: absolute;
  bottom: 8%;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  z-index: 3;
  color: #FFFFFF;
}
```

### Background Color Wash

Full-screen gradient matched to the product's dominant color. Extract the
color from the product image and set via CSS custom properties.

```css
:root {
  --product-color-light: #FFE8D6;
  --product-color-dark: #D4956B;
  --product-color-accent: #C47A4E;
}

.hero-color-wash {
  min-height: 100vh;
  background: linear-gradient(135deg, var(--product-color-light), var(--product-color-dark));
  display: grid;
  place-items: center;
  position: relative;
}
```

### Floating Decorative Elements

Small shapes, icons, or ingredient images scattered around the hero product.
Each with a unique float animation offset for organic movement.

```css
.floating-element {
  position: absolute;
  animation: float-gentle var(--float-duration, 5s) ease-in-out infinite;
  animation-delay: var(--float-delay, 0s);
  pointer-events: none;
  z-index: 1;
}

/* Assign unique delays and durations per element */
.floating-element:nth-child(1) { --float-duration: 5s; --float-delay: 0s; top: 15%; left: 10%; }
.floating-element:nth-child(2) { --float-duration: 6s; --float-delay: 1s; top: 25%; right: 8%; }
.floating-element:nth-child(3) { --float-duration: 4.5s; --float-delay: 0.5s; bottom: 20%; left: 15%; }
.floating-element:nth-child(4) { --float-duration: 5.5s; --float-delay: 1.5s; bottom: 30%; right: 12%; }
.floating-element:nth-child(5) { --float-duration: 7s; --float-delay: 0.8s; top: 60%; left: 5%; }

@keyframes float-gentle {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  25% {
    transform: translateY(-12px) rotate(3deg);
  }
  75% {
    transform: translateY(8px) rotate(-2deg);
  }
}
```

### Minimal UI Overlay

Strip the hero to the absolute essentials: brand logo (top), product name
(bold, centered), and a single CTA (bottom). Everything else removed.

```css
.hero-minimal-ui {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 2rem;
  position: relative;
}

.hero-minimal-ui__logo {
  z-index: 10;
  opacity: 0.8;
}

.hero-minimal-ui__product-name {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: 700;
  text-align: center;
  z-index: 10;
  letter-spacing: 0.05em;
}

.hero-minimal-ui__cta {
  z-index: 10;
  padding: 1rem 3rem;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  border: 1px solid currentColor;
  background: transparent;
  cursor: pointer;
  transition: background 0.3s ease, color 0.3s ease;
}

.hero-minimal-ui__cta:hover {
  background: #FFFFFF;
  color: #0A0A0A;
}
```

### Split Composition

Product on one side, bold stacked text on the other.

```css
.hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
}

@media (max-width: 768px) {
  .hero-split {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr auto;
  }
}

.hero-split__product {
  overflow: hidden;
}

.hero-split__product img {
  width: 100%;
  height: 100vh;
  object-fit: cover;
}

.hero-split__content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: clamp(2rem, 5vw, 6rem);
}

.hero-split__heading {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(3rem, 8vw, 7rem);
  line-height: 0.9;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}
```

### Ingredient / Feature Callouts

Thin lines connecting from the product to floating labels. Using pseudo-elements
with rotation for the connector lines.

```css
.callout {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: rgba(255, 255, 255, 0.8);
  white-space: nowrap;
}

.callout__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--product-color-accent, #C47A4E);
  flex-shrink: 0;
  box-shadow: 0 0 12px var(--product-color-accent, #C47A4E);
}

.callout__line {
  width: 60px;
  height: 1px;
  background: rgba(255, 255, 255, 0.3);
  flex-shrink: 0;
}

/* Angled callout -- rotate the line for diagonal connections */
.callout--angled .callout__line {
  transform: rotate(-30deg);
  transform-origin: left center;
}
```

SVG alternative for more precise line routing:
```html
<svg class="callout-lines" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:5;">
  <!-- Line from product to label. Adjust x1,y1 (product point) and x2,y2 (label point) -->
  <line x1="50%" y1="30%" x2="80%" y2="15%" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
  <circle cx="50%" cy="30%" r="4" fill="var(--product-color-accent, #C47A4E)"/>
</svg>
```

---

## 6. Luxury Dark with Selective Glow

Cinematic dark aesthetic where light itself is the hierarchy tool. Elements
come FORWARD by getting lighter (inverse of typical elevation). Warm accent
colors (gold, amber) provide selective energy on an otherwise restrained palette.

Best for: fashion houses, luxury goods, premium spirits, high-end automotive, jewelry.

**Font recommendations:** Futura PT, Didot, Cormorant Garamond (serif for luxury),
Playfair Display.

### Base Palette Tokens

```css
:root {
  /* Dark base -- never pure black, never pure white */
  --lux-bg-deep: #050505;
  --lux-bg: #0A0A0A;
  --lux-bg-elevated: #111111;
  --lux-bg-hover: #1A1A1A;
  --lux-text: #E8E8E8;
  --lux-text-muted: #888888;
  --lux-border: rgba(255, 255, 255, 0.06);

  /* Warm accents */
  --lux-gold: #C9A84C;
  --lux-gold-light: #E8D5A3;
  --lux-amber: #FF8C00;
  --lux-gold-glow: rgba(201, 168, 76, 0.15);
  --lux-amber-glow: rgba(255, 140, 0, 0.15);
}
```

### Warm Accent Bleed

Diffused warm glow around accent elements. Creates the "light bleeding out"
effect seen on luxury brand sites.

```css
.lux-accent-glow {
  position: relative;
}

.lux-accent-glow::after {
  content: '';
  position: absolute;
  inset: -40px;
  border-radius: inherit;
  background: transparent;
  box-shadow: 0 0 120px 40px var(--lux-gold-glow);
  pointer-events: none;
  z-index: -1;
}
```

Or directly on the element:
```css
.lux-glow-element {
  box-shadow: 0 0 120px 40px var(--lux-gold-glow);
}
```

### Moody Hero Lighting

Dark product/figure with simulated rim light. The image is darkened and
contrast-boosted, then a positioned pseudo-element creates an edge glow.

```css
.lux-hero-image {
  position: relative;
  overflow: hidden;
}

.lux-hero-image img {
  display: block;
  width: 100%;
  filter: brightness(0.7) contrast(1.3);
}

/* Simulated rim light -- radial gradient positioned at edge */
.lux-hero-image::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    ellipse at 80% 20%,
    rgba(201, 168, 76, 0.2) 0%,
    transparent 50%
  );
  pointer-events: none;
}

/* Alternative: dual rim lights (left and right edge) */
.lux-hero-image--dual-rim::after {
  background:
    radial-gradient(ellipse at 0% 50%, rgba(201, 168, 76, 0.15) 0%, transparent 40%),
    radial-gradient(ellipse at 100% 50%, rgba(255, 140, 0, 0.1) 0%, transparent 40%);
}
```

### Selective Text Glow

Apply warm glow to key headings only -- never body text.

```css
.lux-heading-glow {
  color: var(--lux-text);
  text-shadow:
    0 0 40px rgba(255, 140, 0, 0.3),
    0 0 80px rgba(255, 140, 0, 0.1);
}

/* Stronger glow for hero headings */
.lux-heading-glow--strong {
  color: var(--lux-gold-light);
  text-shadow:
    0 0 30px rgba(201, 168, 76, 0.5),
    0 0 60px rgba(201, 168, 76, 0.2),
    0 0 120px rgba(201, 168, 76, 0.08);
}
```

### Gold / Amber CTA Button

```css
.lux-cta {
  background: linear-gradient(135deg, var(--lux-gold), var(--lux-gold-light));
  color: var(--lux-bg);
  font-weight: 600;
  font-size: 0.875rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  padding: 1rem 2.5rem;
  border: none;
  border-radius: 0; /* sharp corners = luxury convention */
  cursor: pointer;
  box-shadow: 0 0 40px var(--lux-gold-glow);
  transition: box-shadow 0.3s ease, transform 0.2s ease;
}

.lux-cta:hover {
  box-shadow:
    0 0 60px rgba(201, 168, 76, 0.3),
    0 0 120px rgba(201, 168, 76, 0.1);
  transform: translateY(-2px);
}

/* Alternative: ghost CTA with gold border */
.lux-cta--ghost {
  background: transparent;
  color: var(--lux-gold);
  border: 1px solid var(--lux-gold);
  box-shadow: 0 0 30px var(--lux-gold-glow);
}

.lux-cta--ghost:hover {
  background: var(--lux-gold);
  color: var(--lux-bg);
}
```

### Vignette Effect

Cinematic edge darkening on the page container.

```css
.lux-vignette {
  position: relative;
}

.lux-vignette::after {
  content: '';
  position: fixed;
  inset: 0;
  box-shadow: inset 0 0 150px rgba(0, 0, 0, 0.8);
  pointer-events: none;
  z-index: 9997;
}
```

### Elevation Through Light (Inverse Z-Elevation)

In luxury dark themes, elements come FORWARD by getting lighter -- the inverse
of typical Material Design elevation. Cards use `#111`, hover state lifts
to `#1A1A1A`, and active/selected goes to `#222`.

```css
.lux-card {
  background: var(--lux-bg-elevated);
  border: 1px solid var(--lux-border);
  padding: 2rem;
  transition: background 0.3s ease, border-color 0.3s ease;
}

.lux-card:hover {
  background: var(--lux-bg-hover);
  border-color: rgba(255, 255, 255, 0.1);
}

.lux-card.active {
  background: #222222;
  border-color: rgba(201, 168, 76, 0.2);
}

/* Layered surfaces example: page < section < card < modal */
.lux-page { background: var(--lux-bg-deep); }         /* #050505 */
.lux-section { background: var(--lux-bg); }             /* #0A0A0A */
.lux-card { background: var(--lux-bg-elevated); }       /* #111111 */
.lux-modal { background: #181818; }                      /* lightest = most prominent */
```

### Full Luxury Dark Page Composition

Putting it all together -- the layered approach for a luxury hero section:

```css
.lux-hero {
  min-height: 100vh;
  background: var(--lux-bg-deep);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

/* Vignette */
.lux-hero::before {
  content: '';
  position: absolute;
  inset: 0;
  box-shadow: inset 0 0 200px rgba(0, 0, 0, 0.7);
  pointer-events: none;
  z-index: 3;
}

/* Ambient glow behind hero content */
.lux-hero::after {
  content: '';
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, var(--lux-gold-glow) 0%, transparent 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 1;
  filter: blur(40px);
}

.lux-hero__content {
  position: relative;
  z-index: 4;
  text-align: center;
}

.lux-hero__title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(3rem, 8vw, 7rem);
  font-weight: 300;
  color: var(--lux-text);
  text-shadow: 0 0 60px rgba(255, 140, 0, 0.15);
  letter-spacing: 0.08em;
  margin-bottom: 1rem;
}

.lux-hero__subtitle {
  font-family: 'Futura PT', 'Futura', sans-serif;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.3em;
  color: var(--lux-text-muted);
  margin-bottom: 3rem;
}
```

---

## Depth & Dimension System

### The 5-Layer Model

Premium sites create depth through layering, not flatness. Every section should have at least 3 of these 5 layers:

```
Layer 1 (furthest):  Background gradient (radial glow, subtle color)
Layer 2:             Grain/texture overlay (SVG noise at 3-5% opacity)
Layer 3:             Geometric canvas / particles (Canvas2D or WebGL)
Layer 4:             Content (text, cards, terminals)
Layer 5 (nearest):   Foreground glow (cursor glow, selective element glow)
```

### Mouse-Parallax Per Layer

Each layer moves at a different speed on mouse movement, creating depth illusion:

```js
// Desktop only — layers move at different speeds
document.addEventListener('mousemove', function(e) {
  var x = (e.clientX / window.innerWidth - 0.5) * 2;  // -1 to 1
  var y = (e.clientY / window.innerHeight - 0.5) * 2;

  // Background moves SLOW (far away)
  gsap.to('.bg-gradient', { x: x * 5, y: y * 5, duration: 1.2, ease: 'power2.out' });
  // Canvas moves MEDIUM
  gsap.to('.geo-canvas', { x: x * 10, y: y * 10, duration: 0.8, ease: 'power2.out' });
  // Content stays FIXED (anchor point)
  // Foreground glow moves FAST (close to viewer)
  gsap.to('.cursor-glow', { x: e.clientX, y: e.clientY, duration: 0.15 });
});
```

### Scroll-Linked Parallax Within Sections

Hero content moves up on scroll while background stays, creating depth:

```js
gsap.to('.hero-content', {
  yPercent: -15,
  ease: 'none',
  scrollTrigger: {
    trigger: '#hero',
    start: 'top top',
    end: 'bottom top',
    scrub: 1.5
  }
});
```

### Color Temperature for Depth
- **Warm colors advance** (teal glow, white text — feels close)
- **Cool colors recede** (muted gray, dark surfaces — feels far)
- Use this to make CTAs "pop forward" and backgrounds "sink back"

### Selective Glow Elevation
Only 2-3 elements per section should glow. Everything else stays flat. This creates hierarchy:
- CTA button: `box-shadow: 0 0 40px rgba(accent, 0.25)`
- Key stat number: `text-shadow: 0 0 30px rgba(accent, 0.3)`
- Everything else: no glow

### Linear/Stripe Gradient Mesh Technique
Animate the radial gradient position on scroll for living backgrounds:

```js
gsap.to('.section::before', {
  '--glow-x': '60%',  // Shift gradient center
  '--glow-y': '40%',
  ease: 'none',
  scrollTrigger: {
    trigger: '.section',
    start: 'top bottom',
    end: 'bottom top',
    scrub: 2
  }
});
```
```
