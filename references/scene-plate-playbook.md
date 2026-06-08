# Scene Plate Playbook — Premium Recessive Backgrounds for Avatar/HUD Overlays

A reusable rubric for generating cinematic background plates that sit behind a foreground subject (avatar, product, or HUD modules). Distilled from 15+ iteration cycles on the KAI mastering-studio scene — captures the discipline that produced an approved pair, plus the failure modes that wasted points along the way.

## When To Use This Playbook

You're generating a **back plate** that:
- Sits behind a separately-lit foreground subject that will be composited or overlaid later (live avatar, 3D model, video element).
- Must read as atmospheric depth, not the focal point.
- Will appear at multiple breakpoints (mobile portrait + desktop landscape, often paired).
- Needs locked lighting/lens consistency across iterations so the foreground subject's key light blends with the environment.

If your image IS the focal point (hero product shot, portrait, etc.), use a different playbook — this one optimizes for recessive-but-alive.

---

## Lesson A — Mobile-First, Paired-Orientation By Default

A 21:9 ultra-wide plate **does not** translate to a phone via center-crop without losing corner content. If both orientations matter, generate them as a paired set, not as one master + crop.

**Rule:**
- Mobile native: 9:16 portrait at 1024×1792 (Nano-Banana-Pro snaps to 768×1376 — both work).
- Desktop native: 21:9 landscape at 1792×768 (snaps to 1568×672 or 1584×672).
- Same `--ref` reference image for both. Same locked prompt. Different sizes only.
- Mobile gets a slightly wider lens equivalent than desktop (8mm mobile vs 10mm desktop) so corner content (e.g. side speaker stacks) compresses inward enough to fit the portrait frame edges.

**Failure mode if you skip this:** at any rectilinear projection, content at the horizontal extremes of a 21:9 frame cannot fit inside a 9:16 center-crop. You'll waste 500pts per regen until you concede paired generation.

---

## Lesson B — Back-Plate Framing Language

Tell the model the image will be **a back plate behind something else**. This single phrase changes the model's lighting/contrast bias from "make it pop" to "leave room for foreground."

**Prompt phrases that work:**
- "Composition is a back plate that knows it's behind a foreground avatar plus HUD elements. Recessive, dim, only the central focal element is bright."
- "Underexposed approximately 2.5 stops below normal interior."
- "Charcoal #0E0E14 dominant across most of the frame."
- "Brightest single element in foreground is the [center spotlight pool / avatar mark] so a separately key-lit subject can be overlaid into it cleanly without lighting mismatch."

**Anti-pattern phrases to avoid:**
- "Cinematic" without modifier — the model will brighten everything and add bloom.
- "Photorealistic" alone — biases toward standard interior exposure.
- "Hero shot" — biases toward making background compete with foreground.

---

## Lesson C — Edit vs. Fresh-Generation Cost Discipline

Nano-Banana-Pro img2img regenerates the latent space — even with "preserve everything except X" prompts, it commonly drops or alters unrelated elements (mixing boards, plants, instruments). This is a known model behavior, not a prompt failure.

**Decision tree:**

| Change scope | Tool | Cost | Risk |
|---|---|---|---|
| Single-element add/remove (e.g. add a plant, remove a chair, change one trim color) | `Nano-Banana edit` ($200pts) | Low | Surgical; preserves pixels not touched. Can lose small details across multiple chained edits. |
| Single-element with character/composition preservation | `Flux-Kontext` ($400pts) — IF available; sometimes 404 on Poe | Medium | Best-in-class for "edit X, keep everything else identical." Verify model availability before relying on it. |
| Lens/framing/camera change (lens equivalent, aspect ratio, perspective) | `Nano-Banana-Pro img2img` ($500pts) | Higher | Required for spatial transforms; expect collateral changes; budget for iteration. |
| Style transfer / lighting overhaul | `Nano-Banana edit` (style_lighting route) | Low | Good for global tone shifts. |
| Crisp typography / text rendering | `GPT-Image-1` ($800pts) | Premium | Use when text accuracy matters. |
| Texture detail / instructional photos | `Imagen-4` ($600pts) | Premium | When you need close-up material truth. |

**Chained-edit hazard:** Each edit pass loses fidelity. If you make 3 successive `Nano-Banana edit` calls (chair removed → plants added → instruments boosted), small details degrade with each pass. Better: batch related edits into one prompt; or accept that you'll need to add lost details back in a follow-up.

