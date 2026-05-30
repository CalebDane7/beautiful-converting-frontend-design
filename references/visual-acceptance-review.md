# Visual Acceptance Review

Use this for any non-trivial browser-visible frontend work. This is the skill's standalone testing gate and does not depend on any outside runtime.

The core rule: self-review is not "I looked at it." Self-review means the rendered output was checked against an explicit acceptance contract, with real evidence and a pass/fail decision.

---

## 1. Visual Acceptance Contract

Before implementation, define what the page or component must prove visually. Keep it short, but make it concrete.

```json
{
  "surface_type": "marketing_page | app_shell | dashboard | pricing | editorial | campaign | prototype",
  "audience": "who this is for",
  "audience_context": "awareness stage, device/context, sophistication, skepticism",
  "design_story": "the belief or product story the visuals should create",
  "primary_action": "what the user should do next",
  "motion_mode": "0 | 1 | 2 | 3",
  "rendering_stack": ["CSS", "GSAP", "Canvas2D"],
  "required_viewports": ["1280x800", "768x1024", "360x668"],
  "required_sections": ["hero", "proof", "pricing", "final_cta"],
  "required_states": ["initial", "scrolled", "hover_or_focus", "mobile"],
  "expected_visible_objects": [
    {"id": "hero_offer", "label": "specific offer headline", "required": true}
  ],
  "forbidden_visual_failures": [
    {"id": "mobile_two_column_cards", "label": "mobile card section renders in two columns", "must_be_absent": true}
  ],
  "interaction_states": [
    {"name": "primary_cta_focus", "must_see": ["visible focus ring"], "must_not_see": ["layout shift"]}
  ],
  "required_visual_dimensions": [
    "contrast_separation",
    "hierarchy",
    "symmetry_balance",
    "space_usage",
    "overlap_occlusion",
    "premium_craft",
    "conversion_clarity",
    "originality",
    "material_craft",
    "accessibility_basics",
    "performance_risk"
  ],
  "requires_3d_scene_review": false,
  "requires_motion_temporal_review": true
}
```

This contract is not paperwork. It is the standard the output must pass.

---

## 2. Evidence To Collect

For browser-visible work, collect evidence from a real render:

- screenshots at every required viewport
- one scrolled state for pages with below-fold content
- hover/focus/click/open state for meaningful interactive elements
- console/runtime error status
- reduced-motion state when motion is central
- mobile state at `360x668`
- 3D/canvas pixel or screenshot checks when the primary experience is canvas/WebGL

Code inspection can support the review, but it cannot replace rendered evidence for layout, contrast, overlap, text fit, motion, or mobile correctness.

---

## 3. Semantic Review Shape

After evidence is collected, write a terse structured review:

```json
{
  "inspected": true,
  "overall_verdict": "PASS | FAIL",
  "request_match": [
    {
      "element": "desktop hero offer",
      "expected": "Specific dream outcome and primary CTA visible above the fold",
      "observed": "Headline and CTA are visible at 1280x800 with clear contrast",
      "pass": true
    }
  ],
  "quality_checks": {
    "contrast_separation": {"pass": true, "detail": "Body text and controls remain readable over actual backgrounds."},
    "hierarchy": {"pass": true, "detail": "One dominant focal point per section."},
    "symmetry_balance": {"pass": true, "detail": "Main content is balanced within the shell/frame."},
    "space_usage": {"pass": true, "detail": "No stretched cards, dead gutters, or accidental empty regions."},
    "overlap_occlusion": {"pass": true, "detail": "No incoherent overlap across breakpoints."},
    "premium_craft": {"pass": true, "detail": "Depth, lighting, borders, and typography feel intentional."},
    "conversion_clarity": {"pass": true, "detail": "Primary action and value are clear without scrolling."},
    "originality": {"pass": true, "detail": "Visual idea follows this project's story rather than copying a trend."},
    "material_craft": {"pass": true, "detail": "Borders, outlines, texture, glow, and section separation are visible where the surface needs them."},
    "accessibility_basics": {"pass": true, "detail": "Keyboard, focus, labels, contrast, and target sizes are acceptable."},
    "performance_risk": {"pass": true, "detail": "No unnecessary heavy scripts or motion for the selected mode."},
    "improvements": {"pass": true, "detail": "No blocking visual improvements remain."}
  }
}
```

