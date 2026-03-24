# Design System Generator Reference

Loaded during Phase 2 (Design System). Use this to generate CSS variables, select fonts, and build palettes.

---

## CSS Variables Template (Universal — adapts to dark/light/custom)

```css
:root {
  /* === BACKGROUND LAYERS === */
  /* Dark theme */
  --bg-primary: #050508;        /* Near-black (NEVER pure #000) */
  --bg-secondary: #0a0d1a;      /* Cards, elevated surfaces */
  --bg-tertiary: #0f1328;       /* Hover states, active elements */
  --bg-card: rgba(255,255,255,0.04);  /* Glass panels */

  /* Light theme alternative */
  /* --bg-primary: #FAFAFA;
     --bg-secondary: #F5F5F0;
     --bg-tertiary: #EBEBEB;
     --bg-card: #FFFFFF; */

  /* === TEXT HIERARCHY === */
  --text-primary: #EDEDED;       /* 93% white — less strain than pure */
  --text-secondary: rgba(255,255,255,0.7);
  --text-muted: rgba(255,255,255,0.4);

  /* === ACCENT SYSTEM — 60-30-10 === */
  --accent-primary: #9b30ff;     /* 10% — hero, CTAs, key highlights */
  --accent-secondary: #4dd9c0;   /* Supporting actions, success */
  --accent-tertiary: #ff2d55;    /* Alerts, emphasis, pain points */

  /* === FUNCTIONAL === */
  --glow-primary: 0 0 40px rgba(155,48,255,0.3);
  --glow-secondary: 0 0 40px rgba(77,217,192,0.3);
  --gradient-text: linear-gradient(135deg, var(--accent-tertiary), var(--accent-primary), #3366ff);
  --gradient-button: linear-gradient(135deg, var(--accent-tertiary), var(--accent-primary));

  /* === GLASS === */
  --glass-bg: rgba(255,255,255,0.04);
  --glass-border: rgba(255,255,255,0.08);
  --glass-blur: blur(12px) saturate(140%);

  /* === TYPOGRAPHY === */
  --font-display: 'Geist', sans-serif;
  --font-body: 'Geist', sans-serif;
  --font-code: 'Geist Mono', monospace;
  --fs-hero: clamp(2.5rem, 6vw, 5rem);
  --fs-h1: clamp(2rem, 4vw, 3.5rem);
  --fs-h2: clamp(1.5rem, 3vw, 2.5rem);
  --fs-h3: clamp(1.2rem, 2vw, 1.5rem);
  --fs-body: clamp(1rem, 1.2vw, 1.15rem);
  --fs-small: 0.875rem;
  --lh-body: 1.6;
  --lh-heading: 1.1;
  --ls-heading: -0.02em;

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
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-pill: 9999px;

  /* === SHADOWS === */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.2);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.3);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.4);

  /* === CURSOR GRADIENT === */
  --mouse-x: 50%;
  --mouse-y: 50%;
  --cursor-glow-color: rgba(155, 48, 255, 0.12);
  --cursor-glow-size: 1200px;
}
```

---

## Palette Construction Rules

- 60% background, 30% secondary/text, 10% accent
- Never distribute evenly — dominant with sharp accents
- Brand color at 1-10% lightness for subtle backgrounds
- Complementary for max attention (purple <-> yellow, teal <-> coral)
- Temperature contrast: Cool bg + warm CTA = instant hierarchy

---

## Font Selection by Tone

| Tone | Display Font | Body Font | Monospace |
|------|-------------|-----------|-----------|
| Tech/SaaS | Geist, Satoshi, Instrument Sans | Same or paired lighter weight | Geist Mono, JetBrains Mono |
| Luxury | Playfair Display, Cormorant, Fraunces | Outfit, General Sans | Berkeley Mono |
| Editorial | Newsreader, Source Serif 4, Lora | Source Sans 3, Noto Sans | Source Code Pro |
| Brutalist | Archivo Black, Bebas Neue, Oswald | Space Mono, IBM Plex Mono | Same |
| Playful | Bricolage Grotesque, Rubik, Nunito | Same at lighter weight | Fira Code |

**NEVER use:** Inter, Roboto, Arial, system fonts, Open Sans, Lato, Montserrat. Vary across projects.

---

## Typography Rules

- Line height: 1.5 body, 1.1 headings, 1.75 long-form
- Letter spacing: -0.02em headings, 0 body
- Font weight: 800 headlines, 400-500 body, 700 emphasis
- Max width: 700px body text (45-75 chars)
- Container: 1100px layouts, 800px content-focused

---

## Dark Theme Rules

1. Never #000000 — use #050508
2. Elevation = lightness (each layer lighter)
3. Reduce white text opacity (93% primary, 70% secondary, 40% muted)
4. Colored shadows: `box-shadow: 0 8px 32px rgba(155,48,255,0.15)`
5. Glow > shadow for emphasis
6. Gradient text for headlines

---

## Light Theme Rules

1. Warm whites (#FAFAFA, #F5F5F0) not pure #FFFFFF backgrounds
2. Depth through shadows, not color (multi-layer shadows)
3. Colored accents on neutral — editorial feel
4. Dark text (#1a1a1a or #0F172A) on light, not pure #000
5. Subtle borders (#E2E8F0) define cards, not heavy shadows

---

## Industry-Specific Profiles

| Industry | Font Pair | Palette | Glass | Vibe |
|----------|-----------|---------|-------|------|
| SaaS/Tech | Geist + Geist Mono | Dark + purple/teal accents | Nav + 3 cards | Linear-clean |
| Luxury/Fashion | Playfair + Outfit | Warm darks + gold accents | Minimal (1-2) | Editorial-premium |
| Healthcare | Source Serif + Noto Sans | Light + blue/green | None | Trust-clean |
| Creative Agency | Bricolage + Space Mono | Dark + bold multicolor | Heavy (5+) | Experimental |
| E-commerce | Satoshi + Satoshi | Light + warm accents | Product cards only | Clean-trustworthy |
| Finance | Newsreader + DM Sans | Dark navy + white/gold | Nav only | Authoritative |
