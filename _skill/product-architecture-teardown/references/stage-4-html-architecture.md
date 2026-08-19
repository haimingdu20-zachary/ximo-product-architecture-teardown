# Stage 4 — Standalone HTML product architecture

This is the final stage. Combine the first three artifacts into one evidence-layered architecture without turning analysis templates into claims about the product.

## Five aligned end-to-end flows

Trace the same representative task across:

1. User interaction: input, confirm, modify, interrupt.
2. Agent control: takeover, judgment, wait, retry, handoff.
3. Tool calls: trigger, parameters, result, validation, failure recovery.
4. Data/context: reads, writes, versions, confirmations, states, errors, billing.
5. Assets: creation, reference, reuse, invalidation, preview, export.

| Step | Trigger | Handler | Reads | Judgment | Tool | Result/asset | State write | User gate | Downstream | Failure branch | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Nine-layer architecture

Every component carries an evidence level and adjacent ID or a clear design rationale.

| Layer | Inspect |
|---|---|
| 1. User and channels | users, login, permission, plan, balance, preferences, private assets, history, publishing channels |
| 2. Interaction/workbench | chat, Agent identity, canvas, cards, forms, confirmation, tasks, preview, editor, history, errors |
| 3. Product application | projects, scripts, entities, storyboard, image/video/audio, assets, versions, publishing |
| 4. Agent/orchestration | controller, specialist Agents, triggers, workflow, state machine, gates, handoff, interruption, rollback, retry, idempotency |
| 5. Tools/services | context read/write, parsing, generation, composition, preview/export, safety, balance, billing, storage |
| 6. Model access/routing | text/image/video/audio models, visible names, capabilities, limits, cost, latency, failure, switching |
| 7. Global context/data | user, project, script, entities, storyboard, asset references, tasks, confirmations, state, error, billing, feedback |
| 8. Knowledge/public assets | style/template libraries, domain knowledge, prompts, model capability rules, safety/copyright/billing, public/private separation |
| 9. Infrastructure/governance | authentication, permissions, storage, delivery, async/task capability, gateway, logs, tracing, evaluation, cost, privacy |

Concrete databases, queues, languages, clouds, and frameworks are `【未知】` unless directly evidenced. It is acceptable to describe required capability, possible option, and recommended design separately.

## Context architecture

Use semantic domains, not alleged real field names:

| Domain | Typical content | Producers | Consumers | Version/invalidation | Level/evidence |
|---|---|---|---|---|---|
| UserContext | identity, language, plan, balance, permissions, private assets | user/account | orchestration, billing, assets | permission-dependent tasks |  |
| ProjectConfig | type, ratio, language, style, model settings | user/planning Agent | downstream Agents | generated assets/previews |  |
| ScriptContext | original and structured script versions | user/writer | design/storyboard/media | entities/storyboards/media |  |
| EntityContext | characters, scenes, props, identities, voices | design functions | storyboard/media | referenced shots |  |
| StoryboardContext | shot plan, prompts, entity/asset references | storyboard function | image/video/audio | shot assets/composition |  |
| AssetContext | media URI/reference, type, version, status | tools/asset service | UI, Agents, composition | preview/final output |  |
| WorkflowState | current Agent/task/gate/error | orchestration/tools | UI and Agents | downstream execution |  |
| BillingContext | balance, estimate, hold, debit, refund | billing capability | orchestration/tools | paid tasks |  |
| EvaluationContext | feedback, validation, failure reason | user/validator | retry/routing/analysis | current or future work |  |

Label all names as semantic architecture templates unless the UI exposes the official schema.

## Knowledge, models, data, and sequence

- Separate project data, user-private assets, platform-public assets, reusable knowledge/rules, and feedback.
- Record only visible model names/capabilities. Do not infer dynamic routing from one selector.
- Include a data-entity table and an ER diagram. Entity names are semantic templates, not table names.
- Include an end-to-end sequence covering input, parameter confirmation, context write, Agent and tool actions, async wait, asset writeback, user validation, modification, failure, interruption, billing, and handoff.
- Include one panoramic diagram from the nine layers. Use line semantics: solid confirmed, dashed inferred, distinct dotted/accent recommended. Unknown and conflicts remain visible.

## As-Is / To-Be separation

| Dimension | As-Is evidence | Problem | To-Be design | Acceptance metric |
|---|---|---|---|---|
| State source |  |  | unified task/asset/preview truth | conflict count, propagation delay |
| Quality |  |  | constraint and media validation | validation pass rate |
| Asset dependency |  |  | version/dependency graph and local recompute | stale-asset miss rate |
| Retry/billing |  |  | idempotency, estimate/hold/refund | duplicate-charge rate |
| Completion gate |  |  | asset + state + confirmation + handoff | false-completion rate |
| Observability |  |  | traceable runs and failure causes | diagnosability, recovery time |

Do not place recommended services inside an As-Is diagram without `【建议设计】` styling.

## Required HTML section order

1. Executive summary.
2. Evidence sources and gaps.
3. Core functional domains.
4. End-to-end five-flow table.
5. Nine-layer product architecture.
6. Agent, tool, and context relationships.
7. Global-context architecture.
8. Knowledge and public/private asset architecture.
9. Model access and routing.
10. Technology capability/option table.
11. Data entities and ER diagram.
12. End-to-end sequence diagram.
13. Panoramic architecture diagram.
14. Current architecture As-Is.
15. Recommended architecture To-Be.
16. Key architecture risks.
17. Architecture-component/evidence traceability.
18. Unresolved questions and stopping point.

## HTML delivery requirements

- Deliver one standalone `.html` file with a descriptive product filename.
- State that it is evidence-led analysis, not an official product artifact.
- Use a sticky or compact table of contents and put evidence gaps near the top.
- Use visible text chips for the four evidence levels; do not rely on color alone.
- Put evidence IDs inside or beside substantive diagram nodes and table rows.
- Use semantic HTML, adequate contrast, desktop/tablet/mobile responsiveness, horizontal scroll for wide tables, and print CSS.
- Prefer inline SVG or native HTML/CSS diagrams. If Mermaid is used, include readable source or a static fallback; do not require a CDN for basic comprehension.
- Add copy buttons only when useful and keep scripts inline and dependency-free.
- Avoid fixed-height content that clips evidence or diagrams.
- Keep the final file understandable offline; use relative local evidence links and verify targets.

## Validation

Run:

```bash
python3 scripts/validate_delivery.py /absolute/path/to/report.html
```

Then inspect representative desktop and narrow widths when a safe visual preview is available. Verify unique IDs, readable diagrams, no overflow outside intended containers, local evidence links, print behavior, and absence of placeholders.

The final answer must link the absolute HTML path and summarize included artifacts, evidence boundary, the strongest architecture finding, and major unresolved gap.
