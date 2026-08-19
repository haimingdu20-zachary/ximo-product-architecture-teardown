# Stage 5 — Layered architecture visual

## Purpose

Create an independent, offline-readable HTML visual that lets a reader grasp the product's nine layers, cross-cutting controls, and one representative end-to-end flow without reading every table in stage 4. This file summarizes the evidence-backed architecture; it must not introduce new hidden-system claims.

## Required content

1. Shared navigation linking files 01–05.
2. Title, snapshot date, evidence scope, and an explicit legend for `【已确认】`, `【合理推断】`, `【建议设计】`, `【未知】`.
3. Compact KPI cards only for defensible counts. A count of report components is acceptable; an unevidenced product metric is not.
4. One nine-layer map, ordered consistently with stage 4:
   - L1 users and channels
   - L2 interaction and workspace
   - L3 product applications
   - L4 Agents and orchestration
   - L5 tools and services
   - L6 model access and routing
   - L7 global context and data
   - L8 knowledge and shared assets
   - L9 infrastructure and governance
5. A cross-cutting concerns section. Choose only concerns supported or required by the target product, such as privacy, authorization, observability, safety, billing, versioning, human review, accessibility, or fulfillment.
6. One representative end-to-end trace aligning the same scenario across five flows: user interaction, Agent control, tools/services, context/data, and asset/output.
7. Evidence-ID table that points back to stages 1–4.
8. Evidence-level distribution. Use exact counts when available; otherwise state that the distribution is qualitative. Never invent percentages.
9. Unresolved questions and the lowest-risk evidence needed next.
10. A short reading guide explaining bottom-up and top-down interpretations.

## Visual grammar

- Give every architecture box an evidence class or adjacent evidence label.
- Use a stable color mapping across the page; do not rely on color alone—include text labels and borders.
- Mark cross-cutting concerns distinctly from layers, for example with dashed borders.
- Keep the nine layers readable as HTML/CSS blocks or inline SVG. Avoid remote scripts, fonts, stylesheets, and image dependencies.
- Provide horizontal scrolling for wide figures, responsive behavior for narrow screens, and print CSS.
- Keep file 05 visually denser and shorter than file 04. It is a map and reading aid, not a second full report.

## Quality gate

- All nine layers appear exactly once in the main map.
- At least one component in each layer has an evidence level.
- The representative trace includes all five flows and names the scenario.
- Cross-cutting concerns are separated from layers.
- Evidence IDs resolve to the shared ledger or earlier files.
- No box converts an unknown or suggested component into a confirmed one.
- Navigation links to all five HTML files exist and use the actual filenames.
- The file is standalone, responsive, printable, and has no unfinished placeholders.
