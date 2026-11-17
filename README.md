# Antigravity Powerhouse Agent Setup

Turn any default Antigravity installation into a **Staff-Level AI Engineer, Solutions Architect, and Product Designer**.

---

## What This Setup Equips

1. **Operating Invariants (`GEMINI.md`)**:
   - **Living Project Spec (`.spec/`)**: Automatically maintains 8 synced markdown documents for zero-hallucination memory across long sessions.
   - **Ponytail v5.3 & Karpathy Guidelines**: Shortest working diff, platform primitive reuse, surgical changes, zero bloated wrappers.
   - **Superpowers TDD & Root Cause**: Never patches bugs without proven diagnosis; test-driven execution.
   - **Charles Liu / Emil Kowalski Craft**: 20 micro-CSS precision rules, 20 animation physics laws, and 20 explicit AI-slop bans.
   - **Staff Architect Protocol**: Compares 2–3 viable tech stacks per client with cost/scale tradeoffs.
2. **37 Curated Production Skills**:
   - `scaffold-spec`, `ui-ux-pro-max`, `taste-skill`, `impeccable`, `charles-polish`, `charles-ux-animation`, `strix` (OWASP Top 10 AppSec), `seo-geo`, `seo-schema`, etc.
3. **Hands & Eyes MCPs**:
   - Autonomous GitHub integration + Playwright headless browser for visual self-healing UI tests.

---

## 1-Click Installation (For New Users)

Open PowerShell as Administrator and run:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
.\install.ps1
```

### What `install.ps1` Does Autonomously:
1. Installs Node.js LTS, Git, and GitHub CLI via `winget`.
2. Downloads Playwright Chromium browser binary.
3. Deploys `GEMINI.md`, `LEARNINGS.md`, and all 37 skills to `~/.gemini/config/`.
4. Configures `mcp_config.json`.

---

## Post-Install: One-Time Authentications

After running the installer:
1. **GitHub Login** (For autonomous pushing):
   ```powershell
   gh auth login
   gh auth setup-git
   ```
2. **Add GitHub Token to MCP** (Optional, for PR/Issue inspection):
   Paste their token into `~/.gemini/config/mcp_config.json`.
