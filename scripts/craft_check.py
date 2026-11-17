#!/usr/bin/env python3
"""
craft_check.py - Antigravity Craft & Living Spec Enforcement Engine
Zero-dependency architectural & visual quality gate.
Exits 1 on HARD ERRORS (spec drift, layout-breaking CSS, banned AI tropes).
Exits 0 on clean runs or non-fatal WARNINGS.
"""

import sys
import os
import re
from pathlib import Path
import argparse

REQUIRED_SPEC_FILES = [
    "1_PRD.md",
    "2_TRD.md",
    "3_DATABASE_SCHEMA.md",
    "4_BACKEND_SCHEMA.md",
    "5_USER_FLOW.md",
    "6_UI_UX_DESIGN.md",
    "7_IMPLEMENTATION_PLAN.md",
    "8_DECISION_LEDGER.md",
]

# Source files to scan for code craft violations
SCANNABLE_EXTENSIONS = {".tsx", ".jsx", ".html", ".vue", ".svelte", ".astro", ".css", ".scss"}

# Ignored directories
IGNORED_DIRS = {
    "node_modules", ".git", ".next", "dist", "build", "out", ".venv", "venv", 
    "__pycache__", "skills", "assets", "vendor", ".spec"
}

# Standard app source directories to prioritize when present
APP_SOURCE_DIRS = ["src", "app", "pages", "components", "lib", "routes"]

# Banned AI marketing buzzwords (Warning)
BUZZWORDS = ["supercharge", "seamless", "seamlessly", "unlock", "game-changing", "revolutionary"]

class Reporter:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, category: str, message: str, file_path: str = "", line_no: int = 0):
        loc = f" ({file_path}:{line_no})" if file_path and line_no else f" ({file_path})" if file_path else ""
        self.errors.append(f"[\033[91mERROR\033[0m] [{category}] {message}{loc}")

    def warning(self, category: str, message: str, file_path: str = "", line_no: int = 0):
        loc = f" ({file_path}:{line_no})" if file_path and line_no else f" ({file_path})" if file_path else ""
        self.warnings.append(f"[\033[93mWARN\033[0m]  [{category}] {message}{loc}")

    def summary(self) -> int:
        print("\n==========================================================")
        print("          ANTIGRAVITY CRAFT & SPEC AUDIT REPORT")
        print("==========================================================")
        
        if not self.errors and not self.warnings:
            print("\033[92m[PASS] All craft, layout, motion, and spec invariants intact.\033[0m\n")
            return 0

        for w in self.warnings:
            print(w)
        for e in self.errors:
            print(e)

        print("\n----------------------------------------------------------")
        print(f"Total Errors: {len(self.errors)} | Total Warnings: {len(self.warnings)}")
        
        if self.errors:
            print("\033[91m[FAIL] Audit failed with blocking errors. Fix before landing task.\033[0m\n")
            return 1
        else:
            print("\033[93m[PASS WITH WARNINGS] Clean execution with advisory notes.\033[0m\n")
            return 0


def check_spec(root: Path, reporter: Reporter):
    spec_dir = root / ".spec"
    if not spec_dir.exists() or not spec_dir.is_dir():
        reporter.error("SPEC", f"Missing living specification folder: {spec_dir.resolve()}")
        return

    for filename in REQUIRED_SPEC_FILES:
        filepath = spec_dir / filename
        if not filepath.exists():
            reporter.error("SPEC", f"Missing required specification document: {filename}")
        elif filepath.stat().st_size == 0:
            reporter.error("SPEC", f"Specification document is empty: {filename}")

    # Check 6_UI_UX_DESIGN.md has UX Laws documented
    ui_spec = spec_dir / "6_UI_UX_DESIGN.md"
    if ui_spec.exists() and ui_spec.stat().st_size > 0:
        ui_content = ui_spec.read_text(encoding="utf-8", errors="ignore").lower()
        ux_laws_found = [law for law in ["jakob", "hick", "miller", "fitts", "restorff", "proximity", "similarity", "common region"] if law in ui_content]
        if not ux_laws_found:
            reporter.warning("SPEC", "6_UI_UX_DESIGN.md missing explicit niche-grounded Laws of UX (e.g. Jakob's, Hick's, Fitts's, Miller's).")

    # Check 2_TRD.md documents scale/resilience
    trd_spec = spec_dir / "2_TRD.md"
    if trd_spec.exists() and trd_spec.stat().st_size > 0:
        trd_content = trd_spec.read_text(encoding="utf-8", errors="ignore").lower()
        if not any(k in trd_content for k in ["resilience", "concurrency", "error boundary", "scale", "pool"]):
            reporter.warning("SPEC", "2_TRD.md missing concurrency, resilience, or error boundary strategy.")

    # Check 8_DECISION_LEDGER.md has content
    ledger = spec_dir / "8_DECISION_LEDGER.md"
    if ledger.exists() and ledger.stat().st_size > 0:
        content = ledger.read_text(encoding="utf-8", errors="ignore")
        if not re.search(r"\d{4}-\d{2}-\d{2}", content):
            reporter.warning("SPEC", "8_DECISION_LEDGER.md contains no ISO-dated architecture records (YYYY-MM-DD)")


