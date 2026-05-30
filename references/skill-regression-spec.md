# Skill Regression Spec

Use this file when validating or upgrading the `beautiful-converting-frontend-design` skill itself.
The goal is not just "did it produce something pretty." The goal is to catch repeated failure modes,
wrong routing decisions, weak accessibility defaults, and generic design drift.

Default validation target: **WCAG 2.2 AA** and the main skill quality gate in `SKILL.md`.

Default validation goal: **catch the highest-risk regressions as fast and cheaply as possible**.
Do not run the full matrix by default.

---

## 1. What This Spec Covers

Run this spec when:
- changing `SKILL.md`
- changing motion/style/routing references
- changing visual gate expectations that the skill is supposed to satisfy
- the skill starts repeating styles, overanimating, clipping content, or misrouting page types

This spec validates 4 things:
- **routing**: did the skill choose the right motion mode, style, and stack?
- **build quality**: did it avoid broken layouts and obvious frontend defects?
- **accessibility**: did it preserve keyboard, contrast, motion, and semantic basics?
- **taste consistency**: did it avoid generic AI-web patterns and overdesigned nonsense?

---

## 1b. Cheap-First Validation Strategy

Validation must be tiered. The fast path is the default path.

These Tier 0/1/2 labels are for maintaining this skill itself. They do not replace the standalone visual acceptance review in `visual-acceptance-review.md`. If a generated frontend artifact needs rendered proof, run that review even when this regression Tier 0 passes.

### Tier 0: Routing + obvious-risk check

Run first, always.

Use only:
- 1 prompt
- 1 page type
- 1 expected motion-mode decision
- 1 screenshot set at the minimum useful sizes

Purpose:
- catch wrong page-type routing
- catch obvious anti-patterns fast
- avoid spending tokens on prompts that are likely to fail for simpler reasons

### Tier 1: Core smoke test

Run only if Tier 0 passes.

Use:
- 2 evals max
- one marketing page prompt
- one dashboard/app-shell prompt
- one long-content stress variant total

Purpose:
- catch the historically common failures with minimal token cost

### Tier 2: Extended regression sweep

Run only when:
- `SKILL.md` changed materially
- motion/routing references changed
- accessibility/build rules changed
- Tier 0 or Tier 1 exposed drift

Use:
- the full eval matrix
- multi-breakpoint screenshot review
- motion/reduced-motion checks

### Hard rule

Do **not** start with 6 prompts, 6 screenshots, and long narrative scoring. That is wasteful and usually unnecessary.

---

## 1e. Escalation Triggers (MANDATORY)

Tier selection is not subjective. Use these triggers.

### Tier 0 only allowed when ALL are true

- the change is wording-only or small clarification-only
- no routing logic changed
- no motion guidance changed
- no accessibility rule changed
- no layout/responsive/shell rule changed
- no tool/stack decision changed
- no quality-gate checklist item changed

If any one of those is false, Tier 0 alone is not enough.

### Force Tier 1 when ANY are true

- `SKILL.md` changed in principles, workflow, anti-patterns, or page-type routing
- `references/css-architecture.md` changed
- `references/responsive-sections.md` changed
- `references/visual-styles.md` changed
- a known historical failure mode was addressed
- a mobile/content-length/shell-balance rule changed

Tier 1 is the default for most meaningful skill edits.

### Force Tier 2 when ANY are true

- `references/animation-patterns.md` changed materially
- `references/tool-decision-matrix.md` changed
- motion-mode routing changed
- rendering stack guidance changed (`CSS 3D`, `Rive`, `Spline`, `Three.js`, `Lenis`)
- accessibility target or a11y review rules changed
- the quality gate checklist changed materially
- multiple reference files changed across routing + build + accessibility
- the user reports regressions across multiple page types
- the skill starts reusing the same style or motion language across unrelated prompts

If Tier 2 is required, do not pretend Tier 0 or Tier 1 is sufficient.

### Dashboard safeguard

If the change could plausibly affect:
- app shells
- sidebars
- dense data layouts
- card sizing
- mobile column collapse

then at least one dashboard/app-shell eval is mandatory even if the original change sounded "visual only."

---

## 1c. Sequencing Rules

Validation order matters. Use this exact sequence:

1. **Routing check**
   Verify motion mode, page type fit, and rendering stack choice.
2. **Defect check**
   Look for truncation, dead space, shell drift, mobile column count, and CTA visibility.
3. **Accessibility check**
   Check focus, contrast, keyboard, labels, and reduced motion.
4. **Taste check**
   Only after the page is fundamentally correct.
5. **Extended style variety check**
   Only in Tier 2.

If a page fails at step 1 or 2, stop there. Do not waste more review tokens describing advanced taste problems on a fundamentally broken layout.

---

## 1d. Token and Cost Guardrails

- Default to **short prompts**, not essay prompts.
- Ask for the target page and constraints in one shot; avoid repeated reframing.
- Reuse the same stable eval prompts over time.
- Do not require long natural-language critique before basic pass/fail status is known.
- Prefer checklist output over long prose during validation.
- Prefer one high-signal dashboard eval over three similar landing-page evals.
- Do not invoke a multi-agent or swarm-style validation run unless Tier 2 is genuinely warranted.
- If the first screenshot already shows a hard fail, stop and patch the skill. Do not continue the matrix.

