---
name: beautiful-converting-frontend-design
description: Create distinctive, conversion-optimized frontend interfaces with context-matched visual identity, strong typography/color, and situational motion. Uses Hormozi conversion architecture, premium craft details, GSAP/Lenis/ScrollTrigger only when appropriate, and a mandatory quality gate that prevents generic or broken output.
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Skill", "Agent", "WebSearch", "WebFetch"]
---

# Beautiful Converting Frontend Design

This skill produces premium, conversion-optimized frontend interfaces. Every output chooses a context-matched visual identity, applies Hormozi clarity where conversion matters, and uses motion/media only when it improves comprehension, trust, or desire. A mandatory quality gate prevents generic, cheap-looking, or broken output from ever reaching the user.

---

## 1. Design DNA — Universal Principles

These are non-negotiable. Every decision filters through them.

### Principle 1: Clarity Creates Beauty

The first job is to make the page instantly understandable. Beauty is hierarchy, confidence, and separation before it is decoration.

**Rules:**
- Above the fold, the user must understand: what this is, why it matters, and what to do next.
- Every section needs one dominant idea. If two things compete, choose the one that drives the user's decision.
- The primary action must be the clearest object in the viewport, not merely another styled button.
- A beautiful page with unclear intent is a failed page.

### Principle 1b: Premium By Default, Never By Template

Every default elevates, but no default becomes the house look. Theme, type, color, motion, texture, borders, and glow adapt to the project. Quality is non-negotiable regardless of palette.

Premium can be dark, light, warm, stark, playful, editorial, utilitarian, brutalist, tactile, or cinematic. It cannot be copied token values, generic card grids, random gradients, or "dark glass with purple/cyan" unless that is the correct brand choice.

### Principle 1c: Typography Is The Voice

Good typography makes the brand feel inevitable. It is not enough to avoid bad fonts.

**Rules:**
- Select type from the product context: audience, industry, price point, reading density, language support, and brand maturity.
- Use the upstream UI/UX font-pair database as candidate input, not as an automatic answer.
- Prefer premium/licensed-quality type when available. There is no reason for a premium surface to use a cheap novelty font.
- Choose at most two families for normal web pages: one display/heading voice and one readable body/UI voice. Single-family systems are allowed for Apple-like, product-led, dense app, or existing design-system surfaces.
- For clean premium technology/product typography, think Apple-like: neutral, flexible, optical-size-aware sans, with a refined serif only when the content needs editorial warmth. Use SF Pro / New York only when licensed/appropriate; otherwise use clean premium equivalents.
- For luxury/fashion typography, think Louis Vuitton-style restraint: geometric wordmark energy, high confidence, no shouting. Futura/Avenir/Neue Haas/Helvetica Now-style grotesks, refined Didot/Bodoni/Cormorant/Canela-style serifs, and careful spacing usually beat decorative fonts.
- Avoid video-game, sci-fi, chunky, novelty, comic, or overly rounded fonts unless the product is actually a game, toy, youth entertainment, or explicit playful brand.
- A distinctive display font is valuable only if it improves recognition and still wraps cleanly on mobile.
- Inter/Roboto/Arial/system fonts are not allowed as lazy defaults. They are allowed only when inherited from an existing design system, required for native platform fidelity, or clearly the best readability choice for dense operational UI.
- Before coding, record why the chosen heading/body pair fits this specific surface.

### Principle 1d: Color Is A Decision System

Color must carry hierarchy, mood, and action. It is not a gradient picker.

**Rules:**
- Start from brand assets when available. If not, search the upstream UI/UX color palettes for 2-3 context-matched candidates, then choose one deliberately.
- Every palette needs roles: background, surface, text, muted text, primary action, secondary accent, border/outline, success, warning/destructive, focus ring.
- Use strong contrast and figure-ground separation. The primary CTA, important proof, and active states must pop clearly from the surrounding surface.
- Do not spread accent colors evenly. One accent leads; others support state, warmth, or emphasis.
- Violet/cyan, blue/purple, gold/black, beige/brown, and dark glass are candidates, not defaults. Reusing them without brand reason is a failure.
- Before coding, record why this palette fits the audience, offer, and surface type.

### Principle 1e: Material Craft Is Visible

Cheap pages feel flat because surfaces do not have edges, texture, light, or tactility. Premium pages have fine-detail separation.

**Rules:**
- Sections need visible separation: contrast bands, thick borders, outline strokes, inset lines, material changes, or clear spatial breaks.
- Cards, panels, media frames, and pricing blocks should have intentional borders/outlines. On expressive surfaces, borders can be thicker and more characterful; on operational surfaces, use quieter but still visible separation.
- Use texture deliberately: grain, paper, brushed metal, glass noise, halftone, fabric, or subtle canvas texture when it fits the brand.
- Glow is a hierarchy tool. Use it for primary actions, active states, hero objects, key stats, or premium display text. Missing glow on a luminous/dark premium surface often makes it feel unfinished.
- Text sheen/gradient/spotlight treatments are for display-sized focal text and major numbers, not body copy, labels, or buttons.
- Fine details must support readability. Glow, texture, and sheen fail if they lower contrast or make text fuzzy.

### Principle 2: Conversion-Aware

Every visual decision has a conversion implication. Design IS the conversion mechanism, not decoration applied after. Sometimes that means motion and counters; sometimes it means a quiet form, a clearer price table, stronger proof hierarchy, or a sharper CTA.

### Principle 3: Motion-Rich, But Context-Aware

Unconsidered static pages feel unfinished on expressive surfaces, but indiscriminate motion is worse than none. Select a motion mode before building:

- **Mode 0 — Minimal UI motion:** docs, utilities, dense dashboards. Hover/focus/state transitions only.
- **Mode 1 — Editorial choreography:** SaaS marketing, product pages, most brand sites. Layered reveals, strong section rhythm, restrained parallax.
- **Mode 2 — Immersive depth:** campaigns, portfolios, launches. Multi-plane parallax, 3D transforms, richer timelines.
- **Mode 3 — Cinematic environment:** only when the page itself is the product or campaign. Scene-based 3D/WebGL is allowed if perf budget survives.

Use the lowest motion mode that makes the surface feel complete. Lenis, snap, ScrollTrigger, BarbaJS, SplitType, WebGL, and custom cursor-reactive effects are all situational choices. Every animation has PURPOSE: reveal, guide, confirm, or delight. No gratuitous motion.

### Principle 4: Distinctive

If you cannot tell the brand from the design, it is too generic. Font, palette, spacing, borders, material, imagery, and layout must feel chosen for this project. Expressive pages need at least one memorable visual decision. Operational surfaces need recognizable craft without spectacle. If it could belong to any brand, it belongs to none.

### Principle 5: Restrained

Fewer elements, more impact. White space signals premium. One focal point per section. 60-30-10 color ratio. Glass on max 5 elements. Generous section padding (`clamp(3rem, 8vh, 6rem)` minimum between sections). Maximalism and minimalism both work — but every element must earn its place.

**Mobile layout rule:** Default to single-column on ALL devices ≤768px. Multi-column grids on mobile are ONLY permitted for inherently narrow content (icon rows <48px, avatar stacks, tag clouds). Feature cards, testimonials, stats, and content blocks: 1 column on mobile, expand to 2-3 on tablet+. "Responsive grid" ALWAYS means collapse to 1 column first, then expand upward. If a card grid exists on mobile, each column must be ≥280px wide (minimum for touch targets + readable text).

### Principle 6: ZERO INLINE CSS — HARD RULE

Never use `style=` attributes in HTML. Never use `element.style.xxx` in JS (except CSS custom properties via `setProperty`). Everything goes in CSS files with classes and variables.

Allowed exception: a small critical CSS `<style>` block is permitted when it materially improves first paint. This is not "inline CSS" for this rule. It must contain tokenized, reusable selectors only, never per-element style attributes.

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

### Principle 8: Readability First — Decoration Never Defeats Text

This is foundational. No animation, particle effect, background visual, or decorative element may compromise text readability. Ever.

