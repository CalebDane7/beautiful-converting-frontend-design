# Premium Frontend Quality Spec

This document is the master quality bar for `beautiful-converting-frontend-design`.

It exists to solve four recurring failures:

1. the skill produces attractive but not premium-enough pages
2. the output drifts away from the intended visual direction
3. the testing layer only checks hygiene and misses premium-craft failures
4. the user has to repeatedly restate the same quality expectations

This spec separates:

- **Hard rules**: measurable, enforceable, or strongly evidenced
- **House rules**: strict style doctrine for this system
- **Preset families**: allowed aesthetic branches
- **Gate proof**: what rendered evidence must confirm before work is considered done

---

## 1. Core Doctrine

Every page must satisfy all of these at once:

- **Audience first.** The design must begin with who the page is for, what they believe, and what flow they are in.
- **Story governs style.** The visual system should tell a specific product/market story, not copy a trend.
- **Clarity governs.** The user should immediately understand what matters, where to look, and what to do next.
- **Premium craft differentiates.** Fine detail, polish, trim, lighting, depth, and separation are part of the product quality.
- **Unintentional flatness is failure.** Default output must not feel bland, underlit, textureless, or visually unresolved.
- **Show, do not over-explain.** Use visuals, animation, diagrams, motion, and media to communicate wherever possible.
- **One clear thing at a time.** Each viewport/section should have one dominant idea, object, or action.
- **Premium must still scale.** No inline CSS, no brittle layout hacks, and no copy architecture that blocks future localization or growth.

---

## 2. Surface Types

The system must classify the page before styling or animation decisions:

### Expressive Surfaces

Use for:

- landing pages
- campaigns
- storytelling pages
- premium heroes
- feature showcases
- brand and conversion surfaces

Bias:

- stronger depth
- richer motion
- more atmosphere
- more illustrative/media support
- more obvious wow moments

### Operational Surfaces

Use for:

- dashboards
- app shells
- forms
- settings
- analytics
- productivity interfaces
- dense working surfaces

Bias:

- stronger scanability
- restrained motion
- faster interaction feedback
- clearer labels and grouping
- less parallax and less spectacle

**WHY:** Premium does not mean every surface gets the same level of theatricality. Expressive surfaces sell, operational surfaces must support work without distraction.

---

## 3. Hard Rules

These rules are black-and-white. Violating them is a fail.

### 3.1 Contrast And Separation

- Text must remain readable against its actual rendered background.
- Important text over dynamic or complex backgrounds must have protection:
  - scrim
  - stroke
  - shadow
  - backing plate
  - contrast-safe highlight treatment
- Important surfaces must be visibly separated from adjacent surfaces.
- Borders, cards, inputs, buttons, overlays, and sections must not visually collapse into each other.
- Primary objects must carry stronger figure-ground separation than secondary ones.
- Contrast is not only text-vs-background. It also includes:
  - surface-vs-surface
  - border-vs-surface
  - primary-vs-secondary hierarchy
  - content-vs-decoration
- Premium surfaces need clear section separation. Use stronger bands, outlines, borders, material shifts, or spacing when adjacent sections blend together.
- Weak contrast, invisible borders, and underlit CTAs are premium-craft failures even when the CSS is technically valid.

### 3.2 Typography And Readability

- Body copy should almost never be below `16px` desktop or `15px` mobile on premium marketing surfaces.
- Use premium-quality type. Avoid novelty, sci-fi, game-like, comic, or chunky fonts unless that is the actual brand.
- Apple-like product surfaces should bias toward clean optical sans systems; luxury/fashion surfaces should bias toward restrained geometric grotesks and refined high-contrast serifs.
- Important UI text must be easy to read at a glance.
- Thin or delicate fonts must not be used for important content.
- Headline scale should maximize clear readable fill without causing ugly wraps, collisions, or balance problems.
- Long-form text should remain scan-friendly and not become dense walls.
- No clipped, truncated, orphaned, or badly wrapped visible text unless the pattern explicitly calls for preview text.
- Headings and key copy must survive longer realistic content states.

### 3.3 Hierarchy, Grouping, And Cognitive Load

- Each section must have one dominant idea.
- Each viewport must avoid too many competing focal points.
- Related elements must be visibly grouped by space, containment, or shared surface.
- Space may only be used to improve grouping, hierarchy, and focus.
- Space is a defect when it weakens the main thing or breaks a functional unit.
- Pages must avoid visible choice overload and unnecessary competing actions.

