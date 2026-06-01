# PDF / Investor Deck Build Playbook

Use this whenever the deliverable is a **downloadable PDF deck rendered from HTML** that must open identically in *any* viewer (Edge, Acrobat, Preview, Chrome) — investor pitches, pre-seed/seed decks, partnership proposals. This is distinct from a scroll-through web "presentation page" (Style 5 main): the craft/clarity rules still apply, but the export pipeline and verification below are mandatory. Hard-won from real seed-deck builds.

## 1. The Edge-safe lossless-image pipeline (NON-NEGOTIABLE)

**Why:** Chrome `--print-to-pdf` emits vector gradients/transparency that **Microsoft Edge's PDF engine renders as blank white**, even though the file is correct. Embedded fonts/transparency also render inconsistently across viewers. The fix is to ship every page as a flat image.

**Pipeline:** render HTML in headless Chrome → rasterize each page with `pdftoppm -r 200` → recombine into a flat image-based PDF. Result has **zero font objects** → opens identically everywhere.

```bash
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
  --no-pdf-header-footer --run-all-compositor-stages-before-draw \
  --virtual-time-budget=8000 --print-to-pdf=deck.pdf deck.html
pdftoppm -png -r 200 deck.pdf out/p                       # 200 DPI rasters
convert out/p-*.png -compress Zip deck-flat.pdf            # lossless Flate; font_objs=0
montage out/p-*.png -tile 3x4 -geometry 400x+6+6 -background '#0a0a12' contact.jpg
```

- **Lossless only.** `img2pdf` is ideal (embeds PNG without re-encoding); ImageMagick `convert ... -compress Zip` is a lossless fallback. **Never** use Pillow `Image.save(...pdf...)` to embed photos — it re-encodes RGB as **lossy JPEG** and quietly degrades product screenshots.
- Deliver **both** letter (`11in 8.5in`) and 16:9 (`13.333in 7.5in`), plus a per-slide PNG folder and a contact-sheet JPG.
- **Never overwrite the user's original/source PDF.** Use new versioned filenames and keep prior versions until the user says otherwise (deleting their files is a user-owned decision).

## 2. Self-contained HTML generator
- One Python generator emits the HTML; embed fonts + images as **base64 data URIs** so the page renders standalone during print (no external fetches).
- Emit both page sizes from the same source via `__PW__/__PH__` placeholder swap.
- `@page{size:__PW__ __PH__;margin:0}` + `.slide{width;height;overflow:hidden;page-break-after:always}` = exactly one slide per page.

## 3. Real product imagery, never fake cards
- Use the **actual product/site screenshot**. Crop **tight** to the content — drop the site's own outer container chrome and dead space — or you get a **nested double-frame** when you add your own card border (a common "this looks weird / overlapping" complaint).
- The cropped UI already has its own borders. Frame it with **one** subtle frame (1px + soft shadow), not a second heavy border.
- Use the **highest-resolution source**; don't upscale at render DPI. If only a lower-res "loaded" state shows a needed detail (e.g., connector lines), use it for that crop and a hi-res source for the rest.

## 4. Diagrams beat text (inline SVG)
One signature diagram per concept replaces paragraphs. `<svg ... shape-rendering="geometricPrecision">`. Investor-grade patterns that consistently land:
- **Supply vs demand / disproportionality** — a dense field of dots (the flood) vs a tiny few (the selected), with the ratio spelled out ("≈50,000 songs per signing"). *Show* the gap; don't describe it.
- **Directional cycle / flywheel** — ALWAYS draw arrows showing flow direction (arc-arrows around the ring + a return arc). A ring of circles *without* arrows reads as abstract decoration, not a loop.
- **Two sides, one core** — for two-sided products, show the unified data **core** (the loop) + the **bridge** (e.g. a "matchmaker") + the **consumer side** tapping in. Don't bury the bridge as just another ring step.
- **The mathematical punch** — convert a big number into a visceral human unit ("100,000 songs/day ≈ 240 days of non-stop listening to hear one day's uploads").
- **Symmetric connectors** — fan from N evenly-spaced source points to N evenly-spaced targets, never all from one point (looks lopsided). Smooth cubic curves; arrowheads at the target.
- **Process strip** — a compact single row of pills with arrows between them.
- TAM/SAM/SOM concentric, ascending bars, donut splits — keep their labels in a separate legend column.

