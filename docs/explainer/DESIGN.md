# Visual Identity — USDA FDC Skills Explainer (Data Drift)

## Style Prompt
Dark analytical canvas evoking data-terminal instrumentation. Near-black field, cyan as primary signal, electric purple as secondary, warm amber as flagged-state alert. Thin geometric rules and ticker-style counters. Motion is fluid, smooth, organic — continuous curves, never bouncy for its own sake. The viewer should feel they are watching real instrumentation telemetry, not marketing.

## Colors
- `#0a0a0a` — canvas (deep black, Data Drift canonical)
- `#06b6d4` — cyan (primary signal, headlines, active elements, SHIPPED_CLEAN)
- `#7c3aed` — electric purple (secondary, orbits, role accents, SHIPPED_PLATEAU)
- `#fbbf24` — warm amber (alert, NOT_SHIPPED, active underline)
- `#a1a1aa` — slate (body, mid-opacity rules)
- `#f4f4f5` — off-white (high-emphasis body)

## Typography
- Display & body: `JetBrains Mono` (weights 400–700). Mono keeps the data-terminal feel and makes counters tabular without extra CSS.
- Headlines use `font-variant-numeric: tabular-nums`.
- Body max-width wraps — never forced `<br>`.

## Motion
- GSAP signature: `sine.inOut`, `power2.out`, `power3.out`, `expo.out`. Smooth, continuous.
- No `elastic` or `back` overshoots on instrumentation/counter readouts.
- Offset first animation 0.1–0.3s from t=0.
- At least 3 different eases per scene.

## What NOT to Do
- No `#333`, `#3b82f6`, or default blues — stay on cyan `#06b6d4`.
- No linear full-screen gradients (H.264 banding) — radial or solid + glow only.
- No bouncy eases on counters/readouts (count deterministically).
- No cutesy icons; prefer thin-line geometric glyphs (unicode allowed).
- No forced `<br>` in body text; let `max-width` wrap.
- No exit animations except in the final scene (transitions handle exits).