The review must say what was observed. Generic pass text such as "looks good" or "matches design" is not evidence.

---

## 4. Required Quality Dimensions

### Layout Safety

Run this before taste review. Any failure here means the design is not done.

Minimum viewports:
- desktop: `1280x800`
- tablet: `768x1024` when the layout has multi-column sections or sidebars
- mobile: `360x668`

Fail if:
- text exits its parent box
- long words, prices, badges, filters, buttons, or nav labels break through borders
- cards/boxes/components overlap accidentally
- a card grid stays multi-column on narrow mobile
- hover/focus/loading changes resize the surrounding layout
- fixed-format elements such as boards, toolbars, counters, tiles, and charts lack stable dimensions
- sticky headers, bottom bars, or safe-area insets cover content or controls

CSS defaults that prevent common failures:

```css
.ui-card,
.ui-button,
.ui-badge,
.ui-panel {
  min-width: 0;
  max-width: 100%;
}

.ui-card :where(p, li, .ui-label, .ui-value),
.ui-button,
.ui-badge {
  overflow-wrap: anywhere;
}

.card-grid {
  display: grid;
  grid-template-columns: 1fr;
  align-items: start;
  gap: var(--space-lg);
}

@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  }
}
```

Use `overflow-wrap: anywhere` selectively for compact UI labels/badges/buttons. Do not use it on display headings if it creates ugly letter-by-letter breaks; adjust the layout or type scale instead.

### Layout

Fail if:
- meaningful text is clipped, hidden, line-clamped, or unreadable
- mobile cards remain multi-column below `768px`
- app-shell content is pushed off-center
- equal-height cards create obvious dead space
- a CTA is hidden or visually weak
- text or controls overlap incoherently

### Accessibility

Fail if:
- contrast is visibly weak in the rendered state
- focus styles are missing or obscured
- important information is hover-only
- icon-only buttons lack names
- primary targets are too small on mobile
- motion is required to understand the UI

### Motion

Fail if:
- motion mode is wrong for the surface type
- every section uses the same fade-up treatment
- scroll is hijacked on a normal business page
- a fake cursor replaces native cursor behavior
- content is hidden during delayed entrance animations
- reduced-motion has no workable path

### Premium Craft

Fail if:
- the design reads as generic AI template work
- the page uses the same purple/blue glass look without brand reason
- there is no intentional depth, texture, lighting, or material logic
- typography is generic or mismatched to the brand
- serious/premium work uses cheap novelty or video-game-like fonts
- section boundaries, card edges, and important surfaces lack clear separation
- dark/luminous premium surfaces have no controlled glow, sheen, rim light, or focal illumination
- visual novelty hurts usability or conversion

### Originality

Fail if:
- the page feels copied from a trend/reference instead of derived from the product story
- the visual metaphor could belong to any product in the category
- the design ignores the project's actual assets, workflow, audience language, or proof
- the chosen style is merely "premium SaaS" without a specific point of view

### Conversion

Fail if:
- the offer is unclear
- the primary action is not obvious
- proof is fake, vague, or unsupported
- decorative sections do not advance the user's decision
- the page is beautiful but the user cannot tell what to do

---

## 5. 3D / Canvas Review

When WebGL, Three.js, R3F, Spline, or Canvas is central, add checks for:

- scene is nonblank
- primary object is visible and framed
- foreground/background layers have real separation
- camera movement or interaction works
- texture/image quality is acceptable
- mobile fallback preserves the experience instead of replacing it with a different product
- reduced-motion still shows the scene in a usable static state

---

## 6. Fix Loop

If any review item fails:

1. Patch the smallest cause.
2. Re-render the affected viewport/state.
3. Update the semantic review.
4. Repeat until the verdict is `PASS`.

Do not deliver a frontend artifact while the acceptance contract has unresolved failures.
