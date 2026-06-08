# Beautiful Converting Frontend Design

Build frontend work that looks expensive, converts clearly, and survives real
browser proof.

This Claude Code skill turns a rough frontend brief into a context-matched
visual direction, conversion-aware page structure, premium typography, tactile
controls, responsive layouts, and a mandatory acceptance gate. It is built for
agents that usually make one of two mistakes: ship a generic template, or add
visual effects that make the page harder to use.

The skill prevents both.

## What It Does

- Audits the product, audience, flow, assets, copy, and existing UI before
  choosing a visual direction.
- Challenges the brief when the requested surface, layout, or motion choice
  would weaken clarity or conversion.
- Builds around a design story, not a copied trend or one-size-fits-all palette.
- Uses Hormozi-style conversion structure when the page needs to sell, but keeps
  operational tools quiet, dense, and usable.
- Chooses GSAP, Lenis, ScrollTrigger, WebGL, scroll snap, and cinematic effects
  only when they serve the surface.
- Enforces premium craft: visible section separation, stronger borders, material
  depth, texture, glow, refined type, and local text contrast.
- Adds real tactile depth to primary CTAs and key buttons instead of flat
  rectangles with a color-change hover.
- Requires rendered visual proof across desktop and mobile before the work is
  considered done.

## Why It Is Different

Most frontend-design skills optimize for a look. This one optimizes for the
decision the user needs to make.

The original approach was useful, but too deterministic: heavy motion by
default, GSAP/Lenis as a habit, and broad premium styling rules that could make
very different products feel similar. This version is stricter where quality
matters and freer where taste matters.

### Improvements Over The Original

| Improvement | Why It Matters |
|-------------|----------------|
| Audience-first workflow | The agent designs for the buyer, user, device, and context instead of starting with effects. |
| Challenge pass | The agent must question weak briefs before building the wrong thing beautifully. |
| Situational motion router | GSAP, Lenis, snap, WebGL, and rich animation are choices, not defaults. |
| Design-story requirement | The visual system has to express the product's real mechanism, not a trend moodboard. |
| Stronger material craft | Borders, outlines, section bands, texture, glow, and depth stop premium pages from feeling flat. |
| Premium typography rules | Fonts are selected by market, price point, density, and brand maturity instead of lazy defaults. |
| Local contrast rule | Text must be readable against the surface directly behind it, not merely on a dark page. |
| Tactile button system | Primary actions get real 3D edges, hover lift, specular sheen, and fast press feedback where appropriate. |
| Mobile and layout safety | Text, buttons, cards, badges, grids, and fixed-format UI must fit at real mobile widths. |
| Visual acceptance contract | Screenshots and rendered proof are part of the gate, not optional polish. |

## Best Use Cases

- SaaS landing pages and product pages that need conversion clarity.
- Premium brand, music, fashion, creator, and campaign surfaces that need a
  distinctive visual identity.
- Startup homepages that need the offer understood in five seconds.
- In-app onboarding, upgrade, or tool surfaces where usability and polish both
  matter.
- Existing frontend work that looks flat, generic, low-contrast, or AI-made.

## What Is Included

```text
SKILL.md
references/
  conversion-framework.md
  design-system-generator.md
  css-architecture.md
  responsive-sections.md
  premium-frontend-quality-spec.md
  premium-typography.md
  premium-buttons.md
  scene-plate-playbook.md
  visual-acceptance-review.md
  skill-regression-spec.md
  animation-patterns.md
  osmo-techniques.md
  performance.md
  visual-styles.md
  tool-decision-matrix.md
  3d-spatial-depth.md
  image-to-3d-environment-workflow.md
  pdf-deck-playbook.md
scripts/
  google_stitch.py
  twenty_first.py
```

## The Quality Gate

Before delivery, the agent must prove:

- The page has a clear primary action and hierarchy.
- The visual direction fits the audience and product.
- Typography and palette are deliberate, not defaults.
- Primary CTAs and key controls have the right depth and states for the surface.
- Text remains readable through local contrast, scrims, plates, or shadows.
- Layouts hold up on mobile and desktop without overflow or accidental overlap.
- Motion helps comprehension, trust, desire, or feedback.
- Accessibility is covered with semantic controls, visible focus, reduced
  motion, and touch target safety.
- Rendered screenshots confirm the result instead of relying on code inspection.

## Install

Clone or copy this directory into your Claude skills folder:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/CalebDane7/beautiful-converting-frontend-design.git \
  ~/.claude/skills/beautiful-converting-frontend-design
```

Claude Code can load the skill automatically when frontend design work is
detected, or you can invoke it directly by name:

```text
Use the beautiful-converting-frontend-design skill to redesign this page.
```

## Mantis Distribution

This skill is also packaged into the Hybrid Mantis runtime bundle, so Mantis
users receive the same current snapshot through the protected bundle update
lane.

Maintainer release flow:

```bash
git push origin main
/home/cabule/.ai-controller-repo/install/maintainer-publish-bundle.sh \
  --repo-dir /home/cabule/.ai-controller-repo --force
mantis update --auto
mantis doctor
```

## License

Copyright (c) 2026 Caleb Dane. All rights reserved.

This software is proprietary. No permission is granted to copy, modify,
distribute, or use this software without explicit written consent from the
copyright holder.