**The minimal-prompt principle:** When using img2img to preserve composition, your prompt should be SHORT and list ONLY what changes. Long descriptive prompts re-bias the model away from the reference. "Keep reference exactly. Change only: (1) X, (2) Y." beats a 500-word recreation prompt.

---

## Lesson D — No-Text-On-Branded-Surfaces Recipe

Nano-Banana-Pro hallucinates gibberish text on logo/brand surfaces (e.g. "GENELEC" turns into "GENLLC", "GLNLEC", etc.). The fix is double-paired NEGATIVE + POSITIVE prompts.

**Recipe:**
- POSITIVE: "clean cabinet face with only the central black coaxial driver donut and tiny green status LED"
- NEGATIVE: "NO text, NO logo, NO brand name, NO writing on cabinet face, NO printed labels"

**Same pattern for:**
- Speaker faces (NO GENELEC text → clean coaxial donut + tiny LED)
- Product packaging (NO label text → matte clean surface)
- Device screens (NO UI text → pure off-glass or specified single color)
- Wall art/posters (NO printed words → abstract texture)

**If text leaks through anyway:** run a `Nano-Banana edit` follow-up specifically targeting the text area: "Remove all text and writing from the speaker cabinet face. Replace with clean uniform cabinet color matching the rest of the cabinet."

---

## Lesson E — Lighting Continuity for Foreground Compositing

If a foreground subject (live avatar, 3D model, video element) will be overlaid on this back plate, the plate's lighting must be authored to **match** the foreground's key-light direction, color, and intensity. Otherwise the composite reads as flat/disconnected.

**Pattern: center spotlight pool sized for avatar overlay.**
- The plate has a clearly-defined warm-tungsten spotlight pool falling from above onto an empty floor area.
- Sharp gradient center-to-edge (not soft circular bloom — actual visible spot cone edge).
- Sized so the foreground subject's silhouette fits inside the pool with rim falloff catching the subject's shoulders/sides.
- Pool color matches the foreground's planned key-light color (e.g. warm tungsten #F7E7CE → 3D `<spotLight>` color #F7E7CE).
- Pool angle matches the foreground's planned key-light angle.

**Verification probe:** After mounting the foreground subject in front of the plate, the subject's centroid should align with the plate's spot pool (within 8px on a 1920px-wide frame, within 3° angular tolerance).

---

## Lesson F — Subtle Atmosphere Via Splash, Not Jungle

When asked to "make the background feel alive," the temptation is to add lush vegetation, complex props, or busy backlighting. Resist.

**Rule:**
- One or two small leafy plants tucked into the deepest corners.
- Half-hidden in shadow, lit only by existing accent lights (warm tungsten or cool teal rim).
- "Just a hint of life in the far back" — sparse, not dense.

**Anti-pattern:** Listing "monstera, devil's-ivy, snake plant, fiddle-leaf fig" in the prompt. The model will add ALL of them and turn the back room into a botanical garden.

**Correct prompt:** "Add a subtle splash of greenery in the far back-room corner — one or two small leafy plants tucked into the deepest corner, half-hidden in shadow. SUBTLE, sparse. NOT a jungle, NOT trailing vines everywhere. Just a hint of life in the far back."

---

## Lesson G — Spotlight Cone Edges (Crisp vs. Soft)

When the user asks for "spotlights that pop" on instruments/props, the failure mode is soft-circular bloom (model default). The fix is explicit cone-edge language.

**Prompt phrase that works:**
- "Each spotlight is a clearly defined narrow cone of warm tungsten or cool teal light with a SHARP visible edge between lit and unlit space, like a stage spotlight cone in haze."
- "Stage-spotlight-in-haze look."
- "Visible cone-edge spotlights."

**Avoid:**
- "Glowing" — softens the cone.
- "Dramatic lighting" — model adds bloom + flares.
- "Cinematic spotlights" — generic, often produces soft pool not cone.

---

## Lesson H — Iteration Discipline (Don't Lose Work)

Each successive edit/regen risks losing earlier-approved details. Strategy:

