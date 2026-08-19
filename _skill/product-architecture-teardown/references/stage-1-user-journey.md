# Stage 1 — User journey evidence

Use this stage to reconstruct what the user experienced from initial input to the latest observable outcome. Do not explain hidden Agent implementation yet.

## Questions to answer

- What requirements, scripts, styles, references, uploads, forms, models, ratios, languages, durations, and other constraints did the user provide?
- What did the product show immediately after each action, confirmation, modification, return, retry, or interruption?
- What changed in chat, canvas, tasks, assets, history, preview, account, and billing?
- Where could the user continue, revise, choose an alternative, stop, return, or recover?
- Did “completed” claims agree with actual assets and preview state?

## Procedure

1. Record scope, snapshot time, entry page, access level, and forbidden actions.
2. Go to the earliest available event and establish the requirement baseline.
3. For every user action, record the immediately following visible response and state delta.
4. After every confirmation or modification, identify created, changed, stale, invalidated, or missing assets.
5. For every completion claim, check task, canvas, asset/history, context/state, and preview independently.
6. Capture every visible branch. Mark unobserved failure, balance, safety, and interruption paths `【未知】` rather than inventing them.
7. Finish the evidence table before drawing the journey.

## Evidence table

| Stage | User goal | User action | Page feedback | User decision | Page/asset state change | Friction | Evidence |
|---|---|---|---|---|---|---|---|

Each evidence cell must contain an evidence ID plus a page phrase, component, Agent, asset, state, error, or screenshot ID.

## Three-lane journey

Use exactly three lanes when drawing the journey:

1. `用户`: goal, action, decision, observable emotion signal, likely thought.
2. `产品界面`: reply, form, button, card, task, error, preview, account, or billing state.
3. `系统结果`: structured state, task result, asset, version, reference, context write, or missing result.

Use diamonds for decisions and label every branch. Include normal, modification/correction, failure, interruption, retry, and balance paths only when evidenced. A required but unobserved path is dashed and labeled `待验证/未知`. Place evidence IDs beside substantive nodes.

## Experience layer

| Stage | Observable emotion signal | Likely thought/feeling | Pain point | Level | Product opportunity |
|---|---|---|---|---|---|

Thought and feeling are normally `【合理推断】` unless the user said them. Opportunities are `【建议设计】`.

## Output order

1. Viewing scope.
2. Inaccessible or unconfirmed evidence.
3. Journey evidence table.
4. Three-lane journey diagram.
5. Normal, modification, failure, interruption, and recovery paths.
6. Emotion, thoughts, pain points, and editable gaps.
7. Product opportunities.
8. Three highest-value experience questions.

## Gate

- chronology has no unexplained gap;
- key actions, buttons, forms, assets, errors, and confirmations have IDs;
- actual state changes are separate from Agent claims;
- all visible surfaces were reconciled;
- unobserved branches are unknown, not facts;
- the user has accepted this scope, or an explicitly authorized end-to-end run has passed the checklist internally.

Do not proceed to Agent contracts until this gate passes.
