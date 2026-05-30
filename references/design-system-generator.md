# Design System Generator Reference

Loaded during Phase 2 (Design System). Use this to generate CSS variables, select fonts, and build palettes.

---

## 0. Persistent Design System Layer

For non-trivial, multi-page, branded, or app-shell work, create or update a persistent design-system artifact before styling implementation.

Preferred file: `DESIGN.md` in the project root or nearest design/docs folder.

Use it to freeze:

- brand/user context and surface type
- project audit notes and design story
- typography choices and fallback policy
- color tokens and semantic roles
- spacing, radius, elevation, z-index, and motion tokens
- border/outline, texture, glow, sheen, and material-craft rules
- component recipes for nav, buttons, cards, forms, shells, modals, charts, and empty states
- responsive rules and safe-area behavior
- do/don't guardrails for this brand
- screenshot/proof contract links for important surfaces

Do not re-solve the visual identity on every page. For multi-page sites, also maintain a short site continuity note such as `.design/SITE.md` or `.design/next-prompt.md` when the project already uses a `.design/` folder.

### DESIGN.md starter

```md
# Design System

## Context
- Product:
- Existing assets/flows audited:
- Audience:
- Surface type:
- Conversion/action:
- Design story:
- Tone:

## Tokens
- Display font and rationale:
- Body/UI font and rationale:
- Background:
- Surface:
- Text:
- Primary action/accent:
- Secondary/state accents:
- Border/outline:
- Texture:
- Glow/sheen:
- Radius:
- Shadow/elevation:
- Motion:

## Component Rules
- Navigation:
- Buttons:
- Cards:
- Forms:
- Data/charts:
- Loading/empty/error:

## Responsive Rules
- Mobile first:
- Safe area:
- Touch targets:
- Content-length stress:

## Do / Don't
- Do:
- Don't:
- Rejected defaults:

## Proof Contract
- Required viewports:
- Required states:
- Expected visible objects:
- Forbidden failures:
```

---

## 0b. Candidate Search Protocol

Do not invent the visual system from memory when the project deserves better.

1. Audit the project: existing screens, assets, logo, copy, audience, workflow, proof, and emotional promise.
2. Search the upstream UI/UX data for candidate palettes and font pairs:
   - colors: `upstream/ui-ux-pro-max/cli/assets/data/colors.csv`
   - typography: `upstream/ui-ux-pro-max/src/ui-ux-pro-max/data/typography.csv`
   - broader style profiles: `upstream/ui-ux-pro-max/src/ui-ux-pro-max/data/design.csv`
3. Pick 2-3 plausible candidates, then choose one direction and explain why.
4. Adapt the chosen candidate to the product. Do not copy a generic SaaS palette or font pair unchanged.
5. Record rejected defaults in `DESIGN.md` so the next pass does not drift back to cheap-looking habits.

Useful commands:

```bash
rg -n "luxury|fashion|premium|editorial|apple|saas|finance|wellness|developer|brutalist" upstream/ui-ux-pro-max/cli/assets/data/colors.csv upstream/ui-ux-pro-max/src/ui-ux-pro-max/data/typography.csv
```

---

## CSS Variables Template (Universal — adapts to dark/light/custom)

The values below are a token schema, not a brand identity. Replace fonts, accents, radii, borders, glow, texture, and material treatments with project-specific choices. Do not ship this template unchanged.