## 5. No overlap, no clipping (hard failures)
- Small text must **never** sit under/over a diagram. Put the diagram in one zone and the stat text in another, separated by a divider. Audit every slide at full res.
- Content-heavy slides (especially the **closing/climax**) overflow fixed slide height and **clip at the bottom**. Don't stack headline+lead+big-diagram+footer+banner through the generic template. Write a **custom slide function** with controlled vertical rhythm: compact the supporting diagram, give the climax its own well-spaced block, and confirm it fits with bottom margin.

## 6. Dark-deck palette + craft
- Near-black stage (`#04050a`), elevation via lighter glass surfaces, vignette + faint grain (SVG noise ~5% `mix-blend:overlay`).
- **Bright accents pop more than muted ones on dark.** Favor lighter cyan/gold/green/violet and use **glow as a hierarchy tool** (champagne→gold headline gradient + glow; accent glow on key nodes/CTAs). Users routinely ask for "more pop / stronger contrast / stronger glow" — start brighter than feels natural.
- Champagne→gold→deep-gold gradient on the wordmark/hero number via `background-clip:text` + text-shadow glow.
- Body text stays **solid high-contrast** (`#eef1f6`/white). Accents are for borders/labels/numbers — never body copy.

## 7. Sourced numbers (credibility)
- Every external stat needs a **citable source on or beside the slide** ("not pulled out of thin air"): IFPI (market size), Luminate (upload volume), RIAA/MBW (signings), WIPO, etc.
- **Verify current figures via web search** — they change yearly (e.g., IFPI global recorded-music revenue updates each March). Don't trust training-data recall for a headline number; a figure that was a forecast last quarter may now be a published actual (or vice-versa).
- Ship a `sources+changes.md` note beside the deck listing every stat + citation and the per-version changes.

## 8. Verification gate (render → READ → confirm)
- **Structural:** each delivered PDF `pages == expected`; `pdffonts` shows 0 fonts (`font_objs=0` → Edge-safe); page-1 brightness `< 60` on a 40-DPI raster (dark, not blank).
- **Visual:** rasterize and actually **READ** the contact sheet + every changed slide at full res. Confirm diagrams are legible, nothing overlaps, nothing clips. Code inspection is NOT enough for a visual claim.
- **Copy constraints:** scan the **visible text only** (strip `<style>`, base64 data URIs, and code comments first — base64 blobs and WHY-comments cause false-positive keyword matches) for any framing the user excluded (e.g. a region the deck must stay global about).

## 9. Process & people
- Expect **several review rounds** — but keep **one** clearly-named "latest" deck and **archive** (move, never delete) superseded drafts into a subfolder. Never overwrite the user's original/source files. A new filename every revision is a trap: the user keeps reopening their already-open (stale) tab, sees no change, and gets (rightly) frustrated. One obvious latest file makes opening the wrong one impossible.
- **Dead-simple for a non-expert.** Write every headline, label, and stat so an investor who knows *nothing* about the domain instantly gets it — "anyone can fund this without understanding the industry." If a slide needs insider knowledge to parse, rewrite it. Jargon and insider framing kill decks; plain words + one idea + one visual win.
- The **team slide** should credit BOTH domain expertise AND building strength; don't imply a key builder is just a coder who'll be swapped out, or that only one founder understands the problem.
- Carry the user's **locked positioning constraints** (global vs regional, preserve-meaning vs rewrite, the chosen hero line) across every regeneration — re-confirm each build.