### 3.4 Interaction Clarity

- Clickable things must look clickable.
- Inputs must look like inputs.
- Primary actions must be unmistakable.
- Critical interactions must not rely on hover alone.
- Focus, active, loading, success, and error states must be intentionally designed where relevant.
- Dead clicks, unclear affordances, and mystery interactions are failures.

### 3.5 Motion Safety And Usefulness

- Motion must support meaning, status, hierarchy, feedback, or delight.
- Motion must not obscure content or delay comprehension.
- Reduced-motion users must have a workable alternative.
- On dense/productivity surfaces, motion must be reduced to feedback and hierarchy.
- On expressive surfaces, motion may be richer but cannot compete with the primary message.

### 3.6 Layout Stability And Responsiveness

- The page must not visibly jump, reflow badly, or shift important content unexpectedly.
- Hero content must remain stable during loading.
- Important content and controls must survive mobile browser chrome and safe-area constraints.
- Responsive behavior must be component-safe, not only page-safe.
- Mobile layouts must not behave like cramped scaled-down desktop layouts.

### 3.7 Forms, Errors, Empty States, Loading States

- Empty states must explain purpose and next step.
- Loading states must preserve the shell and reassure the user immediately.
- Error states must be clear, actionable, and visually intentional.
- Forms must use clear labels, local validation, and mobile-safe structure.
- Major forms must not rely on inline/disappearing labels.

### 3.8 Scalability And Localization

- No inline CSS.
- No unstructured scattered hardcoded UI copy for major interfaces.
- Visible strings must be externalizable and mappable for localization.
- Layouts must survive long-string expansion.
- Components should be built with logical scalability in mind:
  - reusable classes
  - tokenized design system
  - future locale mapping
  - content-length resilience

---

## 4. House Rules

These are strict style rules for this system even when not universally provable.

### 4.1 Premium Depth

Depth and separation must be visible by default, but intensity depends on the surface type.

For expressive/premium marketing surfaces, require at least **3** depth or material cues.
For hero surfaces, primary objects, and major feature surfaces, require at least **4** cues.
For operational surfaces, use quieter cues but still make grouping, edges, and active states obvious.

Allowed cues:

- atmospheric layer: gradient field, spotlight, glow cloud, mesh, texture
- surface separation: visible border/divider with tonal contrast
- light cue: sheen, highlight, bevel-like rim, specular edge, inner rim light
- occlusion cue: shadow or contact shadow
- z-layer cue: overlap, parallax, staggered planes, foreground/background layering

**Flat shadow-only treatment is not enough.**

### 4.2 Premium Typography Treatment

- Important text should not feel flat.
- Major headings and hero text should usually carry dimensional treatment:
  - sheen
  - gradient
  - highlight edge
  - depth-supporting shadow
  - strong contrast-safe lighting
- Readability always wins over styling.

### 4.3 Border And Surface Separation

- Important surfaces should have visible borders or equally strong separators.
- Borders must contribute to clarity, not just decoration.
- Default separator logic should be high-contrast enough to clearly define interactive and structural zones.
- Expressive/premium sections often need thicker strokes, double borders, inset outlines, rim lights, or high-contrast divider bands to avoid looking cheap and flat.
- Thin hairlines are appropriate only when they are still visible and match the brand's restraint.

### 4.4 Symmetry And Balance

- Pages should feel balanced and centered around the main object or task.
- Random underweighted left/right composition is a fail.
- Odd groupings must still resolve into balanced compositions.
- The main thing should get the most real estate.

### 4.5 Texture, Atmosphere, And Lighting

- Premium pages should usually have some atmospheric treatment:
  - grain
  - spotlighting
  - glow
  - texture
  - layered gradients
- Atmosphere must enrich the page, not muddy it.
- Dark premium themes must stay crisp, not gray and muddy.
- Glow is part of lighting, not an afterthought. Use controlled glow for primary actions, active states, hero objects, premium stats, and display text when the surface is luminous or dark.
- Missing glow/sheen on a dark premium hero can be a craft failure; excessive glow on dense UI is also a failure.

### 4.6 Premium Motion

