---
name: beautiful-converting-frontend-design
description: Create distinctive, conversion-optimized frontend interfaces. Fuses Hormozi conversion architecture with GSAP/Lenis/ScrollTrigger animations, OSMO-level techniques, and cutting-edge design. Mandatory quality gate prevents generic output.
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Skill", "Agent", "WebSearch", "WebFetch"]
---

# Beautiful Converting Frontend Design

This skill produces premium, conversion-optimized frontend interfaces. Every output fuses Hormozi conversion architecture with GSAP/Lenis/ScrollTrigger animations, OSMO-level techniques, and cutting-edge visual design. A mandatory 24-point quality gate prevents generic output from ever reaching the user.

---

## 1. Design DNA — 7 Universal Principles

These are non-negotiable. Every decision filters through them.

### Principle 1: Premium by Default

Every default elevates. Distinctive fonts (NEVER Inter/Roboto/Arial). Depth through glass, grain, gradients, shadows — not flat. Theme adapts to the project (dark, light, or custom). Quality is non-negotiable regardless of palette.

### Principle 2: Conversion-Aware

Every visual decision has a conversion implication. Scroll-triggered value stacks create anticipation. Parallax creates depth behind testimonials. Counter animations make stats feel earned. Design IS the conversion mechanism — not decoration applied after.

### Principle 3: Motion-Rich

Static is dead. Every section has scroll-triggered GSAP animation. Lenis smooth scroll is mandatory. BarbaJS page transitions when multi-page. Every animation has PURPOSE: reveal, guide, confirm, or delight. No gratuitous motion.

### Principle 4: Distinctive

If you cannot tell the brand from the design, it is too generic. Font tells industry. Palette is unexpected. Layout breaks the grid somewhere. One "wow" moment per page minimum. If it could belong to any brand, it belongs to none.

### Principle 5: Restrained

Fewer elements, more impact. White space signals premium. One focal point per section. 60-30-10 color ratio. Glass on max 5 elements. Generous section padding. Maximalism and minimalism both work — but every element must earn its place.

### Principle 6: ZERO INLINE CSS — HARD RULE

Never use `style=` attributes in HTML. Never use `element.style.xxx` in JS (except CSS custom properties via `setProperty`). Everything goes in CSS files with classes and variables. No exceptions.

Why: Inline styles have specificity 1000, cannot use media queries, cannot find/replace, and break theming. Dynamic values use CSS custom properties. Per-item styles inject `<style>` blocks. Theme changes = edit ONE file.

### Principle 7: FAST — PageSpeed 90+ Mandatory

Beautiful animations are worthless if users bounce. Hard targets:

- **LCP** < 2.5s
- **INP** < 200ms
- **CLS** < 0.1
- Critical CSS inline (under 14KB)
- All JS deferred at end of body
- Fonts: `display=swap`, max 2 families, subset latin
- Hero image preloaded, below-fold lazy
- Only animate `transform`/`opacity` (GPU composited)
- Canvas paused off-screen, particles reduced on mobile
- Glass elements capped (max 5)

### Color Theme — OPEN

Theme is determined by project brief, not by skill default:

- **Dark**: Near-black `#050508`, elevation = lightness, colored glow shadows
- **Light**: Warm whites `#FAFAFA`/`#F5F5F0`, subtle shadows, colored accents
- **Custom**: User's brand palette adapted to the principles above

---

## 2. Mandatory 6-Phase Workflow

No phase may be skipped. No output delivered without Phase 6.

```
Phase 1: UNDERSTAND
  Read brief → identify brand maturity → select conversion style → commit to design direction
  Read upstream/ui-ux-pro-max/ for industry-specific style guidance (67 UI styles, 161 industry rules)

Phase 2: DESIGN SYSTEM
  Read references/design-system-generator.md → generate tokens (fonts, colors, spacing, radii, shadows)
  Cross-reference upstream/ui-ux-pro-max/ for color palettes (161) and font pairings (57)

Phase 3: STRUCTURE
  Select conversion style → Read references/conversion-framework.md
  Invoke: Skill("copywriting") + Skill("page-cro") + Skill("marketing-psychology")
  Build complete page architecture with copy

Phase 4: BUILD
  Read references/css-architecture.md + references/performance.md + references/visual-styles.md + references/responsive-sections.md
  Select visual style(s) matching the brand (neumorphism, brutalist, luxury dark, etc.)
  Implement HTML + CSS (zero inline styles)

Phase 5: ANIMATE
  Read references/animation-patterns.md + references/osmo-techniques.md
  Add GSAP/Lenis/ScrollTrigger animations with purpose

Phase 6: SELF-REVIEW
  Run 24-point quality gate → fix ALL failures → deliver only when clean
```

