# 3D Spatial Depth System — Complete Implementation Guide

> Making flat UIs feel like dimensional spaces you look INTO, not AT.
> Researched from Linear.app, Apple Vision Pro spatial UI, osmo.supply, awwwards winners.

---

## When to Apply

| Site Type | Apply? | Notes |
|-----------|--------|-------|
| AI dashboard / command center | **YES** — full 6-layer system | The UI IS the product |
| Product demo / campaign page | **YES** — layers 1-4 + selective 5-6 | Creates "wow" spatial feel |
| SaaS marketing / landing page | **SELECTIVE** — layers 1-3 + 5 (parallax) | Depth without distraction |
| Portfolio / creative showcase | **YES** — full system | Experience is the pitch |
| App settings / forms / admin | **NO** — flat is better | Depth distracts from function |
| Data-dense dashboards | **NO** — or very subtle (layers 1-2 only) | Readability > ambiance |

Map to Motion Modes: Mode 2 (immersive depth) = all 6 layers. Mode 1 (editorial) = layers 1-3 + 5. Mode 0 = skip entirely.

---

## The 6-Layer MECE Depth Model

Each layer is **independent** — you can add or remove any layer without breaking the others. Use all 6 for maximum spatial feel, or selectively omit for subtler depth.

---

### Layer 1: BACKGROUND DEPTH — The Room

Creates the void/environment that everything else floats in. Without this, everything sits on a flat dark surface.

#### A. Ambient Gradient Orbs

2-3 large radial gradients positioned absolutely behind all content. They ARE the room's ambient light.

```css
/* WHY: Creates the "dark room with colored spotlights" feeling.
   Pure CSS, zero JS, zero performance cost. This is how Linear.app
   creates their dimensional dark mode. */
.spatial-room {
  position: relative;
  overflow: hidden;
  background: var(--bg-deep, #050508);
}

.spatial-room::before,
.spatial-room::after {
  content: '';
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
  mix-blend-mode: screen;
  pointer-events: none;
  z-index: 0;
}

/* WHY: Deep purple orb in top-right creates ceiling ambient.
   15s breathing animation makes the room feel alive without
   competing with foreground content. */
.spatial-room::before {
  width: 600px;
  height: 600px;
  top: -200px;
  right: -100px;
  background: radial-gradient(circle, rgba(26, 5, 51, 0.6) 0%, transparent 70%);
  animation: orb-breathe-1 15s ease-in-out infinite;
}

/* WHY: Teal-blue orb in bottom-left creates floor ambient.
   Different duration (12s) than first orb creates organic,
   non-synchronized breathing. */
.spatial-room::after {
  width: 500px;
  height: 500px;
  bottom: -150px;
  left: -100px;
  background: radial-gradient(circle, rgba(0, 26, 40, 0.5) 0%, transparent 70%);
  animation: orb-breathe-2 12s ease-in-out infinite;
}

@keyframes orb-breathe-1 {
  0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.5; }
  50% { transform: translate(20px, 10px) scale(1.1); opacity: 0.7; }
}

@keyframes orb-breathe-2 {
  0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.4; }
  50% { transform: translate(-15px, -10px) scale(1.15); opacity: 0.6; }
}

/* WHY: Optional third orb for richer environments.
   Use a <div> since ::before and ::after are taken. */
.spatial-orb-accent {
  position: absolute;
  width: 400px;
  height: 400px;
  top: 40%;
  left: 50%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 229, 209, 0.15) 0%, transparent 70%);
  filter: blur(100px);
  mix-blend-mode: screen;
  pointer-events: none;
  z-index: 0;
  animation: orb-breathe-3 18s ease-in-out infinite;
}

@keyframes orb-breathe-3 {
  0%, 100% { transform: translate(-50%, 0) scale(1); }
  50% { transform: translate(-50%, -20px) scale(1.08); }
}
```

#### B. SVG Noise Grain Texture

```css
/* WHY: Prevents the "AI-generated smoothness" that Gen Z reads as generic.
   3-4% opacity adds analog warmth without reducing readability.
   mix-blend-mode: overlay makes it respond to underlying colors. */
.spatial-grain {
  position: fixed;
  inset: 0;
  z-index: 9999;
  pointer-events: none;
  opacity: 0.035;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 256px 256px;
}
```

#### C. Optional WebGL Particle Field (Polish Pass)

Use R3F `<Canvas>` or raw Three.js `Points` with `BufferGeometry`. Thousands of particles in one draw call via `InstancedMesh`. Subtle drift 0.1-0.3px/frame. Mobile fallback: CSS gradient blobs. See `6c. Three.js Integration Patterns` in SKILL.md.

---

### Layer 2: STRUCTURAL DEPTH — The Room's Geometry

This is the single highest-impact technique. CSS `perspective` creates actual 3D rendering on the GPU.

```css
/* WHY: perspective on the container tells the GPU to render children
   in 3D space. 1200px is the "camera distance" — smaller = more dramatic
   foreshortening, larger = subtler. 1200px is the sweet spot for dashboards.
   perspective-origin shifts where the "camera" looks from. */
.spatial-container {
  perspective: 1200px;
  perspective-origin: 50% 40%;
}

/* WHY: preserve-3d on the grid makes children actually render at their
   translateZ positions instead of flattening to 2D.
   Without this, translateZ has no visual effect. */
.spatial-grid {
  transform-style: preserve-3d;
  position: relative;
  z-index: 1;
}

/* WHY: Different Z-values create geometric depth.
   GPU composites these as actual 3D planes — not simulated. */
.z-back    { transform: translateZ(-20px); }  /* Recessed panels */
.z-base    { transform: translateZ(0px); }    /* Grid structure */
.z-mid     { transform: translateZ(20px); }   /* Secondary tiles */
.z-front   { transform: translateZ(40px); }   /* Hero element */
.z-accent  { transform: translateZ(60px); }   /* Floating nav/badges */
```

#### Colored Elevation Shadows

```css
/* WHY: On dark backgrounds, pure black shadows are invisible.
   Accent-colored shadows create warmth and connect to the design language.
   Stack 3-4 shadows per level for realistic light diffusion
   (Josh Comeau layered shadow technique). */
:root {
  --shadow-z-back: 0 1px 2px rgba(0,0,0,0.2);
  --shadow-z-base: 0 2px 4px rgba(0,229,209,0.02), 0 4px 8px rgba(0,0,0,0.15);
  --shadow-z-mid:  0 2px 4px rgba(0,229,209,0.04), 0 4px 12px rgba(0,229,209,0.03), 0 8px 24px rgba(0,0,0,0.2);
  --shadow-z-front: 0 4px 8px rgba(0,229,209,0.06), 0 8px 24px rgba(0,229,209,0.04), 0 16px 48px rgba(0,0,0,0.3);
  --shadow-z-accent: 0 4px 12px rgba(0,229,209,0.08), 0 12px 32px rgba(0,229,209,0.05), 0 24px 64px rgba(0,0,0,0.35);
}
```

---

### Layer 3: CONTENT DEPTH — Floating Glass Panes

Cards feel like frosted glass surfaces suspended in the room. Apple Vision Pro / Liquid Glass language.

```css
/* WHY: backdrop-filter: blur creates the "frosted glass floating over
   gradient background" effect. The low background opacity (0.03-0.06)
   lets the ambient gradient orbs subtly show through — cards feel
   transparent, not opaque boxes. Border catches light like glass edges. */
.spatial-tile {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  transform: translateZ(var(--tile-z, 20px));
  box-shadow: var(--shadow-z-mid);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* WHY: Fallback for browsers without backdrop-filter support.
   Solid near-black with slight transparency still creates depth
   against the gradient background. */
@supports not (backdrop-filter: blur(12px)) {
  .spatial-tile {
    background: rgba(24, 24, 27, 0.92);
  }
}

/* WHY: Stagger Z-depths by tile importance so the spatial hierarchy
   is visible even without mouse interaction. Hero elements closest
   to viewer, supporting elements recessed. */
.tile-hero     { --tile-z: 40px; }  /* AI avatar, main feature */
.tile-primary  { --tile-z: 25px; }  /* Key data: momentum, royalty */
.tile-secondary { --tile-z: 15px; }  /* Supporting: quests, leaderboard */
.tile-compact  { --tile-z: 10px; }  /* Compact strips, badges */
```

---

### Layer 4: ACCENT DEPTH — Light Catches and Glows

Subtle effects that make glass surfaces feel real by simulating how light interacts with edges.

```css
/* WHY: Inner glow on top edge simulates overhead lighting hitting
   the glass surface. Creates the "premium glass" look. */
.spatial-tile {
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.06),  /* top-edge light catch */
    var(--shadow-z-mid);                         /* external depth shadow */
}

/* WHY: Per-tile radial glow makes each tile appear to softly emit
   its accent color. At 4-5% opacity it's felt more than seen.
   Creates spatial separation between adjacent tiles. */
.spatial-tile::after {
  content: '';
  position: absolute;
  inset: -20px;
  border-radius: inherit;
  background: radial-gradient(
    circle at 50% 50%,
    var(--kai-active-accent, rgba(0, 229, 209, 0.05)) 0%,
    transparent 70%
  );
  pointer-events: none;
  z-index: -1;
}

/* WHY: Animated gradient border on hero element only.
   @property enables smooth angle animation. Use sparingly —
   one animated border per page maximum. */
@property --border-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.spatial-tile-hero {
  position: relative;
}

.spatial-tile-hero::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  background: conic-gradient(
    from var(--border-angle),
    transparent 25%,
    var(--kai-accent-default, #00e5d1) 50%,
    transparent 75%
  );
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  padding: 1px;
  z-index: -1;
  animation: border-spin 4s linear infinite;
}

@keyframes border-spin {
  to { --border-angle: 360deg; }
}
```

---

### Layer 5: INTERACTIVE DEPTH — The Room Responds

Mouse tracking creates the "looking into a room" effect. Each depth layer shifts at a different rate.

```javascript
// WHY: GSAP quickTo is optimized for continuous pointer tracking.
// Unlike creating a new tween per mousemove, quickTo reuses
// a single tween and just updates the target value. Zero GC pressure.
function initSpatialParallax(container) {
  const layers = container.querySelectorAll('[data-depth]');
  const quickTos = [];

  layers.forEach(layer => {
    const depth = parseFloat(layer.dataset.depth); // 0.005 to 0.03
    quickTos.push({
      x: gsap.quickTo(layer, 'x', { duration: 0.6, ease: 'power3' }),
      y: gsap.quickTo(layer, 'y', { duration: 0.6, ease: 'power3' }),
      depth
    });
  });

  const rect = container.getBoundingClientRect();
  const centerX = rect.width / 2;
  const centerY = rect.height / 2;

  container.addEventListener('pointermove', (e) => {
    // WHY: Calculate offset from center, not from edge.
    // This creates symmetrical parallax that feels like
    // rotating a box in your hands.
    const dx = e.clientX - rect.left - centerX;
    const dy = e.clientY - rect.top - centerY;

    quickTos.forEach(({ x, y, depth }) => {
      x(dx * depth);
      y(dy * depth);
    });
  });

  // WHY: Reset to center on mouse leave — elements shouldn't
  // stay offset when cursor leaves the dashboard.
  container.addEventListener('pointerleave', () => {
    quickTos.forEach(({ x, y }) => {
      x(0);
      y(0);
    });
  });
}
```

#### Card Tilt on Hover

```javascript
// WHY: Tilt calculated from cursor position relative to card center.
// Max 3-5 degrees — more feels gimmicky, less is imperceptible.
// Creates "picking up a card" feeling on hover.
function initCardTilt(card, maxTilt = 4) {
  card.addEventListener('pointermove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;  // -0.5 to 0.5
    const y = (e.clientY - rect.top) / rect.height - 0.5;

    gsap.to(card, {
      rotateY: x * maxTilt,
      rotateX: -y * maxTilt,
      duration: 0.4,
      ease: 'power2.out'
    });
  });

  card.addEventListener('pointerleave', () => {
    gsap.to(card, { rotateY: 0, rotateX: 0, duration: 0.6, ease: 'elastic.out(1, 0.5)' });
  });
}
```

#### Tile Hover Z-Lift

```css
/* WHY: On hover, tile lifts toward the viewer in Z-space.
   Shadow deepens to match new position. scale(1.02) amplifies
   the lift without being jarring. */
.spatial-tile:hover {
  transform: translateZ(calc(var(--tile-z, 20px) + 20px)) scale(1.02);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.08),
    var(--shadow-z-front);
}
```

---

### Layer 6: AMBIENT MOTION — The Room Breathes

Without autonomous movement, the space feels static/dead. These micro-animations make it feel alive.

```javascript
// WHY: Each tile gently bobs at a different speed/offset.
// Staggered durations (3-5s range) ensure tiles never synchronize.
// Only animates transform — zero layout cost.
function initFloatingTiles(tiles) {
  tiles.forEach((tile, i) => {
    gsap.to(tile, {
      y: '+=4',
      duration: 3 + i * 0.4,  // 3s, 3.4s, 3.8s, 4.2s...
      yoyo: true,
      repeat: -1,
      ease: 'sine.inOut',
      delay: i * 0.2  // staggered starts
    });
  });
}
```

---

## Mode Transitions as Camera Movements

When a mode/tab/section changes, the transition should feel like the camera pivoting through the 3D space.