- Motion direction is situational. Dramatic/cinematic motion belongs only where the surface type permits it.
- Parallax is an available depth signal on expressive surfaces, not a default for every page.
- Flat static expressive pages are not acceptable by default; operational pages may be mostly static if interaction states are polished.
- Ambient motion is welcome, but primary clarity must remain dominant.
- Important boxes/cards/buttons should usually respond to interaction.

---

## 5. Preset Families

All presets inherit the same master quality bar.

- **Glossy Futuristic**
  - polished, luminous, high-contrast, glossy surfaces, controlled futurism
- **Cinematic Tech**
  - dark premium, strong depth, motion-led, dramatic but controlled
- **Luxury Dark**
  - elegant, high-contrast, rich materials, deliberate restraint with strong polish
- **Editorial Premium**
  - strong type, hierarchy, balance, premium spacing, restrained but not flat
- **Warm Tactile**
  - textured, human-made, atmospheric, rich materials, softer premium depth
- **Minimal Premium**
  - clear, spacious, premium restraint, but still dimensional and polished
- **High-Contrast Product Demo**
  - demo-focused, obvious hierarchy, sharp separation, clarity-first
- **Gen Z Textured / Grunge Premium**
  - dark or high-contrast, textured, characterful, imperfect edges, but still readable and premium

**Glossy futuristic is first-class, not optional.**

---

## 6. Motion And Media Routing

### Stay Web-Native When

- the effect is best authored as live UI
- the page needs hover/focus/click/scroll interactivity
- CSS/GSAP/SVG/canvas can produce the effect at premium quality

### Escalate To Remotion When

- the page needs a rendered motion asset:
  - waveform
  - microphone visual
  - transparent loop
  - animated explainer
  - kinetic text movie
  - composited diagram

### Escalate To Poe Media When

- bespoke source media does not exist yet
- the design needs generated stills, textures, plates, or motion ingredients

### Chain Poe -> Remotion When

- source media must be generated first and then animated/composited into a premium asset

**Rule:** use the highest-quality path that best preserves clarity, performance, and craft.

---

## 7. Testing Gate Proof

A page is not done because it renders. It is done when rendered evidence proves the intended quality bar.

The gate must eventually prove:

### 7.1 Coverage

- every visible interactive element exercised
- below-fold sections captured
- desktop and mobile states covered
- important hover/click/focus/loading/success/error states exercised where relevant

### 7.2 Hard-Fail Checks

- unreadable text
- weak contrast / weak separation
- clipping / truncation / bad wraps
- broken symmetry / balance
- wasted space that weakens the primary object
- flat styling on surfaces that should carry depth
- weak hero emphasis
- invisible or weak primary action
- motion that hides content or feels broken
- missing important interaction states
- mobile-safe-area / chrome breakage

### 7.3 Premium-Craft Review Targets

The gate must check rendered evidence for:

- depth cues
- border separation
- hero prominence
- spacing and grouping
- balance and symmetry
- surface hierarchy
- texture / atmosphere
- lighting / sheen treatment
- non-flat typography treatment on major text
- real-estate usage aligned to the primary object

### 7.4 Animation Proof

Still screenshots are not enough for motion quality.

The gate should use:

- before/after state captures
- hover/click/scroll state transitions
- timed observation steps
- stateful screenshots after change

---

## 8. Scalability Architecture

Every implementation should assume future growth.

- use componentized structure
- use tokenized variables for color, spacing, radii, shadow, motion, and materials
- use CSS variables as the system source of truth
- avoid one-off styling islands
- externalize user-facing text
- plan for long copy and additional sections later

Recommended vanilla structure:

- `variables.css`
- `base.css`
- `typography.css`
- `components.css`
- `layout.css`
- `animations.css`
- `utilities.css`

---

## 9. Research Backbone

This spec is grounded in two layers:

### Hard Evidence

- W3C / WCAG
- Apple HIG
- Material Design
- NN/g
- Baymard
- CXL
- Laws of UX
- IxDF
- web.dev

### Current Premium Practice

- Awwwards / judged web craft
- Webflow trend and template ecosystems
- Framer marketplace patterns
- modern premium template systems

The implementation must keep these layers separate:

- **hard rules** are pass/fail
- **house rules** are strict doctrine for this system

---

## 10. Implementation Order

1. use this spec as the master source of truth for the frontend skill
2. mirror gate requirements into the skill's standalone testing and review flow
3. emit structured verification expectations from the skill
4. verify rendered evidence against those expectations
5. expand presets over time without weakening the master bar