Each phase MUST load its reference files before proceeding.

---

## 3. Conversion Intelligence — 4 Adaptive Styles

### The Hormozi Value Equation (applies to ALL styles)

```
Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort & Sacrifice)
```

Every section maps to this equation. Design maximizes the numerator, minimizes the denominator.

### Style 1: Hormozi/ClickFunnels — Direct Conversion (DEFAULT)

**Use for:** SaaS landing pages, lead gen, product launches, course sales, SMB sites.

- Dream outcome headlines, pain agitation, value stacking, risk reversal
- Ultra-clear, specific, number-driven copy: "97% accuracy" not "high accuracy", "in 30 seconds" not "quickly"
- Single action per page, CTA repeated after every value section
- **9-section page flow:**
  1. Hero (dream outcome + primary CTA)
  2. Pain (agitate the problem)
  3. Solution (introduce the mechanism)
  4. Value Stack (pile on benefits with specificity)
  5. Social Proof (testimonials, logos, stats)
  6. How It Works (3-step simplicity)
  7. CTA (repeat with urgency)
  8. Objection Handling (FAQ, risk reversal, guarantees)
  9. Final CTA (last chance, scarcity)

### Style 2: Brand/Aspirational — Apple/Nike/Givenchy/AMBUSH

**Use for:** Established brands, luxury, consumer hardware, fashion, streetwear, creative agencies, beauty/skincare.

- Minimal copy, maximum visual impact. Emotion over logic.
- Product as hero. Short declarative statements.
- Still conversion-aware: CTA exists, just subtler.
- **Visual style selection** (read `references/visual-styles.md` for CSS recipes):
  - Fashion/streetwear → Brutalist typography + glitch effects
  - Luxury goods → Dark theme with selective glow + serif accents
  - Consumer hardware/tech → Neumorphism or 3D product integration
  - Beauty/skincare → Immersive product-as-hero + floating elements
- **Product-as-hero layout**: product fills 60%+ viewport, text overlays minimally, background gradient matches product color
- **Neumorphism vs glassmorphism**: neumorphism for soft/approachable (wellness, utility), glassmorphism for tech/futuristic. Never combine both.
- **Page flow** (5 sections, not 9 — brevity is luxury):
  1. Hero (product as hero, brand name, single tagline)
  2. Story (one powerful image + one declarative statement)
  3. Details (product features, minimal text, large imagery)
  4. Social proof (editorial press quotes, not star ratings)
  5. CTA (subtle, premium — "Discover" not "Buy Now")

### Style 3: Editorial/Technical — Stripe/Linear

**Use for:** Developer tools, B2B enterprise, APIs, technical infrastructure.

- Long-form storytelling, technical precision, developer trust.
- Still conversion-aware: "Start free" CTA earned through respect.

### Style 4: Community/Social — Notion/Figma

**Use for:** Platforms, tools with network effects, marketplaces.

- User-generated proof. Templates, showcases, "see what others built."
- Still conversion-aware: "Join 10M+ teams" as social proof conversion.

### How the Skill Decides

- Phase 1 identifies project's brand maturity, audience, and goal
- Startup / SMB / unknown → **Style 1 (Hormozi)** by default
- Established brand with existing identity → Style 2 or 3
- Platform / community product → Style 4
- **Hormozi CLARITY principles (specificity, reasons, active voice) apply to ALL styles**

---

## 4. Copy Rules (Hormozi — Apply to ALL Styles)

- **One story per section.** One idea. One emotion. One action.
- **Headline = Dream Outcome.** Subhead = How you deliver it.
- **Give reasons.** Every claim has evidence. "X because Y."
- **Specificity > vagueness.** Numbers, timeframes, percentages.
- **Reduce friction.** Remove qualifiers, hedging, passive voice. Direct. Active. Certain.
- **Max text width: 700px.** 45-75 characters per line optimal readability.

---

## 5. Design Thinking (Phase 1 Decisions)

Before any code, commit to a direction:

- **Purpose**: What does this interface solve? Who uses it? What action?
- **Tone**: Dark luxury, brutally minimal, retro-futuristic, organic warmth, editorial precision, playful delight, industrial utility. Aesthetic MUST serve conversion.
- **Constraints**: Framework, performance budget, accessibility.
- **Differentiation**: What will someone remember 10 minutes after leaving? Design for THAT.

**CRITICAL**: Intentionality over intensity. Bold maximalism and restrained minimalism both convert — every choice must be deliberate. No default values. No "it looks fine."