```javascript
// WHY: rotateY(3deg) during content swap creates the feeling
// of a camera panning. Spring physics on tile entrance
// reinforces spatial depth (tiles "land" at their Z-positions).
function modeTransition(container, newContent, newAccent) {
  const tl = gsap.timeline();

  // Phase 1: Camera pivots away (200ms)
  tl.to(container, {
    rotateY: 3,
    opacity: 0.7,
    duration: 0.2,
    ease: 'power2.in'
  });

  // Phase 2: Swap content + accent color
  tl.call(() => {
    // Swap DOM content
    // Update CSS custom property
    document.documentElement.style.setProperty('--kai-active-accent', newAccent);
  });

  // Phase 3: Camera pivots back + tiles stagger in (200ms)
  tl.to(container, {
    rotateY: 0,
    opacity: 1,
    duration: 0.2,
    ease: 'power2.out'
  });

  tl.from('.spatial-tile', {
    y: 20,
    opacity: 0,
    duration: 0.3,
    stagger: 0.05,
    ease: 'elastic.out(1, 0.5)'
  }, '-=0.15');
}
```

---

## Performance Rules

| Rule | Why |
|------|-----|
| Only animate `transform` and `opacity` | GPU composited, no layout/paint |
| `will-change: transform` only on actively animating elements | Each promoted element is a GPU texture — too many wastes VRAM |
| Keep promoted layers under 20 | Browser compositor limit before perf degrades |
| Never animate `backdrop-filter`, `width`, `height`, `top`, `left` | Triggers layout recalculation every frame |
| `pointer-events: none` on all decoration layers | Prevents click interference |
| `z-index` discipline: decorations < structure < content < interactive | Prevents event blocking |

### Mobile Fallbacks (≤768px)

```css
@media (max-width: 768px) {
  /* WHY: No cursor on mobile — parallax is meaningless.
     Reduce perspective for less dramatic foreshortening.
     Halve Z-range to avoid clipping issues on small screens. */
  .spatial-container { perspective: 800px; }
  .z-back    { transform: translateZ(-10px); }
  .z-mid     { transform: translateZ(10px); }
  .z-front   { transform: translateZ(20px); }
  .z-accent  { transform: translateZ(30px); }

  /* WHY: backdrop-filter blur is expensive on mobile GPUs.
     Solid fallback maintains dark glass aesthetic. */
  .spatial-tile {
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }
}

/* WHY: Touch devices have no hover — disable tilt and Z-lift.
   pointer: coarse catches mobile/tablet even on larger screens. */
@media (pointer: coarse) {
  .spatial-tile:hover {
    transform: translateZ(var(--tile-z, 20px));
  }
}
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* WHY: Keep static Z-positions for structural depth (accessibility
     doesn't require removing spatial layout). Disable all motion:
     parallax, float, tilt, breathing, spinning borders. */
  .spatial-room::before,
  .spatial-room::after,
  .spatial-orb-accent { animation: none !important; }
  .spatial-tile-hero::before { animation: none !important; }
  .spatial-tile { transition: none !important; }
}
```

---

## Anti-Patterns for 3D Spatial UIs

| # | Don't | Why | Do Instead |
|---|-------|-----|------------|
| 1 | `translateZ(200px+)` on content | Text becomes huge/blurry, clips viewport | Max 60px for content, 80px for accents |
| 2 | `perspective: 300px` (too aggressive) | Fish-eye distortion, text unreadable | 800-1500px range for dashboards |
| 3 | Parallax on touch devices | No cursor, feels like a bug | Device orientation API or static |
| 4 | `transform-style: preserve-3d` on body | Entire page becomes 3D, breaks fixed elements | Only on grid/container elements |
| 5 | `will-change` on every element | Promotes 50+ layers, kills VRAM | Only on actively animating elements |
| 6 | Same float amplitude on all tiles | Looks synchronized/mechanical | Stagger duration (3-5s range) and amplitude (2-6px) |
| 7 | Tilt > 5 degrees | Gimmicky, text becomes unreadable | Max 3-4 degrees |
| 8 | Animated background competing with text | Violates Principle 8 (readability) | Content sections get near-opaque scrim |
| 9 | 3D on forms/settings/tables | Depth distracts from function | Keep utility UI flat |
| 10 | Pure black shadows on dark theme | Invisible | Accent-colored shadows with low saturation |

---

## Quality Gate — 3D Spatial Depth

```
[ ] 3D-ROOM       — Gradient orbs + grain texture create ambient room feeling?
[ ] 3D-PERSPECTIVE — CSS perspective active on container? preserve-3d on grid?
[ ] 3D-ZLAYERS     — At least 3 distinct translateZ planes visible?
[ ] 3D-GLASS       — Tiles use backdrop-filter blur + low-opacity bg + light-catch border?
[ ] 3D-SHADOWS     — Colored accent shadows, not pure black? Depth scales with Z?
[ ] 3D-PARALLAX    — Mouse parallax working? Layers shift at different rates?
[ ] 3D-TILT        — Card tilt on hover? Max 3-5 degrees? Elastic return on leave?
[ ] 3D-FLOAT       — Tiles have ambient floating motion? Staggered, not synchronized?
[ ] 3D-BREATHE     — Gradient orbs slowly breathing? Room feels alive when idle?
[ ] 3D-MOBILE      — Parallax disabled, blur reduced, Z halved on ≤768px?
[ ] 3D-REDUCED     — prefers-reduced-motion keeps depth but stops all animation?
[ ] 3D-PERF        — Only transform/opacity animated? will-change on <20 elements?
[ ] 3D-READABLE    — All text zones have sufficient contrast against animated bg?
```

---

# PART II — THE REAL 3D RUBRIC (WebGL-First)

> Added 2026-04-17. The CSS-3D system above is **decoration depth** — it makes a flat page feel slightly lifted. It is NOT a volumetric studio. For products where the UI IS the environment (AI command centers, spatial dashboards, product worlds), you need **real WebGL 3D** via React Three Fiber. CSS translateZ is cheap lift. R3F is real space.

## The Binary Escalation Rule

Before picking a 3D stack, answer this:

> **Is the central element supposed to feel like it exists in a 3D space, or like it's a flat element with a lift effect?**

| Answer | Stack | Scope |
|--------|-------|-------|
| "Exists in space" | **R3F + drei + three.js** | Full volumetric scene |
| "Flat with lift effect" | **CSS 3D (Part I above)** | Decoration depth only |

Never mix the two as the primary system. CSS-3D fakery around a supposedly-real 3D centerpiece breaks the illusion. Pick one commitment.

### When You MUST Escalate to R3F (not optional)

1. **AI avatar / product as environmental centerpiece** — Kai, Aria, any "the AI IS the interface" product. If the centerpiece should zoom forward / recede / get rim-lit based on state, CSS can't do it.
2. **Studio / room / world metaphor** — If the brand promise is "step into a space", you need a space. CSS perspective is a sticker; R3F is a stage.
3. **True camera behavior** — If the user should feel like THEY are moving, not the content (mouse moves the camera, not tiles), R3F camera rigs are the only real answer.
4. **Volumetric lighting / emissive materials / refraction** — Light that wraps around objects, glass that bends what's behind it. CSS can fake one material at a time; R3F does real PBR.
5. **Content at genuinely different Z distances that must occlude / sort correctly** — CSS z-index is manual and breaks with any rotation. R3F scene graph sorts by actual world position.

### When CSS 3D Is Still The Right Answer

- Landing pages where depth is supporting (not the product)
- Dashboards where the UI is a tool, not an environment
- Marketing sites where performance budget doesn't allow WebGL
- Content-dense pages where text is the focus
- Anything mobile-only

---

## The 7-Layer R3F Studio Architecture

This is the canonical composition for "AI as environment" products. It's what KAI uses.

### Layer 0: Canvas + Stack Setup

```tsx
// components/kai-3d/Studio.tsx
"use client";

import { Canvas } from "@react-three/fiber";
import { Suspense } from "react";
import dynamic from "next/dynamic";

// WHY: R3F touches document/window; must be client-only.
// Dynamic import with ssr:false prevents SSR crashes.
// Suspense fallback renders the 2D dashboard while scene loads.
const StudioScene = dynamic(() => import("./StudioScene"), {
  ssr: false,
  loading: () => <MobileFallback />,
});

export function Studio(): React.ReactElement {
  return (
    <Canvas
      camera={{ position: [0, 0, 1000], fov: 35, near: 10, far: 5000 }}
      dpr={[1, 2]}
      gl={{ antialias: true, alpha: true, powerPreference: "high-performance" }}
    >
      <Suspense fallback={null}>
        <StudioScene />
      </Suspense>
    </Canvas>
  );
}
```

**Why these camera values:**
- `fov: 35` — human eye feels natural at 30-40°. 50+ is fisheye distortion. 20- is flat telephoto.
- `position: [0, 0, 1000]` — camera at Z=+1000 looking at origin. All Z values below are relative to this.
- `near: 10, far: 5000` — clipping planes matching our Z-range (-2000 back to +600 front, with room).
- `dpr: [1, 2]` — render at device pixel ratio up to 2x. 3x+ tanks perf without visible gain.
- `powerPreference: "high-performance"` — picks the discrete GPU on dual-GPU laptops.

### Layer 1: Environment + Fog (Z -2000)

```tsx
// WHY: The void the studio exists in. Fog makes depth cues work —
// far objects get hazier, creating atmospheric perspective.
import { Environment, Fog } from "@react-three/drei";

<fog attach="fog" args={["#050508", 800, 3000]} />
<Environment preset="studio" environmentIntensity={0.3} />
```

Fog `args={[color, near, far]}` — starts fading at Z +800 (behind camera = foreground), fully opaque at Z +3000. This is what makes distant orbs feel "far".

### Layer 2: Atmospheric Light Orbs (Z -800)

```tsx
// components/kai-3d/AtmosphereOrbs.tsx
import { useRef } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

export function AtmosphereOrbs(): React.ReactElement {
  const violet = useRef<THREE.Mesh>(null);
  const cyan = useRef<THREE.Mesh>(null);

  // WHY: Emissive material with no lighting dependency — orbs self-illuminate.
  // bloom postprocessing (added later) turns these into genuine light sources.
  useFrame((state) => {
    const t = state.clock.elapsedTime;
    if (violet.current) {
      violet.current.position.x = -400 + Math.sin(t * 0.2) * 100;
      violet.current.position.y = 200 + Math.cos(t * 0.15) * 80;
    }
    if (cyan.current) {
      cyan.current.position.x = 400 + Math.cos(t * 0.18) * 120;
      cyan.current.position.y = -150 + Math.sin(t * 0.22) * 90;
    }
  });

  return (
    <>
      <mesh ref={violet} position={[-400, 200, -800]}>
        <sphereGeometry args={[250, 32, 32]} />
        <meshBasicMaterial color="#8b5cf6" transparent opacity={0.4} />
      </mesh>
      <mesh ref={cyan} position={[400, -150, -800]}>
        <sphereGeometry args={[280, 32, 32]} />
        <meshBasicMaterial color="#06b6d4" transparent opacity={0.35} />
      </mesh>
    </>
  );
}
```

**Why `meshBasicMaterial` not `meshStandardMaterial`:** basic material ignores lighting. These orbs ARE lights visually. Adding lighting calculations would darken them against our fog.

### Layer 3: Back Glass Tiles (Z -200)

```tsx
// components/kai-3d/FloatingTile.tsx
import { Html, MeshTransmissionMaterial } from "@react-three/drei";

type Props = {
  position: [number, number, number];
  rotation?: [number, number, number];
  width: number;
  height: number;
  dimmed?: boolean;
  children: React.ReactNode;
};

export function FloatingTile({
  position,
  rotation = [0, 0, 0],
  width,
  height,
  dimmed = false,
  children,
}: Props): React.ReactElement {
  return (
    <group position={position} rotation={rotation}>
      {/* WHY: Glass plane for the light-catching backdrop of the tile.
          MeshTransmissionMaterial is real glass — it refracts what's behind it.
          This is what makes tiles feel like floating panes, not stickers. */}
      <mesh>
        <planeGeometry args={[width, height]} />
        <MeshTransmissionMaterial
          thickness={0.2}
          roughness={0.15}
          transmission={0.95}
          ior={1.45}
          chromaticAberration={0.02}
          backside
        />
      </mesh>
      {/* WHY: HTML content rendered AT the tile's 3D position.
          transform makes it follow the plane's rotation correctly.
          distanceFactor scales the HTML inversely to camera distance
          (farther = smaller, same as 3D objects). */}
      <Html
        transform
        occlude="blending"
        distanceFactor={800}
        style={{
          width: `${width}px`,
          height: `${height}px`,
          opacity: dimmed ? 0.2 : 1,
          filter: dimmed ? "blur(8px)" : "none",
          transition: "opacity 400ms ease, filter 400ms ease",
          pointerEvents: dimmed ? "none" : "auto",
        }}
      >
        {children}
      </Html>
    </group>
  );
}
```

**Why `distanceFactor={800}`:** at camera Z +1000 looking at a tile at Z 0, the tile is 1000 units away. `distanceFactor` = 800 makes the HTML content render at 1:1 pixel size at that distance. Too high = content oversized. Too low = content tiny.

**Why `occlude="blending"`:** HTML content gets alpha-blended with 3D objects in front of it. Without this, tiles always render on top. This setting is what makes foreground orbs / primary tiles occlude back tiles correctly.