def scan_code_files(root: Path, reporter: Reporter):
    for current_dir, dirs, files in os.walk(root):
        # Prune ignored directories in-place
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith(".")]
        
        for file in files:
            path = Path(current_dir) / file
            if path.suffix.lower() not in SCANNABLE_EXTENSIONS:
                continue

            try:
                lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
            except Exception:
                continue

            for idx, line in enumerate(lines, start=1):
                raw = line.strip()
                if not raw or raw.startswith("//") or raw.startswith("/*") or raw.startswith("*"):
                    continue

                # 1. Layout & Mobile: Raw 100vh check
                if re.search(r"(?<!d)100vh\b", raw):
                    # Flag 100vh if not preceded by 'd' (e.g. 100dvh)
                    reporter.error("LAYOUT", "Banned '100vh' detected (breaks on mobile Safari/Chrome toolbars). Use '100dvh'.", str(path), idx)

                # 2. Layout: Arbitrary Tailwind padding violating 4px grid (e.g. p-[11px], py-[13px])
                odd_pad = re.search(r"\b(?:p|px|py|pt|pb|pl|pr)-\[(\d+)px\]", raw)
                if odd_pad:
                    px_val = int(odd_pad.group(1))
                    if px_val % 4 != 0:
                        reporter.error("LAYOUT", f"Arbitrary padding '{odd_pad.group(0)}' breaks the 4px spacing grid.", str(path), idx)

                # 3. Motion: Banned ease-in on UI transitions/entrances
                if re.search(r"['\"]?ease-in['\"]?(?!\w)", raw) and not re.search(r"ease-in-out", raw):
                    reporter.error("MOTION", "Banned 'ease-in' transition detected. Use snappy 'ease-out' or spring curves.", str(path), idx)

                # 4. Motion: Transition duration > 300ms on interactive controls
                duration_match = re.search(r"(?:duration|transition.*duration)[:\s-]+(\d{3,4})ms", raw)
                if duration_match:
                    ms_val = int(duration_match.group(1))
                    if ms_val > 300:
                        reporter.warning("MOTION", f"Transition duration {ms_val}ms exceeds 300ms craft threshold for interactive UI.", str(path), idx)

                # 5. Typography: Trailing period inside button or heading text
                # Matches JSX: <button ...>Click Here.</button> or <h1>Headline.</h1>
                btn_period = re.search(r"<(?:button|h[1-6]|span|a)[^>]*>[^<]*[a-zA-Z0-9]+(\.)\s*</(?:button|h[1-6]|span|a)>", raw)
                if btn_period:
                    reporter.error("TYPOGRAPHY", "Trailing period detected on title or interactive control.", str(path), idx)

                # 6. AI Slop: Decorative emoji badges in buttons
                emoji_button = re.search(r"<button[^>]*>[^<]*(?:🚀|✨|🔥|🎉|💡|⚡)[^<]*</button>", raw)
                if emoji_button:
                    reporter.error("AI_SLOP", "Emoji badge detected inside action button control (banned AI trope).", str(path), idx)

                # 7. AI Slop: Marketing buzzwords in user-facing copy
                for buzz in BUZZWORDS:
                    if re.search(rf"\b{buzz}\b", raw, re.IGNORECASE) and "<" in raw and ">" in raw:
                        reporter.warning("COPY", f"AI buzzword '{buzz}' detected in UI copy. Say plainly what the feature does.", str(path), idx)

                # 8. Style: Hard block shadows without neo-brutalist exemption
                if re.search(r"box-shadow:\s*\d+px\s+\d+px\s+0", raw) and "neo-brutalist" not in raw.lower():
                    reporter.warning("STYLE", "Hard block shadow detected without 'neo-brutalist' exemption comment.", str(path), idx)


def audit_pattern(root: Path, pattern: str, reporter: Reporter):
    """Exhaustive multi-file regex inventory for codebase-wide refactors."""
    regex = re.compile(pattern)
    matches_found = []
    for current_dir, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith(".")]
        for file in files:
            path = Path(current_dir) / file
            if path.suffix.lower() not in SCANNABLE_EXTENSIONS and path.suffix.lower() not in {".ts", ".js", ".json", ".md"}:
                continue
            try:
                lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
                for idx, line in enumerate(lines, start=1):
                    if regex.search(line):
                        matches_found.append((str(path), idx, line.strip()))
            except Exception:
                continue

    if matches_found:
        print(f"\n[INVENTORY] Found {len(matches_found)} occurrences matching pattern: '{pattern}'")
        for f, l, content in matches_found:
            print(f"  -> {f}:{l} | {content[:80]}")
        reporter.error("PATTERN_AUDIT", f"Codebase still contains {len(matches_found)} un-refactored occurrences of '{pattern}'.")
    else:
        print(f"\n[INVENTORY] 0 occurrences of pattern '{pattern}' found. Clean eradication verified.")


def main():
    parser = argparse.ArgumentParser(description="Antigravity Craft & Living Spec Enforcement Engine")
    parser.add_argument("path", nargs="?", default=".", help="Target project root directory (default: current directory)")
    parser.add_argument("--skip-spec", action="store_true", help="Skip .spec/ folder integrity audit")
    parser.add_argument("--pattern", type=str, default="", help="Enforce zero occurrences of a deprecated pattern across the codebase")
    args = parser.parse_args()

    target_root = Path(args.path).resolve()
    print(f"\nScanning workspace: {target_root}")
    
    reporter = Reporter()

    if args.pattern:
        audit_pattern(target_root, args.pattern, reporter)

    if not args.skip_spec:
        check_spec(target_root, reporter)
    
    scan_code_files(target_root, reporter)

    exit_code = reporter.summary()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
