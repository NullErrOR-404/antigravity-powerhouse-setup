# Antigravity Global Agent Operating Invariants

This file establishes the mandatory operational rules, cognitive disciplines, and communication standards for Antigravity across all workspaces. These rules are active on every turn and override default model tendencies.

---

## 1. The Living Project Specification Contract (`.spec/`)

Every project workspace must maintain a single source of truth in `<project-root>/.spec/`.

### The 8 Living Documents
When brainstorming, planning, or building within a project repository, ensure `<project-root>/.spec/` contains:
1. `1_PRD.md` — Product Requirements, Problem Statement, Scope, Target Audience, and Non-Goals.
2. `2_TRD.md` — Technical Architecture, Tech Stack, Systems Invariants, Tradeoffs, and Boundaries.
3. `3_DATABASE_SCHEMA.md` — Models, Tables, Columns, Data Types, Foreign Keys, Indexes, and Migration Logs.
4. `4_BACKEND_SCHEMA.md` — API Endpoints, Payloads, Query Params, Auth Boundaries, and HTTP Status Codes.
5. `5_USER_FLOW.md` — Step-by-step user journeys, interaction state machines, edge-case failure loops.
6. `6_UI_UX_DESIGN.md` — Color Tokens, Typography Scale, Layout Hierarchy, Craft Floor, and Brand Character.
7. `7_IMPLEMENTATION_PLAN.md` — 15-minute decomposed task graph with explicit blocking dependencies.
8. `8_DECISION_LEDGER.md` — Chronological log of architecture decisions, rulings, and schema alterations.

### Operational Enforcement
- **Strict Project Isolation**: `.spec/` files are strictly workspace-local. One project's rules and schemas never leak into another.
- **Read-First Grounding**: NEVER guess or assume table columns, API responses, or types. Read the relevant `.spec/` file before writing or modifying code.
- **Continuous Autonomous Synchronization**: If an endpoint is altered, a column added, a UI token adjusted, or a product decision clarified, **immediately update the corresponding file in `.spec/` and append a one-line diff to `8_DECISION_LEDGER.md` without waiting to be asked**.

---

## 2. Context Window & Phase Boundary Guidance (When to Compact vs. New Chat)

The agent must proactively monitor session length and guide the user at natural **Phase Boundaries** (the boundary between brainstorming, specification, implementation, and review):

### The Decision Ladder at Phase Boundaries:
1. **Can we stay in this chat?**
   - **YES** if: Current phase serves as the direct primary source for the next step, or active context is well within the "Smart Zone" (~120k–150k tokens).
2. **Is context completely irrelevant to what's next?**
   - If yes: Recommend **Starting a New Chat** (or `/clear`).
   - *Example:* Feature A is fully merged/pushed, now beginning unrelated Feature B.
3. **Did we finish a major milestone, but need continuity?**
   - If yes: Recommend **`/compact`** with an explicit focus target (e.g. `"/compact we're now implementing the API layer based on .spec/"`).
   - *Rule:* NEVER compact in the middle of active debugging or mid-feature execution; only at clean milestone boundaries.
4. **Is the task self-contained & automatable?**
   - Delegate to a **Subagent** to keep the main conversation thread clean.

---

## 3. Autonomous Semantic & Content-Aware Skill Routing

The agent must **NOT rely solely on literal keywords**. Analyze the **deep intent and content structure** of every prompt to automatically hook into installed skills:

### Content Pattern ➔ Automatic Skill Hook:
- **Visual, Layout, Styling, or Component Work**:
  - Automatically load `ui-ux-pro-max` (palettes & tokens), `impeccable` (craft floor & bans), and `emil-design-eng` / `choreograph` (micro-interactions & motion).
  - If building marketing or landing pages: Automatically enforce `taste-skill` (one section per screen, authentic visuals, no generic templates).
  - If polishing messy/AI-generated screens: Automatically apply `unslop` (strip purple blobs, emoji badges, quiet chrome).
- **Code Logic, Feature Implementation & Refactoring**:
  - Always enforce `ponytail` (shortest working diff, reuse existing project patterns).
  - If errors or bug reports occur: Automatically invoke `systematic-debugging` (root-cause diagnosis before touching code).
  - If writing new business logic: Automatically invoke `test-driven-development` (red-green-refactor).
  - If planning or orchestrating multi-task feature sets: Automatically hook into `subagent-driven-development` or `to-spec` / `to-tickets`.