### Layer 4: Kai's Plane (Z 0 — centerpiece)

```tsx
// components/kai-3d/KaiPlane.tsx
import { useRef } from "react";
import { useFrame, useLoader } from "@react-three/fiber";
import { VideoTexture } from "three";
import { useSpeechState } from "./SpeechStateContext";
import * as THREE from "three";

export function KaiPlane({ src }: { src: string }): React.ReactElement {
  const mesh = useRef<THREE.Mesh>(null);
  const material = useRef<THREE.MeshStandardMaterial>(null);
  const { state } = useSpeechState();

  // WHY: Video as texture on a plane. Standard <video> element attached
  // via ref, then VideoTexture wraps it for GPU upload each frame.
  const videoTexture = useVideoTexture(src);

  useFrame((_, delta) => {
    if (!mesh.current || !material.current) return;
    const targetScale = state === "speaking" ? 1.15 : 1.0;
    const targetEmissive = state === "speaking" ? 1.5 : 0.4;

    // WHY: lerp toward target every frame. Smooth transitions without tween libs.
    mesh.current.scale.x = THREE.MathUtils.lerp(mesh.current.scale.x, targetScale, delta * 3);
    mesh.current.scale.y = THREE.MathUtils.lerp(mesh.current.scale.y, targetScale, delta * 3);
    material.current.emissiveIntensity = THREE.MathUtils.lerp(
      material.current.emissiveIntensity,
      targetEmissive,
      delta * 3
    );

    // WHY: Idle breathing — slow subtle scale pulse so Kai feels alive, not frozen.
    if (state === "idle") {
      const breathe = 1 + Math.sin(Date.now() * 0.001) * 0.01;
      mesh.current.scale.multiplyScalar(breathe / mesh.current.scale.x);
    }
  });

  return (
    <mesh ref={mesh} position={[0, 0, 0]}>
      <planeGeometry args={[400, 600]} />
      <meshStandardMaterial
        ref={material}
        map={videoTexture}
        emissive="#f7e7ce"
        emissiveIntensity={0.4}
        toneMapped={false}
      />
    </mesh>
  );
}
```

**Why `toneMapped={false}`:** video colors should render 1:1, not get clamped by the scene's tone mapper. Without this, the video looks washed out.

### Layer 5: Primary Glass Tiles (Z +200)

These flank Kai's plane. They're the hero data — Momentum, Royalty. Same `FloatingTile` as Layer 3 but forward in Z. When Kai speaks, these dim via the `dimmed` prop.

### Layer 6: Foreground Accents (Z +400)

Mode switcher pills, HUD badges. Small glass pills rendered via `FloatingTile` with smaller `width`/`height`. Closest to camera, get the sharpest rendering.

### Layer 7: Integrated Input (Z +600)

```tsx
// The "not a chat widget" input. Floats under Kai's face in the Z+600 plane.
<FloatingTile position={[0, -320, 600]} width={500} height={72}>
  <div className="kai-input-pill">
    <button className="kai-input-mic">🎙</button>
    <input className="kai-input-text" placeholder="Ask Kai anything..." />
  </div>
</FloatingTile>
```

**Why this replaces ChatPanel:** ChatPanel was pinned to the bottom of the screen as a slide-up widget. The new input is anchored IN THE 3D SCENE under Kai's face. It lives with Kai, not separately. Typed text appears as a transcript floating near Kai's mouth. Voice works the same way — press mic, Kai listens, transcript renders.

---

## The Camera Rig (Mouse Parallax Done Right)

**Wrong way (CSS 3D):** Move the tiles on mouse move. They look separate and disconnected.

**Right way (R3F):** Move the camera. Everything shifts together because they're all in a real scene.

```tsx
// components/kai-3d/CameraRig.tsx
import { useRef } from "react";
import { useFrame, useThree } from "@react-three/fiber";
import * as THREE from "three";

export function CameraRig(): null {
  const { camera, pointer } = useThree();
  const target = useRef(new THREE.Vector3(0, 0, 1000));

  useFrame((_, delta) => {
    // WHY: Move the camera in an arc around the scene, not straight translate.
    // Arcing keeps the framing of Kai stable while creating real parallax.
    target.current.x = pointer.x * 60;     // ±60 units X
    target.current.y = pointer.y * 40;     // ±40 units Y
    target.current.z = 1000 - Math.abs(pointer.x) * 20 - Math.abs(pointer.y) * 20;

    camera.position.lerp(target.current, delta * 3);
    camera.lookAt(0, 0, 0);
  });
  return null;
}
```

**Why arc (not plain translation):** if camera only moves in X/Y, close objects shift too fast and far objects barely move — correct parallax, but Kai slides off-center. The Z-dip keeps Kai framed while backgrounds shift more than foregrounds, which is what "looking into a room" actually feels like.

---

## Kai Speech State Reactivity (The Whole Product Breathes)

The state machine lives in React context and drives 3D behavior:

```tsx
// components/kai-3d/SpeechStateContext.tsx
type SpeechState = "idle" | "listening" | "thinking" | "speaking" | "returning";

// WHY: Every 3D component subscribes to this context.
// When state changes to "speaking", EVERYTHING reacts:
//   - Kai plane scales up, emissive glow intensifies (KaiPlane)
//   - Primary tiles set dimmed=true (FloatingTile opacity+blur)
//   - Back tiles set dimmed=true with stronger blur
//   - Ambient orbs pulse brighter (AtmosphereOrbs)
//   - Key light intensifies (LightingRig)
// When state returns to "idle":
//   - All of the above animate back over 400ms
// This is what "the AI IS the interface" means in implementation.
```

---

## Mode Transitions as Camera Pans (NOT Panel Swaps)

When the user clicks a mode button:

```tsx
import gsap from "gsap";

function switchMode(newMode: Mode): void {
  const tl = gsap.timeline();

  // 1. Fade current tiles
  tl.to(".kai-tile-group", { opacity: 0, duration: 0.2 }, 0);

  // 2. Pan camera to new angle
  const angles = {
    default: [0, 0, 1000],
    inbox:    [-80, 40, 980],
    analytics:[ 80, 40, 980],
    content:  [0, 80, 960],
  };
  const [x, y, z] = angles[newMode];
  tl.to(camera.position, { x, y, z, duration: 0.35, ease: "power2.inOut" }, 0);

  // 3. Morph accent color through ambient lighting
  tl.to(ambientLight, {
    color: MODE_ACCENTS[newMode],
    duration: 0.4,
  }, 0.1);

  // 4. New tiles fade in at new Z positions
  tl.to(".kai-tile-group-new", { opacity: 1, duration: 0.25 }, 0.4);
}
```

**Why this is the right way:** each mode isn't a different panel — it's a different vantage point into the same studio. The same Kai, the same atmosphere, a different angle revealing different data. Investor reaction: "it's a different room" — that's the win.

---

## Mobile Fallback (2D With Real Depth)

Feature-detect WebGL; if unavailable or perf-budget blown, render the 2D version:

```tsx
export function ArtistDemoPage(): React.ReactElement {
  const [supports3D, setSupports3D] = useState(false);

  useEffect(() => {
    // WHY: Check WebGL support + device perf. Mobile Safari on older
    // iOS can run WebGL but chokes on MeshTransmissionMaterial (real glass).
    const canvas = document.createElement("canvas");
    const gl = canvas.getContext("webgl2") || canvas.getContext("webgl");
    const isDesktop = window.innerWidth >= 1024;
    setSupports3D(!!gl && isDesktop);
  }, []);

  return supports3D ? <Studio /> : <MobileFallback />;
}
```

`MobileFallback` renders the tiles in the Phase 7 CSS-3D depth system from Part I. They still have translateZ, colored shadows, parallax, floating bob — premium 2D. Just not volumetric.

---

## Quality Gate (R3F-specific additions to Section 7)

```
[ ] R3F-CANVAS     — <Canvas> uses dynamic import with ssr:false? Suspense fallback present?
[ ] R3F-CAMERA     — FOV 30-40°? near/far clip planes match Z-range? dpr=[1,2]?
[ ] R3F-FOG        — Scene has fog with sensible near/far? Creates atmospheric perspective?
[ ] R3F-LIGHTS     — Real lights (not just basic material everywhere)? Emissive on light orbs?
[ ] R3F-KAI        — Kai plane has VideoTexture, toneMapped=false, speech-reactive scale + emissive?
[ ] R3F-GLASS      — Primary tiles use MeshTransmissionMaterial (real glass, not fake alpha)?
[ ] R3F-HTML       — drei <Html> uses transform + occlude=blending + distanceFactor matching camera?
[ ] R3F-CAMERARIG  — Mouse parallax MOVES the camera (not the tiles)?
[ ] R3F-STATES     — Speech state machine drives Kai plane + tile opacity + lighting simultaneously?
[ ] R3F-MODES      — Mode transitions pan camera + morph lighting + recompose tiles (not swap panels)?
[ ] R3F-FALLBACK   — Non-WebGL / mobile gets a full 2D version that doesn't look broken?
[ ] R3F-PERF       — Desktop 60fps idle, 45fps+ during transitions? Mobile fallback no regression?
[ ] R3F-A11Y       — All text content still in DOM via drei <Html>? Keyboard reachable? Screen-reader accessible?
[ ] R3F-MOTION     — prefers-reduced-motion: disable camera parallax + Kai breathing + orb drift but keep static depth?
```

---

## Anti-Patterns (R3F-specific additions)

| # | Anti-Pattern | Why It Fails | Do Instead |
|---|--------------|--------------|------------|
| 32 | Using R3F for a landing page that doesn't need it | Ships 300KB+ of three.js for a marketing page. Slower LCP, no real gain. | CSS 3D depth from Part I. Reserve R3F for environment-centric products. |
| 33 | Moving tiles for parallax instead of camera | Tiles slide independently; feels disconnected. Breaks the "one room" illusion. | Move the camera; tiles stay fixed in world space. |
| 34 | Using `<Html>` without `transform` prop | HTML always renders at screen center regardless of 3D position. Breaks scene composition. | Always `<Html transform occlude="blending" distanceFactor={...}>` |
| 35 | Rendering Kai video via `<video>` DOM element layered on top of canvas | Video floats above the scene, doesn't participate in 3D lighting/fog/sort. Looks fake. | `VideoTexture` on a plane mesh — Kai is IN the scene, not ON it. |
| 36 | Skipping fog entirely | Everything at all depths looks equally crisp — no atmospheric perspective, depth cues lost. | `<fog>` with near/far tuned to scene Z-range. |
| 37 | Using `meshStandardMaterial` on light orbs | Orbs get lit BY the scene, darkening them. They should BE lights. | `meshBasicMaterial` (ignores lighting) for anything self-illuminated. |
| 38 | Loading scene synchronously at page-load | Blocks initial paint for 300-500ms. LCP destroyed. | Dynamic import with Suspense; 2D fallback renders first, scene streams in. |
| 39 | No WebGL feature detection | Mobile Safari crashes on `MeshTransmissionMaterial`; users see blank black canvas. | Feature-detect + fallback. Desktop gets studio, mobile gets premium 2D. |
| 40 | Static scene (no breathing, no drift) | Frozen 3D is more uncanny than 2D. The room needs to be alive. | Per-frame animation in `useFrame`: orb drift, Kai breathe, camera drift. |

---

## Full Working Reference: KAI Studio

See `unsign/components/kai-3d/` for the canonical implementation of this rubric in production. It's the living example — if this doc drifts from the code, the code wins.

---

# PART III — WHAT THE DOCS DON'T TELL YOU (Real-World R3F + Next.js Setup)

> Added 2026-04-17 after painful forensic debugging. Part II's "install R3F v9 RC and it works" is misleading. This section captures what actually fails silently and how to avoid it.

## The Stack Version Reality Check