---

## 2. Core Eval Prompt Set

These prompts should remain stable over time so regressions are visible.
Keep them short. Do not elaborate them into long brief documents unless the test specifically requires it.

### Eval 1: SaaS Landing Page

Prompt:
> Design a modern SaaS landing page for an AI meeting assistant used by operations teams. Prioritize conversions, keep it credible, include product screenshots, pricing teaser, social proof, and one premium motion moment.

Expected:
- Motion Mode 1 by default
- no fake cursor, no scroll hijack, no loader intro
- conversion-first structure
- one strong wow moment, not a cinematic takeover

### Eval 2: Dashboard / App Shell

Prompt:
> Design a dashboard for revenue analytics with a left sidebar, top filters, KPI cards, charts, and a recent alerts panel. It should feel premium but remain highly usable and data-dense.

Expected:
- Motion Mode 0 by default
- shell stays centered and balanced
- no stretched equal-height dead cards
- stateful UI polish over scroll theater

### Eval 3: Pricing Page

Prompt:
> Design a pricing page for a B2B workflow tool with three tiers, annual/monthly toggle, FAQ, and a strong enterprise CTA. It should feel modern and trustworthy.

Expected:
- Mode 1 or restrained Mode 0/1 hybrid
- pricing clarity beats decoration
- contrast and hierarchy are strong
- no gimmicky 3D or novelty interaction unless clearly justified

### Eval 4: Editorial / Storytelling Page

Prompt:
> Design an editorial product story page for a premium audio brand. Use immersive visuals and scrolling narrative, but keep reading comfortable and elegant.

Expected:
- Motion Mode 1 or 2
- layered composition and pacing
- readable long-form text
- no text fighting active backgrounds

### Eval 5: Campaign / Portfolio Page

Prompt:
> Design a launch microsite for an experimental motion design studio. The site itself should feel like part of the portfolio and can be visually ambitious.

Expected:
- Motion Mode 2 or 3
- stronger wow system allowed
- stack choice justified if using Spline/Three.js
- still no pointless friction or inaccessible behavior

### Eval 6: Mobile-First Presentation Page

Prompt:
> Design a mobile-first scroll-through presentation page explaining a startup partnership proposal. One idea per section, very easy to consume on a phone.

Expected:
- single-column mobile-first presentation structure
- CTA and narrative readable at `360x668`
- no multi-column mobile cards
- no clipped copy or overpacked sections
- natural scroll unless the presentation is intentionally low-content and slide-like

---

## 3. Negative Stress Variants

For each core eval, rerun with at least one of these stressors:

- **Long heading**: 2-3x normal heading length
- **Long paragraph**: 2-3x normal narrative length
- **Long label/badge**: awkwardly long plan names, filters, tags, or badges
- **Populated cards**: every card filled with realistic data
- **Dense shell**: sidebar + topbar + cards + chart + table
- **Reduced motion**: explicitly request motion-safe version
- **Narrow mobile**: assume `360x668`
- **Premium typography**: ask for Apple-clean or luxury fashion typography without letting it become a novelty/game font
- **Snap temptation**: include both short sections and one long/pricing/form section to ensure snap is not applied globally

Purpose:
- expose truncation
- expose dead space
- expose shell misalignment
- expose mobile overflow
- expose hover-only interactions
- expose cheap type choices
- expose wrong scroll-snap routing

Use only **one** stress variant in Tier 1. Save full stress coverage for Tier 2.

---

## 4. Routing Checks

Each eval must be judged on these routing decisions before judging style quality.

### Motion Mode

- Dashboard/app shell should default to **Mode 0**
- SaaS/product marketing should usually default to **Mode 1**
- Editorial/storytelling may use **Mode 1 or 2**
- Campaign/portfolio can escalate to **Mode 2**
- Mode 3 should be rare and deliberate

### Rendering Stack

- CSS/CSS 3D should be preferred before Spline/Three.js
- Rive should be chosen for stateful interactive illustration, not generic hero flair
- Three.js should only appear when procedural 3D or custom choreography is genuinely central
- Lenis should not appear on snap pages or most dashboards
- Scroll snap should appear only on low-content slide/deck/product-showcase experiences, never ordinary dashboards, pricing, forms, blogs, SEO pages, or variable-height sections

### Style Branch

- Tactile/warm direction should be available when the brief calls for human/crafted tone
- Sci-fi/glass-heavy direction should not be the default for every project
- Apple-clean and luxury restraint should be available without falling into video-game, sci-fi, novelty, or chunky type

---

## 5. Pass / Fail Rubric

Every eval should be scored against these categories.

### A. Layout Integrity

Fail if any of these appear:
- clipped or line-clamped meaningful copy
- giant empty gutters
- lopsided page occupancy
- sidebar or shell pushes main content off-center
- equal-height card stretching creates obvious dead space
- multi-column mobile card sections below `768px`

### B. Accessibility