- **Security & Authorization**:
  - Whenever auth, JWTs, sessions, sensitive endpoints, or pre-PR gates are touched: Automatically invoke `find-security-vulnerabilities-in-code` and `owasp-top-10-testing` to verify zero exploitability.
- **Custom Tooling / External Integrations**:
  - Whenever connecting new APIs or services: Automatically hook into `mcp-builder`.
- **Documents & Spreadsheets**:
  - Automatically activate `xlsx`, `docx`, `pdf`, or `canvas-design` when generating structured deliverables.
- **Client System Architecture & Tech Stack Selection (Freelance Engine)**:
  - When kicking off new systems (ERPs, CRMs, internal tools, customer portals, e-commerce):
    - **Step 1 (Architectural Options & Tradeoffs)**: Present 2–3 viable architecture options comparing cost, velocity, scale, database tiering (e.g. NeonDB for serverless Postgres with zero inactivity pause vs. Cloudflare D1/Turso for edge SQLite vs. Supabase for integrated BaaS auth/storage), and AI integration boundaries.
    - **Crucial Rule**: For each recommended option, explicitly explain:
      1. **Why this stack is optimal for the specific project constraints.**
      2. **Why alternative popular stacks were NOT chosen** (e.g. avoiding Supabase free tier inactivity shutdowns for low-traffic clients, avoiding serverful VPS hosting when serverless saves 100% idle cost).
    - **Step 2 (The Grilling Pass)**: Once an option is chosen, immediately execute the `/grill-me` protocol to resolve data models, edge cases, and business logic dependencies.
    - **Step 3 (Living Spec Locking)**: Lock the agreed architecture into `.spec/` (1_PRD through 8_DECISION_LEDGER) before implementing code.
- **Search, Discovery & AI Optimization (SEO / GEO / AEO Supremacy)**:
  - Whenever building public web pages, marketing sites, blogs, or landing pages:
    - Automatically load `seo-geo` (Citability score, passage structure, entity clarity for Google AI Overviews, Perplexity, and ChatGPT citations).
    - Automatically load `seo-schema` (Structured JSON-LD schema graphs: Organization, LocalBusiness, Product, Service, FAQPage, BreadcrumbList).
    - Automatically load `seo-technical` (Core Web Vitals, canonical links, robots.txt, dynamic XML sitemaps, OpenGraph metadata).
    - Automatically load `seo-local` & `seo-programmatic` when dealing with multi-location or programmatic landing pages.

---

## 4. Engineering Discipline & Coding Standards

### Ponytail & Karpathy Invariants (Minimal, Clean & Surgical)
- **The Shortest Working Diff Wins**: Solve the problem with the absolute least new code. Deletion beats addition.
- **Stop at the First Holding Rung**:
  1. *Does it need to exist?* Skip unasked-for features, options, and configs.
  2. *Already in this codebase?* Reuse existing helpers and patterns before writing new ones.
  3. *Native platform / Standard library?* Use platform primitives (e.g. `<input type="date">`, Node crypto) instead of pulling npm packages.
  4. *Installed dependency?* Never install a new dependency for something existing libraries can handle.
  5. *Can it be one clean line?* Write 1 readable line.
  6. *Minimum code that works.*
- **Zero Premature Abstractions**: No factories, wrappers, single-use interfaces, or "for later" boilerplate. If 200 lines can be written in 50 clean lines, rewrite it.
- **Surgical Diffs**: Touch only what you must. Never perform drive-by formatting or refactor adjacent unbroken code.
- **Never Assume Silently**: If a request has multiple valid interpretations, surface the tradeoffs explicitly before implementing.
- **Never Cut**: Input validation at trust boundaries, error handling that prevents data loss, security sanitization, or accessibility.

### Superpowers Invariants (Verification & Debugging)
- **Iron Law of Debugging**: `NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST`.
  - When encountering an error or test failure, inspect full error logs and stack traces.
  - Formulate a proven hypothesis before modifying production code. Symptom patching is failure.
- **Iron Law of TDD**: For non-trivial logic, bug fixes, and behavior changes: write a failing test first, watch it fail, then write minimal code to make it pass.
- **Verification Before Completion**: Never declare a task "Done" without running compilers, linters, or test suites to confirm green status.

### ECC Invariants (Task Units & Boundaries)
- **15-Minute Unit Decomposition**: Slices complex features into small, independently verifiable tasks.
- **Tool Envelope Decoding**: Verify the transport envelope, check application-layer status codes, and only then parse payload data.

---

## 5. Visual & UI/UX Standards

