---
version: 1.0.0
name: Physical Device & Interactive Walkthrough Simulator Archetype
description: |
  Specialized presentation pattern for demonstrating mobile apps, POS terminals, and responsive products
  inside a desktop web interface. Includes interactive phone chassis frame, ticket-stub confirmation cards,
  bilingual status toggles, and companion walkthrough state rails.

tokens:
  colors:
    canvas: "#f4ede4"               # Soft neutral studio backdrop
    device-bezel: "#0f172a"         # Phone outer titanium/slate frame
    device-screen-bg: "#f8fafc"     # Active simulated mobile screen
    ticket-bg: "#1e293b"            # Deep navy physical ticket stub
    ticket-text: "#ffffff"
    border-subtle: "rgba(0, 0, 0, 0.08)"

components:
  device_simulator_chassis:
    outer_frame: "w-[380px] h-[780px] bg-device-bezel rounded-[44px] p-3 shadow-2xl border-4 border-slate-700/60 flex flex-col relative mx-auto"
    notch_pill: "w-28 h-5 bg-black rounded-full mx-auto mb-2 shrink-0"
    screen_viewport: "flex-1 bg-device-screen-bg rounded-[32px] overflow-hidden flex flex-col"

  ticket_stub_receipt:
    container: "relative bg-ticket-bg text-ticket-text p-6 rounded-2xl shadow-md text-center overflow-hidden"
    perforated_punchout_left: "absolute left-0 top-1/2 -translate-y-1/2 -translate-x-1/2 w-5 h-5 rounded-full bg-device-screen-bg"
    perforated_punchout_right: "absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/2 w-5 h-5 rounded-full bg-device-screen-bg"
    token_display: "text-3xl font-black font-mono tracking-tight my-2 block"

  companion_walkthrough_rail:
    container: "w-80 p-6 flex flex-col gap-4 text-xs"
    state_pill_button: "px-3 py-1.5 rounded-full bg-white border border-slate-200 text-slate-700 hover:bg-slate-900 hover:text-white transition-all text-xs font-medium"