```css
:root {
  /* === BACKGROUND LAYERS — replace from chosen palette === */
  --bg-primary: #0b0b0c;
  --bg-secondary: #151518;
  --bg-tertiary: #202027;
  --bg-card: rgba(255,255,255,0.055);

  /* === TEXT HIERARCHY === */
  --text-primary: #EDEDED;       /* 93% white — less strain than pure */
  --text-secondary: rgba(255,255,255,0.7);
  --text-muted: rgba(255,255,255,0.4);

  /* === ACCENT SYSTEM — replace from chosen palette === */
  --accent-primary: #f4c76b;     /* Primary action / hero highlight */
  --accent-secondary: #7aa7ff;   /* Supporting accent or active state */
  --accent-tertiary: #ff6b6b;    /* Warning/destructive/emphasis */

  /* === FUNCTIONAL === */
  --glow-primary: 0 0 36px rgba(244,199,107,0.28);
  --glow-secondary: 0 0 32px rgba(122,167,255,0.18);
  --gradient-text: linear-gradient(135deg, #f8f8f4, var(--accent-primary), #9f8f72);
  --gradient-button: linear-gradient(135deg, var(--accent-primary), #d99f39);

  /* === GLASS === */
  --glass-bg: rgba(255,255,255,0.055);
  --glass-border: rgba(255,255,255,0.16);
  --glass-blur: blur(12px) saturate(140%);

  /* === MATERIAL CRAFT === */
  --border-subtle: rgba(255,255,255,0.14);
  --border-strong: rgba(255,255,255,0.34);
  --outline-glow: 0 0 0 1px var(--border-strong), 0 0 30px rgba(244,199,107,0.16);
  --texture-opacity: 0.045;

  /* === TYPOGRAPHY === */
  --font-display: 'Futura PT', 'Avenir Next', 'Helvetica Neue', sans-serif;
  --font-body: 'SF Pro Text', 'Avenir Next', 'Helvetica Neue', sans-serif;
  --font-code: 'Geist Mono', monospace;
  --fs-hero: 4.5rem;
  --fs-h1: 3rem;
  --fs-h2: 2rem;
  --fs-h3: 1.35rem;
  --fs-body: 1rem;
  --fs-small: 0.875rem;
  --lh-body: 1.6;
  --lh-heading: 1.1;
  --ls-heading: 0;

  /* === SPACING (8px grid) === */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 4rem;
  --section-padding: clamp(4rem, 8vw, 8rem) clamp(1.5rem, 4vw, 4rem);
  --container-max: 1100px;

  /* === EFFECTS === */
  --transition-fast: 0.2s cubic-bezier(0.22, 1, 0.36, 1);
  --transition-base: 0.3s cubic-bezier(0.22, 1, 0.36, 1);
  --transition-slow: 0.5s cubic-bezier(0.22, 1, 0.36, 1);
  --radius-sm: 8px;
  --radius-md: 8px;
  --radius-lg: 8px;
  --radius-pill: 9999px;

  /* === LAYERS === */
  --z-base: 0;
  --z-raised: 10;
  --z-sticky: 100;
  --z-overlay: 1000;
  --z-modal: 1100;
  --z-toast: 1200;

  /* === SHADOWS === */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.2);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.3);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.4);

  /* === CURSOR GRADIENT === */
  --mouse-x: 50%;
  --mouse-y: 50%;
  --cursor-glow-color: rgba(244, 199, 107, 0.10);
  --cursor-glow-size: 1200px;
}

@media (max-width: 768px) {
  :root {
    --fs-hero: 2.75rem;
    --fs-h1: 2.25rem;
    --fs-h2: 1.65rem;
    --fs-h3: 1.2rem;
  }
}
```

---

## Palette Construction Rules

- 60% background, 30% secondary/text, 10% accent
- Never distribute evenly — dominant with sharp accents
- Brand color at 1-10% lightness for subtle backgrounds
- Complementary for max attention when it fits the brand; avoid reflex purple/cyan
- Temperature contrast: Cool bg + warm CTA = instant hierarchy
- Every palette needs semantic roles: background, surface, text, muted text, CTA, secondary accent, border/outline, focus, success, warning/destructive
- Contrast must be strong in the actual rendered state, including surface-vs-surface and section-vs-section separation
- Expressive/premium sections should normally have visible border/outline or material transition between sections

---

## Font Selection by Tone