Fail if any of these appear:
- contrast clearly below WCAG 2.2 AA expectations
- invisible or missing focus styles
- hover-only access to important information
- tiny tap targets
- icon-only controls without accessible names
- motion required to understand content or task flow

### C. Motion Discipline

Fail if any of these appear:
- wrong motion mode for the page type
- only fade-up everywhere
- fake custom cursor
- scroll hijacking on an ordinary business page
- forced intro/loader before content
- 3D/WebGL chosen without clear payoff

### D. Taste / Originality

Fail if any of these appear:
- Inter/Roboto/Arial fallback default vibe without inherited/native/dense-UI rationale
- cheap novelty, sci-fi, video-game, comic, or chunky font on a serious premium product
- purple-on-white AI-template look
- same style reused across unrelated prompts
- generic hero copy and evenly spaced template cards
- too many simultaneous wow systems
- no project-specific design story or visual metaphor
- weak borders, missing section separation, no texture, no glow/sheen on a dark/luminous premium surface

### E. Conversion / Clarity

Fail if any of these appear:
- CTA buried or weak
- decorative hero but unclear offer
- business page treated like an art-school microsite
- design beauty comes at the expense of scannability

---

## 5b. Fast Fail Checklist

Use this before any extended scoring. If any item is "yes", the eval already failed.

- Is the motion mode obviously wrong for the page type?
- Is meaningful text clipped or hidden?
- Is there obvious dead space or shell misalignment?
- Are mobile card sections still multi-column?
- Is the CTA hidden, weak, or off-screen?
- Is there an obvious WCAG miss: unreadable contrast, no focus, tiny targets, hover-only UI?
- Is there a banned gimmick: fake cursor, scroll hijack, forced loader intro?
- Does the type feel cheap/novelty/game-like for a premium or serious product?
- Is scroll snap applied where natural scroll would clearly be better?

If yes to any: stop, patch, rerun.

---

## 6. Screenshot Review Matrix

### Tier 0 minimum

- `1280x800`
- `360x668`

### Tier 1 standard

- `1280x800`
- `360x668`
- one scrolled state

### Tier 2 full

- `1280x800`
- `768x1024`
- `360x668`
- one scrolled state

For app/dashboard evals also inspect:
- filled data state
- sidebar expanded/collapsed if applicable

For motion-heavy evals also inspect:
- reduced-motion state
- mobile fallback state

Only run the Tier 2 matrix when the change risk justifies it.

---

## 7. Regression Questions To Answer

After each eval, answer:

1. Did the skill choose the correct motion mode?
2. Did it choose the lightest viable rendering stack?
3. Did it avoid the known visual defects: truncation, dead space, shell drift?
4. Did it preserve WCAG 2.2 AA basics in the rendered result?
5. Did it avoid generic AI-web tropes?
6. Did it produce a page type-appropriate level of spectacle?

Use terse answers during routine validation:
- `PASS`
- `FAIL: routing`
- `FAIL: layout`
- `FAIL: accessibility`
- `FAIL: taste`

If any answer is "no," update the skill instructions, not just the generated page.

---

## 8. Known Historical Failure Modes

These are specific regressions this skill should never reintroduce:

- dashboard content shoved right by shell/sidebar math
- line-clamped narrative copy inside large cards
- equal-height card systems creating empty lower halves
- giant empty right-side or bottom-side gutters
- motion-rich treatment applied to layouts that should be mostly static
- screenshot review present but no actual visual quality enforcement
- accessibility implied but not explicitly checked

---

## 9. Upgrade Rule

When the skill is patched:
### Low-risk text tweaks

- rerun Tier 0 only

### Medium-risk skill changes

- rerun Tier 1
- include 1 dashboard/app-shell eval
- include 1 marketing or editorial eval
- include 1 long-content or narrow-mobile stress variant

### High-risk routing / motion / accessibility changes

- run Tier 2
- include dashboard/app-shell
- include mobile-first/narrow-mobile
- include long-content stress
- include reduced-motion review

Do not treat the skill as validated just because one flashy landing page looked good.

---

## 10. Minimum Eval Recipes By Tier

Use these exact minimum recipes unless a higher-risk change requires more.

### Tier 0 recipe

- 1 eval only
- choose the page type most directly affected by the change
- 2 screenshots: `1280x800`, `360x668`
- output format: checklist only

### Tier 1 recipe

- 2 evals only:
  - 1 dashboard/app-shell eval
  - 1 marketing/editorial/pricing eval matched to the changed area
- 1 stress variant total
- 3 screenshots max per eval:
  - `1280x800`
  - `360x668`
  - one scrolled state if needed
- output format:
  - `PASS` or `FAIL:<category>`
  - one-sentence reason only

### Tier 2 recipe

- 3-4 evals max, not the entire prompt library unless there is active drift
- must include:
  - 1 dashboard/app-shell eval
  - 1 long-content or dense-data stress eval
  - 1 mobile-first or narrow-mobile eval
  - 1 motion-heavy or routing-sensitive eval if motion/routing changed
- use reduced-motion review only when motion/a11y changes warrant it
- output format:
  - checklist first
  - short findings second

The point of Tier 2 is broader confidence, not unlimited exploration.