**Rules:**
- **Text zones get opaque or near-opaque backgrounds.** If a section has body text, stats, cards, or any content meant to be read, the background behind it must provide sufficient contrast. Semi-transparent scrims (rgba with 0.85-0.95 opacity) let subtle depth peek through while keeping text crisp.
- **Decoration-only zones can be transparent.** Hero sections where the animation IS the visual, or CTA sections with only large bold headings, can let effects show through. But even here, heading text must have enough size/weight to remain readable.
- **Readability is LOCAL contrast, not a dark page.** What matters is the contrast between text and the surface DIRECTLY behind it — it must be near-opposite, like black-on-white or white-on-black. The overall background can be bright, colorful, busy, or even white; readability comes from each text element's *immediate* backing, not from dimming the whole page. So you do NOT fix a washed-out screen by darkening the entire background — you give each text element its own high-contrast plate: a dark (or light) scrim/section behind it, or a deep shadow around the text, so it stays legible no matter what's further back. **Bright text on a bright field** (white-on-neon, light-on-light, a label floating over a vivid gradient) is the failure. Fix it locally: darken the backing right behind the text (a deep shadow/plate/section, even a small one), or flip the text to a dark color — never rely on a globally dark background to carry it. Rule of thumb: every heading, number, label, and badge should still pass if you imagine the background behind it swapped for its brightest possible state.
- **Never match decoration color to text color.** Teal particles behind teal text = unreadable. Red particles behind red text = unreadable. If the animation color matches the text color in a section, either change the animation color, add a scrim, or make the section opaque.
- **Small text (< 18px) gets full protection.** Body copy, descriptions, labels, and footer links must NEVER compete with background animations. Only large headings (32px+, bold weight) can coexist with active backgrounds.
- **Test with screenshots, not assumptions.** Always capture and visually inspect the actual rendered page. Text that looks fine in code can be invisible when particles, gradients, or effects overlap in the browser.
- **Never use low-contrast text-on-background combinations.** Dark text on dark backgrounds = invisible. White text on white/light backgrounds = invisible. Pink/magenta/teal as body text on dark backgrounds = unreadable. All body text must be high-contrast (#FAFAFA on dark, #09090B on light). Accent colors (violet, cyan, teal) are for borders, glows, labels, and decorative elements — NEVER for body copy or stat numbers that must be read at a glance.

**Implementation pattern for fixed canvas backgrounds:**
```css
/* Sections where the effect IS the content — fully transparent */
.effect-active .s-hero,
.effect-active .s-cta {
  background: transparent !important;
}

/* Content sections — near-opaque scrim preserves readability */
.effect-active .s-content,
.effect-active .s-features,
.effect-active .s-testimonials {
  background: rgba(8, 8, 12, 0.92) !important;
}
```

### Principle 8b: WCAG-Compliant By Default

Accessibility is not optional polish. The default target is **WCAG 2.2 AA** unless the brief explicitly requires stricter standards.

**Rules:**
- Meet contrast requirements for text, controls, focus states, and meaningful graphics.
- All interactive controls must be keyboard reachable, visibly focusable, and have semantic names.
- Motion must respect `prefers-reduced-motion` and must not be required to understand the UI.
- Hover-only affordances are incomplete. Critical information and actions must also work on keyboard and touch.
- Use semantic landmarks, real headings, real buttons, real links, proper labels, and alt text for meaningful images.
- Touch targets must be comfortably tappable; small decorative hit areas are not acceptable for primary actions.
- Accessibility applies to premium aesthetics too. “Luxury,” “minimal,” and “experimental” do not excuse unreadable contrast, missing labels, or hidden focus.

### Principle 9: Build for Real Content, Not Placeholder Content

The first build must survive realistic content. Do not design around the shortest or prettiest string.

**Rules:**
- **Use longest-content thinking during implementation.** Before calling a layout "done," mentally test shortest, typical, and longest realistic states for headings, card descriptions, badges, table cells, and narrative blocks.
- **Default to readable full copy.** Do NOT line-clamp, ellipsize, or hide meaningful user-visible body text unless the brief explicitly asks for preview cards or teaser excerpts.
- **Prefer intrinsic height over forced height matching.** If sibling cards contain materially different amounts of content, let them size to content unless the empty space still looks intentional and premium.
- **Do not ship stretched dead space.** A tall card with one small block of content and a huge empty lower half is a broken layout, not "breathing room."
- **App shells must balance first.** In dashboards, sidebars, split panes, and admin layouts, validate left/right occupancy and centering of the primary content region before styling internal cards.
- **Backend-driven UI still counts as frontend.** If server-rendered/backend data changes can affect the page shape, spacing, or content length, build defensively as if the UI can receive longer real data tomorrow.

### Principle 9b: Layout Safety Is Table Stakes

Beautiful is irrelevant if the layout breaks. These are hard failures, not polish requests:

- Text must stay inside its container on desktop and mobile.
- Buttons, labels, badges, cards, charts, and nav items must not overflow their boxes.
- Boxes/components must not overlap each other unless overlap is the explicit design choice and readability is still protected.
- Long words, long labels, long prices, long plan names, and long headings must not burst through borders.
- Fixed-format UI elements need stable dimensions: grids, boards, toolbars, icon buttons, counters, tiles, and cards should not resize unpredictably on hover, load, or content changes.
- Mobile is not a scaled desktop. Verify at least `360x668` and a normal desktop viewport before calling a layout complete.

### Principle 10: Layer With Intent, Not Effect Spam

Modern premium sites feel dimensional because they are composed in planes, not because they stack random effects.

**Rules:**
- Build with a **4-plane model** when depth is desired: atmosphere/background, structural midground, content plane, accent/foreground plane.
- Movement intensity must decrease as semantic importance increases. Background can drift; readable content should remain stable.
- One dominant wow system per page is enough. If 3D, particles, glitch, split-text, parallax, and cursor tricks all compete, the page is already wrong.
- Treat tactile / warm / human-made aesthetics as equally modern to glossy sci-fi. Pick the branch that fits the brand.

### Principle 10b: Gen Z Native Design (2025-2026)

When the target audience is Gen Z (born 1997-2012), apply these research-backed preferences:

- **Dark mode by default.** Base: `#09090B` (near-black, never pure `#000`). Elevation = lightness steps (`#18181B`, `#27272A`, `#3F3F46`).
- **40% of Gen Z feel all apps look the same** — standing out visually is critical. Generic = death.
- **"Tactile maximalism":** Layered, textured, bold but usable. Grain/noise textures signal authenticity vs AI-generated smoothness.
- **Grain overlay:** SVG noise at 3-5% opacity, `mix-blend-mode: overlay`, `pointer-events: none`. Analog warmth signal.
- **Condensed bold typography** for headings (Space Grotesk, Bricolage Grotesque, not smooth sans-serif). Body: Geist or Satoshi. Weights: 700-900 headings, 400-500 body.
- **Mobile-first always.** Thumb-zone optimized. Design for 375x812 first, expand upward.
- **Personality in microcopy** and error states. Generic copy = "Facebook energy" = cringe.
- **Holographic/iridescent accents** for premium moments: `@property --holo-angle` with `conic-gradient` rotation.
- **Violet-to-Cyan** (`#8B5CF6` -> `#06B6D4`) is only a candidate signal for music/creative apps, not a default. Use it only when the brand/audience fit is explicit, and do not reuse it across unrelated builds.
- **iMessage-style glass pills** for chat interfaces: violet (user), cyan (AI/system), pill border-radius with glass background.
- **Avoid:** Corporate polish, forced slang, stock photos, "Facebook energy", flat 2D layouts, smooth gradients without texture.

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
  Audit the full project first: existing pages, product flows, assets, copy, competitors/references if relevant, and current visual system
  Audience first: who they are, what they know, what they fear, what they want, where they arrive from, and what device/context they use
  Map the conversion/user flow: entry point → first impression → proof path → objection handling → action → follow-up state
  Define the design story: what belief the visual experience should create, and how each section advances that story
  Challenge the request: is this the right surface, structure, audience framing, offer, motion level, and visual style?
  State the better marketing/design path when the user's literal ask would weaken conversion, trust, or usability
  Read brief → identify brand maturity → select conversion style → commit to design direction
  If a named brand/product/current release is involved, verify facts and gather assets before designing
  Read references/tool-decision-matrix.md → choose surface type, motion mode, scroll behavior, and rendering stack
  Read references/premium-frontend-quality-spec.md → lock hard rules, house rules, preset family, and gate bar
  Read references/visual-acceptance-review.md → define visual acceptance contract + review rubric
  Search upstream/ui-ux-pro-max color/font/style data for candidates that match the context

Phase 2: DESIGN SYSTEM
  Read references/design-system-generator.md → generate tokens (fonts, colors, spacing, radii, shadows)
  Create/update DESIGN.md or project design context when the build is non-trivial or multi-page
  Record chosen typography, palette, material craft, border/outline, glow, and texture rationale

Phase 3: STRUCTURE
  Select conversion style → Read references/conversion-framework.md
  Invoke: Skill("copywriting") + Skill("page-cro") + Skill("marketing-psychology")
  Build complete page architecture with copy

Phase 4: BUILD
  Read references/css-architecture.md + references/performance.md + references/visual-styles.md + references/responsive-sections.md + references/premium-buttons.md (real 3D tactile buttons for CTAs/key controls)
  Select visual style(s) matching the brand (neumorphism, brutalist, luxury dark, etc.)
  Apply Phase 4 construction invariants before styling polish
  Implement HTML + CSS with no `style=` attributes; use classes, variables, and tokenized selectors

Phase 5: ANIMATE
  Read references/animation-patterns.md + references/osmo-techniques.md + references/performance.md
  Choose motion escalation level + scroll behavior intentionally
  Add CSS/GSAP/Lenis/ScrollTrigger only when the selected surface type justifies them

Phase 6: SELF-REVIEW
  Read references/premium-frontend-quality-spec.md → validate against hard rules and house-style doctrine
  Read references/visual-acceptance-review.md → verify screenshots, semantic review, and state coverage
  Read references/skill-regression-spec.md when validating or upgrading the skill itself
  Use the cheap-first tiered validation path; do not run full regressions unless the change risk justifies it
  Apply the mandatory escalation triggers from the regression spec; do not treat high-risk edits as Tier 0
  Run the mandatory quality gate → fix ALL failures → deliver only when clean
```

Each phase MUST load its reference files before proceeding.

### Challenge-First Design Protocol

Before designing visuals, challenge the brief constructively. The goal is not obedience; the goal is the highest-converting, clearest, most premium answer for the audience.

Ask internally:
- What does this project already have: product screens, data, assets, language, customer proof, brand cues, interaction patterns?
- Who is the real audience, and what do they believe before the page loads?
- What is their buying/use context: phone, desktop, urgency, sophistication, skepticism, budget, risk?
- What flow are they in: cold visitor, warm lead, returning user, internal operator, investor, buyer, creator, developer?
- What story should the design tell: authority, speed, craft, safety, exclusivity, delight, proof, transformation, control, status, or relief?
- What must they understand first, second, and third before the CTA makes sense?
- What proof, objection handling, demo, comparison, or artifact would move them faster than another decorative section?
- Is the requested format wrong: should this be an app workflow, calculator, product demo, deck, comparison page, form, or shorter landing page instead?
- Would the requested motion/style reduce trust, readability, performance, or seriousness for this audience?

If the better answer differs from the literal request, say so briefly, then build the stronger version unless the user explicitly rejects it.

### Originality Protocol

Originality comes from the project, not from copying trend sites.

- Audit the product's actual mechanics, audience language, assets, workflow, proof, constraints, and emotional promise.
- Choose one design story that only this project can credibly tell.
- Use references for technique only. Do not reproduce another site's layout, palette, hero composition, motion pattern, or brand voice unless the user explicitly asks for a clone.
- The memorable visual idea should come from the product metaphor, customer transformation, data shape, workflow, or artifact, not a generic "cool" effect.
- If the project lacks assets or proof, create an honest visual metaphor or ask/search for real material. Do not fill the gap with stock AI-template sections.

### Skill-Native Acceptance Gate

This skill must define what "good" means before it builds, then judge the rendered result against that definition.

- Before implementation, write a short visual acceptance contract: surface type, audience, conversion action, motion mode, rendering stack, required viewports, required states, expected visible objects, forbidden failures, and quality dimensions.
- After implementation, collect rendered evidence against that contract. Browser screenshots are preferred for browser-visible work; code inspection alone is not enough for visual claims.
- The review must be semantic, not just mechanical: explain what is visible, what changed on interaction/scroll, whether forbidden failures are absent, and what still needs improvement.
- Use agents for parallel visual audits, screenshot review, and disjoint implementation slices when that speeds the work. Assign disjoint files/modules and integrate results in the parent session.
- External examples, current UI patterns, library choices, or source-data claims used to justify implementation should be recorded in the working notes or design artifact so the output is auditable later.

See `references/visual-acceptance-review.md`.

### Context And Asset Protocol

Do not design from vibes when the work is branded, product-specific, or current.

- If the brief names a product, company, version, launch, or current UI, verify facts from current sources before assuming.
- For branded work, logo, product shots, and UI screenshots are first-class assets. Colors and fonts are secondary.
- If real assets are unavailable, use honest labeled placeholders and ask or search; do not fake product screenshots, logos, testimonials, customer logos, or usage stats.
- For vague briefs, choose the real design problem first: conversion page, app workflow, brand artifact, pitch narrative, product demo, or prototype. If the likely better path is not a website/page, say so before building.
- For multi-page work, freeze nav/footer/shared components in `DESIGN.md` or `.design/SITE.md` so later pages do not redesign the system.
- Treat upstream UI/UX palettes, font pairings, and style profiles as a candidate library. Do not copy the first matching palette blindly; choose the one that best fits the product, audience, density, and emotional job.
- If the user already has a design system, extend it instead of replacing it with this skill's preferred look.

### Phase 4 Construction Invariants (MANDATORY)

These are build-time rules, not review-time suggestions.

1. **No truncation by default.** User-visible copy stays fully readable unless the brief explicitly calls for a preview/excerpt pattern.
2. **No equal-height theater.** Do not force equal-height cards when one card has substantially longer content and the result creates dead space.
3. **Center the shell before styling internals.** For app/dashboard layouts, verify the main content region is centered and occupancy is balanced before polishing card internals.
4. **Use content-driven sizing first.** Start with intrinsic layout (`auto`, `min-content`, `fit-content`, natural flow). Only stretch/fill after proving the stretched state still looks intentional.
5. **Design for longest realistic state.** Build against at least one long heading, long paragraph, long badge/label, and populated-card scenario.
6. **Whitespace must earn its keep.** Premium spacing is not random emptiness. Large empty zones must reinforce hierarchy or focus; otherwise they are defects.
7. **If a page has shell chrome, check the whole frame.** Sidebar, header, content column, and gutters are one composition. Do not tune cards in isolation.
8. **Loading skeletons must mirror the page shell.** If the page uses wrapper classes that CSS `:has()` selectors depend on (e.g., sidebar-hide rules), the `loading.tsx` / Suspense fallback MUST include those same outermost classes. Otherwise the loading state shows a completely different layout (sidebar visible, wrong theme) before the real page replaces it — a guaranteed FOUC.
9. **No `opacity: 0` in entrance animation `from` keyframes.** Entrance animations with `animation-fill-mode: both` and `from { opacity: 0 }` hide content for the entire delay duration. Content must render at full opacity immediately; use transform-only animations for entrance polish.
10. **Tooltips: use `title` attribute or JS components, never CSS `::after`.** CSS `content: attr(data-*)` pseudo-element tooltips leak as visible text during async CSS loading. Native `title` is immune to CSS load order.

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

### Style 5: Presentation/Pitch Deck — Premium Storytelling

**Use for:** Business plans, investor pitches, partnership proposals, methodology breakdowns, timeline narratives, any page primarily viewed on mobile as a "scroll-through presentation."

- One decision per section. Low information density, not empty information. Every section must carry one evidence unit: metric, example, diagram, proof point, concrete ask, or decision implication.
- Single-column ONLY — even on desktop. Max content width 600px centered.
- Sections are tall (`min-height: 80svh` for key impact sections, `auto` for content-heavy).
- Text is large and scannable. Hierarchy is visual, not typographic density.
- Animated SVG icons replace all emoji/icon fonts. Each icon has CSS `@keyframes`.
- If motion is used, it is diverse: slide-left, slide-right, scale-rotate, clip-path reveal, pop. Never just fade-up.
- Counter animations are useful for headline metrics when the number is a focal proof point. Static numbers are better for dense tables or repeated stats.
- Self-drawing SVG paths are useful for timelines/process flows when the path clarifies sequence.
- Canvas particle/network backgrounds are only for tech/AI topics where atmosphere helps. Avoid them when readability, seriousness, or mobile performance would suffer.
- **No card grids. No feature grids. Each concept gets its own vertical block.**
- **Page flow** (variable sections, one idea each):
  1. Hero (headline + tagline, full viewport, particles visible)
  2. Summary (3-4 tight points, not paragraphs)
  3. Core concept (process flow with animated drawing path)
  4. Features (vertical list, one per block, alternating slide directions)
  5. [Repeat for each key section]
  6. Numbers/costs (counter-animated, large type)
  7. Timeline (vertical with animated connector)
  8. Closing statement + next steps

**PDF / rendered investor-deck builds** — when the deliverable is a downloadable **PDF deck that must open identically in any viewer** (Edge, Acrobat, Preview), not a scroll-through web page: the clarity/craft above still applies, but the HTML→Chrome→**lossless-image-PDF** pipeline (Edge renders Chrome's vector print output as blank white otherwise), real-screenshot cropping (avoid nested double-frames), the investor-grade diagram patterns (supply/demand disproportionality, directional flywheels, two-sides-one-core, sourced stats), the **no-overlap + no-clip** discipline, the brighter-accent-on-dark palette with stronger glow, and the render-and-READ verification gate are all codified in **`references/pdf-deck-playbook.md` — read it before building any exported/PDF deck.**

### How the Skill Decides

- Phase 1 identifies project's brand maturity, audience, and goal
- Startup / SMB / unknown → **Style 1 (Hormozi)** by default
- Established brand with existing identity → Style 2 or 3
- Platform / community product → Style 4
- Business plan / investor pitch / partnership proposal / "show on phone" → **Style 5 (Presentation)**
- **Hormozi CLARITY principles (specificity, reasons, active voice) apply to ALL styles**

### Situational Technique Router

Use this before choosing effects. The question is not "can this look cool?" The question is "does this technique make the surface clearer, more trusted, or more desirable?"

| Technique | Use When | Avoid When |
|---|---|---|
| Scroll snap | Basic low-content landing page, deck-like presentation, simple product showcase where each section is a self-contained slide | dashboards, docs, blogs, pricing pages, forms, SEO pages, long/variable sections, any section taller than viewport |
| Lenis smooth scroll | Continuous-scroll editorial/marketing page where smoother momentum improves perceived polish | apps, admin, dashboards, snap pages, forms, pages with native scroll expectations |
| GSAP ScrollTrigger | Expressive reveals, product storytelling, counters, diagram drawing, section choreography | dense operational UI, simple static content, anything where CSS transitions are enough |
| GSAP pin/scrub | Narrative product explanation or visual walkthrough where scroll position controls meaning | ordinary landing pages, mobile-heavy pages, forms, snap pages, long SEO content |
| SplitType/kinetic text | One signature display moment where typography is the hero | every heading, body copy, accessibility-sensitive text, dense app UI |
| WebGL/Three/R3F | The 3D scene is the product/demo/campaign experience and performance budget is credible | decorative backgrounds behind readable text, dashboards, simple card depth, mobile-first utility pages |
| Canvas particles | Atmosphere, network/AI metaphor, lightweight ambient backdrop behind protected text | serious trust pages, dense content, low-power mobile, text without opaque backing |
| Thick borders/outlines | Expressive sections, pricing cards, hero/product frames, brutalist/editorial/tactile systems | delicate luxury surfaces where hairlines are the brand, dense tables where thick borders add noise |
| Glow/sheen | Dark/luminous premium surfaces, primary CTAs, active states, hero objects, key display text | light utilitarian UI, body copy, labels, disabled states, anything already high-noise |
| Card grids | Comparable repeated items with equal priority | narrative pages, presentations, premium brand stories, mobile sections with wide content |

### Motion Mode Routing (MANDATORY)

Choose one before implementing animation:

| Site Type | Default Motion Mode | Escalate Only If | Usually Avoid |
|---|---|---|---|
| App/dashboard/admin | Mode 0 | flagship hero, launch moment, empty state illustration | scroll theater, heavy parallax, WebGL as background to dense text |
| SaaS/product marketing | Mode 1 | premium launch, strong visual metaphor, short page | scroll hijack, custom cursor, loader intro |
| Editorial/storytelling | Mode 1 or 2 | the narrative benefits from depth and pacing | repetitive fade-up on every section |
| Portfolio/campaign | Mode 2 | the experience itself is part of the pitch | conversion-hostile friction, hard-to-skip intros |
| Experimental microsite | Mode 3 | performance stays credible and content volume is low | using the same treatment on ordinary business pages |

### Wow Moment Catalog (choose ONE primary system, optional one secondary)

- Particle-reactive hero
- Kinetic typography corridor
- Self-drawing SVG story path
- Layered zoom reveal
- Product orbit / exploded-view scene
- Elastic bento grid
- Shader-like image dissolve
- Narrative timeline with scrubbed focus shifts
- Tactile collage / warm textured reveal

Do not pile on three unrelated wow systems just to signal effort.

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

## 6. Anti-Patterns — Things to NEVER Do

| # | Anti-Pattern | Why It Fails | Do Instead |
|---|-------------|-------------|------------|
| 1 | Defaulting to Inter/Roboto/Arial/system fonts | Lazy typography makes output feel generated | Use a context-matched premium font pair; use system fonts only for inherited/native/dense UI reasons |
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
| 20 | Emoji icons (🚀💡✅ as UI elements) | Generic, template-like, low-effort signal. Screams AI-generated. | Inline SVG icons (Heroicons, Lucide, or custom animated SVGs with CSS `@keyframes`). Emoji in copy is fine — emoji as functional icons = FAIL. |
| 21 | Multi-column card grids on mobile | Cramped, unreadable, template look on phones | Single column ≤768px. Cards/features stack vertically. Expand to 2-3 cols only on tablet+. See Principle 5 mobile rule. |
| 22 | Same animation on every section | Monotonous, feels auto-generated | Minimum 3 distinct animation types per page (e.g. slide-left, scale-rotate, clip-path reveal). Fade-up alone is not variety. |
| 23 | Scroll hijacking on ordinary pages | Removes control, widely disliked, hurts usability | Native scroll or restrained Lenis on continuous-scroll pages only |
| 24 | Fake custom cursor replacement | Usually laggy, gimmicky, hurts precision | Keep native cursor. Ambient cursor-reactive glows only, desktop pointer-fine only |
| 25 | Giant loader intros / forced splash screens | Adds friction before value | Enter fast; if needed use sub-400ms polish, never a cinematic gate |
| 26 | 3D/WebGL without performance budget | Impresses briefly, then stutters | Use CSS 3D first, then Spline/Rive/Three only if justified |
| 27 | Spectacle on the wrong page type | Destroys trust and clarity | Match motion mode to site type before styling |
| 28 | Entrance-only motion with dead states | Feels theatrical but not interactive | Design hover, focus, active, success, loading, and error states too |
| 29 | `animation-fill-mode: both` with `opacity: 0` in entrance keyframes | Backwards fill applies `from` state BEFORE animation delay — hides ALL content for the delay duration, causing FOUC (flash of blank/dark screen on first load) | Use transform-only entrance animations (`scale`, `translateY`, `rotateX`) without opacity. Content renders instantly, transforms provide polish. |
| 30 | CSS `::after` with `content: attr(data-*)` for tooltips | During async CSS loading (Next.js dev HMR, chunked CSS), the pseudo-element content renders as visible text BEFORE `opacity: 0` is applied. Text leaks into layout. | Use native HTML `title` attribute (browser-handled, immune to CSS load order) or JS-controlled tooltip components. |
| 31 | Loading skeleton missing page shell classes | If `loading.tsx` (or equivalent Suspense fallback) lacks the same wrapper classes as the page (e.g., `.aurora-shell`), CSS `:has()` selectors won't fire during loading phase — sidebar flashes, layout shifts, wrong styles shown before real content loads | Loading skeletons MUST mirror the page's outermost shell class structure. If the page renders `.aurora-shell .grunge-shell`, the skeleton must too. |
| 32 | Stale Next.js build cache hiding env-var changes | `NEXT_PUBLIC_*` env vars are statically substituted at compile time. If `.next/build` mtime predates the env-var change, the shipped bundle still has the old value baked in — every architectural fix is invisible until the cache is cleared. | Cache cycle protocol: stop dev process → `rm -rf .next/` → restart `npm run dev`. Confirm via module-init `console.info` that the new flag value reached the bundle. |
| 33 | UV-shift fragment shader as photographic backdrop with foreground 3D | UV-shift (akella "Fake 3D" Codrops 2019, Codrops "Reactive Depth" 2026) is a 2.5D image-space hack designed for STANDALONE hero animations. It cannot host depth-correct foreground 3D — z-fighting, wrong perspective, no 360° wrap. | Use drei `<Environment background files={equirectJpg}>` equirectangular skybox. Production-proven across Spotify Wrapped, Active Theory, Lusion. See `references/image-to-3d-environment-workflow.md`. |
| 34 | 2D dashboard substitute as mobile/low-tier "fallback" for a 3D experience | Substituting a different product on weaker hardware breaks the brand contract. Tier-down should preserve the experience, not replace it. | Tier-down via lower-resolution skybox asset (4K vs 8K), DPR clamp, and disable expensive postFX. NEVER substitute 2D for 3D. WebGL-genuinely-absent users see a brand-styled "browser doesn't support 3D" notice, NOT the 2D dashboard. |
| 35 | 2-state WebGL probe (`useState<boolean>(false)`) | The 2-state form forces `!canRender3D` true on every first render, flashing the WebGL-missing UI on every supported device before the post-hydration `useEffect` can resolve. | Use 3-state sentinel: `useState<boolean \| null>(null)`. null = probing (render layout-stable placeholder, NO error UI), true = ready (Canvas mounts), false = WebGL absent (error UI renders). |
| 36 | Viewport-scoped (rather than UA-scoped) skybox URL selection | Viewport-scoped detection requires `window.matchMedia` which is client-only. SSR renders the wrong URL → browser preloader fetches it → useEffect flips state → drei `useTexture` fetches the other URL → mobile downloads BOTH assets. | UA-scoped contract: detect mobile/tablet server-side via `userAgent({ headers })` from `next/server`, thread `isMobile` as a prop, render the correct URL on FIRST paint. Document the desktop-UA-on-mobile-viewport edge case explicitly. |
| 37 | Copying the token template unchanged | The skill creates its own recognizable cheap house style | Pick context-specific type, color, borders, texture, glow, and material treatment before coding |
| 38 | Video-game or novelty fonts on serious products | Makes premium work feel cheap, childish, or off-market | Use Apple-clean, LV/Futura-like, editorial serif, or premium grotesk systems unless playful/game context is explicit |
| 39 | Pretty palette with no semantic roles | Colors look decorative but do not guide action or state | Assign roles: background, surface, text, CTA, accent, border, focus, success, warning, destructive |
| 40 | Thin invisible borders and weak section separation | Sections collapse together and the page feels unfinished | Use visible contrast bands, thicker outlines, inset borders, dividers, or material shifts |
| 41 | No glow/sheen on luminous premium surfaces | Dark premium work reads flat and underlit | Add controlled glow to primary CTA, hero object, active state, or display text; keep body text solid |
| 42 | Scroll snap because the page has sections | Snap becomes a gimmick and breaks variable content | Use snap only for low-content slide-like pages that fit every viewport |
| 43 | Flat lifeless buttons on a premium/expressive surface | The #1 cheap tell — a styled rectangle reads as a placeholder, not a control | Real 3D tactile button: visible rim/edge, hover lift + specular, fast press that collapses the rim, asymmetric timing. See `references/premium-buttons.md` |

---

## 6b. Framework CSS Loading Traps (Lessons Learned)

Hard-won rules from production Next.js/React projects. These bugs are invisible in code review and only manifest at runtime.

### Trap 1: Loading Skeletons Must Mirror Shell Classes

Next.js `loading.tsx` creates an automatic Suspense boundary. The skeleton renders BEFORE page content arrives. If the page relies on CSS `:has()` selectors that depend on specific wrapper classes (e.g., `:has(> .aurora-shell)` to hide a sidebar), the loading skeleton MUST include those same classes — otherwise the `:has()` rule doesn't fire during loading, and the old layout (sidebar visible, wrong styles) flashes before the real content replaces it.

**Rule:** Every `loading.tsx` must mirror the outermost shell class structure of its corresponding `page.tsx`. If the page renders `<div className="aurora-shell grunge-shell dark">`, the skeleton must too.

```tsx
// WRONG — sidebar flashes because :has(.aurora-shell) doesn't fire
export default function Loading() {
  return <div className="animate-pulse">Loading...</div>;
}

// RIGHT — matches page shell, CSS :has() rules fire immediately
export default function Loading() {
  return (
    <div className="aurora-shell grunge-shell dark">
      <main className="aurora-room">
        <div className="h-64 rounded-lg bg-zinc-900 animate-pulse" />
      </main>
    </div>
  );
}
```

### Trap 2: CSS `::after` Tooltips Leak During Async Loading

CSS `content: attr(data-tooltip)` creates a text pseudo-element. During async CSS loading (Next.js dev mode HMR, chunked CSS in production), the `::after` element's `opacity: 0` rule may not be applied yet — the tooltip text renders as visible, positioned content that leaks into the layout. Users see random tooltip text between UI elements.

**Rule:** Never use CSS `::after` with `content: attr()` for tooltips. Use native HTML `title` attribute (browser-handled, immune to CSS load order) or JavaScript-controlled tooltip components (Radix, Headless UI).

```html
<!-- WRONG — "Momentum = releases + streams..." leaks as visible text during CSS loading -->
<div data-tooltip="Momentum = releases + streams + engagement">

<!-- RIGHT — browser handles tooltip natively, zero CSS dependency -->
<div title="Momentum = releases + streams + engagement">
```

### Trap 3: Entrance Animations with `opacity: 0` Cause FOUC

`animation-fill-mode: both` applies the `from` state BEFORE the animation delay starts (backwards fill). If `from { opacity: 0; ... }` with delays of 0.1s-1s, ALL animated content is invisible for up to a second while the dark/empty background renders immediately. Users see a "flash of black" before content appears.

**Rule:** Never use `opacity: 0` in entrance `from` keyframes. Use transform-only animations for entrances. Content renders at full opacity instantly; transforms provide subtle motion polish.

```css
/* WRONG — content invisible for 0.8s delay (backwards fill) */
@keyframes enter {
  from { opacity: 0; transform: scale(0.85) rotateY(8deg); }
  to { opacity: 1; transform: scale(1) rotateY(0); }
}
.panel { animation: enter 0.7s ease 0.8s both; }

/* RIGHT — content visible immediately, transform adds polish */
@keyframes enter {
  from { transform: scale(0.92) rotateY(5deg); }
  to { transform: scale(1) rotateY(0); }
}
.panel { animation: enter 0.7s ease 0.3s both; }
```

### Trap 4: Verify in Dev Mode, Not Just Production Build

Next.js dev mode loads CSS asynchronously via HMR. This exposes FOUC, CSS load-order issues, and pseudo-element text leaks that are invisible in production builds (where CSS is bundled and loaded synchronously). Always test visual changes in dev mode — if it looks broken in dev, users on slow connections will see the same breakage in production.

---

## 6c. Three.js Integration Patterns (Lessons Learned)

> (Formerly 6b)

When adding Three.js for 3D particle effects, shader-based morphing, or camera choreography:

### CDN Version Selection
- **Three.js dropped UMD builds after v0.160.** Versions 0.161+ only ship ES module builds (`three.module.min.js`).
- If using global `THREE` variable (no bundler), pin to `three@0.160.0` on jsdelivr: `https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js`
- If using ES modules / import maps, use latest version with `three.module.min.js`
- **cdnjs uses `rXXX` versioning** (e.g., `r169`) but many versions 404. jsdelivr is more reliable for Three.js.
- Always add `onerror="window._threeLoadFailed=true"` on the script tag for graceful fallback.

### Canvas Placement — Two Approaches

**Approach 1: Two-Column Layout (PREFERRED for section-based pages)**
- Text in left column (55%), Three.js canvas in right column (45%)
- Canvas container is `position: sticky; top: 0; height: 100svh` — stays visible while text scrolls
- Animations are BESIDE text, never behind it — zero readability conflicts
- Per-section 3D objects morph/transition as user scrolls between sections
- Mobile: stacks vertically — animation above text at ~40vh height
```css
/* WHY: Two-column separates animation from text — no readability conflicts */
section { display: grid; grid-template-columns: 55% 45%; min-height: 100svh; }
.section-visual { position: sticky; top: 0; height: 100svh; }
@media (max-width: 768px) {
  section { grid-template-columns: 1fr; }
  .section-visual { position: relative; height: 40svh; }
}
```

**Approach 2: Fixed Canvas Behind DOM (fallback for continuous-scroll pages)**
- Three.js canvas is `position: fixed; inset: 0; z-index: 0; pointer-events: none !important`
- **CRITICAL: Opaque section backgrounds will cover the canvas.** Use selective transparency:
  - Decoration-only sections (hero, CTA): `background: transparent`
  - Content sections: `background: rgba(8, 8, 12, 0.92)` — near-opaque scrim
- **NEVER make ALL sections transparent** — particles behind text = unreadable
- Remove transparency in `.catch()` fallback so 2D canvas mode keeps opaque backgrounds.

### Render Loop Must Be Explicitly Started
- `MantisScene.init()` creates scene/camera/renderer but does NOT start the rAF loop.
- `MantisParticles.init()` loads shaders and creates geometry but does NOT render.
- You MUST call `MantisScene.render()` (or equivalent) after all setup completes to start `requestAnimationFrame`.
- For reduced-motion: do a single `renderer.render(scene, camera)` instead of starting the loop.

### Initialization Chain
```
MantisScene.init()          → returns true/false (sync)
  └→ MantisParticles.init() → returns Promise (async shader load)
       └→ MantisCamera.setup()  → void (creates ScrollTriggers)
            └→ MantisScene.render()  → starts rAF loop
```
Each step depends on the previous. Camera MUST come after particles (it calls particle methods). Render MUST come last.

### prefers-reduced-motion
- Browsers (especially automation/headless) often have `prefers-reduced-motion: reduce` enabled by default.
- The reduced-motion branch runs BEFORE the normal animation path and returns early.
- Ensure the reduced-motion branch also handles Three.js init (body class, single-frame render).
- **Windows/Chrome gotcha**: Chrome on Windows maps the Win32 `SPI_GETANIMATION.iMinAnimate` flag to `prefers-reduced-motion: reduce`. Many users disable Windows animations for performance without realizing it kills ALL web animations (GSAP, Three.js, CSS transitions — everything behind a reduced-motion check).
  - **Diagnose**: In browser console: `matchMedia('(prefers-reduced-motion: reduce)').matches` → if `true`, check Windows setting.
  - **Check Windows**: PowerShell `Add-Type -TypeDefinition 'using System;using System.Runtime.InteropServices;public class AnimInfo{[DllImport("user32.dll")]public static extern bool SystemParametersInfo(uint a,uint b,ref ANIMATIONINFO c,uint d);[StructLayout(LayoutKind.Sequential)]public struct ANIMATIONINFO{public uint cbSize;public int iMinAnimate;}}'; $a=New-Object AnimInfo+ANIMATIONINFO; $a.cbSize=8; [AnimInfo]::SystemParametersInfo(0x0048,0,[ref]$a,0); $a.iMinAnimate` → `0` means animations disabled.
  - **Fix**: Set `iMinAnimate = 1` via `SystemParametersInfo(0x0049, ...)` and restart Chrome (it caches the media query at launch).
  - **Immediate override (no restart)**: Use CDP `Emulation.setEmulatedMedia` with `features: [{name: 'prefers-reduced-motion', value: 'no-preference'}]` to override for the current session.
  - **Testing implication**: Always verify `prefers-reduced-motion` status before concluding animations are broken. A "no animations visible" bug is often this flag, not a code issue.

### Fallback Pattern
```js
try {
  if (!window._threeLoadFailed && typeof MantisScene !== 'undefined' && MantisScene.init()) {
    document.body.classList.add('mantis-3d-active');
    MantisParticles.init().then(function() {
      MantisCamera.setup();
      MantisScene.render();
    }).catch(function() {
      document.body.classList.remove('mantis-3d-active');
      MantisScene.dispose();
      initCanvases(); // 2D fallback
    });
  } else {
    initCanvases(); // 2D fallback
  }
} catch (e) {
  console.warn('[MANTIS] 3D init failed, using 2D fallback', e);
  initCanvases();
}
```

---

## 6d. Scroll Snap — Rare, Conditional Implementation Guide

### When to Use Snap
- Basic low-content landing pages where each section is a self-contained slide
- Deck-like presentations viewed as a sequential story
- Simple product showcases/campaign pages with full-viewport panels
- NOT for dashboards, app shells, forms, pricing tables, long-form content, blogs, SEO pages, or variable-height sections

Snap is not a normal website default. A page can be premium with natural scroll.

### CSS Scroll Snap (when snap is chosen)
```css
/* WHY: CSS scroll-snap is native, works on all browsers, and avoids
   conflicts with smooth scroll libraries. GSAP ScrollTrigger snap has
   known bidirectional issues with Lenis (GitHub: darkroomengineering/lenis#389) */
html {
  scroll-snap-type: y mandatory;
}
section {
  scroll-snap-align: start;
  scroll-snap-stop: always; /* WHY: prevents skipping sections on fast swipe */
  min-height: 100svh; /* WHY: svh accounts for mobile browser chrome, vh does not */
}
```

### Lenis Compatibility — CRITICAL WARNING
- **Lenis smooth scroll BREAKS CSS scroll-snap.** Lenis overrides native scroll behavior, making snap points unreliable.
- **GSAP ScrollTrigger snap + Lenis has known issues** — scrolling up to previous snap point is nearly impossible ([GitHub #389](https://github.com/darkroomengineering/lenis/issues/389)).
- **The `lenis/snap` package has the reverse problem** — scrolling down becomes difficult.
- **Solution**: For snap-section pages, **do NOT use Lenis**. Use native scroll + CSS snap. GSAP ScrollTrigger still works without Lenis for entrance animations (`onEnter`, `onLeave` callbacks).
- **Lenis is still great for** continuous-scroll pages WITHOUT snap (portfolios, editorial sites, product detail pages).

### Section Height Contract
- Every snapping section MUST fit within one viewport height at ALL breakpoints
- Use `100svh` not `100vh` — `svh` (small viewport height) accounts for mobile browser chrome
- If ANY section's content exceeds viewport → either reduce content or set `scroll-snap-align: none` on that section
- Test at: 1920x1080 (desktop), 768x1024 (tablet), 375x812 (iPhone), 360x668 (worst-case Android)
- **GSAP pin is INCOMPATIBLE with snap** — pinned sections consume extra scroll distance, breaking snap calculations. Remove ALL pins when using snap.

### Per-Section 3D Object Transitions (with snap)
When combining Three.js with CSS snap:
- Use `IntersectionObserver` (not ScrollTrigger `scrub`) to detect which section is active
- On section enter: morph 3D object to that section's shape using GSAP tween
- Kill any in-progress morph tween before starting a new one (`gsap.killTweensOf(...)`)
- Dual-buffer morph: keep two shape arrays (`aFrom` + `aTo`), interpolate via shader uniform
- This avoids storing all shapes as GPU attributes — only two in memory at once

---

## 6e. 3D Spatial Depth System — Making Flat UIs Feel Dimensional

> Read `references/3d-spatial-depth.md` for full CSS code, GSAP patterns, and performance rules.

### When to Apply

Apply 3D spatial depth when the UI is the product or the experience itself — dashboards, command centers, AI interfaces, campaign pages, product demos. Do NOT apply to standard forms, settings pages, or dense data tables. Match to Motion Mode 2 or Mode 3.

### The 6-Layer MECE Depth Model

Every dimensional interface is composed of 6 independent depth systems. Use all 6 for maximum spatial feel, or selectively omit layers for subtler depth:

| Layer | System | Technique | Cost |
|-------|--------|-----------|------|
| **1. Background** | Ambient gradient orbs + noise grain | `radial-gradient()` pseudo-elements + SVG noise | Zero (pure CSS) |
| **2. Structure** | CSS `perspective` + `preserve-3d` | Container `perspective: 1200px`, child `translateZ()` | Zero (GPU composited) |
| **3. Content** | Dark glassmorphism at staggered Z | `backdrop-filter: blur(12px)`, per-element `translateZ` | Low (blur is GPU) |
| **4. Accent** | Inner glow borders + radial halos | `box-shadow: inset`, `::after` radial-gradient | Zero |
| **5. Interactive** | Mouse parallax + card tilt + Z-lift | GSAP `quickTo` on `pointermove`, hover `rotateX/Y` | Low (transform only) |
| **6. Ambient** | Floating tiles + gradient breathing | GSAP `yoyo` bobs, CSS `@keyframes` on pseudo-elements | Zero |

### Key Implementation Rules

1. **`perspective` goes on the container, `translateZ` on children.** Never both on the same element.
2. **`transform-style: preserve-3d`** on the grid/layout element so children render in actual 3D space (not flattened).
3. **Colored shadows on dark themes.** Use accent-hsl shadows instead of pure black — creates warmth and connects shadows to the design language.
4. **Mouse parallax via GSAP `quickTo`** — optimized for continuous tracking, no tween spam. Each Z-layer shifts at a different rate: background 0.5%, content 1-2%, foreground 3%.
5. **Card tilt max 3-5 degrees.** More than 5° feels gimmicky. Calculate from cursor position relative to card center.
6. **Floating amplitude max 4px.** Duration 3-5s with staggered starts. Only animate `transform`.
7. **`will-change: transform`** only on actively animating elements, not the whole tree. Keep promoted layers under 20.
8. **Mobile**: disable mouse parallax, reduce perspective to 800px, reduce Z-range 50%, disable tilt, reduce blur to 8px or use solid fallback.
9. **`prefers-reduced-motion`**: disable parallax + float + tilt, keep static Z-positions for structural depth.
10. **Never animate `backdrop-filter`, `width`, `height`, `top`, `left`** — only `transform` and `opacity`.

### Quality Gate Items (added to Section 7)

```
[ ] 3D-PERSPECTIVE — CSS perspective active on layout container? preserve-3d on grid?
[ ] 3D-ZLAYERS — Elements at different translateZ values? At least 3 distinct Z-planes?
[ ] 3D-PARALLAX — Mouse parallax working on desktop? Layers shift at different rates?
[ ] 3D-FLOAT — Tiles/cards have ambient floating motion? Staggered, not synchronized?
[ ] 3D-SHADOWS ��� Colored accent shadows, not pure black? Shadow depth scales with Z?
[ ] 3D-MOBILE — Parallax disabled, blur reduced, Z-range halved on ≤768px?
[ ] 3D-REDUCED — Reduced-motion keeps static depth but disables all motion?
```

---

## 6f. Premium Typography — Gradient Text, Sheens & Spotlight Effects

> Read `references/premium-typography.md` for full CSS code, color palettes, animation patterns, and anti-patterns.

### When to Apply

Apply premium gradient typography to **display headings (48px+)** on dark themes where the brand identity is premium, luxury, aspirational, or "golden palace" in energy. This is NOT for every project — it's for products where the typography itself should feel like illuminated metallic surfaces with beams of light hitting them.

**Use when:** Dark theme + premium brand + display-sized headings + the text IS the focal point (hero, dashboard scores, revenue numbers).
**Skip when:** Light theme, dense data UI, body text, buttons, labels, or any text under 24px.

### The 5-Layer Typography Depth Model

Each layer adds depth to display text. Use all 5 for maximum "golden palace" feel, or selectively for subtler premium:

| Layer | Effect | Technique | When to Use |
|-------|--------|-----------|-------------|
| **1. Metallic Gradient** | Text appears as warm metal | `linear-gradient` multi-stop (dark→light→dark) + `background-clip: text` | Display headings where premium typography is the focal treatment |
| **2. Animated Sheen** | Light sweeps across text | `background-size: 300%` + `@keyframes` moving `background-position` | Hero h1 only, 2.5-3.5s cycle |
| **3. Spotlight** | Directional light hitting text | `radial-gradient` ellipse overlay positioned off-center | Optional, hero headings |
| **4. Warm Glow** | Text radiates warmth | `text-shadow` with champagne/accent color, max 50px blur | Display headings, mode-reactive |
| **5. Holographic** | Rotating metallic reflection | `@property --holo-angle` + `conic-gradient` | Max 1-2 elements per page (special moments) |

### Gradient Hierarchy (Intensity Decreases with Heading Level)

```
h1 (48px+, hero)    → Full metallic (7+ stops) + sheen animation + glow
h2 (32-47px)        → Metallic (3-5 stops) + glow, NO animation
h3 (24-31px)        → Subtle gradient (2-3 stops), NO glow
Stat numbers         → Champagne or brand gradient (contextual)
< 24px               → NEVER gradient. Solid color ONLY.
Body text            → ALWAYS solid #FAFAFA. Never gradient.
```

### Color Palette: "Golden Palace" Warm Premium

The "golden palace" feel is **warm white with champagne/platinum sheens** — NOT literal gold everywhere.

| Color | Hex | Role |
|-------|-----|------|
| Warm White (peak) | `#f8f8f4` | Primary gradient highlight |
| Champagne | `#f7e7ce` | Warm accent stop |
| Warm Silver | `#d4d4c8` | Mid-tone metallic |
| Dark Warm Gray | `#8a8a7e` | Shadow edge |
| Deep Shadow | `#3a3a38` | Darkest gradient edge |

**NEVER use:** Pure gold `#ffd700` (cheap), pure yellow (jarring), neon gold (Vegas), heavy glow > 50px (tacky).

### Key Implementation Rules

1. **`background-clip: text` + `-webkit-background-clip: text` + `-webkit-text-fill-color: transparent`** — all three required. Always include `color` fallback.
2. **Sheen sweep timing: 2.5-3.5 seconds.** Faster = cheesy. Slower = sluggish. Use `ease-in-out`, never `linear`.
3. **`will-change: background-position`** only on actively animated text. Max 3 animated headings per page.
4. **Gradient intensity = heading importance.** h1 gets full treatment, h2 gets reduced, h3 gets barely-there.
5. **Warm glow via `text-shadow`**: max 2 layers, max 50px blur. Use champagne/accent color, not pure white.
6. **Holographic conic gradient** is for 1-2 special moments ONLY (revenue reveals, achievement unlocks).
7. **Pair with 3D spatial depth** — gradient text at different `translateZ` values creates genuine depth hierarchy.
8. **Reduced motion**: disable sweep/rotation animations, keep static gradients (the metallic look comes from the color stops, not the motion).
9. **Test at 2x DPI on mobile** — gradient text rendering quality varies, check for banding.
10. **Never animate gradient text inside scrolling containers** — scroll + animation compositing conflicts on mobile.

### Quality Gate Items (added to Section 7)

```
[ ] TYPO-GRADIENT  — If premium gradient typography is chosen, display headings (48px+) have real metallic depth, not flat white?
[ ] TYPO-SHEEN    — If hero heading is the focal premium moment, sheen sweep exists and timing is 2.5-3.5s?
[ ] TYPO-GLOW     — Dark/luminous premium display text has warm controlled glow? ≤50px blur?
[ ] TYPO-HIERARCHY — Gradient intensity decreases h1 > h2 > h3 > solid?
[ ] TYPO-BODY     — Body text, labels, buttons are solid color (NO gradient)?
[ ] TYPO-WARM     — Colors warm/premium, not cold/clinical or cheap/neon?
[ ] TYPO-FALLBACK — `color` fallback set? `@supports` query for old browsers?
[ ] TYPO-MOTION   — Reduced-motion keeps static gradient, disables sweep?
```

---

## 6g. Premium 3D Buttons — Tactile, High-Class, Animated

> Read `references/premium-buttons.md` for full CSS recipes, timing, and accessibility.

### When to Apply

Apply real 3D tactile buttons to **primary CTAs, hero actions, and key interactive controls** on
premium/expressive surfaces (dark luxury, fintech, product, campaign). Buttons should feel like
physical high-tech controls — visible depth, a hover that lifts and catches light, and a **tactile
press that slams down**. Skip for dense toolbars, table-row actions, and tertiary links where flat
is correct. A flat fill with a color-change hover is the #1 cheap tell on a premium surface.

### The Core Technique (3 states + asymmetric timing)

1. **Rest** — raised, with a visible **3D edge/rim** (a hard colored `box-shadow` below the button).
2. **Hover** — `translateY` lift + `brightness(1.08)` + a specular glare sweep; the rim grows.
3. **Press (`:active`)** — fast slam-down (~34ms) that **collapses the rim** → a real tactile click.

The tactile secret is **asymmetric timing**: lightning press (~34ms), springy hover rise (~220ms,
`cubic-bezier(0.3,0.7,0.4,1.5)` overshoot), leisurely settle (~600ms) — same duration everywhere
reads lifeless. Default = single-element chunky hard-3D push (upgrades a plain `<button>`, no extra
markup); Josh-Comeau front/edge/shadow when you control the markup; neumorphic press for soft/calm
surfaces. Token-driven colors, real `<button>`, `:focus-visible`, ≥44px target, and reduced-motion
keeps the depth static. Full recipes in `references/premium-buttons.md`.

---

## 7. Self-Review Quality Gate (MANDATORY)

All points must pass BEFORE showing ANY output to the user:

```
=== DESIGN ===
[ ] AUDIENCE    — Audience, sophistication, device/context, awareness stage, and skepticism understood before styling?
[ ] PROJECT-AUDIT — Existing product, assets, copy, flows, design system, and proof inspected or explicitly unavailable?
[ ] STORY       — Clear design story defined? Does each major section advance that story rather than copying a trend?
[ ] FLOW        — Entry point → first impression → proof path → objection handling → action mapped?
[ ] CHALLENGE   — Literal request challenged for better marketing/design outcome? Wrong surface/style/motion called out before building?
[ ] CONTEXT     — Existing product/design system/assets inspected or explicitly unavailable? Named brands/products/current facts verified?
[ ] TYPE-RATIONALE — Premium font pair chosen for this audience/surface? No cheap novelty/video-game font unless explicitly appropriate?
[ ] COLOR-RATIONALE — Palette chosen from brand/upstream candidates with semantic roles and strong contrast? NOT default template colors?
[ ] THEME       — Intentional choice (dark/light/custom) appropriate for project?
[ ] CRAFT       — Expressive/premium surfaces show fine details: section separation, borders/outlines, texture, controlled glow/sheen, and material hierarchy?
[ ] DEPTH       — Expressive surfaces have visible depth cues? Operational surfaces have enough separation without theatrical decoration?

=== ICONS (NEW — Anti-Pattern #20) ===
[ ] ICON-QUALITY — Zero emoji icons used as UI elements? Grep HTML for emoji Unicode (U+1F000–U+1FFFF). All functional icons must be SVG (inline, Heroicons, or Lucide). Emoji in body copy is fine — emoji as card/section icons = FAIL.

=== BUTTONS (NEW — Anti-Pattern #43) ===
[ ] BTN-3D     — Primary CTA + key buttons have real tactile depth (a visible 3D rim/edge), not a flat fill, on premium/expressive surfaces? See references/premium-buttons.md.
[ ] BTN-STATES — Hover (lift + brightness), active (fast press that collapses the rim), focus-visible, and disabled states all covered — not entrance-only?
[ ] BTN-MOTION — Press is fast (≤40ms) with a springy hover rise and a slower settle (asymmetric timing)? Only transform/box-shadow/filter animated? Reduced-motion keeps the depth, drops the press motion?
[ ] BTN-A11Y   — Real <button>/<a> (never a styled div), visible focus ring, touch target ≥44px?

=== ANIMATION ===
[ ] MODE        — Motion mode selected explicitly and appropriate for site type? Mode 0/1/2/3 justified?
[ ] MOTION-COVERAGE — Expressive surfaces have section choreography where useful; operational surfaces have state/focus/hover/loading motion only. No dashboard/admin scroll theater.
[ ] VARIETY     — For Mode 1/2/3 expressive pages only: at least 3 genuinely different motion/state treatments where motion is part of the design. Mode 0 apps may pass with high-quality microstates only.
[ ] WOW         — For expressive marketing/brand/campaign pages: at least one memorable craft moment. For operational UI: one premium craft detail or interaction state is enough; no forced spectacle.
[ ] STATES      — Motion exists beyond entrances? Hover/focus/active/loading/success states reviewed where relevant?

=== MOBILE (NEW — Anti-Pattern #21) ===
[ ] MOBILE-GRID — Test at 360x668. Count visible columns in every card/feature/stat section. Must be exactly 1 column on mobile (≤768px). Multi-column cards on mobile = FAIL. Exception: icon-only rows (<48px icons).
[ ] MOBILE-CTA  — Primary CTA visible without scrolling at 360x668 (worst-case Android with browser chrome)?
[ ] REVIEW-SHOTS — Verify actual screenshot artifacts at 1280x800, 768x1024, 360x668, plus one scrolled/interaction state. Record file paths. Do not trust code inspection alone.

=== VISUAL ACCEPTANCE REVIEW ===
[ ] VISUAL-CONTRACT — For non-trivial frontend work, define the visual acceptance contract before final review: surface type, motion mode, stack, required viewports, sections, states, expected visible objects, forbidden failures, and quality dimensions.
[ ] SEMANTIC-REVIEW — Screenshot proof includes structured semantic review: inspected=true, verdict=PASS, request_match entries, quality_checks, and explicit evidence that required objects/states are visible and forbidden failures are absent.
[ ] EVIDENCE-INTEGRITY — Browser proof has concrete screenshot artifact paths or equivalent rendered artifacts, console/runtime status, and cannot be replaced by a generic build/test pass.
[ ] INTERACTION-INVENTORY — Every meaningful interactive control/state in the contract was exercised or explicitly marked out of scope.

=== CONVERSION ===
[ ] SCROLL      — Scroll behavior chosen situationally? Snap only for low-content slide-like pages; Lenis only when continuous-scroll polish materially helps; native scroll is allowed and often best.
[ ] CONVERSION  — Page follows chosen conversion style? (Hormozi DEFAULT, Presentation for business plans/pitches)
[ ] COPY        — Clear, specific, no hedging? Hormozi clarity applies to ALL styles?
[ ] CTA         — Primary CTA above fold at desktop (1280x800) AND highest contrast element?

=== VISUAL DEFECTS (NEW) ===
[ ] TRUNCATION  — No user-visible copy clipped, ellipsized, or line-clamped unless the brief explicitly requires truncation. Longest realistic text still readable.
[ ] TEXT-CONTAIN — Text/buttons/badges/labels stay inside their parent boxes at desktop and 360x668? No words or controls burst through borders?
[ ] NO-OVERLAP  — Boxes, cards, nav, charts, media, and text do not overlap incoherently. Any intentional overlap is readable and clearly designed.
[ ] STABLE-SIZE — Fixed-format UI elements have stable dimensions and do not resize/jump on hover, load, or dynamic content.
[ ] SHELL-ALIGN — Main content is visually centered within the app shell/page frame. No accidental sidebar offset, off-center grid, or asymmetric left/right occupancy.
[ ] SPACE-USAGE — No stretched cards, giant empty gutters, dead zones, or equal-height artifacts that create obvious wasted space.
[ ] LIVE-STATES — Test the longest/populated/realistic content state, not just placeholder-short copy. Cards, tables, badges, and narrative boxes must still hold up.
[ ] LAYERS      — Depth uses intentional planes (background / structure / content / accent) rather than random overlapping effects.
[ ] LOCAL-CONTRAST — Does every text element (heading, number, label, badge) have near-opposite contrast against its IMMEDIATE backing — a dark/light scrim, plate, section, or deep shadow right behind it — so it stays readable even if the background behind it is bright? No bright-on-bright text? (Fix readability locally around the text, not by dimming the whole page.)

=== CSS LOADING ORDER (Anti-Patterns #29-31) ===
[ ] LOADING-SHELL  — If a loading.tsx/Suspense fallback exists, does it include the same outermost shell/wrapper classes as the page? CSS :has() rules that depend on these classes (sidebar hide, theme switch) must fire during loading phase too.
[ ] NO-OPACITY-ENTRANCE — Grep all @keyframes in CSS: do ANY entrance animation `from` blocks contain `opacity: 0`? If yes with `animation-fill-mode: both` → content is invisible during delay → FOUC. Remove opacity from entrance keyframes.
[ ] NO-CSS-TOOLTIPS — Grep for `content: attr(data-` in CSS. If found, the tooltip text WILL leak as visible text during async CSS loading. Replace with native `title` attribute or JS tooltip component.
[ ] DEV-MODE-TEST — After visual changes, test in Next.js dev mode (not just production build). Dev mode loads CSS asynchronously, exposing FOUC and load-order bugs invisible in prod.

=== AI-SMELL (MEASURABLE) ===
[ ] AI-SMELL    — Run this checklist. ANY "yes" = FAIL, fix before delivering:
                  • Emoji used as section/card icons? (→ Anti-Pattern #20)
                  • Uniform card grid (all same size, evenly spaced)? (→ Anti-Pattern #16)
                  • Expressive page uses only fade-up animations? (→ Anti-Pattern #22)
                  • Inter/Roboto/Arial/system font used as a lazy default rather than inherited/native/dense-UI rationale? (→ Anti-Pattern #1)
                  • Generic hero ("Welcome to..." / "Discover...")? (→ Anti-Pattern #17)
                  • Centered everything with no visual tension? (→ Anti-Pattern #15)
                  • Laggy fake cursor or scroll-hijack behavior? (→ Anti-Pattern #23/24)
                  • Cheap novelty/video-game font on a serious or premium product? (→ Anti-Pattern #38)
                  • Weak borders/no section separation/no glow on a dark premium surface? (→ Anti-Patterns #40-41)

=== ACCESSIBILITY ===
[ ] A11Y        — WCAG 2.2 AA target met? prefers-reduced-motion? Focus indicators? Semantic HTML?
[ ] CONTRAST    — Text, controls, and key graphics meet contrast requirements in their actual rendered state?
[ ] KEYBOARD    — All primary flows work by keyboard alone. No hover-only or pointer-only critical interactions.
[ ] TARGETS     — Touch/click targets are comfortably tappable and not overly tight or tiny.
[ ] LABELS      — Inputs, icon buttons, landmarks, and meaningful media have names/labels/alt text.
[ ] SVH         — Uses svh/min-height (not fixed vh) for full-viewport sections?
[ ] SAFE-AREA   — viewport-fit=cover meta tag? env(safe-area-inset-*) on sticky elements?
[ ] WORDWRAP    — All headings use overflow-wrap: normal? No break-word or break-all?

=== PERFORMANCE / STACK CHOICE ===
[ ] STACK       — Rendering stack chosen intentionally? CSS 3D vs Rive vs Spline vs Three.js justified for page type?
[ ] BUDGET      — Motion/3D budgets respected for the chosen mode and breakpoint?
[ ] MOBILE-PERF — Heavy shaders/WebGL/blur reduced or removed on mobile/low-power devices?
[ ] NO-INTRO    — No forced cinematic intro blocks the user from content/CTA?

=== SNAP (if applicable) ===
[ ] SNAP-JUSTIFY — Snap is justified by a low-content slide/deck/product-showcase experience, not merely because the page has sections?
[ ] SNAP        — If snap enabled: EVERY snapping section fits within viewport at ALL breakpoints?
[ ] SNAP-WORKS  — Actually scroll and verify snap in BOTH directions. No Lenis if CSS snap.
[ ] SNAP-ESCAPE — Tall/pinned/variable sections are exempted or page uses natural scroll instead?

=== DATA INTEGRITY ===
[ ] STATS-VERIFIED  — All numbers/stats on page verified against actual source data?
[ ] COUNTER-FALLBACK — Any counter-animated numbers have correct final values in HTML as fallback (not "0" or "$0")? If GSAP fails to load, do the numbers still display correctly?
[ ] LINKS-WORK      — Every link points to a real destination (no dead href="#")?
[ ] ANCHOR-TARGETS  — Every href="#id" has a matching id="" element? No orphan anchors?
```

If ANY point fails, fix it before delivering. This gate is not optional.

---

## 8. Tool Registry + Intelligent Routing

| Tool | Invoke | When | Fallback |
|------|--------|------|----------|
| **GSAP** | CDN + references/animation-patterns.md | Expressive pages, product storytelling, diagram/counter/text choreography, and complex interaction states | CSS transitions for simple/static/operational UI |
| **Lenis** | CDN + references/animation-patterns.md | Continuous-scroll editorial/marketing pages where smoother momentum materially helps | Native scroll, especially for apps or snap pages |
| **BarbaJS** | CDN + references/animation-patterns.md | Multi-page sites where transitions improve narrative continuity | Native navigation |
| **Rive** | External embed/runtime | Stateful interactive illustrations, product explainers, polished UI states | SVG/CSS animation |
| **Spline** | External embed | Lightweight hero scene when a prebuilt 3D composition is enough | CSS 3D or static illustration |
| **Three.js / R3F** | references/animation-patterns.md | Custom immersive hero, procedural particles, scene choreography | CSS 3D, Canvas 2D, Spline |
| **Poe Media** | `Skill("poe-media")` | Generate source stills/video plates/textures when the page needs bespoke media that does not already exist: hero image plates, animated background ingredients, style-consistent product mockups, texture passes, short ambient loops | Build with CSS/SVG/GSAP from existing assets |
| **Google Stitch** | `python3 scripts/google_stitch.py` | Layout inspiration + visual prototyping. Generate sections individually with EXACT copy pasted in. Never use Stitch output directly — extract layout ideas, rebuild with skill Phases 4-6. See `references/tool-decision-matrix.md` for setup + prompting rules. | Build manually (often better — more control) |
| **21st.dev** | `python3 scripts/twenty_first.py` | Specific pre-built component | Build from scratch |
| **uipro-cli** | `uipro init --ai claude` | Industry-specific design tokens | references/design-system-generator.md |
| **Antigravity** | RECOMMEND to user | Full app scaffold | N/A — external IDE |
| **Web Designer** | RECOMMEND to user | HTML5 ads/banners | N/A — external GUI |
| **Remotion** | `Skill("remotion-best-practices")` | Video file output (MP4/WebM): frame-driven animations (useCurrentFrame), scene transitions (TransitionSeries), audio visualization (spectrum/waveform/bass-reactive), TikTok-style captions, 3D (ThreeCanvas), animated charts (SVG/D3), Lottie embedding, AI voiceover (ElevenLabs), parametric videos (Zod), maps (Mapbox) | N/A — different domain (video files, not web pages) |
| **Marketing Skills** | `Skill("copywriting")` etc. | Phase 3 (Structure) | references/conversion-framework.md |

**CRITICAL:** This skill produces genius output with ZERO external tools. Stitch/21st.dev/uipro-cli are enhancements only. The skill works perfectly with only GSAP CDN + its reference files.

`references/premium-frontend-quality-spec.md` is the master bar for:

- clarity
- premium craft
- surface classification
- preset families
- motion/media routing
- rendered-page verification expectations

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

### Video/Animation Content — Delegate to Remotion:

```
Skill("remotion-best-practices")  -> Video rendering (MP4/WebM), audio visualization
                                     (spectrum bars, waveforms, bass-reactive effects),
                                     TikTok-style captions with word highlighting,
                                     animated charts (bar/pie/line/stock), 3D scenes
                                     (ThreeCanvas), Lottie animations, AI voiceover
                                     (ElevenLabs TTS), parametric data-driven videos
```

**Decision rule:** If the output is a **video file** (rendered with React via useCurrentFrame, NOT CSS animations), use Remotion. If the output is an **interactive web page** (scroll-triggered, responsive, conversion-optimized), use this skill. Key difference: Remotion FORBIDS CSS transitions/animations — everything is frame-driven.

### Animation / Media Escalation Contract (MANDATORY)

The main frontend skill owns the page. It must decide when to stay web-native and when to invoke helper skills. Do NOT make the user manually request `poe-media` or `remotion-best-practices` for normal page builds.

**Default rule:** Prefer web-native motion first.

- Use CSS/GSAP/SVG/canvas for interactive page motion, hover states, scroll reveals, counters, text choreography, sticky storytelling, and cursor-reactive ambience.
- Escalate only when the page needs a media asset the DOM should consume, not when ordinary frontend animation would do the job.

**Escalate to `Skill("poe-media")` when:**

- The design needs bespoke source media that does not exist yet.
- A section should **show, not tell** with a custom hero still, product plate, texture pass, atmospheric plate, or short stylized motion plate.
- The page needs branded media ingredients for later animation work.

**Escalate to `Skill("remotion-best-practices")` when:**

- The design needs a **rendered asset** rather than DOM-only animation.
- The page needs a transparent or loopable WebM/MP4 hero layer, explainer loop, waveform/microphone visualization, animated diagram, kinetic text movie, or high-craft scene that is easier to author frame-by-frame than with CSS/GSAP.
- The page needs animation embedded beside copy so the explanation is visual, not text-heavy.

**Chain `poe-media` -> `remotion-best-practices` when:**

- Media must be generated first, then composited/animated into a premium loop or explainer asset.
- Example: generate a stylized microphone/product/environment plate with Poe, then animate it in Remotion into a transparent loop for the page.

**Do NOT escalate when:**

- A reveal, hover, tilt, parallax, SVG line draw, counter, marquee, SplitType text entrance, or canvas particle field will solve the problem cleanly.
- The result must remain deeply interactive with live DOM state. Remotion outputs files; it does not replace live UI behavior.

### Asset Selection Matrix

| Need | Primary Tool | Why |
|---|---|---|
| Hover, focus, click, scroll, sticky section choreography | This skill + GSAP/CSS/SVG | Native, lightweight, interactive |
| Particle fields, network lines, ambient procedural motion | This skill + Canvas/Three.js | Better as live page motion |
| Transparent loop over hero/product frame | `Skill("remotion-best-practices")` | Frame-perfect loop, exportable WebM |
| Waveform, microphone, audio-reactive visual | `Skill("remotion-best-practices")` | Audio visualization is already a first-class Remotion pattern |
| Custom stills, textures, surreal plates, media ingredients | `Skill("poe-media")` | Fast source-asset generation |
| Generated still/plate that then needs premium animation | `Skill("poe-media")` then `Skill("remotion-best-practices")` | Best split of generation vs compositing |

### Page-Build Rules For Motion/Media

1. Build the page shell and conversion structure first.
2. Identify where text should be replaced or reinforced by visual explanation.
3. Decide whether each motion need is:
   - `live_ui_motion`
   - `generated_media`
   - `rendered_motion_asset`
4. Invoke helper skills only for the latter two.
5. Bring the returned asset back into the page and test it in the real layout.

**WHY:** Premium pages fail when every effect is attempted in the DOM or when the model over-explains in text. This routing keeps ordinary UI motion lightweight, while allowing cinematic media/explainer assets when they materially improve clarity and perceived quality.

### Required Motion Coverage

If the page contains a major hero, explainer section, comparison section, or feature demonstration, the skill must actively consider whether one of these would improve comprehension faster than extra copy:

- animated product walkthrough
- waveform / voice / microphone loop
- animated schema / process diagram
- transparent hero overlay loop
- stylized ambient media plate

If the answer is yes, invoke the relevant helper skill instead of shipping a text-heavy compromise.

---

## 10. Conditional CDN Links

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

Include only the libraries selected in Phase 1:

- GSAP/ScrollTrigger: expressive marketing, editorial, product, portfolio, or campaign pages with real choreography.
- Lenis: continuous-scroll marketing/editorial pages only. Never dashboards/admin pages. Never CSS scroll-snap pages.
- BarbaJS: multi-page narrative transitions only.
- SplitType: one signature typography moment only, not every heading.

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
4. **Build with zero `style=` attributes.** Use CSS classes, variables, and tokenized styles; small critical `<style>` blocks are allowed when justified.
5. **Animate with purpose.** Every GSAP/Lenis/ScrollTrigger decision has a reason, and native/CSS-only is valid when better.
6. **Run the mandatory quality gate.** Fix failures. Do not deliver until clean.
7. **The output must be distinctive to this project.** If it smells like AI-generated template work, copied trend work, or cheap novelty styling, it is not done.

The standard is not "good enough." The standard is "someone screenshots this and shares it."