| Tone | Display Font | Body Font | Monospace |
|------|-------------|-----------|-----------|
| Apple-clean product | SF Pro, Avenir Next, Neue Haas Grotesk, Helvetica Now, Satoshi | Same family or clean UI companion | SF Mono, Berkeley Mono, JetBrains Mono |
| Luxury / LV restraint | Futura PT, Avenir Next, Optima, Neue Haas Grotesk | Avenir Next, Suisse/General Sans style | Berkeley Mono sparingly |
| Luxury editorial | Canela, Didot, Bodoni 72, Cormorant Garamond, Playfair Display | Neue Haas/General Sans/Optima style | Berkeley Mono |
| Tech/SaaS premium | Geist, Satoshi, Suisse/General Sans style, Instrument Sans | Same or paired lighter weight | Geist Mono, JetBrains Mono |
| Editorial | Newsreader, Source Serif 4, Lora, Fraunces | Source Sans 3, Noto Sans | Source Code Pro |
| Brutalist / culture | Archivo Black, Bebas Neue, Oswald, Druk-style condensed | IBM Plex Sans/Mono, Space Mono | Same |
| Playful only when appropriate | Bricolage Grotesque, Rubik, Nunito | Same at lighter weight | Fira Code |

Avoid video-game, sci-fi, chunky, novelty, comic, or overly rounded fonts unless the product is actually a game/toy/youth entertainment surface.

Inter, Roboto, Arial, system fonts, Open Sans, Lato, and Montserrat are not lazy defaults. Use them only when inherited from an existing design system, required for native platform fidelity, or clearly best for dense operational UI.

---

## Typography Rules

- Line height: 1.5 body, 1.1 headings, 1.75 long-form
- Letter spacing: 0 headings, 0 body
- Font weight: 800 headlines, 400-500 body, 700 emphasis
- Max width: 700px body text (45-75 chars)
- Container: 1100px layouts, 800px content-focused
- Premium clean typography often uses restraint: fewer weights, more precise spacing, stronger hierarchy, and better optical sizing rather than decorative type.
- Display fonts must be tested on mobile for ugly wraps and cheap all-caps density.

---

## Dark Theme Rules

1. Never #000000 — use #050508
2. Elevation = lightness (each layer lighter)
3. Reduce white text opacity (93% primary, 70% secondary, 40% muted)
4. Borders must be visible. Dark-on-dark cards need `1px` to `2px` outlines plus occasional stronger section dividers.
5. Glow > shadow for primary emphasis, active states, hero objects, and luminous premium text.
6. Gradient/sheens are for display headings and major numbers only; body text stays solid.
7. Texture/grain should be subtle but present when the surface otherwise reads flat.

---

## Light Theme Rules

1. Warm whites (#FAFAFA, #F5F5F0) not pure #FFFFFF backgrounds
2. Depth through shadows, not color (multi-layer shadows)
3. Colored accents on neutral — editorial feel
4. Dark text (#1a1a1a or #0F172A) on light, not pure #000
5. Borders (#D8DEE8 / warm neutral equivalents) define cards and sections; use thicker or darker outlines on hero/pricing/proof blocks when separation is weak.
6. Glow must be restrained on light themes: use soft colored halos, focus rings, and luminous button edges rather than neon bloom.

---

## Industry-Specific Profiles

| Industry | Font Pair | Palette | Glass | Vibe |
|----------|-----------|---------|-------|------|
| SaaS/Tech | Geist/Satoshi/SF-like + Mono | Brand-led, not reflex purple/teal | Nav or hero only | Linear-clean |
| Luxury/Fashion | Futura/Avenir/Didot/Canela-style + clean sans | Warm darks, ivory, brass, deep neutrals | Minimal (0-2) | Editorial-premium |
| Healthcare | Source Serif + Noto Sans | Light + blue/green | None | Trust-clean |
| Creative Agency | Bricolage/Syne + disciplined sans/mono | Bold but role-based multicolor | Only if concept fits | Experimental |
| E-commerce | Satoshi + Satoshi | Light + warm accents | Product cards only | Clean-trustworthy |
| Finance | Newsreader + DM Sans | Dark navy + white/gold | Nav only | Authoritative |
