# Image-to-3D-Environment Workflow (LOCKED 2026-04-29)

> Required reading whenever a brief mentions "3D environment", "photo backdrop", "skybox", or "navigable scene" with photographic content.

## Why this workflow exists

Most 2D-photo-to-3D techniques are wrong for "photo backdrop with foreground 3D content":

- **UV-shift fragment shaders** (akella "Fake 3D" Codrops 2019, Codrops "Reactive Depth" 2026-02-17) are 2.5D image-space hacks for STANDALONE hero animations. They cannot host depth-correct foreground 3D — z-fighting, wrong perspective, no 360° wrap. (Anti-Pattern #33.)
- **Vertex-displaced flat plane** with a depth map sculpts geometry that intersects foreground objects (avatar, tiles). This is the "gray pillar" failure mode that drove KAI v6.4-v6.11.
- **Single-image NeRF / Gaussian splat** needs multi-view capture; an AI-generated still PNG is not enough input.

The right primitive for "photo backdrop + foreground 3D" is the **drei `<Environment>` equirectangular skybox**. Production-proven across Spotify Wrapped, Active Theory, Lusion. The skybox renders at infinity; foreground avatar (z=0) + tiles (z=+200..+600) write to the depth buffer and composite IN FRONT.

## The 8-step workflow

Every step has a gate. Skipping a gate is what produces broken environments.

### Step 1 — Solicit user reference / vibe direction

Ask the user, via `AskUserQuestion` or natural prompt, for one of:
- (a) a starting reference image
- (b) a textual aesthetic direction
- (c) "use the most recently approved scene plate from `public/scenes/asset-ledger.json`"

**Gate:** the workflow MUST NOT proceed to image generation without explicit user input. No silent assumption that "the existing scene is fine".

### Step 2 — Generate via `Skill("poe-media")` — Nano-Banana-Pro

Hand off to the poe-media skill with:
- Reference image (if provided) as `--ref`
- Aesthetic-locked prompt drawn from `references/scene-plate-playbook.md`
- Output to a local generated-media or project asset folder, then mirror/copy to the user's chosen review location when visual inspection is needed
- Use **Nano-Banana-Pro** (Poe API ~500 pts) for 4K text-accuracy + cinematic detail. NOT Nano-Banana basic. NOT TopazLabs/Clarity/Remini upscalers (locked BLACKLIST per existing playbook).

### Step 3 — Open generated image on the user's Windows Desktop

```bash
cp /tmp/<gen>.png /mnt/c/Users/Kaleeb/Desktop/<gen>.png
cmd.exe /c start "" "C:\Users\Kaleeb\Desktop\<gen>.png"
```

This avoids embedding image bytes into the parent JSONL transcript (existing image-payload guard).

### Step 4 — User approval / iteration

Use `AskUserQuestion` with options: "Approved", "Regenerate with changes" (free-text notes), "Different approach". Iterate until explicit approval. **NEVER auto-approve subjective taste.**

### Step 5 — On approval, mirror approved PNG into the project

```
public/scenes/kai-studio-scene-{viewport}-v{N+1}.png
```

Compute sha256, append to `public/scenes/asset-ledger.json` with `approvedAt`, `approvedBy: "user"`, dimensions, role.

### Step 6 — Convert approved PNG → equirectangular skybox JPG

Try in this order:

**Primary — Blockade Labs Skybox AI Remix-from-image** (https://skybox.blockadelabs.com/)
- Free tier 3 generations/week
- Outputs 8K equirect (8192x4096)
- User uploads via browser; skill fetches the result URL.

**Fallback A — Poly Haven CC0 mastering studio HDRI** (https://polyhaven.com/hdris/studio)
- Instantly available
- Works as initial baseline if Skybox AI rate-limited

**Future v7+ — Luma iOS phone-scan + drei `<Splat>`**
- True 6DoF photoreal navigation
- Tracked, NOT current scope (requires multi-view capture)

Convert HDR → JPG via ffmpeg. Generate paired desktop 8K + mobile 4K:

```bash
ffmpeg -y -i source.hdr -vf scale=8192:4096 -q:v 3 studio-skybox-v6-8k.jpg
ffmpeg -y -i studio-skybox-v6-8k.jpg -vf scale=4096:2048 -q:v 3 studio-skybox-v6-4k.jpg
```

Add both to asset-ledger with sha256 + dimensions + 2:1 aspect assertion + provenance fields (source URL, license, transform command).

### Step 7 — Mount via drei `<Environment background files={...} />`

The architectural primitives:

```tsx
// app/route/page.tsx (Server Component)
import { headers } from "next/headers";
import { userAgent } from "next/server";

export default async function Page() {
  const ua = userAgent({ headers: await headers() });
  const isMobile = ua.device.type === "mobile" || ua.device.type === "tablet";
  const skyboxHref = isMobile ? "/scenes/...-4k.jpg" : "/scenes/...-8k.jpg";
  return (
    <>
      <link rel="preload" as="image" href={skyboxHref} />
      <Studio isMobile={isMobile} />
    </>
  );
}
```

```tsx
// components/StudioSkybox.tsx (inside R3F Canvas)
"use client";
import { Environment } from "@react-three/drei";
import { useStudioState } from "@/lib/use-studio-state";
import sceneManifest from "@/public/scenes/scene-manifest.json";

export function StudioSkybox() {
  const isMobile = useStudioState((s) => s.isMobile);
  const files = isMobile ? sceneManifest.skybox.mobileUrl : sceneManifest.skybox.desktopUrl;
  return <Environment background files={files} backgroundBlurriness={0} backgroundIntensity={1} />;
}
```

**Mandatory contracts:**
- **UA-scoped, not viewport-scoped** (Anti-Pattern #36): the 4K-mobile contract applies only to UA-detected mobile/tablet. DevTools responsive mode without UA spoof gets the 8K asset. Viewport-scoped detection requires `window.matchMedia` which is client-only and re-introduces the useEffect-flip double-fetch hazard.
- **3-state WebGL probe** (Anti-Pattern #35): `useState<boolean | null>(null)` — null=probing, true=ready, false=missing. The 2-state form (`useState<boolean>(false)`) flashes error UI on every first render.
- **DOM error UIs render OUTSIDE Canvas**: SkyboxLoadError + WebGLMissingNotice are plain React DOM. Three.js crashes if non-three children mount inside the Canvas tree. The in-Canvas `SceneTreeErrorBoundary` signals via zustand; the DOM siblings render in the wrapping client component.
- **NO 2D fallback** (Anti-Pattern #34): tier-down via lower-resolution skybox + DPR clamp + StudioPostFX disable. Never substitute a 2D dashboard.
- **NO UV-shift fragment shaders** (Anti-Pattern #33): wrong technique for backdrop-with-foreground-3D.

### Step 8 — Stage 3 verification on desktop + mobile + UA-spoof edge

Cold-restart dev:
```
rm -rf .next/ && npm run dev
```

Open `/your-route` in fresh tabs:
- 1280x800 with desktop UA → loads 8K skybox
- 375x812 with mobile UA → loads 4K skybox
- 375x812 with desktop UA (DevTools responsive without spoof) → loads 8K (UA-scoped contract)

Run `npm run test:v6.13` (or your project's equivalent):
- skybox-asset (sha256 + dims + 2:1)
- no-uv-shift-shader (greps for forbidden patterns)
- no-2d-fallback (greps for MobileFallback / GPUTierGate)
- route-authority (canonical page.tsx is sole route owner)
- no-blank-transition (StudioScene always mounts exactly one backdrop)
- prebuild-chain-clean (active script chain free of legacy test names)
- skybox-mounted (runtime probe — drei `<Environment>` is in the scene-graph)
- viewport-skybox-resolution (each viewport+UA combo loads expected single asset)
- webgl-probe-no-error-flash (DOM never shows error UI before WebGL probe completes)

Screenshot all three combos to user's Desktop for visual approval.

## Reliability invariants the skill enforces

- Never skip Step 1 (reference solicitation).
- Never auto-approve Step 4 (subjective taste).
- Always run Step 8 verification before claiming success.
- Asset-ledger sha256 ledger is the source of truth for approved scenes.
- All steps wired through existing skills:
  - `poe-media` for generation
  - `agent-browser` for upload/screenshot
  - `beautiful-converting-frontend-design` for the architectural primitives

## Tool registry

| Tool | Output | Free tier | Best for | Verdict |
|------|--------|-----------|----------|---------|
| **Blockade Labs Skybox AI** | 8K equirect JPG | 3 gens/week | photo → 360° backdrop | **PRIMARY** |
| Poly Haven HDRIs | equirect HDR (CC0) | unlimited | generic studio baseline | **FALLBACK A** |
| Luma iOS + drei `<Splat>` | Gaussian splat | Free | physical-space scan | future v7+ |
| Luma AI Genie | 3D mesh | Free | text/image → 3D scene | overkill; mesh wrong shape |
| Microsoft TRELLIS | textured mesh | OS MIT | image → mesh | wrong shape |
| Tencent Hunyuan3D | textured mesh | OS | single image → mesh | weak on interiors |

## References

- Skybox AI: https://skybox.blockadelabs.com/
- drei `<Environment>`: https://drei.docs.pmnd.rs/staging/environment
- pmndrs/drei: https://github.com/pmndrs/drei
- thefrontdev — HDRI in R3F: https://www.thefrontdev.co.uk/mastering-skybox-realism-loading-and-applying-hdri-with-three-and-r3f/
- R3F Tutorials — Environment: https://sbcode.net/react-three-fiber/environment/
- Active Theory Spotify Wrapped 2018: https://medium.com/active-theory/spotify-wrapped-2018-technical-case-study-5b7cfb7e9d3a

## Anti-Patterns enforced

- **#33** UV-shift fragment shader as backdrop forbidden — wrong technique for backdrop-with-foreground-3D.
- **#34** MobileFallback as 2D dashboard substitute forbidden — tier-down via asset resolution, not via 2D.
- **#35** 2-state WebGL probe forbidden — must use 3-state sentinel to avoid first-render error-UI flash.
- **#36** Viewport-scoped (rather than UA-scoped) skybox URL selection forbidden — viewport-scoped requires client-only matchMedia which forces a useEffect URL flip + double-fetch.