1. **Snapshot every approved version** to a versioned filename: `kai-studio-scene-desktop-v6.png`, `v10.png`, `v12.png`, `v14.png`, `v15.png`.
2. **Always `--ref` the most recent approved version**, not an early version.
3. **If a regression appears (e.g. mixing board disappeared), don't try to "fix it back" with a third pass on the bad result** — go back to the last approved version and re-issue the original change with stricter preservation language.
4. **Lock the approved pair** by copying to `public/scenes/` (or equivalent production-asset dir) only after BOTH orientations are explicitly approved by the user.
5. **Approval ledger** in plan/spec doc: "v14 desktop approval timestamp: PENDING / verbatim: PENDING" — fill in only after explicit user "APPROVED".

---

## Proven Example — KAI Mastering Studio Scene (2026-04-28)

After 15 iterations the locked recipe that produced approved desktop + mobile pair:

**Tool:** Nano-Banana-Pro img2img + Nano-Banana edit (chained surgical edits).

**Locked composition:**
- Mastering studio control room at night.
- Camera pulled back several meters behind engineer position.
- Bottom: AVID-S6-style mixing console (mixing board peeking behind, no chair).
- Mid-third left/right corners: flagship Genelec coaxial mains (8351A/8341A on W371A woofer towers), deep teal #1a3a3a, clean cabinet face (no text/logo).
- Mid-center: large dark display screen + glass control-room window.
- Through glass: live room with brick walls, polished concrete floor, drum kit + electric guitar + vertical microphone, subtle plants in far corner.
- Ceiling: black acoustic-foam pyramid panels (NOT wood).
- Trim: brushed aluminum (NOT wood, NOT painted).

**Locked lighting:**
- Super low-key moody, ~2.5 stops underexposed vs typical interior.
- Charcoal #0E0E14 dominant.
- Single warm tungsten #F7E7CE center spot pool over chair-removed area (Kai's mark).
- Soft warm grazing key on console top edge.
- Through-glass: tight tungsten + cool teal #06B6D4 spotlight cones with sharp visible edges, each grazing one instrument.
- Tiny green status LEDs on speaker bottoms.

**Locked lens:**
- Desktop: 10mm equivalent rectilinear (no fisheye, no barrel, no curvature).
- Mobile: 8mm equivalent rectilinear (wider) — needed so speaker stacks fit at 9:16 portrait edges.

**Sizes:**
- Desktop: 1792×768 native (Nano-Banana-Pro returns 1568×672 or 1584×672).
- Mobile: 1024×1792 native (Nano-Banana-Pro returns 768×1376).

**Iteration cost (for budgeting future similar scenes):**
- ~7 desktop regens × 500pts = 3500pts
- ~6 mobile regens × 500pts = 3000pts
- ~5 surgical edits × 200pts = 1000pts
- 2 upscales × 250-300pts = 500-600pts
- Total: ~8,000pts for one approved scene pair

**Final output:**
- `kai-studio-scene-desktop-v15.png` (1584×672, locked).
- `kai-studio-scene-mobile-v14.png` (768×1376, locked).
- 4x upscaled versions follow same naming with `-4x` suffix.

---

## Reusable Prompt Template

For future similar premium-recessive back plates:

```
Photorealistic [SCENE_TYPE] at [TIME_OF_DAY], [LENS]mm equivalent rectilinear lens (no fisheye, no barrel distortion, no visible lens curvature). Camera position pulled back so [FOCAL_SUBJECT_PLACEMENT].

LIGHTING: super low-key moody, underexposed approximately 2.5 stops below normal interior, [DOMINANT_DARK_HEX] dominant across most of frame. ONLY light sources permitted:
1. Single [KEY_LIGHT_COLOR_HEX] center spot pool falling from above onto [FOCAL_OVERLAY_AREA] — sharp circular gradient center fading to dim edges, brightest single element in foreground for an avatar/subject overlay to align with.
2. [Optional] Soft [KEY_COLOR] grazing key on [SECONDARY_SURFACE].
3. [Optional] Through-[SEPARATOR] tight narrow [WARM_HEX] plus cool [ACCENT_HEX] spotlight cones each grazing one [BACKDROP_PROP] — clearly defined narrow cone of light with SHARP visible edge between lit and unlit space, stage-spotlight-in-haze look.

COMPOSITION (preserve from reference):
- [LIST FIXED ELEMENTS]
- Cabinet/branded surfaces: clean face with only [SPECIFIC_DETAIL], NO text, NO logo, NO writing.
- Trim: [BRUSHED_ALUMINUM / SPECIFIED_MATERIAL] (NOT wood, NOT painted).
- Ceiling: [BLACK_ACOUSTIC_FOAM / SPECIFIED_MATERIAL].

ATMOSPHERE: subtle splash of [GREENERY/PROPS] in far corners only, half-hidden in shadow, sparse not dense.

NEGATIVE: NO visible lens distortion, NO fisheye, NO barrel warp; NO daylight, NO neon, NO saturated colors, NO bright key fill, NO uniform interior brightness, NO mid-tone overall exposure, NO bright pendants, NO ambient flood, NO wood ceiling/walls/trim/slats, NO painted trim, NO clutter, NO water stains, NO grime, NO mold, NO scratches, NO sterile-new-build, NO occupied seats/furniture, NO person, NO UI/text, NO logo on branded surfaces.

Hasselblad full-frame look, faint analog grain, subtle vignette, dust visible only in spot beams.
```

