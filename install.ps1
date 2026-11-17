<#
.SYNOPSIS
    Antigravity Powerhouse 1-Click Installer
.DESCRIPTION
    Installs all runtimes (Node.js LTS, Git, GitHub CLI, Playwright Chromium),
    deploys global operating invariants (GEMINI.md), 37 curated skills, and MCP configs.
#>

$ErrorActionPreference = "Stop"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   Antigravity Powerhouse 1-Click Setup Installer" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Install Runtimes via winget
Write-Host "`n[1/5] Checking and installing prerequisite runtimes..." -ForegroundColor Yellow

$packages = @(
    @{ id = "OpenJS.NodeJS.LTS"; name = "Node.js LTS" },
    @{ id = "Git.Git"; name = "Git" },
    @{ id = "GitHub.cli"; name = "GitHub CLI" }
)

foreach ($pkg in $packages) {
    Write-Host "Verifying $($pkg.name)..." -NoNewline
    winget install --id $pkg.id -e --accept-source-agreements --accept-package-agreements | Out-Null
    Write-Host " [OK]" -ForegroundColor Green
}

# 2. Update User PATH for current session and future sessions
Write-Host "`n[2/5] Configuring environment paths..." -ForegroundColor Yellow
$userPath = [Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::User)
if ($userPath -notmatch "nodejs") {
    [Environment]::SetEnvironmentVariable("Path", $userPath + ";C:\Program Files\nodejs", [System.EnvironmentVariableTarget]::User)
}
$env:Path = "C:\Program Files\nodejs;C:\Program Files\Git\cmd;C:\Program Files\GitHub CLI;" + $env:Path

# 3. Install Playwright Chromium engine
Write-Host "`n[3/5] Installing Playwright Chromium browser engine..." -ForegroundColor Yellow
cmd.exe /c "npx -y playwright install chromium"

# 4. Deploy Antigravity Configuration
Write-Host "`n[4/5] Deploying Global Operating Invariants & Skills..." -ForegroundColor Yellow
$targetDir = "$HOME\.gemini\config"
if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Copy GEMINI.md
Copy-Item -Force "$scriptDir\GEMINI.md" "$targetDir\"
Write-Host " -> Deployed GEMINI.md (Invariants, Micro-CSS, .spec contract)" -ForegroundColor Green

# Copy LEARNINGS template if not exists
if (-not (Test-Path "$targetDir\LEARNINGS.md")) {
    Copy-Item -Force "$scriptDir\LEARNINGS.template.md" "$targetDir\LEARNINGS.md"
    Write-Host " -> Initialized LEARNINGS.md" -ForegroundColor Green
}

# Copy skills
Copy-Item -Recurse -Force "$scriptDir\skills" "$targetDir\"
Write-Host " -> Deployed 37 Curated Production Skills" -ForegroundColor Green

# Deploy mcp_config.json if not exists
if (-not (Test-Path "$targetDir\mcp_config.json")) {
    Copy-Item -Force "$scriptDir\mcp_config.template.json" "$targetDir\mcp_config.json"
    Write-Host " -> Initialized mcp_config.json template" -ForegroundColor Green
}

# 5. GitHub Authentication Prompt
Write-Host "`n[5/5] GitHub Setup & Authentication..." -ForegroundColor Yellow
Write-Host "To give your agent autonomous git push permissions, run:" -ForegroundColor White
Write-Host "    gh auth login" -ForegroundColor Cyan
Write-Host "    gh auth setup-git" -ForegroundColor Cyan

Write-Host "`n==========================================================" -ForegroundColor Cyan
Write-Host " [SUCCESS] Antigravity Powerhouse Setup is 100% Complete!" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
