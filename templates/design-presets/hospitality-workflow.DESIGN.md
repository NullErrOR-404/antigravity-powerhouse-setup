---
version: 1.0.0
name: Hospitality & Order Workflow Archetype
description: |
  Clean, warm organic styling for restaurants, cafes, bakeries, QR ordering, and table management systems.
  Features soft pistachio/matcha accents, step-wizard progress flows, scannable QR token cards, and light borders.

tokens:
  colors:
    canvas: "#fbfbfa"
    surface: "#ffffff"
    surface-subdued: "#f4f6f0"
    border: "rgb(0 0 0 / 0.07)"
    text-primary: "#1c1917"
    text-secondary: "#57534e"
    text-muted: "#a8a29e"

    # Brand & Status Accents
    accent-brand: "#65a30d"         # Fresh olive / matcha green
    accent-brand-deep: "#15803d"    # Forest green (actions & verified checks)
    accent-pill-bg: "#ecfccb"       # Soft green badge background
    accent-pill-text: "#3f6212"     # Dark olive text
    accent-callout-bg: "#f0fdf4"    # Ambient callout container
    accent-callout-border: "#dcfce7"

  typography:
    font-sans: "Inter, -apple-system, system-ui, sans-serif"
    headline:
      weight: "700"
      tracking: "-0.02em"
    label:
      weight: "600"
      size: "11px"
      transform: "uppercase"
      tracking: "0.05em"

components:
  step_workflow_bar:
    container: "grid grid-cols-3 gap-3 p-4 rounded-xl bg-surface border border-border"
    step_item: "flex items-center justify-between p-3 rounded-lg bg-surface-subdued border border-black/[0.04]"
    step_badge: "w-6 h-6 rounded-full bg-accent-callout-bg text-accent-brand-deep flex items-center justify-center font-bold text-xs"

  qr_token_card:
    card: "p-5 rounded-2xl bg-surface border border-border shadow-sm text-center flex flex-col items-center"
    qr_frame: "p-4 rounded-xl bg-white border border-black/[0.06] shadow-inner inline-block"
    table_pill: "px-3 py-1 rounded-full bg-surface-subdued text-text-primary text-xs font-bold mb-2"

  contextual_callout:
    box: "p-4 rounded-xl bg-accent-callout-bg border border-accent-callout-border text-xs text-text-secondary leading-relaxed"
