# Tool Decision Matrix

Loaded during Phase 1 for routing decisions. Every tool has a fallback — the skill produces genius output with ZERO external tools.

---

## Decision Flow

```
START → Is this a complete page from scratch?
  YES → Is Google Stitch available?
    YES → Use Stitch for initial generation → enhance with skill
    NO → Build manually with skill (full 6-phase workflow)
  NO → Is this a specific component?
    YES → Check 21st.dev library first → python3 scripts/twenty_first.py fetch "component"
      Found → Use as starting point, customize
      Not found → Build from scratch with skill
    NO → Is this a design system?
      YES → Is uipro-cli installed?
        YES → uipro init --ai claude → customize tokens
        NO → Use references/design-system-generator.md
      NO → Is this copy/conversion optimization?
        YES → Invoke marketing skills (copywriting, page-cro, marketing-psychology)
        NO → Default: Full 6-phase workflow
```

---

## Tool Availability Checks

```bash
# Check Google Stitch CLI
[ -n "$STITCH_API_KEY" ] || [ -f ~/.config/stitch/api-key ] || gcloud auth application-default print-access-token >/dev/null 2>&1 && echo "Stitch: available" || echo "Stitch: not configured (set STITCH_API_KEY or gcloud ADC)"

# Check uipro-cli
command -v uipro >/dev/null 2>&1 && echo "uipro: available" || echo "uipro: not installed"

# Check 21st.dev API key
[ -n "$TWENTYFIRST_API_KEY" ] || [ -f ~/.config/21st-dev/api-key ] && echo "21st.dev: available" || echo "21st.dev: no API key"
```

---

## Tool Combination Patterns

| Scenario | Tools | Workflow |
|----------|-------|---------|
| New SaaS landing page | Skill (all phases) + copywriting + page-cro | Full conversion-first build |
| Redesign existing page | Stitch (extract DNA) → Skill (enhance) | Stitch captures current → skill improves |
| Add specific component | 21st.dev (fetch) → Skill (customize) | Start from pre-built, make distinctive |
| New brand/project | uipro (tokens) → Skill (build) | Generate system → build on top |
| Pricing page | Skill + pricing-strategy + page-cro | Conversion-focused pricing design |
| Multi-page site | Skill + BarbaJS transitions | Full build with page transitions |

---

## Fallback Hierarchy

| Tool Unavailable | Fallback |
|-----------------|----------|
| Google Stitch CLI | Build manually (actually often better — more control) |
| 21st.dev | Build component from scratch using skill patterns |
| uipro-cli | references/design-system-generator.md |
| Marketing skills | references/conversion-framework.md |
| GSAP CDN down | Local copy or CSS animations (degraded but functional) |

---

## External Tool Notes

**Google Stitch CLI** (`python3 scripts/google_stitch.py`) — Google's AI UI design tool. Free (350 gen/month). Auth via API key or gcloud ADC. Subcommands: `tools`, `call`, `build`, `code`, `image`. Can generate complete pages from prompts and extract screen code/images. Enhancement only — don't depend on it.

**21st.dev** — Component library with AI refinement. REST API: `POST https://magic.21st.dev/api/fetch-ui`. Can browse and refine components. Use for common patterns (nav, hero, pricing cards) as starting points.

**uipro-cli** — Design system generator. `uipro init --ai claude` generates tokens for 161 industries and 67 styles. Good for rapid project kickoff. Customize output with skill principles.

---

## Google Stitch — First-Time Setup

### Option A: API Key (simplest)

1. Go to [stitch.withgoogle.com](https://stitch.withgoogle.com) → Settings → API Keys
2. Generate a key
3. Save it:
   ```bash
   mkdir -p ~/.config/stitch && echo "YOUR_KEY" > ~/.config/stitch/api-key
   ```
   OR add to `~/.bashrc`: `export STITCH_API_KEY="YOUR_KEY"`
4. Test: `python3 scripts/google_stitch.py call list_projects`

### Option B: gcloud ADC (team/CI setups)

1. Install gcloud: `curl https://sdk.cloud.google.com | bash`
2. Auth: `gcloud auth application-default login`
3. Pick a project: `gcloud projects list`
4. Add quota project to ADC credentials:
   ```bash
   # Edit ~/.config/gcloud/application_default_credentials.json
   # Add: "quota_project_id": "YOUR_PROJECT_ID"
   ```
5. Enable the API: visit `https://console.developers.google.com/apis/api/stitch.googleapis.com/overview?project=YOUR_PROJECT_ID` → click Enable
6. Test: `GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID python3 scripts/google_stitch.py call list_projects`

---

## Google Stitch — Prompting Rules (from real testing)

### What Stitch does well
- Layout structure (card grids, navbars, hero layouts, section spacing)
- AI-generated hero images and illustrations
- Quick visual prototyping (complete page in ~30 seconds)

### What Stitch does poorly
- Ignores color/theme instructions (defaults to dark)
- Invents generic SaaS copy instead of using provided content
- Adds fake social proof logos (Slack, Google, OpenAI, GitHub)
- Always outputs Tailwind CDN with generic utility classes
- No animations, no scroll effects, no GSAP

### 5 Prompting Rules

1. **Generate ONE section at a time**, not entire pages. A full-page prompt produces generic results.
2. **Paste EXACT copy** into the prompt — never describe it ("a hero section about AI"). Paste the actual headline, subhead, and body text you want.
3. **Specify theme aggressively**: "CRITICAL: Use white background #FFFFFF. Do NOT use dark theme. No dark:bg classes."
4. **Use Stitch for LAYOUT INSPIRATION only** — never ship its Tailwind/copy directly. Extract the structural ideas, rebuild in the skill's CSS architecture.
5. **Always rebuild** extracted layout ideas using skill Phases 4-6 (Build → Animate → Self-Review).

### Recommended Workflow

```
1. create_project → name it descriptively
2. generate_screen_from_text → paste EXACT copy, specify theme/colors
3. get_screen_image → download screenshot for layout reference
4. get_screen_code → download HTML to study structure
5. Extract layout ideas (grid ratios, spacing, section order)
6. Rebuild from scratch using skill's CSS architecture + GSAP animations
```

### Available Stitch Tools

| Tool | Purpose |
|------|---------|
| `create_project` | Create a new Stitch project |
| `list_projects` | List all your Stitch projects |
| `get_project` | Get project details |
| `list_screens` | List screens in a project |
| `get_screen` | Get screen details |
| `generate_screen_from_text` | Generate a screen from a text prompt (requires `projectId` + `prompt`) |
| `edit_screens` | Edit existing screens |
| `generate_variants` | Generate design variants |