The pmndrs/react-three-next starter (R3F maintainers' own canonical Next.js reference, verified 2026-04-17 via direct GitHub fetch) is STILL on:

```
next: ^14.0.4
react: ^18.2.0
three: ^0.160.0
@react-three/fiber: ^8.15.12
@react-three/drei: ^9.92.7
tunnel-rat: ^0.1.2
```

**If you use Next 15/16 + React 19 + R3F v9 RC, you are ahead of the maintainers' own reference implementation.** No working example exists to copy. You're debugging a stack nobody has validated end-to-end yet.

### Symptoms Of The "Ahead Of The Canonical Stack" Problem

- Canvas mounts, WebGL context alive, but meshes don't render
- `meshBasicMaterial + boxGeometry` renders once, then stops after HMR
- `meshStandardMaterial` renders black even with lights in scope
- Turbopack serves stale modules after file edits
- Chrome loses CDP connection, next-server zombies hold port 3000

These aren't code bugs — they're the stack being untested at this version combination.

## Three Honest Paths

### Path A — Match the canonical stack (safest)
Downgrade to Next 14 + React 18 + R3F v8. Zero version-mismatch risk. Ship today.

### Path B — Live on the edge (mitigated)
Next 15/16 + React 19 + R3F v9 RC. Required mitigations:

1. **Pin specific versions** (never `@rc` or `latest`):
   ```bash
   npm install @react-three/fiber@9.0.0-rc.8 @react-three/drei@9.114.3 three@0.168.0 tunnel-rat@0.1.2
   ```
   - `@rc` tag moves and breaks you
   - `three@latest` may be ahead of R3F v9 RC's compatible range (r160-170)

2. **Add `transpilePackages` to `next.config.ts`:**
   ```typescript
   export default {
     transpilePackages: ['three', '@react-three/fiber', '@react-three/drei'],
   };
   ```
   Without this, Next bundler treats three.js as opaque ESM and some r3f calls silently fail.

3. **Dev with webpack, not Turbopack:**
   ```json
   { "scripts": { "dev": "next dev --webpack" } }
   ```
   Turbopack + R3F has documented HMR/chunking instability in Next 15/16 (vercel/next.js issues #73025, #76182, #77102, #72402).

4. **Use `tunnel-rat` for the Canvas pattern** (see below).

5. **Never rely on HMR for R3F scene edits.** Full page reload after every Canvas-child change.

### Path C — Raw Three.js (last resort)
Skip R3F entirely. Import `three` dynamically in `"use client"`, manage scene/camera/renderer in `useEffect`. No JSX primitive magic. More boilerplate, zero abstraction risk.

## The Canonical "One Canvas, Tunneled Content" Pattern

From pmndrs/react-three-next. What premium R3F apps ACTUALLY do. Solves chunk load errors, SSR hydration mismatch, page-transition canvas destroys, memory leaks.

### Structure
```
app/layout.tsx           # mounts the single global <Scene> canvas
app/[route]/page.tsx     # uses tunnel-rat <r3f.In> to send 3D content into global canvas
components/canvas/
  Scene.tsx              # the global <Canvas>, mounted ONCE
  ViewTunnel.tsx         # tunnel-rat setup
```

### Code

```tsx
// components/canvas/ViewTunnel.tsx
"use client";
import tunnel from "tunnel-rat";
export const r3f = tunnel();
```

```tsx
// components/canvas/Scene.tsx
"use client";
import { Canvas } from "@react-three/fiber";
import { r3f } from "./ViewTunnel";

export function Scene(): React.ReactElement {
  return (
    <Canvas
      style={{ position: "fixed", inset: 0, zIndex: 0, pointerEvents: "none" }}
      camera={{ position: [0, 0, 5], fov: 35 }}
    >
      <r3f.Out />
    </Canvas>
  );
}
```

```tsx
// app/layout.tsx
import { Scene } from "@/components/canvas/Scene";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {children}
        <Scene />
      </body>
    </html>
  );
}
```

```tsx
// app/some-page/page.tsx
"use client";
import { r3f } from "@/components/canvas/ViewTunnel";

export default function SomePage() {
  return (
    <>
      <div>Page DOM content</div>
      <r3f.In>
        <ambientLight intensity={0.5} />
        <mesh>
          <sphereGeometry args={[1, 64, 64]} />
          <meshStandardMaterial color="#8b5cf6" />
        </mesh>
      </r3f.In>
    </>
  );
}
```

## Verification Checklist Before Assuming You Broke Something

```
[ ] Stack matches canonical (Path A) OR Path B mitigations all applied
[ ] transpilePackages added to next.config
[ ] Dev is WEBPACK, not Turbopack
[ ] No zombie next-server on port 3000 (ss -tlnp | grep :3000)
[ ] Chrome CDP session fresh (agent-browser close + reopen)
[ ] curl the URL and check returned HTML — <canvas> tag present?
[ ] Check .next/dev/logs/next-development.log for actual compile errors
[ ] Browser WebGL: canvas.getContext("webgl2").isContextLost() === false
[ ] tunnel-rat <r3f.Out /> is inside <Canvas>, not outside
[ ] Consuming page has "use client" directive
```

If all pass and still blank → likely a stack-version edge case. Downgrade via Path A.

## Additional Anti-Patterns

| # | Anti-Pattern | Why It Fails | Do Instead |
|---|---|---|---|
| 41 | Using `@rc` tag or `@latest` for three/r3f/drei | RC versions break weekly; latest three may be incompatible | Pin exact versions |
| 42 | Turbopack for R3F development | Known HMR + chunk instability | `next dev --webpack` |
| 43 | Assuming R3F docs describe current Next.js state | Docs are Next-14-era | Read pmndrs/react-three-next repo directly |
| 44 | Per-page dynamic-import Canvas | Chunk load errors + SSR mismatch | One global Canvas at layout root + tunnel-rat |
| 45 | Skipping `transpilePackages: ['three']` | Three.js doesn't compose with Next bundler | Always add |
| 46 | Relying on HMR for R3F scene changes | Stale module graph | Full page reload after Canvas-child edits |
| 47 | Debugging "sphere doesn't render" at code level | Real cause is usually dev tooling | Verify tooling stack first |
| 48 | Agent-browser screenshot as proof of render | CDP may be stale, cache may lie | curl + HTML grep FIRST, screenshot last |

## The Honest Lesson

Most R3F debugging sessions spend 80% of time in the wrong layer (code) when the real issue is stack/tooling/environment. Before touching any R3F JSX:

1. Pin versions to canonical stack OR Path B mitigated setup
2. Verify dev server is webpack variant
3. Verify no zombie processes serving stale builds
4. Verify HTML endpoint returns what you expect (curl, not browser)
5. Keep one canonical "health check" page — if it breaks, stack is broken, not your code

If all five pass and JSX still won't render → downgrade. Don't grind on untested stack combinations.

---

# PART IV — THE CANONICAL pmndrs/react-three-next PATTERN (VERIFIED 2026-04-17)

> Fetched directly from https://github.com/pmndrs/react-three-next/tree/main — the R3F maintainers' own Next.js reference. Every file below is the EXACT source (not paraphrase).

## File Tree (what the starter ships)

```
app/
  layout.jsx           # server component — wraps children with <Layout>
  page.jsx             # client page using <View> for 3D sections
  global.css
components/
  canvas/
    Scene.jsx          # client — the ONE Canvas with <r3f.Out/> + <Preload all/>
    View.jsx           # client — drei View tracked to a DOM ref + <Three> tunnel
    Examples.jsx       # sample 3D content (logo, duck, dog)
  dom/
    Layout.jsx         # client — mounts Scene dynamically (ssr:false), forwards events
helpers/
  components/
    Three.jsx          # client — <r3f.In>{children}</r3f.In> wrapper
  global.js            # exports r3f = tunnel()
```

## Full Source — All 6 Key Files (copy-paste ready)

### 1. `helpers/global.js` — the tunnel instance
```js
import tunnel from 'tunnel-rat'

export const r3f = tunnel()
```

### 2. `helpers/components/Three.jsx` — tunnel-in wrapper (pages use this)
```jsx
'use client'

import { r3f } from '@/helpers/global'

export const Three = ({ children }) => {
  return <r3f.In>{children}</r3f.In>
}
```

### 3. `components/canvas/Scene.jsx` — the global Canvas
```jsx
'use client'

import { Canvas } from '@react-three/fiber'
import { Preload } from '@react-three/drei'
import { r3f } from '@/helpers/global'
import * as THREE from 'three'

export default function Scene({ ...props }) {
  // Everything defined in here will persist between route changes, only children are swapped
  return (
    <Canvas {...props}
      onCreated={(state) => (state.gl.toneMapping = THREE.AgXToneMapping)}
    >
      <r3f.Out />
      <Preload all />
    </Canvas>
  )
}
```

### 4. `components/canvas/View.jsx` — the DOM-tracked 3D viewport
```jsx
'use client'

import { forwardRef, Suspense, useImperativeHandle, useRef } from 'react'
import { OrbitControls, PerspectiveCamera, View as ViewImpl } from '@react-three/drei'
import { Three } from '@/helpers/components/Three'

export const Common = ({ color }) => (
  <Suspense fallback={null}>
    {color && <color attach='background' args={[color]} />}
    <ambientLight />
    <pointLight position={[20, 30, 10]} intensity={3} decay={0.2} />
    <pointLight position={[-10, -10, -10]} color='blue' decay={0.2} />
    <PerspectiveCamera makeDefault fov={40} position={[0, 0, 6]} />
  </Suspense>
)

const View = forwardRef(({ children, orbit, ...props }, ref) => {
  const localRef = useRef(null)
  useImperativeHandle(ref, () => localRef.current)

  return (
    <>
      <div ref={localRef} {...props} />
      <Three>
        <ViewImpl track={localRef}>
          {children}
          {orbit && <OrbitControls />}
        </ViewImpl>
      </Three>
    </>
  )
})

View.displayName = 'View'
export { View }
```

### 5. `components/dom/Layout.jsx` — wrapper that mounts Scene
```jsx
'use client'

import { useRef } from 'react'
import dynamic from 'next/dynamic'
const Scene = dynamic(() => import('@/components/canvas/Scene'), { ssr: false })

const Layout = ({ children }) => {
  const ref = useRef()

  return (
    <div
      ref={ref}
      style={{
        position: 'relative',
        width: ' 100%',
        height: '100%',
        overflow: 'auto',
        touchAction: 'auto',
      }}
    >
      {children}
      <Scene
        style={{
          position: 'fixed',
          top: 0,
          left: 0,
          width: '100vw',
          height: '100vh',
          pointerEvents: 'none',
        }}
        eventSource={ref}
        eventPrefix='client'
      />
    </div>
  )
}

export { Layout }
```

### 6. `app/layout.jsx` — root layout wraps EVERY page
```jsx
import { Layout } from '@/components/dom/Layout'
import '@/global.css'

export const metadata = {
  title: 'Next.js + Three.js',
  description: 'A minimal starter for Nextjs + React-three-fiber and Threejs.',
}

export default function RootLayout({ children }) {
  return (
    <html lang='en' className='antialiased'>
      <head />
      <body>
        <Layout>{children}</Layout>
      </body>
    </html>
  )
}
```

### 7. `app/page.jsx` — how a page uses View to render 3D in a DOM slot
```jsx
'use client'

import dynamic from 'next/dynamic'
import { Suspense } from 'react'

const Logo = dynamic(() => import('@/components/canvas/Examples').then((mod) => mod.Logo), { ssr: false })
const View = dynamic(() => import('@/components/canvas/View').then((mod) => mod.View), {
  ssr: false,
  loading: () => <div className='h-96' />,
})
const Common = dynamic(() => import('@/components/canvas/View').then((mod) => mod.Common), { ssr: false })

export default function Page() {
  return (
    <div>
      <div className='w-full md:w-3/5'>
        <View className='flex h-96 w-full'>
          <Suspense fallback={null}>
            <Logo scale={0.6} position={[0, 0, 0]} />
            <Common />
          </Suspense>
        </View>
      </div>
    </div>
  )
}
```

## The Critical Insight

Pages DON'T import the Canvas directly. They import `View` (which uses `gl.scissor` internally to carve out a portion of the global Canvas matching the DOM ref's bounding box). That's how one Canvas renders multiple 3D sections — each `<View>` claims a rectangle of the Canvas viewport.

**This means:** ONE `<Canvas>` globally, MANY `<View>` components per page, each tracking its own DOM div. No hydration race, no chunk load error, no per-page mount/unmount.

## Minimum Files To Copy To Start

To replicate this pattern in your Next.js app:

1. `npm install @react-three/fiber@9.0.0-rc.8 @react-three/drei@9.114.3 three@0.168.0 tunnel-rat@0.1.2`
2. Copy files 1-6 into your project (adjust paths)
3. In `app/layout.tsx` (root), wrap `{children}` with `<Layout>{children}</Layout>`
4. Any page that needs 3D: dynamic-import `View` (ssr:false), render `<View><SceneContent /></View>`

## When This Pattern Still Fails

After copying the canonical pattern, if 3D still doesn't render:

1. **Auth middleware redirecting static assets** — if videos / textures / gltf files get redirected to `/auth/login`, the scene suspends forever on asset load. Fix: add media extensions to middleware matcher exclude list.

2. **Turbopack stale cache** — `rm -rf .next && npm run dev` or switch to `next dev --webpack`.

3. **Stale zombie next-server on port 3000** — `ss -tlnp | grep :3000` + `kill -9 <pid>`.

4. **Agent-browser CDP session lost** — `agent-browser close` + reopen. Don't debug R3F through a stale CDP connection.

5. **The screenshot lies** — verify via `curl` + HTML grep BEFORE trusting the screenshot. Check for `<canvas>` tag in returned HTML.

## Migration Note For KAI

KAI's `app/demo/environment-probe/page.tsx` currently uses the canonical pattern but mounts `DomLayout` per-page instead of at the root. That works but is non-canonical. For Phase 12 production, move `<DomLayout>` wrapping to `app/demo/layout.tsx` (Next.js nested layout) so the Canvas persists across all `/demo/*` routes.

---

# PART V — Next 16 + R3F v9 Defensive Checklist (Verified April 2026)

_Added after losing ~4 hours debugging TWO silent failures in Next 16 + R3F v9 that no existing guide covers. Read this BEFORE writing any Canvas code on Next 16 + React 19. Every rule sourced to a GitHub issue or docs URL — no speculation._

## The two session-killing bugs that cost us 2026-04-17

### Bug #1 — Stale R3F RC pins
Installing `@react-three/fiber@rc` or `@react-three/drei@rc` pulls stale prerelease versions (rc.10, rc.3) that predate the React 19.2 reconciler bundling fix (landed in fiber 9.5.0). Symptom: Canvas mounts, WebGL context created, but commit phase silently drops for `<meshStandardMaterial>` + lights. Only `<meshBasicMaterial>` renders. No error.

**FIX**: pin exact stable — never `@rc`, never `@latest`, never `^`:
```bash
npm install --save-exact \
  @react-three/fiber@9.6.0 \
  @react-three/drei@10.7.7 \
  three@0.184.0 \
  react@19.2.0 react-dom@19.2.0
```
Source: pmndrs/react-three-fiber releases, npm peerDependencies (fiber 9.6.0 peer: `react: >=19 <19.3`).

### Bug #2 — `cacheComponents: true` in next.config.ts
Next 16's new Cache Components feature wraps EVERY route in React `<Activity>`. Activity's mount/hidden lifecycle breaks R3F Canvas's imperative mount (useLayoutEffect + ResizeObserver). Canvas DOM element never gets created. NO error is thrown. Silent.

**FIX**: remove `cacheComponents: true` from next.config.ts project-wide, OR opt out per-route on Canvas pages. Project-wide off is safest until R3F ships an Activity-aware release.

Source: pmndrs/react-three-fiber#3595 — CLOSED as "not planned". pmndrs will NOT fix this; responsibility is on the consumer.

## Hard Rules (never violate)

1. **Exact stable pins only** — fiber 9.6.0, drei 10.7.7, three 0.184.x, react 19.2.x, next 16.x. Never `@rc` / `@latest` / `^`.
2. **Never `cacheComponents: true`** on a route that mounts `<Canvas>`.
3. **`<Canvas>` must mount via `dynamic(() => import, { ssr: false })`**. Direct import hangs the SSR stream because WebGLRenderer constructor touches `window`.
4. **`transpilePackages` contains ONLY `'three'`**. Adding fiber/drei triggers vercel/next.js#85316 (Turbopack monorepo bug) + HMR corruption.
5. **`globals.d.ts` with `ThreeElements` JSX augmentation required** — R3F v9 removed hardcoded JSX intrinsics:
   ```ts
   import type { ThreeElements } from '@react-three/fiber';
   declare module 'react' {
     namespace JSX { interface IntrinsicElements extends ThreeElements {} }
   }
   ```
6. **Fail-closed on WebGL detect** — no context → render 2D/DOM fallback.
7. **Never `setState` inside `useFrame`**. Mutate refs.
8. **Never `new THREE.*()` constructor inside `useFrame`**. Allocate outside, call `.set()` inside.
9. **Every Canvas-internal `useEffect` MUST have cleanup** — R3F v9 now inherits StrictMode. Effects double-fire → duplicate lights, doubled audio, shader recompile spam.
10. **Pin single zustand + single three** via `package.json` overrides — tunnel-rat 0.1.2 uses zustand 4; fiber/drei use zustand 5:
    ```json
    "overrides": { "zustand": "5.x", "three": "0.184.0" }
    ```

## Pre-flight Checklist (run BEFORE writing any Canvas code)

- [ ] `npm ls @react-three/fiber @react-three/drei three` → exact stable, no `rc.*`
- [ ] `next.config.ts`: `transpilePackages: ['three']` only; no `cacheComponents` on Canvas routes; no fiber/drei in `serverExternalPackages`
- [ ] `globals.d.ts` with `ThreeElements` augmentation exists, included in `tsconfig.json`'s `**/*.ts` glob
- [ ] Canvas imported via `dynamic(..., { ssr: false })`
- [ ] Non-WebGL fallback UI renders during ssr:false load AND when WebGL unavailable
- [ ] `package.json` overrides pin single zustand + single three
- [ ] Self-hosted HDR in `/public/hdr/` if using `<Environment>` (pmndrs CDN flaky in prod)
- [ ] Draco/Meshopt decoder in `/public/draco/` if using compressed GLB
- [ ] Every Canvas-internal `useEffect` has cleanup (StrictMode double-fires)
- [ ] No `setState` or `new THREE.*()` in `useFrame`
- [ ] `<Suspense>` at asset leaf, NOT around whole Canvas
- [ ] `useGLTF.preload()` / `useTexture.preload()` at module scope for above-fold
- [ ] Color textures: `texture.colorSpace = THREE.SRGBColorSpace` (v9 removed auto sRGB)

## Diagnostic Playbook (in order, STOP at first fix)

1. **Versions** — `npm ls @react-three/fiber @react-three/drei`. Any `rc.*`, repin stable. STOP.
2. **cacheComponents** — check next.config.ts. Remove or route-exclude. STOP.
3. **Canvas import** — must be `dynamic(() => import('./Scene'), { ssr: false })`. Static import silently hangs SSR stream.
4. **Console** — "R3F hooks outside Canvas" | "alpha is null" (cacheComponents) | "ReactCurrentOwner undefined" (version mismatch).
5. **transpilePackages** — only `'three'`. Remove any R3F packages.
6. **`next dev --webpack`** fallback — if scene renders, Turbopack bug → file upstream, don't ship Webpack perm.
7. **Duplicate packages** — `npm ls three` + `npm ls zustand`. Multiple → overrides.
8. **WebGL availability** — `document.createElement('canvas').getContext('webgl2')` in browser console.
9. **Network tab** — failed HDR/GLB/Draco = empty scene.
10. **StrictMode off temporarily** — if bug disappears, uncleaned effect. Fix cleanup, don't ship off.

## Gotchas by Category

### A. Turbopack (Next 16 default)
- Historical R3F resolution failure (vercel/next.js#74277) — stable 16.1+, fallback `--webpack` if "Module not found" for installed package.
- Monorepo `transpilePackages` unreliable (vercel/next.js#85316) — publish internal R3F wrappers as built ESM.
- Stricter than Webpack on Node-only imports — `turbopack.resolveAlias` shim for three.js loaders pulling `fs`/`path`.
- HMR: `extend()` catalog goes stale on reload → hard refresh.

### B. React 19 lifecycle
- **R3F v9 inherits StrictMode from react-dom** (v8 didn't). Canvas-internal effects double-fire. Missing cleanup = duplicate lights, audio, shaders.
- `forwardRef` deprecated → pass `ref` as normal prop.
- Ref callbacks support cleanup returns → dispose three objects on detach: `ref={(m) => { if (!m) return; return () => m.geometry.dispose() }}`.
- Suspense side-effects no longer re-fire during suspension in v9.
- `useFrame` reads state via refs, not hooks — `useThree()` reads inside frame callback can tear under concurrent rendering.

### C. SSR / hydration
- Canvas MUST be ssr:false.
- Anti-pattern: `const [ok] = useState(() => checkWebGL())` — SSR/client diverge. Use `useEffect(() => setOk(checkWebGL()), [])`.
- `typeof window !== 'undefined'` guards in client components.
- Always ship non-WebGL fallback BEFORE Canvas resolves.

### D. drei-specific
- `useVideoTexture` closure-captures video. Changing `src` suspends indefinitely. Remount component OR update imperatively (`texture.source.data.src = newSrc; texture.needsUpdate = true`).
- `<Environment preset>` hits pmndrs CDN — flaky in prod. Self-host `files={'/env.hdr'}` from `/public/hdr/`.
- R3F context helpers require `<Canvas>` parent: `useThree`, `useFrame`, `Environment`, `OrbitControls`, `Sky`, `Stars`, `Html`, `ContactShadows`, `PresentationControls`, `Effects`.
- `<Html>`: no default z-index / pointer-events — silently eats mesh clicks. Set `pointer-events: none` on decorative wrapper. `<Html transform occlude>` for 3D-placed hiding. Creates separate react-dom root → context must be re-provided via tunnel-rat.
- `<OrbitControls>` blocks mobile scroll (drei#1233), SSR break (drei#376) — dynamic-import the whole scene.
- **R3F v9 removed automatic sRGB texture conversion** — `texture.colorSpace = THREE.SRGBColorSpace` or colors wash out in prod (fine in dev).

### E. tunnel-rat
- zustand version mismatch: tunnel-rat 0.1.2 → zustand 4; fiber → zustand 5. Bug tunnel-rat#21 missed `create` export when 4.5 resolved alongside older. Pin via `overrides: { zustand: "5.x" }`.
- `<tunnel.Out />` MUST mount before `<tunnel.In>` renders children. Memoize singleton at module scope — never re-create per render.
- Still the recommended DOM↔Canvas bridge in v9.

### F. Performance
- `<instancedMesh>` for >~20 copies but `count` is HARD CEILING — `count={1_000_000}` with 10 drawn costs more than modest ceiling. Set to realistic max.
- `<Suspense>` at leaf not Canvas — scene remount = every shader recompile.
- `useGLTF.preload()` / `useTexture.preload()` at MODULE scope for above-fold.
- Stale-closure `useFrame` → read via ref or zustand selector.
- Memoize materials + geometries with `useMemo`, share across meshes.
- `frameloop="demand"` for static scenes; call `invalidate()` on change.
- **WebGLRenderer leaks on route change** (R3F#514, #2655). Safari/iOS 8-context limit = 4 nav = white screen. Call `gl.dispose()` + `gl.forceContextLoss()` in Canvas unmount cleanup.
- Dispose GLTFs: traverse + dispose geometry/material/texture.

### G. Mobile / fallback strategy
- Bail BEFORE Canvas when: no WebGL2, `hardwareConcurrency < 4` + `deviceMemory < 4`, `prefers-reduced-motion: reduce`, iOS Low Power.
- Render 2D/DOM fallback visually equivalent.
- Progressive enhancement: ship DOM-first, mount Canvas AFTER LCP.
- No built-in `prefers-reduced-motion` in R3F — wire via `useMediaQuery` + `frameloop="never"`.

### H. Production-only breaks
- three trees poorly (~500-700KB gz). Enforce single copy via `overrides`.
- `optimizePackageImports: ['three', '@react-three/drei']` reduces drei barrel.
- HDR CDN fails in restricted networks → self-host.
- GLB + Draco: decoder in `public/draco/`, `useGLTF.setDecoderPath('/draco/')`.
- `serverExternalPackages` must NOT contain three/R3F — they're client-only. Fix the importer.
- iOS prod-only crashes (R3F#2837) = context loss on bg/fg → handle `webglcontextlost`/`webglcontextrestored`.

### I. Ecosystem state (April 2026)
- NO official Vercel Next 16 + R3F starter exists.
- `pmndrs/react-three-next` still Next 14 — reference only, don't clone `package.json`.
- Community starters lag — audit `package.json`, most pin React 18.
- R3F v10 in planning (#3662) — cross-platform Canvas context. Not ready.

## Canonical Sources

- pmndrs/react-three-fiber#3595 — Next 16 cacheComponents (THE critical one)
- vercel/next.js#74277 (Turbopack R3F resolve), #85316 (transpilePackages monorepo), #71836 (ReactCurrentOwner)
- pmndrs/react-three-fiber#514, #2655 (WebGLRenderer leaks), #2837 (iOS prod crash), #3662 (v10 context)
- pmndrs/tunnel-rat#21 (zustand 4.5 export)
- pmndrs/drei#319 (Html pointer-events), #376 (OrbitControls SSR), #1233 (mobile scroll), #1983 (tunnel-rat prod build)
- mrdoob/three.js#24757 (VideoTexture src), #24199 (tree-shaking)
- Next.js 16 upgrade + cacheComponents + turbopack + serverExternalPackages + package bundling docs
- R3F v9 migration + pitfalls + scaling + install guides
- React 19 forwardRef + StrictMode
- 14islands — Progressive Enhancement with WebGL and React

---

# Part VI — Production 3D Rubric (2026-04-19 research pass)

_Authoritative rubric for any future "design a 3D site" session. Distilled from 11+ parallel research agents: industry-leading 3D sites (Lusion, Bruno Simon, Monogrid, Active Theory, Basement, Apple Vision Pro marketing), top R3F engineers (pmndrs / Paul Henschel, Bruno Simon, Maxime Heckel, Varun Vachhar, Yuri Artiukh, ggsimm), R3F community patterns (Reddit/HN), GPU performance budgets with tier tables, video-cutout state of the art (Tavus CVI chromakey, Anam live WebRTC, MediaPipe Selfie/Image Segmenter, WebCodecs), typography in 3D, and extreme-contrast color theory._

Use Part VI in preference to any Part III/IV guidance where they conflict. Part V remains authoritative for Next 16 + R3F v9 + React 19.2 stack rules.

## VI.1 — The 6-layer MECE depth model

Every premium 3D scene is composed as six mutually-exclusive-collectively-exhaustive depth layers. Each has a distinct purpose, motion profile, and material rule.

| # | Layer | Z-range (unit-agnostic) | Purpose | Motion | Typical material |
|---|---|---|---|---|---|
| 1 | **Atmosphere** | -∞ (skybox) | Mood + fog color | None or slow drift | Color-only + fog |
| 2 | **Deep-back** | Z = -800 to -600 | Environment depth cue | Parallax at 0.3× mouse | Matte + point light, DOF-blurred |
| 3 | **Mid-back** | Z = -300 to 0 | Structural context (glass, walls) | Subtle float | MeshTransmissionMaterial / matte |
| 4 | **Content** | Z = 0 to +200 | The subject (avatar, tiles) | Full-range animation | Holographic / HTML overlays |
| 5 | **Foreground** | Z = +400 to +700 | Framing (console, monitors) | Parallax at 1.2× mouse | meshBasicMaterial, matte-black silhouette |
| 6 | **Post-FX** | Screen-space | Bloom, DOF, grain | — | EffectComposer pass order matters |

**Rule: motion intensity decreases as semantic importance increases.** Deep-back drifts with mouse; content stays stable. User's eye rests where text must read.

## VI.2 — Camera & composition

Default "back-of-control-room" pattern for environment-based scenes:

```ts
const CAMERA_DEFAULT = { position: [0, 80, 1200], target: [0, 0, 0], fov: 35 };
// FOV 35° is cinematic, compresses depth, reads premium.
// dpr capped [1, 2] universally.
// Parallax: mouse dX × 0.05 → camera.x, mouse dY × -0.03 → camera.y, damped over 0.12s.
```

Mode-based dolly for state changes:

| Mode | Camera Z | Tiles opacity |
|---|---|---|
| default | 1200 | 1.0 |
| inbox / analytics / content_machine | 1400 | 1.0 |
| live (avatar takeover) | 600 | 0.05 |

## VI.3 — Foreground frame (Layer 5)

Matte black silhouettes, no texture, no lighting — they read as shape against the lit mid-scene.

- **Structural foreground element** (e.g., mixing console, dashboard chrome): `meshBasicMaterial color #000000`.
- **Small emissive details** (VU meters, LEDs, indicator dots): instanced planes with emissive accent color at 0.6 intensity.
- **Warm accent light**: point light `#f7e7ce` (tungsten) intensity 0.3 distance 400 — represents a practical light source.

**Never** use `meshStandardMaterial` on the foreground frame — it costs lighting computation and the element will NOT be the focus. Keep cheap and matte.

## VI.4 — Mid-plane (Layer 3) glass pane

```tsx
<MeshTransmissionMaterial
  transmission={1}
  thickness={0.4}
  roughness={0.0}
  ior={1.5}
  chromaticAberration={0.05}
  anisotropy={0.1}
  distortion={0.05}
  distortionScale={0.2}
  temporalDistortion={0.1}
  backside
/>
```

**Perf invariant: exactly ONE MeshTransmissionMaterial per scene.** It does a buffer pass per frame; two collapses framerate on mid-tier GPUs. Scoped invariant — enforce via `grep -c "MeshTransmissionMaterial" components/**/*.tsx` equals 1.

## VI.5 — Deep-back (Layer 2)

- Primitive-stack silhouettes at Z=-600 with `meshStandardMaterial color #1a1a20 roughness 0.8`.
- One warm point light at Z=-800, Y=+200: `pointLight color #f7e7ce intensity 1.2 distance 1000` with subtle flicker (sine-mod intensity ±5%).
- Back wall at Z=-1000: dark matte plane `color #0a0a0e`.
- **Scene fog**: `<fog attach="fog" color={BASE_COLOR} near={600} far={1800} />` — softens deep-back and gives DOF something to bite.

Fog color MUST match the scene base color. Black fog on near-black scene is correct. Different colors = visible "wall of fog."

## VI.6 — Content plane (Layer 4): avatar + HTML tiles

**Avatar video-plane stack** (innermost → outermost):

1. **Base mesh**: plane ~400×600, single-sided.
2. **Video source**: `THREE.VideoTexture(videoElement)` — create MANUALLY via `useMemo(() => new THREE.VideoTexture(el), [el])`. NEVER wrap the video element itself in Suspense; that traps the whole scene.
3. **Chromakey shader** (custom `ShaderMaterial`): discards pixels where green channel dominates (for live green-screen streams). Fragment core:
   ```glsl
   vec3 col = texture2D(map, vUv).rgb;
   float gMatch = smoothstep(0.35, 0.55, col.g - max(col.r, col.b));
   if (gMatch > 0.1) discard;
   col.g = min(col.g, (col.r + col.b) * 0.5 + 0.1); /* spill suppression */
   gl_FragColor = vec4(col, 1.0 - gMatch);
   ```
4. **Holographic overlay** (Fresnel + scanlines + chromatic aberration). Drop-in library or hand-rolled ~30 lines GLSL. Parameters: Fresnel bias 0.2, scale 1.0, power 2.0, scanline density 80, speed 0.3, hologram brightness 1.2.
5. **Light wrap**: ambient sample of surrounding scene color injected as rim-light uniform — makes the avatar feel *in the room* instead of pasted over it.

**Contact shadow**: `<ContactShadows position={[0, -300, z]} opacity={0.4} blur={2} scale={600} />` — grounds the avatar in space.

**HTML tiles**: `<drei.Html transform occlude="blending" distanceFactor={800}>` wrapping the tile's JSX. HTML text is crisp, accessible, SEO-crawlable.

**Speak-to-highlight pattern** (drive via Zustand or Context `currentTopic`):
- All tiles: CSS transition, opacity → 0.2, blur(8px), translateZ(-60px).
- Focused tile: opacity 1, blur 0, translateZ(+30px), outline 2px solid accent, box-shadow 0 0 40px rgba(accent, 0.6).
- Unknown/null topic: zero tiles highlighted; all return to base state. Never crash on unknown topic strings.

## VI.7 — Post-FX pipeline

```tsx
<EffectComposer disableNormalPass>
  <DepthOfField focusDistance={0} focalLength={0.02} bokehScale={3} />
  <Bloom intensity={0.9} luminanceThreshold={0.85} luminanceSmoothing={0.3} mipmapBlur />
  <Noise opacity={0.03} premultiply blendFunction={BlendFunction.MULTIPLY} />
  <Vignette offset={0.3} darkness={0.5} />
</EffectComposer>
```

**Pass order matters**: DOF → Bloom → Noise → Vignette. DOF first (focus the frame), Bloom second (glow the in-focus regions), Noise third (film grain on the composite), Vignette last (frame the shot). Any other order degrades the look.

**DOF focus control**: `focusDistance` is normalized 0..1 over camera far. Drive imperatively via ref; convert `worldZ → normalized` as `(targetZ - camera.near) / (camera.far - camera.near)` each frame.

## VI.8 — GPU-tier budget

```ts
import { getGPUTier } from "detect-gpu";
const tier = await getGPUTier(); // 0..3
```

| Tier | Device class | DOF | Bloom | AA | Particles | Canvas dpr | Fallback |
|---|---|---|---|---|---|---|---|
| 3 (Hi) | Desktop RTX / M2+ | full | full | 2× MSAA | full | [1, 2] | — |
| 2 (Mid) | Mid laptop / M1 | half-res | full | 2× MSAA | half | [1, 2] | — |
| 1 (Low) | Integrated | off | intensity 0.4 | FXAA | off | [1, 1.5] | — |
| 0 | iPhone SE / 2015 Android | off | off | none | off | [1, 1] | 2D fallback UI |

**Tier-gate component** wraps the Canvas mount and renders the 2D fallback on tier 0. Five-branch decision tree (resolved 0/1/2/3, pending, rejected, SSR) — all non-canvas branches funnel to the 2D path. Never blank.

## VI.9 — Video cutout strategies (avatar integration)

Three paths, choose based on source type:

- **Path A — Live WebRTC with green-screen backdrop (Anam, Tavus CVI live)**: provider sets `sceneBackgroundColor: "#00ff00"`, WebRTC MediaStream → hidden `<video>` → `VideoTexture` → chromakey shader → material map. Real-time. Zero pre-processing.
- **Path B — Pre-rendered MP4 with MediaPipe segmentation (fallback + cached)**: `video.ontimeupdate` → draw frame to offscreen canvas → MediaPipe Image Segmenter produces person mask → composite RGBA to second canvas → `CanvasTexture`. 30fps on mid tier, 15fps on low, skip on tier 0.
- **Path C — Pre-masked alpha-channel MP4 (best perf, requires asset re-export)**: VP9 or HEVC alpha-channel MP4 → direct `VideoTexture`, transparent frames already. No shader, no segmenter.

**"In the room" treatment** (mandatory when integrating avatar into 3D scene):
- Rim-light uniform pulled from ambient environment sample.
- Contact shadow grounds the plane.
- Fog overlay in avatar's shader tints edges toward scene fog color.
- Edge-blur post-process (2px gaussian) dissolves the cut-out tell.

Without these four, the avatar looks like a sticker. With them, she feels present.

## VI.10 — Typography in 3D

| Use case | Component | Rationale |
|---|---|---|
| Dashboard tile body text | `drei.Html` (transform, occlude="blending") | Crisp HTML text, real DOM, accessible, SEO-crawlable |
| Large floating caption | `drei.Text` (SDF) | Sharp at all distances, cheap, baked-once font |
| Hero headline (once per page) | `drei.Text3D` + `MeshBasicMaterial color=#fff` | Depth-mesh impact, heavy — limit to ONE per page |

**Extreme-contrast recipe**:
- Text always `#FAFAFA` (near-white) on dark.
- Backing pane `meshBasicMaterial` with the section's hard-color accent behind text (no transparency).
- NEVER text on transparent glass — always a scrim.
- Small body text (<18px) → `drei.Html` with backdrop-filter blur + solid-dark scrim + accent border.

Accent colors (violet, cyan, magenta, teal) are for borders, glows, labels, and decorative — NEVER for body copy or stats.

## VI.11 — R3F production patterns (non-negotiable)

From pmndrs / Bruno Simon / Monogrid:

1. **No allocation in useFrame**: pre-allocate vectors at module scope, mutate in place.
   ```ts
   const _tmpVec = new THREE.Vector3();
   useFrame(() => { _tmpVec.set(x, y, z); mesh.current.position.copy(_tmpVec); });
   ```
2. **Uniforms by ref**: `useRef` + mutate `.current.value`. NEVER recreate uniform objects per render.
3. **State via Zustand**: cross-scene state (speech mode, camera target, DOF focus) in a Zustand store. Read with selectors — no prop drilling through 4 layers.
4. **InstancedMesh when N≥10**: particles, LED strips, repeated props.
5. **No Suspense on Canvas**: Suspense wraps ASSET leaves (Model, Video), never the whole `<Canvas>`.
6. **dynamic + `ssr: false`**: Canvas wrapper only, at one single boundary. All 3D imports go through it.
7. **Disposal**: Canvas auto-disposes on unmount. For manually-created textures/geometries, call `.dispose()` explicitly in `useEffect` cleanup.
8. **Event delegation**: pointer events on meshes, not on DOM overlays. `<drei.Html>` stops propagation unless configured.
9. **`useFrame` for 60fps; `useEffect` for mount/unmount; `useLayoutEffect` never**.

## VI.12 — 32-point 3D quality gate

Before any 3D page ships:

**Perf (8)**:
- [ ] Canvas `dpr` capped `[1, 2]`
- [ ] Perf monitor enabled in dev
- [ ] No allocations in `useFrame`
- [ ] All uniforms memoized / ref-stable
- [ ] InstancedMesh for N≥10 similar geometries
- [ ] Textures compressed (KTX2 / Basis)
- [ ] Total polycount < 500k on mid tier
- [ ] GPU tier check + fallback path

**Correctness (8)**:
- [ ] `next.config.ts` has NO `cacheComponents` (or `cacheComponents: false`)
- [ ] `transpilePackages` contains ONLY `three`
- [ ] `@react-three/fiber@9.x` pinned (no rc, no latest)
- [ ] `@react-three/drei@10.x` pinned
- [ ] `overrides: { zustand, three }` in package.json
- [ ] `npm ls` shows single runtime copies, no RC
- [ ] Canvas mounts via `dynamic(..., { ssr: false })` at ONE boundary
- [ ] No Suspense wrapping the whole Canvas

**Accessibility (8)**:
- [ ] `aria-hidden` on `<canvas>` element
- [ ] All text in `drei.Html` (crawlable DOM)
- [ ] Focus-visible rings on HTML inputs
- [ ] Keyboard navigation through tiles (tab order)
- [ ] Touch targets ≥ 48px
- [ ] WCAG AA contrast (4.5:1 body, 3:1 large text)
- [ ] `prefers-reduced-motion` disables parallax + camera dolly
- [ ] `prefers-reduced-transparency` reduces glass alpha

**Polish (8)**:
- [ ] Fog color matches background color
- [ ] DOF focus follows camera target (or focused tile)
- [ ] Bloom AFTER tonemapping (pass order)
- [ ] Contact shadow on all floating content
- [ ] Hero image preloaded
- [ ] WebGL2 feature detection + fallback
- [ ] Autoplay policy respected (muted + gesture gate)
- [ ] Canvas pauses off-screen (IntersectionObserver)

## VI.13 — Avatar / live-call integration (port-contract)

When integrating a live AI avatar into a 3D scene or flat dashboard, treat the token-mint + SDK adapter + React hook as **shared infrastructure** that is copied verbatim, never rebuilt.

**Required infrastructure pieces** (any production-grade avatar integration has these):

1. Server route that mints a short-lived session token from the provider API (Anam / Tavus / etc.), scoped by `surface` (artist/label/custom). Server-only; provider API key never crosses to client.
2. Adapter interface: `connect(config, token) → {stream, onTranscript, onError, disconnect}`.
3. Provider-specific adapter (anam-provider / tavus-provider) implementing the interface.
4. React hook `useAvatarStream({surface})` with imperative `start()` / `stop()`. Hook NEVER mints on mount.
5. `<LiveAvatarFrame>` client component: full-size video with `srcObject = session.stream`, bottom-center captions, text input, End button.
6. `<StartKaiButton>` gate: explicit user-click trigger. Disables during `minting`/`connecting`. Hides once live.
7. Optional bridge to 3D scene: `HolographicKai` or equivalent accepts `stream?: MediaStream` prop; when present, binds to its internal `<video>`; otherwise falls back to pre-rendered MP4.

**Budget rule (free-tier providers like Anam)**: ~3 min/session, concurrent cap = 1. **Agent NEVER mints a session during implementation** — verification is static-only (`curl -I`, `grep`, bundle-chunk evidence). Runtime testing is user-owned.

**Never-rules**:
- Never auto-mint on component mount.
- Never make the Start button implicit or auto-triggered.
- Never wire the text-input to submit a default prompt on focus.
- Never share state between two surfaces (artist / label system prompts stay scoped by `surface` query).

## VI.14 — Extreme-contrast palette (Gen Z / music-industry default)

Hard-color pairs only. No soft gradients for body elements.

| Role | Token | Value |
|---|---|---|
| Base | `--base` | `#050508` |
| Ink | `--ink` | `#FAFAFA` |
| Violet (primary accent) | `--violet` | `#8B5CF6` |
| Cyan (artist surface) | `--cyan` | `#06B6D4` |
| Amber (label surface) | `--amber` | `#F5A524` |
| Magenta (alert / energy) | `--magenta` | `#FF2BD6` |
| Teal (growth) | `--teal` | `#00E5D1` |
| Tungsten (warmth) | `--tungsten` | `#F7E7CE` |
| Console red (retro LED) | `--console-red` | `#FF2B4D` |

No pink / teal / magenta as body text — accents ONLY. Body text is ALWAYS `--ink` on dark. All accent-on-base pairs must meet WCAG AA 4.5:1 for body, 3:1 for large headings.

## VI.15 — Universal patterns from industry-leading 3D sites

What Lusion, Bruno Simon, Monogrid, Active Theory, Basement, and Apple Vision Pro marketing all share (regardless of aesthetic):

1. **Single Canvas, portaled content** (tunnel-rat OR a self-contained scene). Never two Canvas elements competing.
2. **One wow-system per page** (3D particles OR glitch OR split-text OR parallax — never all four).
3. **Decreasing motion up the semantic hierarchy**: atmosphere drifts, content reads still.
4. **Progressive enhancement**: 2D works without WebGL; 3D is an upgrade.
5. **Explicit motion modes**: 0 (minimal), 1 (editorial), 2 (immersive), 3 (cinematic). Default to 1.
6. **Performance budget enforced by hard numbers, not vibes**: INP < 200ms, LCP < 2.5s, CLS < 0.1, frame budget 16.6ms on Tier 2.
7. **Accessibility is not negotiable** — the 8 a11y items in VI.12 are pass/fail.

Any 3D site that violates 2+ of these reads as amateur or broken. Hit all seven and the site reads premium regardless of budget.

## Part VII — Lessons learned building a real Next 16 + R3F 9.6 + React 19 3D studio (2026-04-20)

These are non-negotiable rules derived from an actual multi-hour debug cycle on the `/demo/studio` route of the unsign codebase. Every rule below is backed by reproduced failure evidence. Apply on every new R3F page.

### VII.1 — Cross-root state rule (THE most important R3F rule)

**Never use React Context for state that crosses a Canvas or drei.Html boundary.**

- `<Canvas>` from `@react-three/fiber` creates a new React root via `createRoot` internally.
- `<Html>` from `@react-three/drei` ALSO creates a new React root via `ReactDOM.createRoot(el)` (verified in source at `@react-three/drei/web/Html.js:143`).
- React Context does NOT propagate across separate roots.
- A Context provider placed ABOVE `<Canvas>` is invisible to any `useContext` call inside the Canvas scene.
- A Context provider placed inside `<Canvas>` but OUTSIDE `<Html>`'s portal is invisible to any component rendered inside the Html.

**What to use instead:** Zustand (module-scoped external store, read via `useSyncExternalStore`, cross-root safe). Jotai works too. Any external-store library. The cost is approximately zero — you keep the `useXxx()` hook signature identical so consumers don't change.

**Symptom when you get this wrong:** `Error: useXxx must be used inside XxxProvider` thrown from a component that LOOKS like it's inside the provider. The component is technically a descendant of the provider JSX element, but across a createRoot boundary.

**Recipe for converting a Context to a zustand store while preserving public API:**

```ts
// BEFORE — React Context pattern (breaks inside drei.Html)
const MyContext = createContext<MyValue | null>(null);
export function MyProvider({ children }) {
  const [state, setState] = useState(initial);
  return <MyContext.Provider value={{state, setState}}>{children}</MyContext.Provider>;
}
export function useMy() {
  const ctx = useContext(MyContext);
  if (!ctx) throw new Error("useMy must be used inside MyProvider");
  return ctx;
}

// AFTER — zustand store, same public shape
import { create } from "zustand";
const useMyStore = create<MyValue>((set) => ({
  ...initial,
  setState: (next) => set({ state: next }),
}));
// MyProvider becomes a no-op pass-through so existing call sites don't break.
export function MyProvider({ children }) { return <>{children}</>; }
export function useMy() { return useMyStore(); }
```

### VII.2 — Next 16 dev cross-origin HMR rule

Next 16 blocks `/_next/webpack-hmr` WebSocket connections from any origin that is not `localhost`. If you reach the dev server from any other host (WSL2 eth0 IP, LAN IP, `.local` hostname, device hostname), HMR fails silently and **React client hydration aborts on the main app tree** — only the Next devtools portal hydrates. The page freezes on SSR output.

**Fix:** add the host to `allowedDevOrigins` in `next.config.ts`:

```ts
const nextConfig: NextConfig = {
  // ...
  allowedDevOrigins: ["172.29.51.209", "10.255.255.254", "localhost"],
};
```

Dev-only; `next build` / `next start` ignore it. Docs: https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins

**Symptom when missing:** Body tree has zero React fibers. Only `NEXTJS-PORTAL` has fibers. Console shows `WebSocket connection to 'ws://<host>:<port>/_next/webpack-hmr' failed`. CDP listener (`Runtime.enable` + `Log.entryAdded`) catches it; `agent-browser errors` does NOT.

### VII.3 — Turbopack HMR is not reliable for scene-graph edits

When editing R3F scene components during dev, HMR may appear to reload but leave stale chunks in Chrome memory. Stack traces will point at lines that are comments in the new code.

**Hard reset recipe:**

1. `kill -9 <next-server-pid>`
2. `rm -rf .next`
3. Cold `npm run dev` restart
4. Hard reload in Chrome with `ignoreCache: true` via CDP `Page.reload`

Skipping steps 1–3 produces phantom bug reports from stale bundles.

### VII.4 — Always verify the render loop with a test cube first

When the canvas renders black and you're about to adjust fog/lighting/camera/DOF/materials, STOP. First drop a naive test cube into the scene:

```tsx
<mesh position={[0, 0, 0]}>
  <boxGeometry args={[200, 200, 200]} />
  <meshBasicMaterial color="#ff00ff" toneMapped={false} />
</mesh>
```

`meshBasicMaterial` needs no lighting, is not tone-mapped, and ignores scene shading. With a typical camera (`[0, 80, 1200]` fov 35 looking at origin), this cube WILL be visible if the render loop runs and the WebGL context is valid.

- Cube visible → render loop + WebGL OK; your problem is fog / lighting / materials / DOF / camera frustum.
- Cube invisible → render loop is broken (`useFrame` throwing, Canvas suspended, WebGL context lost, alpha-compositing hiding the frame). Do NOT tune scene settings until the cube shows up.

### VII.5 — drei.Html transform + distanceFactor can degenerate

When `<Html transform distanceFactor={N}>` interacts with a wide FOV or large scene scale, the CSS `matrix3d` transform can produce runaway values (1e7+ in the Z translation slot). The tile ends up millions of units off-screen.

**Verify at runtime:**

```js
const t = document.querySelector('.kai-tile-3d');
const wrapper = t?.closest('div[style*=matrix3d]');
console.log(wrapper?.style.transform);
// If you see "matrix3d(..., 1.67572e+07, 1)" or similar scientific notation, bug confirmed.
```

**Fix:** reduce `distanceFactor` toward its default (10) and re-test. Or avoid `transform` mode entirely if you want plain DOM overlays.

### VII.6 — WebGL framebuffer sanity check

When the canvas looks black, sample real pixel values before assuming scene is just dark:

```js
const c = document.querySelector('canvas');
const cn = document.createElement('canvas');
cn.width = 20; cn.height = 20;
cn.getContext('2d').drawImage(c, 0, 0, 20, 20);
const d = cn.getContext('2d').getImageData(0, 0, 20, 20).data;
let maxR=0, maxG=0, maxB=0, maxA=0;
for (let i=0; i<d.length; i+=4) { maxR=Math.max(maxR,d[i]); maxG=Math.max(maxG,d[i+1]); maxB=Math.max(maxB,d[i+2]); maxA=Math.max(maxA,d[i+3]); }
console.log({maxR, maxG, maxB, maxA});
```

- All zeros (including alpha=0) → WebGL context is transparent and drawing nothing. `gl={{ alpha: false }}` not honored or render loop not running.
- RGB near zero, alpha=255 → scene IS painting, just very dark. Tune lighting/fog.
- CSS background `#050508` bleeding through (5,5,8) → canvas transparent, CSS underlay showing; decide if that's intentional.

### VII.7 — Scene background must be explicit

Don't rely on CSS `background` on the `<canvas>` element to provide the scene's base color. Set it explicitly in the scene:

```tsx
<color attach="background" args={["#050508"]} />
// OR at Canvas level:
<Canvas style={{ background: "#050508" }} gl={{ alpha: false }} />
```

If `alpha: false` isn't reliably honored by Turbopack-cached bundles, the CSS fallback protects you. If `alpha: false` IS honored, scene.background takes over. Belt AND suspenders.

### VII.8 — The visual review path for 3D routes

Every 3D page gets the same verification order during development:

1. **Dev server up, route 200.** Simple curl from the same network Chrome will use.
2. **Hydration check.** Walk the DOM body for `__reactFiber$` keys. Zero = hydration broke; fix upstream (origin, env, bundle) before anything else.
3. **Canvas element present.** `document.querySelector('canvas')` non-null.
4. **Pixel sample.** Per VII.6. Not all zeros? Render loop is alive.
5. **Test cube visible.** Per VII.4. Visible? Scene graph + camera are OK.
6. **Remove test cube, tune fog/lighting/DOF.**
7. **Parallax + click-to-focus.** Only after the static scene reads correctly.

Skipping steps produces hour-long rabbit holes where you tune DOF while the render loop isn't even ticking.

### VII.9 — Camera + parallax + click-to-focus reference impl (spatial storytelling)

For the "Kai is in the studio, she directs the camera" pattern:

```tsx
// components/kai-3d/CameraRig.tsx (sketch; ground-truth lives in the repo)
const { camera, pointer } = useThree();
const focusedTopic = useSpeechStore((s) => s.currentTopic); // zustand, cross-root
const tilePositions = {/* topic → vec3 */};

useFrame((_, delta) => {
  // Neutral target (no focus): lerp camera to base POV + mouse parallax.
  const base = MODE_CAMERA[selectedId] ?? MODE_CAMERA.default;
  const target = new THREE.Vector3(
    base[0] + pointer.x * 60,
    base[1] + pointer.y * 40,
    base[2] - Math.abs(pointer.x) * 20 - Math.abs(pointer.y) * 20,
  );
  camera.position.lerp(target, delta * 3);

  // Yaw/pitch parallax — small, lerped, feels like head turn not slide.
  const yawRad = pointer.x * THREE.MathUtils.degToRad(3);
  const pitchRad = -pointer.y * THREE.MathUtils.degToRad(2);
  const lookTarget = new THREE.Vector3(0, 0, 0);
  if (focusedTopic && tilePositions[focusedTopic]) {
    lookTarget.copy(tilePositions[focusedTopic]);
  }
  camera.lookAt(lookTarget);
  // Apply additional yaw/pitch offsets via quaternion slerp if desired for
  // cursor-driven head turn on top of lookAt.
});
```

Tile focus state in zustand:

```ts
const useSpeechStore = create<...>((set) => ({
  state: "idle",
  currentTopic: null,
  setState: (next) => set((prev) =>
    prev.state === "speaking" && next !== "speaking"
      ? { state: next, currentTopic: null } // auto-clear topic when leaving speaking
      : { state: next }
  ),
  setCurrentTopic: (t) => set({ currentTopic: t }),
}));
```

DOF follows focus distance via the same store:

```tsx
// StudioPostFX.tsx
const focusedTopic = useSpeechStore((s) => s.currentTopic);
const focusDistance = useRef(0); // lerp toward target
useFrame(() => {
  const target = focusedTopic && tilePositions[focusedTopic]
    ? camera.position.distanceTo(tilePositions[focusedTopic]) / (camera.far - camera.near)
    : 0;
  focusDistance.current = THREE.MathUtils.lerp(focusDistance.current, target, 0.1);
});
<DepthOfField focusDistance={focusDistance.current} focalLength={0.02} bokehScale={3} />
```

This is the canonical shape for "Kai narrates, scene reframes, tile expands" — three modules (CameraRig, StudioPostFX, FloatingTile) all subscribe to the same zustand store. One source of truth, no Context, cross-root safe.

### VII.10 — Quality gate additions for Part VII

```
[ ] VII-1  No React Context used for state that crosses Canvas or drei.Html. zustand/external-store only.
[ ] VII-2  Next 16 dev: allowedDevOrigins covers every host the dev server is reached from.
[ ] VII-3  After any R3F edit: kill dev, rm .next, cold restart, hard reload. No HMR trust.
[ ] VII-4  Test cube at origin visible BEFORE tuning fog/lighting/DOF/materials.
[ ] VII-5  drei.Html transform matrices sampled; no 1e7+ values in Z translation slot.
[ ] VII-6  Canvas pixel sample non-zero before declaring "scene is just dark".
[ ] VII-7  Scene background set explicitly via <color attach="background"> or Canvas CSS (both).
[ ] VII-8  Visual review walks hydration → canvas → pixels → test cube → scene in that order.
[ ] VII-9  Camera parallax + click-to-focus + DOF drive from ONE external store; no Context plumbing.
[ ] VII-10 WebGL context attributes verified: gl.getContextAttributes().alpha matches intent.
```

---

## Part VIII — 2D-Photo-to-3D-Parallax Recipe (LOCKED, 2026-04-28)

> **Why this section exists:** the KAI v6.4-v6.11 build cycle repeatedly tried to convert a flat photographic studio plate into a 3D parallax scene by piling vertex-displacement geometry on top of legacy 3D primitives. Stage 3 review at /demo/studio (2026-04-28 22:00) revealed a "gray pillar" failure: meshStandardMaterial + displacementMap + 256x128 subdivisions on a 3000x1500 plane sculpted vertex relief that intersected the foreground console + tiles + Kai. User direction: "DO NOT EXPIUERMENT SEE HOW OTHERS HAVE ALREADY SUCCESSFULY DONE THIS / DO EXTENSIVE Research / DO not assume / FOLLOW A PROVEN PLAN". This section captures the canonical, research-cited pattern so future iterations cannot repeat the failure.

### VIII.1 — When to use

You have a flat 2D photograph (or AI-generated still) plus a paired greyscale depth map (closer-pixel-brighter convention). You want camera dolly + cursor parallax to read as a 3D scene without modeling props or running splat reconstruction.

| Use case | UV-shift on flat plane (Section VIII.3) | Vertex displacement (Section VIII.4 anti-pattern) |
|---|---|---|
| Photo back plate behind 3D foreground content | ✅ correct | ❌ sculpts geometry into foreground |
| Sculpted relief landscape / terrain | ❌ wrong technique | ✅ correct |
| Cinematic Ken Burns from a single still | ✅ correct | ❌ overkill |
| Photo plate with no foreground 3D | both work | both work |

### VIII.2 — Cited proven sources

These are the references this recipe is distilled from. When in doubt, read them, do not improvise.

- Codrops "Reactive Depth: Building a Scroll-Driven 3D Image Tube with React Three Fiber" (2026-02-17) — the most current end-to-end R3F implementation.
- Codrops "Scroll, Refraction and Shader Effects in Three.js and React" (2019-12-16) — long-standing canonical pattern.
- akella "Facebook 3D Photos with Three.js" (Medium) — depth-map UV-offset baseline.
- Alan Zucconi "Parallax Shaders & Depth Maps" (alanzucconi.com) — the math behind why UV offset works.
- `blaineo/react-depth-map` (GitHub) — shipping React component reference.

### VIII.3 — Canonical UV-shift recipe

The depth map drives a per-pixel UV offset in the fragment shader. The plane geometry stays flat. The parallax illusion lives entirely in image space — no geometry intersects foreground content.

```tsx
// components/SpatialPhotoPlate.tsx
"use client";

import { useFrame, useThree } from "@react-three/fiber";
import { useTexture } from "@react-three/drei";
import { useMemo, useRef, type ReactElement } from "react";
import * as THREE from "three";

const VERTEX = /* glsl */ `
  varying vec2 vUv;
  void main() {
    vUv = uv;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

const FRAGMENT = /* glsl */ `
  varying vec2 vUv;
  uniform sampler2D uTexture;
  uniform sampler2D uDepthMap;
  uniform vec2 uMouse;
  uniform float uIntensity;
  void main() {
    float depth = texture2D(uDepthMap, vUv).r;
    float parallax = (depth - 0.5) * 2.0 * uIntensity;
    vec2 offsetUv = vUv + (uMouse * parallax);
    gl_FragColor = texture2D(uTexture, offsetUv);
  }
`;

type Props = {
  albedoUrl: string;
  depthUrl: string;
  position?: [number, number, number]; // default [0, 0, -1000]
  intensity?: number;                  // default 0.04 desktop / 0.025 mobile
};

export function SpatialPhotoPlate({
  albedoUrl,
  depthUrl,
  position = [0, 0, -1000],
  intensity = 0.04,
}: Props): ReactElement {
  const { camera } = useThree();
  const albedo = useTexture(albedoUrl);
  const depth = useTexture(depthUrl);

  const { width, height } = useMemo(() => {
    // Plane sizing: height = 2 * tan(vFov/2) * distance from camera.
    // Width follows albedo aspect so the texture fills uniformly.
    const persp = camera as THREE.PerspectiveCamera;
    const distance = Math.abs(camera.position.z - position[2]);
    const vFov = (persp.fov * Math.PI) / 180;
    const h = 2 * Math.tan(vFov / 2) * distance;
    const img = albedo.image as { width?: number; height?: number } | undefined;
    const aspect =
      img?.width && img.height
        ? img.width / img.height
        : 16 / 9;
    return { width: h * aspect, height: h };
  }, [camera, position, albedo.image]);

  const uniforms = useMemo(
    () => ({
      uTexture: { value: albedo },
      uDepthMap: { value: depth },
      uMouse: { value: new THREE.Vector2(0, 0) },
      uIntensity: { value: intensity },
    }),
    [albedo, depth, intensity],
  );

  const target = useRef(new THREE.Vector2(0, 0));
  useFrame(({ pointer }) => {
    target.current.set(pointer.x * 0.5, pointer.y * 0.3);
    uniforms.uMouse.value.lerp(target.current, 0.08);
  });

  return (
    <mesh position={position}>
      {/* Flat plane, ZERO subdivisions. UV-shift lives in fragment shader. */}
      <planeGeometry args={[width, height, 1, 1]} />
      <shaderMaterial
        vertexShader={VERTEX}
        fragmentShader={FRAGMENT}
        uniforms={uniforms}
        transparent={false}
        depthWrite={false}
        side={THREE.FrontSide}
      />
    </mesh>
  );
}
```

**Plane sizing formula** (intrinsic to UV-shift technique):

```
height = 2 * tan(vFov / 2) * distance
width  = height * (albedoWidth / albedoHeight)
```

For a camera at z = +1200, plate at z = -1000, FOV = 35°: distance = 2200, height ≈ 1387 scene-units. Width follows the photo aspect ratio.

**Position rule:** plate sits behind ALL foreground content. If foreground tiles live at z=+200..+600 in scene-units, plate at z=-1000 leaves a 1200-unit clearance. Closer than ~500 units risks z-fighting under camera dolly.

**Intensity rule:** 0.04 (desktop) / 0.025 (mobile). Higher values amplify edge swim and break the illusion. Lower values barely register.

### VIII.4 — Anti-Pattern #32: Vertex displacement on 2D-photo-to-3D plates (FORBIDDEN)

```tsx
// ❌ FORBIDDEN — produces sculpted geometric relief that intersects
// foreground content. This is the "gray pillar" failure mode.
<mesh position={[0, 0, -500]}>
  <planeGeometry args={[3000, 1500, 256, 128]} />
  <meshStandardMaterial
    map={albedo}
    displacementMap={depth}
    displacementScale={200}
  />
</mesh>
```

**Why this fails:** `displacementMap` shifts vertex Z by `(map - 0.5) * displacementScale`. With 256x128 subdivisions, the plane warps into a sculpted relief that pokes through anything sitting at z > plate-position - max-displacement. With foreground tiles at z=+200 and a plate at z=-500 with displacementScale=200, displaced vertices reach z=-300 — close enough to the foreground that bright depth-map regions sculpt a "pillar" between Kai and the tiles.

**Why UV-shift wins:** the plane stays flat. Depth drives where the texture *samples* from, not where geometry *sits*. A bright depth pixel is just "sample this texel from a slightly offset UV"; no Z-coordinate ever moves.

### VIII.5 — Section 6c Trap 5: Dual-mounting legacy 3D primitives + photo plate

```tsx
// ❌ FORBIDDEN — produces double-environment overlap.
return (
  <>
    <StudioRoom />            {/* legacy 3D console + glass + drum kit */}
    <SpatialPhotoPlate ... /> {/* photo with same content baked in */}
  </>
);
```

**Why this fails:** the photo plate's texture already contains the room (console, drum kit, glass, mic stand, speakers). Rendering legacy 3D primitives in front of it creates double-console / double-glass / double-drum-kit overlap. Both versions of the room compete for the same screen pixels.

**Correct contract:** environment rendering is a SINGLE-MOUNT branch. Either the plate (when flag ON, Loaded, no error) OR the legacy primitives (flag OFF or any fallback path). Never both.

```tsx
// ✅ CORRECT — single-mount contract. StudioBackground returns
// either the plate or the fallback primitives, never both.
function StudioBackground() {
  const { Loaded, loadFailed } = useDepthMeshModule();
  if (!FLAG_ON) return <LegacyStudioRoom />;
  if (loadFailed) return <LegacyStudioRoom />;
  if (!Loaded) return <LegacyStudioRoom />;
  return (
    <ErrorBoundary fallback={<LegacyStudioRoom />}>
      <Suspense fallback={<LegacyStudioRoom />}>
        <Loaded layerKey={...} />
      </Suspense>
    </ErrorBoundary>
  );
}
```

### VIII.6 — Quality Gate DEPTH-PARALLAX-RECIPE (LOCKED)

```
[ ] DPR-1  Vertex shader is passthrough — no position mutation.
[ ] DPR-2  Fragment shader samples depth, computes parallax = (depth - 0.5) * 2 * intensity, offsets UV by uMouse * parallax.
[ ] DPR-3  Geometry is planeGeometry [width, height, 1, 1] — ZERO subdivisions.
[ ] DPR-4  Material is THREE.ShaderMaterial — NOT meshStandardMaterial / meshBasicMaterial / meshPhysicalMaterial with a displacementMap prop.
[ ] DPR-5  No `displacementMap`, `displacementScale`, `displacementBias`, or `subdivisions: [N, M]` on the photo-plate component.
[ ] DPR-6  Plane sizing matches `height = 2 * tan(vFov/2) * distance` formula; aspect derived from albedo image.
[ ] DPR-7  Plate position z is BEHIND every foreground 3D element; clearance ≥500 scene-units to nearest foreground z.
[ ] DPR-8  Environment render is SINGLE-MOUNT — legacy primitives render only inside the plate's fallback path, never alongside.
[ ] DPR-9  uIntensity ≤ 0.05 desktop / ≤ 0.03 mobile. Higher values produce edge swim.
[ ] DPR-10 Provenance: photo + depth referenced via a manifest with sha256 ledger; runtime probe verifies loaded URL hash matches ledger entry.
```

### VIII.7 — DO-NOT-USE upscaler BLACKLIST (cross-link from poe-media skill)

When the photo-plate albedo needs higher resolution, do not run it through:

- **TopazLabs** — HTTP 500 image-field bug as of 2026-04. Confirmed broken on the Poe API endpoint.
- **Clarity-Upscaler** — produces edge artifacts ("really weird and many strange artifacts" — user verbatim 2026-04-28).
- **Remini-Upscaler** — outputs lossy 1024x768 JPEG regardless of `--scale` flag, defeating the purpose.

If a photo plate needs sharper detail, regenerate at native resolution from the source model (Nano-Banana-Pro 1792x768 or 1024x1792 native), or render the plate at the camera's pixel-resolved size and skip upscaling entirely. The bundled `references/scene-plate-playbook.md` carries the locked BLACKLIST as the authoritative source.


---

## Lesson appended 2026-05-04 (KAI v7 Phase B)

**Decoration without semantic data is forbidden in Mode 3 cinematic environments.**

In KAI Studio v7 (project: /home/cabule/unsign), an earlier session shipped `AtmosphereOrbs.tsx` — two violet/cyan `meshBasicMaterial` spheres at z=-800 with random sinusoidal drift at desynced frequencies (0.15/0.18/0.20/0.22 Hz). They were intended as ambient stage-lighting decoration but violated three rules:

1. **Master plan rule**: "motion must be user-triggered, state-driven, or ambient breathing — never random."
2. **Principle 5 (Restrained)**: every element must earn its place; pure decoration without data binding is dead weight.
3. **User-stated defect**: "two big circles just moving and animating randomly that have nothing to do with the plan" — the orbs read as visual noise, not atmosphere.

The fix in v7 Phase B: delete the file, remove the import + JSX from StudioScene.tsx, and replace the orbs' actual function (warmth + atmosphere) with the existing tungsten pendant point-light + hemisphere ambient already specified in the plan — accomplishes the mood without orbital geometry.

**Generalizable rule**: when a 3D scene needs "warmth" or "atmosphere," use lighting (point lights, hemisphere, fog, post-FX bloom) NOT additional decorative geometry. Geometry should always carry semantic meaning (data, controls, navigation). Lighting is the right tool for mood.
