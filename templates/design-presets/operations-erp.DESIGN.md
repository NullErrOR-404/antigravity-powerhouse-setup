---
version: 1.0.0
name: High-Density Operations & ERP (JavaDript Archetype)
description: |
  Specialized design system for multi-location inventory, logistics networks, warehouse management,
  and financial subledgers. Built on high-density information architecture, quiet light-mode canvas,
  tabular numeric precision, SVG flow connectors (Sankey-lite), and horizontal stacked allocation bars.

tokens:
  colors:
    canvas: "#f8f9fa"
    surface: "#ffffff"
    surface-subdued: "#f1f3f5"
    surface-inverse: "#111827"
    border: "rgb(0 0 0 / 0.08)"
    border-subdued: "rgb(0 0 0 / 0.04)"
    
    # Text tiers
    text-primary: "#111827"
    text-secondary: "#4b5563"
    text-muted: "#9ca3af"
    text-inverse: "#f9fafb"

    # Status & Allocation Accents
    accent-available: "#15803d"      # Forest green (available stock)
    accent-committed: "#1d4ed8"      # Deep cobalt blue (committed orders)
    accent-transit: "#6b7280"        # Neutral grey (in transit)
    accent-warning: "#d97706"        # Amber
    accent-danger: "#dc2626"         # Crimson red

    # Channel & Location Identity Pills
    entity-brown: "#9a3412"          # Roastery / Production
    entity-blue: "#1e40af"           # 3PL West Coast
    entity-teal: "#0f766e"           # 3PL East Coast
    entity-purple: "#6b21a8"         # Co-packing
    entity-navy: "#1e1b4b"           # Amazon FBA
    entity-green: "#166534"          # Shopify

  typography:
    font-family-sans: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    font-family-mono: "'JetBrains Mono', 'SF Mono', Consolas, monospace"
    metrics:
      display-metric:
        size: "28px"
        weight: "700"
        tracking: "-0.03em"
        tabular: true
      section-heading:
        size: "14px"
        weight: "600"
        tracking: "-0.01em"
      body-dense:
        size: "12px"
        weight: "400"
        line-height: "1.4"
      caption-micro:
        size: "10px"
        weight: "500"
        tracking: "0.02em"
        transform: "uppercase"

structural_patterns:
  layout:
    type: "asymmetric-multi-pane"
    sidebar_width: "180px"
    grid_gap: "12px"
    card_padding: "16px"
    card_radius: "8px"
    card_border: "1px solid rgb(0 0 0 / 0.08)"
    card_shadow: "0 1px 2px 0 rgb(0 0 0 / 0.03)"

  components:
    # 1. Flow-Node Sync (Sankey-Lite)
    flow_node_sync:
      description: "Visualizes multiple disparate inventory sources converging into a centralized ledger"
      left_nodes: "Stack of source badges with sync timestamps and item counts"
      connector_curves: "SVG bezier curves (M x1 y1 C cx1 cy1, cx2 cy2, x2 y2) with stroke #d1d5db"
      target_node: "High-contrast dark inverted card (bg-neutral-900 text-white) showing total aggregate units"

    # 2. Horizontal Stacked Allocation Bars
    allocation_bar:
      description: "Two-tone proportional bar showing Committed vs Available vs In-Transit"
      height: "8px"
      radius: "9999px"
      segments:
        - name: "committed"
          color: "var(--accent-committed)"
        - name: "available"
          color: "var(--accent-available)"
        - name: "transit"
          color: "var(--accent-transit)"

    # 3. Micro-Data Tables (FIFO Lots)
    data_table:
      row_height: "32px"
      border_bottom: "1px solid rgb(0 0 0 / 0.04)"
      text_align_numbers: "right"
      font_variant: "tabular-nums"
      hover_state: "bg-surface-subdued/50"

usage_guidelines:
  when_to_use:
    - "Multi-warehouse inventory, supply chain, and logistics tracking"
    - "Financial reconciliation, subledgers, and landed-cost calculations"
    - "ERP systems, wholesale order processing, and manufacturing batches"
  anti_patterns:
    - "DO NOT use circular donut or pie charts when comparing inventory splits; use horizontal stacked bars."
    - "DO NOT use dead untinted grays; use warm slate or zinc neutral surfaces."
    - "DO NOT hide sync timestamps or reconciliation variances; state them plainly beside totals."
