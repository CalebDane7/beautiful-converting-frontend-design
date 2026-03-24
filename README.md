# Beautiful Converting Frontend Design

A Claude Code skill that produces premium, conversion-optimized frontend interfaces. Every output fuses Hormozi conversion architecture with GSAP/Lenis/ScrollTrigger animations, OSMO-level techniques, and cutting-edge visual design.

**This is not a template generator.** It's an opinionated design system that enforces quality through a mandatory 12-point gate — no generic output ever reaches the user.

## Copyright

Copyright (c) 2026 Caleb Dane. All rights reserved.

## What It Does

Give it a brief ("build a landing page for X") and it produces complete, production-ready HTML + CSS + JS with:

- Distinctive typography (never Inter/Roboto/Arial)
- Scroll-triggered GSAP animations on every section
- Lenis smooth scrolling
- Conversion-optimized page architecture
- Zero inline CSS — everything in classes and variables
- PageSpeed 90+ performance targets
- Accessibility baked in (`prefers-reduced-motion`, semantic HTML, focus indicators)

## What's Included

```
SKILL.md                              # Core skill definition (300+ lines)
references/
  design-system-generator.md          # Design tokens, fonts, colors, spacing
  css-architecture.md                 # CSS structure, glassmorphism, backgrounds
  animation-patterns.md               # GSAP, ScrollTrigger, Lenis, Three.js, Canvas
  osmo-techniques.md                  # 9 categories of Awwwards-quality animations
  conversion-framework.md             # Hormozi value equation, 9-section page flow
  performance.md                      # Core Web Vitals, critical rendering path
  visual-styles.md                    # Premium visual styles (NEW)
  tool-decision-matrix.md             # When to use Stitch, 21st.dev, uipro-cli
scripts/
  google_stitch.py                    # Google Stitch CLI wrapper
  twenty_first.py                     # 21st.dev component library CLI
```

## 4 Conversion Styles

| Style | Use For | Approach |
|-------|---------|----------|
| **Hormozi/ClickFunnels** (default) | SaaS, lead gen, product launches, SMB | Dream outcome headlines, value stacking, 9-section flow |
| **Brand/Aspirational** | Luxury, fashion, hardware, beauty | Product as hero, minimal copy, 5-section flow |
| **Editorial/Technical** | Dev tools, B2B, APIs | Long-form storytelling, technical precision |
| **Community/Social** | Platforms, marketplaces | User-generated proof, social validation |

## 6 Visual Styles (references/visual-styles.md)

Copy-paste CSS/JS recipes for premium design techniques:

| Style | Best For | Key Technique |
|-------|----------|---------------|
| **Neumorphism** | Wellness, fintech, utility apps | Soft dual box-shadows, no backdrop-filter |
| **Glitch Effects** | Tech, gaming, streetwear, crypto | RGB channel split, clip-path slicing |
| **Brutalist Typography** | Fashion, music, editorial | 15vw+ headings, rotated/overlapping text |
| **3D Product Integration** | E-commerce, hardware, beauty | Spline embeds, Three.js GLTF viewers |
| **Product-as-Hero** | Beauty, food, consumer electronics | Product fills 60%+ viewport |
| **Luxury Dark** | Fashion houses, premium brands | Near-black + selective warm glow |

## 7 Design Principles

1. **Premium by Default** — distinctive fonts, depth through glass/grain/gradients
2. **Conversion-Aware** — every visual decision has a conversion implication
3. **Motion-Rich** — GSAP scroll-triggered animation on every section
4. **Distinctive** — if it could belong to any brand, it belongs to none
5. **Restrained** — fewer elements, more impact; 60-30-10 color ratio
6. **Zero Inline CSS** — everything in classes and CSS variables
7. **Fast** — PageSpeed 90+, LCP < 2.5s, only animate transform/opacity

## 12-Point Quality Gate

Every output must pass ALL 12 before delivery:

- [ ] **FONT** — distinctive, recognizable
- [ ] **COLOR** — unexpected palette
- [ ] **THEME** — intentional dark/light/custom choice
- [ ] **GSAP** — every section animated
- [ ] **LENIS** — smooth scroll initialized
- [ ] **CONVERSION** — follows chosen style
- [ ] **COPY** — clear, specific, no hedging
- [ ] **CTA** — above fold, highest contrast
- [ ] **DEPTH** — 2+ visual layers
- [ ] **WOW** — at least one Awwwards-worthy moment
- [ ] **AI-SMELL** — would someone detect AI? If yes, fix
- [ ] **A11Y** — reduced-motion, focus indicators, semantic HTML

## 19 Anti-Patterns

Things this skill will never do:

1. Use Inter/Roboto/Arial
2. Purple gradient on white
3. Glass on every element
4. Static flat backgrounds
5. Even color distribution
6. Pure black (#000)
7. Animations everywhere without rhythm
8. Stock photos
9. Vague copy
10. CTA buried below fold
11. Ignore mobile performance
12. Same fonts every project
13. Inline CSS
14. Render-blocking JS
15. Center everything
16. Uniform card grids
17. Generic hero text
18. No reduced-motion respect
19. Same visual style every project

## Animation Stack

Every project includes (via CDN, deferred):

- **Lenis** — smooth scroll with GSAP sync
- **GSAP + ScrollTrigger** — scroll-triggered reveals, parallax, counters
- **SplitType** — character/word-level text animations
- **BarbaJS** — page transitions (multi-page only)

## Optional Tool Integrations

| Tool | Purpose |
|------|---------|
| Google Stitch | Layout inspiration + visual prototyping |
| 21st.dev | Pre-built component library |
| uipro-cli | Industry-specific design tokens |

The skill produces excellent output with zero external tools. These are enhancements only.

## Usage

This is a [Claude Code](https://claude.com/claude-code) skill. Place the directory in `~/.claude/skills/` and invoke it when building frontend interfaces.

```
~/.claude/skills/beautiful-converting-frontend-design/
```

Claude Code will automatically load the skill when frontend design work is detected, or you can invoke it directly.

## License

Copyright (c) 2026 Caleb Dane. All rights reserved.

This software is proprietary. No permission is granted to copy, modify, distribute, or use this software without explicit written consent from the copyright holder.