---

## 6. Anti-Patterns — 18 Things to NEVER Do

| # | Anti-Pattern | Why It Fails | Do Instead |
|---|-------------|-------------|------------|
| 1 | Inter/Roboto/Arial/system fonts | AI-slop indicator #1 | Geist, Satoshi, Bricolage Grotesque, Instrument Sans |
| 2 | Purple gradient on white bg | Most cliche AI aesthetic | Intentional palette with contrast hierarchy |
| 3 | Glass on every element | Kills perf, dilutes effect | Glass on nav, CTAs, 2-3 key cards max |
| 4 | Static flat backgrounds | Boring, no depth | 3-layer system (gradient + particles + grain) |
| 5 | Even color distribution | No hierarchy | 60-30-10 with one dominant accent |
| 6 | Pure black (#000) | Void, not depth | Near-black (#050508) or warm whites |
| 7 | Animations everywhere | Overwhelms, no rhythm | One orchestrated stagger per section |
| 8 | Stock photos | Generic | Product screenshots, diagrams, custom illustrations |
| 9 | Vague copy | "Better experience" | Specific: "97% accuracy", "150 WPM", "30 seconds" |
| 10 | CTA buried below fold | Missed conversions | Primary CTA visible immediately |
| 11 | Ignoring mobile perf | Laggy glass on phones | Feature-detect, reduce effects |
| 12 | Same fonts every project | Pattern detected | Deliberately vary across generations |
| 13 | `style="..."` inline CSS | Specificity 1000, unmaintainable | CSS classes + variables + data-attributes |
| 14 | Render-blocking JS in head | Blocks first paint, kills LCP | `defer` at end of body, critical CSS inline |
| 15 | Centered everything | No visual tension | Asymmetric layouts, Z-pattern, intentional alignment |
| 16 | Uniform card grids | Template look | Bento grids, varied sizes, featured items |
| 17 | Generic hero ("Welcome to...") | Zero differentiation | Bold claim, specific dream outcome, or provocative question |
| 18 | No reduced-motion respect | Accessibility violation | `prefers-reduced-motion` media query on all animations |
| 19 | Same visual style every project | Pattern detected, AI-slop | Rotate: glassmorphism, neumorphism, brutalism, luxury dark, product-hero based on brand |

---

## 7. Self-Review Quality Gate — 24 Points (MANDATORY)

All 24 must pass BEFORE showing ANY output to the user:

```
[ ] FONT       — Distinctive? Would I recognize the brand from the font alone?
[ ] COLOR      — Unexpected palette? NOT default template colors?
[ ] THEME      — Intentional choice (dark/light/custom) appropriate for project?
[ ] GSAP       — Every section has scroll-triggered animation?
[ ] LENIS      — Smooth scroll initialized with GSAP sync? Anchor link handler with lenis.scrollTo() for all a[href^="#"]? Mobile fallback to scrollIntoView?
[ ] CONVERSION — Page follows chosen conversion style? (Hormozi 9-section DEFAULT)
[ ] COPY       — Clear, specific, no hedging? Hormozi clarity applies to ALL styles?
[ ] CTA        — Primary CTA above fold at desktop (1280x800) AND highest contrast element?
[ ] DEPTH      — At least 2 layers (gradient + grain, glass + glow, shadow + texture)?
[ ] WOW        — At least one moment that would impress on Awwwards?
[ ] AI-SMELL   — Would someone identify this as AI-generated? (If yes -> FIX)
[ ] A11Y       — prefers-reduced-motion? Focus indicators? Semantic HTML?
[ ] SNAP        — If snap enabled: EVERY section fits within viewport at ALL breakpoints? If ANY section overflows → snap disabled for that section or globally?
[ ] SECTIONS    — Every section fits within one viewport height at ALL breakpoints (desktop, tablet, Android)?
[ ] SVH         — Uses svh/min-height with nav-height subtraction (not fixed vh) for full-viewport sections?
[ ] MOBILE-CTA  — Primary CTA visible without scrolling at 360x668 (worst-case Android with browser chrome)?
[ ] SAFE-AREA   — viewport-fit=cover meta tag? env(safe-area-inset-*) on container/sticky elements?
[ ] WORDWRAP   — All headings use overflow-wrap: normal? No heading allows break-word or break-all?
[ ] DEPTH      — At least 3 visual layers visible (gradient + texture + content separation)?
[ ] SNAP-FEEL  — Snap duration max >= 2s? Delay present? Directional enabled?
[ ] VARIETY    — At least 3 DIFFERENT entrance animation types used across sections?
[ ] STATS-VERIFIED — All numbers/stats on page verified against actual source data?
[ ] LINKS-WORK — Every link on page points to a real destination (no dead href="#")?
[ ] ANCHOR-TARGETS — Every href="#id" has a matching id="" element on the page? No orphan anchors?
```

If ANY point fails, fix it before delivering. This gate is not optional.

---

## 8. Tool Registry + Intelligent Routing

| Tool | Invoke | When | Fallback |
|------|--------|------|----------|
| **GSAP+Lenis+BarbaJS** | CDN + references/animation-patterns.md | EVERY project (mandatory) | N/A — core requirement |
| **Google Stitch** | `python3 scripts/google_stitch.py` | Layout inspiration + visual prototyping. Generate sections individually with EXACT copy pasted in. Never use Stitch output directly — extract layout ideas, rebuild with skill Phases 4-6. See `references/tool-decision-matrix.md` for setup + prompting rules. | Build manually (often better — more control) |
| **21st.dev** | `python3 scripts/twenty_first.py` | Specific pre-built component | Build from scratch |
| **uipro-cli** | `uipro init --ai claude` | Industry-specific design tokens | references/design-system-generator.md |
| **Antigravity** | RECOMMEND to user | Full app scaffold | N/A — external IDE |
| **Web Designer** | RECOMMEND to user | HTML5 ads/banners | N/A — external GUI |
| **Marketing Skills** | `Skill("copywriting")` etc. | Phase 3 (Structure) | references/conversion-framework.md |

**CRITICAL:** This skill produces genius output with ZERO external tools. Stitch/21st.dev/uipro-cli are enhancements only. The skill works perfectly with only GSAP CDN + its reference files.

---

## 9. Marketing Skill Delegation Map

### Phase 3 (Structure) — ALWAYS invoke:

```
Skill("copywriting")           -> Headlines, body copy, CTAs
Skill("page-cro")              -> Conversion optimization
Skill("marketing-psychology")  -> Cognitive biases, persuasion triggers
```

### Phase 3 (specific page types):

```
Skill("pricing-strategy")      -> Pricing page design
Skill("form-cro")              -> Form optimization
Skill("popup-cro")             -> Exit intent, lead capture
Skill("signup-flow-cro")       -> Registration optimization
```

### Copywriting delegation adapts by style:

- **Style 1:** `Skill("copywriting")` + `Skill("page-cro")` + `Skill("marketing-psychology")` — full Hormozi stack
- **Style 2:** `Skill("copywriting")` with brand-voice guidance — minimal, aspirational
- **Style 3:** `Skill("copywriting")` with technical depth — storytelling, credibility
- **Style 4:** `Skill("copywriting")` with community framing — social proof, belonging

All marketing skills check for `~/.agents/product-marketing-context.md` — invoke `Skill("product-marketing-context")` first if it does not exist.

---

## 10. CDN Links (Include in Every Project)

```html
<!-- Lenis Smooth Scroll -->
<script src="https://unpkg.com/lenis@1/dist/lenis.min.js" defer></script>

<!-- GSAP + ScrollTrigger -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>

<!-- BarbaJS (multi-page only) -->
<script src="https://unpkg.com/@barba/core" defer></script>

<!-- SplitType (text animations, optional) -->
<script src="https://unpkg.com/split-type" defer></script>
```

All scripts use `defer` and go at the end of `<body>`. Never in `<head>`. Never render-blocking.

---

## 11. Reference Designs (Inspiration, NOT Imitation)

Study these for technique and ambition:

- **Linear.app** — Dark theme, bento grids, animated borders, gradient text
- **Vercel.com** — Geist font, minimal dark, geometric precision, subtle motion
- **Raycast.com** — Bold accent colors, noisy textures, abstract gradients
- **Stripe.com** — Animated gradient meshes, editorial precision, color confidence
- **Framer.com** — Fluid animations, scroll-driven design, playful interactions
- **osmo.supply** — Cutting-edge technique showcase, 170+ components

---

## 12. Execution Contract

When this skill activates:

1. **Read the brief.** Understand before building.
2. **Follow all 6 phases.** Load reference files at each phase.
3. **Select conversion style deliberately.** Hormozi is default, not automatic.
4. **Build with zero inline CSS.** No exceptions. Ever.
5. **Animate with purpose.** Every GSAP call has a reason.
6. **Run the 24-point gate.** Fix failures. Do not deliver until clean.
7. **The output must be distinctive.** If it smells like AI-generated template work, it is not done.

The standard is not "good enough." The standard is "someone screenshots this and shares it."