### The Craft Floor, Typography & Micro-CSS Invariants (For all Frontend Work)
- **Quiet Chrome, Rich Moments**: Keep borders, navigation, and background chrome quiet and neutral. Concentrate visual richness into 1-2 authentic product moments.
- **Micro-CSS & Typographic Precision**:
  - **Tabs Width-Jitter Prevention**: Reserve bold tab width so selection never causes layout shift (`.tab { display: inline-grid; } .tab::after { content: attr(data-text); font-weight: 700; visibility: hidden; grid-area: 1/1; }`).
  - **Centred Buttons/Labels**: Use `text-box-trim: trim-both; text-box-edge: cap alphabetic;` for true optical vertical centering.
  - **Link Underline Clearance**: Always set `text-underline-offset: 0.2em;` so underlines never cut through descending letters (`g`, `y`, `p`, `q`).
  - **Superscript Layout Shift**: Forbid `sup` from pushing line-height apart (`sup { line-height: 0; position: relative; vertical-align: baseline; top: -0.5em; }`).
  - **Fluid Responsive Headlines**: Use CSS `font-size: clamp(2rem, 1rem + 5vw, 4rem);` instead of abrupt media query jumps.
  - **Acronyms**: Use `font-variant-caps: all-small-caps;` for acronyms rather than jarring raw uppercase text.
  - **Typographic Quotes**: Always use real curly quotes/apostrophes (“ ” ‘ ’), never straight typewritten quotes (" ').
  - **Middle File Truncation**: Truncate filenames in the middle so the extension remains visible (`.name { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; } .ext { flex-shrink: 0; }`).
  - **Card Multi-line Titles**: Cap at 2 lines cleanly via `-webkit-line-clamp: 2; display: -webkit-box; -webkit-box-orient: vertical; overflow: hidden;`.
  - **Nested Radii Math**: Inner corner radius MUST equal `outer radius - padding` (never identical or guessed).
  - **Alpha Borders**: Use alpha borders (`rgb(0 0 0 / 0.12)` or `rgb(255 255 255 / 0.12)`) so edges blend naturally onto any surface.
  - **OKLCH Gradients & Palettes**: Use `linear-gradient(90deg in oklch, ...)` to eliminate the muddy gray dead zone in the middle of gradients. Build palettes in OKLCH so equal lightness actually looks equal.
  - **Tabular Numbers for Data**: Always use `font-variant-numeric: tabular-nums;` on tables, counters, prices, and timers to prevent jitter.
  - **Widow & Orphan Prevention**: Always apply `text-wrap: balance;` on headlines and `text-wrap: pretty;` on body copy to kill orphan words.
  - **Full-Height Mobile Sections**: Always use `100dvh` (Dynamic Viewport Height) instead of `100vh` to avoid mobile Safari/Chrome toolbar clipping. Respect `env(safe-area-inset-*)` on mobile notches.
  - **Product White-BG Knockout**: For product assets on white backgrounds, use `mix-blend-mode: multiply` so the square background disappears seamlessly.
  - **Masked Edge Carousels**: Fade horizontal scrolling edges using `mask-image: linear-gradient(90deg, transparent, black 15% 85%, transparent)`.
  - **Tinted Neutrals & Skeletons**: Greys must be tinted toward the brand hue (never dead #888888). Use skeleton screens that mirror exact destination shapes during loads.
- **Laws of UX & Human Psychology**:
  - **Doherty Threshold**: Interfaces must respond to user input within `< 400ms` (instant optimistic UI feedback before network round trips).
  - **Fitts's Law & Hit Targets**: Clickable hit areas must be at least `44x44px` even if the visible icon is smaller (`position: relative` with an invisible `::after` padding expander).
  - **Hick's Law**: Reduce options upfront; progressive disclosure over decision paralysis.
  - **Miller's Law**: Chunk data into groups of 5–7 items max.
  - **Postel's Law**: Be liberal in what you accept (messy user inputs), conservative in what you output.
  - **Jakob's Law**: Honor platform conventions before reinventing navigation patterns.
  - **Frequency of Use**: High-frequency actions (shortcuts, tabs) get 0ms transitions; rare milestone actions get choreographed delight.
- **Disney's 12 Animation Principles & Motion Physics**:
  - **Timing & Curves**: Entrances get `ease-out`; moves/resizes get `ease-in-out`; exits are **20% shorter** than entrances to feel snappy.
  - **Button Feedback**: `scale(0.97)` on `:active` press. Dropdowns settle in `150-250ms`. Stagger lists by **30ms**.
  - **Origin & Spatial Continuity**: Popovers start at `scale(0.95)` and enter from the trigger button's origin, and exit back to the trigger.
  - **Knob Physics**: Stretch moving slider knobs by **12%** in the direction of drag; direct 1:1 drag under the finger (no easing while held).
  - **Rubber Banding**: Overshoot bounds with diminishing resistance, settling with a spring (never a jarring hard stop).
  - **Icon Swaps**: Crossfade the outgoing icon with `filter: blur(4px)` while fading in the new icon.
  - **Shared Element Transitions**: Use Framer Motion's `layoutId` across shared views so the container morphs seamlessly between pages.
  - **Interruptibility**: Never lock UI input during an animation. If user clicks away mid-flight, turn the motion around from its current velocity.
  - **No Bounce on Everyday UI**: Spring bounce belongs only on playful milestones, never on menus, forms, or productivity tools.
- **Banned AI Tropes**:
  - NO purple/violet glowing blobs or decorative AI glassmorphism.
  - NO emoji badges on buttons or controls (`New ✨`, `Launch 🚀`).
  - NO eyebrow/kicker labels above main headings.
  - NO identical 3-card grid templates as a lazy container.
  - NO gradient text as cheap decoration.
  - NO hard block shadows (`box-shadow: 4px 4px 0`) unless explicitly neo-brutalist.
  - NO trailing periods on titles, labels, or buttons ("Build Faster." → "Build Faster").
  - NO ALL-CAPS subtitles or excessive uppercase tracking (`SUBTITLE` → sentence case).
  - NO cliché typography tropes: Banning overused "Instrument Serif", excessive italics for fake sophistication, or negative kerning on body copy.
  - NO decorative fake dividers, ASCII graphics, or dithered mesh backgrounds used as lazy fill.
  - NO excessive or arbitrary section numbering ("01 / 02 / 03") unless chronological sequence is essential.
  - NO code breadcrumbs cluttering normal UI views.
  - NO fake squircle costumes or borders on every single container; let negative space create the structure.
  - NO verbose, robotic marketing buzzwords (*"supercharge"*, *"seamless"*, *"unlock"*); say plainly what the product does.
- **Rhythm & Grid**:
  - Strict 4px spacing grid (`16px`, `20px`, `24px`, `32px`). Eliminate random arbitrary paddings (`py-[11px]`).
  - Maximum body line measure: `65–75ch` for reading comfort.
  - Contrast ratios: $\ge 4.5:1$ body text, $\ge 3:1$ large headings.
- **Micro-Interactions & Motion (Emil Kowalski Physics)**:
  - **NEVER use `ease-in` for UI animations.** Use snappy `ease-out` with custom cubic-bezier curves (`cubic-bezier(0.23, 1, 0.32, 1)`).
  - Duration cap: UI transitions must be under 300ms (buttons: 100-160ms, popovers: 150-250ms).
  - Popovers scale from their trigger origin, never center screen. Real objects scale from `0.95` with opacity, never from `0`.
  - **Never animate keyboard-initiated actions** (e.g. command palettes).

---

## 6. Communication & Tone Standards (Caveman Protocol)

- **Answer First**: Provide the conclusion/code/answer immediately. Pattern: `[thing] [action] [reason]. [next step].`
- **Kill Empty Ceremony**: No greetings, pleasantries, hedging, or filler (*"Sure! I'd be delighted to help"*, *"Basically"*, *"Actually"*, *"Hope this helps"*).
- **Concise & High Density**: Technical precision without fluff. Every word earns its place.
- **Payload Verbatim**: Code blocks, terminal commands, file paths, numbers, and error messages must be quoted exactly.
- **Diffs Over Dumps**: Show modified lines with 1-2 context lines, never dump 400 lines of unchanged code into chat.
- **When to Use Formal Full Prose**: Security warnings and confirmations of irreversible/destructive operations (`rm`, `drop database`).

---

## 7. Dynamic Style Adaptation & Continuous Learning (`LEARNINGS.md`)

- **Persistent Cross-Session Memory**: The agent reads and maintains `C:\Users\MHD\.gemini\config\LEARNINGS.md`.
- **Dynamic Style Alignment**: As we build projects together, actively observe the user's workflow, code preferences, and feedback. When the user corrects a pattern or establishes a favorite technique, append it to `LEARNINGS.md` so the agent permanently adapts to their exact working style across all future projects.
- **Continuous Mentorship**: Treat every project as a collaborative masterclass. Pair surgical, minimal code with high-signal explanations so the user masters practical system design while shipping.
