---
version: 1.0.0
name: Swiss Editorial & Brand Catalog Archetype
description: |
  High-end lifestyle, collector showcase, and editorial brand commerce. Features linen canvas surfaces,
  bold contrast typography (Grotesque Sans paired with elegant serif/script accents), clean 1px borders,
  and high-impact oversized footer watermarks.

tokens:
  colors:
    canvas: "#f5f4ef"               # Warm organic linen
    surface: "#ffffff"              # Pure white cards
    surface-dark: "#171717"         # Void charcoal for high-contrast breaks
    border: "rgb(0 0 0 / 0.08)"
    
    text-primary: "#171717"
    text-secondary: "#525252"
    text-muted: "#a3a3a3"

    # Editorial Accents
    accent-vermilion: "#ea580c"     # Electric Swiss orange / red
    accent-amber: "#d97706"         # Warm ochre
    accent-olive: "#4d7c0f"         # Muted botanical green

  typography:
    display-hero:
      font-family: "'Cabinet Grotesk', -apple-system, sans-serif"
      weight: "800"
      tracking: "-0.04em"
      line-height: "0.95"
    display-accent-italic:
      font-family: "'Playfair Display', Georgia, serif"
      style: "italic"
      weight: "400"
    meta-tabular:
      font-family: "'JetBrains Mono', monospace"
      size: "11px"
      tracking: "0.05em"
      tabular: true

components:
  catalog_product_card:
    card: "group p-4 bg-surface rounded-none border border-border flex flex-col justify-between transition-all hover:border-black"
    image_frame: "aspect-square w-full bg-slate-100 overflow-hidden relative"
    badge_pill: "absolute top-2 left-2 px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider bg-black text-white"

  oversized_brand_footer:
    container: "bg-surface-dark text-white px-8 py-16 border-t border-white/10"
    watermark_title: "text-[12vw] font-black tracking-tighter opacity-15 select-none leading-none block"
    meta_columns: "grid grid-cols-4 gap-8 text-xs text-slate-400 mt-8"
