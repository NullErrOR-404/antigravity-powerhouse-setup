---
version: 1.0.0
name: Night Executive & Institutional Analytics Archetype
description: |
  High-density dark executive dashboard system for large-scale institutional analytics, university ERPs,
  hospital networks, and complex financial monitoring. Combines twilight deep dark canvas with vibrant KPI sparks,
  dual-metric spline curves, and radial donut progress indicators.

tokens:
  colors:
    canvas: "#0b0f19"               # Deep twilight navy-black
    surface: "#111827"              # Surface card elevation 1
    surface-elevated: "#1f293d"     # Interactive hover & modal layer
    border: "rgb(255 255 255 / 0.08)"
    border-subdued: "rgb(255 255 255 / 0.04)"
    
    text-primary: "#f9fafb"
    text-secondary: "#94a3b8"
    text-muted: "#64748b"

    # KPI & Metric Accents
    accent-blue: "#3b82f6"          # Primary volume
    accent-emerald: "#10b981"       # Positive collection / target
    accent-amber: "#f59e0b"         # Outstanding dues / warnings
    accent-rose: "#ef4444"          # Exceptions / alerts / drops
    accent-purple: "#8b5cf6"        # AI summary & intelligence pill

    # Executive Hero Gradient
    hero-gradient: "linear-gradient(135deg, #1e3a8a 0%, #312e81 50%, #4c1d95 100%)"

components:
  hero_executive_banner:
    container: "p-6 rounded-2xl bg-gradient-to-r from-blue-950 via-indigo-950 to-purple-950 border border-white/10 text-white relative overflow-hidden"
    action_pill: "px-3 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 backdrop-blur-md text-xs font-semibold text-white border border-white/20"

  kpi_metric_strip:
    card: "p-4 rounded-xl bg-surface border border-border flex flex-col justify-between"
    metric_number: "text-2xl font-bold font-mono tracking-tight tabular-nums text-text-primary"
    sparkline_container: "h-6 w-full mt-2"

  spline_chart_card:
    container: "p-5 rounded-xl bg-surface border border-border"
    spline_curve_primary: "stroke-accent-rose stroke-2 fill-none"
    spline_curve_forecast: "stroke-slate-400 stroke-2 stroke-dashed fill-none"

  radial_donut_panel:
    container: "p-5 rounded-xl bg-surface border border-border flex items-center gap-6"
    donut_segment_paid: "#10b981"
    donut_segment_partial: "#f59e0b"
    donut_segment_overdue: "#ef4444"