Replace bracketed placeholders for the specific scene. Keep the structure (LIGHTING / COMPOSITION / ATMOSPHERE / NEGATIVE) — it's the structure that produces consistent results, not the words.

---

## Quick Reference Card

| Need | Tool | Cost | Native Size |
|---|---|---|---|
| Fresh paired plate (mobile + desktop) | Nano-Banana-Pro txt2img + Nano-Banana-Pro img2img | 1000pts | 1024×1792 + 1792×768 |
| Add/remove single element | Nano-Banana edit | 200pts | preserves ref size |
| Lens/aspect change | Nano-Banana-Pro img2img | 500pts | per --size |
| Lock resolution | (no working upscaler — see BLACKLIST below; ship un-upscaled native Nano-Banana-Pro output) | n/a | 1568×672 / 768×1376 |
| Premium photorealism with hard text accuracy | GPT-Image-1 | 800pts | 1024×1024 default |

---

## DO-NOT-USE BLACKLIST — Upscalers (verified broken/low-quality 2026-04-28)

User direction (verbatim, recorded 2026-04-28):
> "NO THE NEW ONES ARE ABSOLUTELY SHIT NEVER USE THOSE MODELS EVER AGAIN MAKE SURE THE NOTE IN THE SKILL SAYS TO DO NOT USE THOSE."

These three upscale models all fail on cinematic studio plates and must NOT be used for back-plate workflows:

- **Clarity-Upscaler** — Returned 4x output successfully (6336×2688) BUT introduced visible weird edges and strange artifacts on the back-plate composition. User explicitly rejected. Do NOT use for any premium-recessive back plate.
- **Remini-Upscaler** — Ignored the `--scale 4` parameter and returned a fixed-size 1024×768 lossy JPEG (not PNG, not actually upscaled). Useless for production-quality assets.
- **TopazLabs** — Returns persistent HTTP 500 from Poe API: `'Please provide an image by populating the image field in the form data.'` This is a Poe-side integration bug in `poe_media_gen.py`'s upload mechanism. Two consecutive attempts on the same input failed identically. Until the script is fixed (image-field encoding), TopazLabs is unusable through this CLI.

**Correct path for cinematic back plates (until upscalers are fixed):**
- Ship the native Nano-Banana-Pro output un-upscaled. Native size (1568×672 desktop / 768×1376 mobile) is the highest fidelity available through this stack.
- If higher resolution is genuinely required and the user accepts img2img-regen risk (collateral element changes), try Imagen-4 (~600pts, "texture detail" routing) or Flux.2-Pro (~700pts, "photorealism") with the source as `--ref`. This is regeneration, not upscaling, but produces sharp consistent output without scale-related artifacts. Get explicit user approval first because img2img regen can lose unrelated details (mixing boards, plants, etc. — see Lesson H iteration discipline).
- If a true non-regenerative upscale is required, fix `poe_media_gen.py`'s TopazLabs image-field upload encoding before retrying.

---

## Approval Workflow

1. Generate paired set (or single).
2. Mirror to user-accessible Desktop with stable filename.
3. Open in Windows image viewer (or equivalent) so user can review.
4. Wait for explicit "APPROVED" or correction list.
5. Iterate via surgical edits on the most-recent-approved version.
6. After both orientations approved, run upscale.
7. Lock final filenames into the production asset directory + manifest.
8. Update this playbook if a new failure mode emerged.
