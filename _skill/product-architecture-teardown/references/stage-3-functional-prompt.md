# Stage 3 — Functional-equivalent Agent prompt

Use this stage for one Agent whose observable contract is already complete. The deliverable reproduces behavioral boundaries; it is not the vendor’s official prompt.

## Boundary interview

Answer with evidence before drafting:

1. What problem does the Agent solve?
2. When does it take over?
3. Who or what triggers it?
4. Who receives its output?
5. What belongs to it?
6. What is outside its boundary?
7. Can user edits retrigger it?
8. When must it stop?
9. When may it auto-continue?
10. Which actions require user confirmation?

## Output-contract check

Cover natural-language replies, page components, assets, global-context writes, and downstream tasks. A usable prompt must govern all five, not only chat wording.

## State machine

Adapt names to the evidence, but cover these semantics:

| State | Entry | Allowed | Forbidden | Exit |
|---|---|---|---|---|
| `waiting_input` | required input missing | ask, read context | paid generation | input complete |
| `planning` | input complete | check dependencies, form plan | claim asset completion | plan executable/confirmable |
| `waiting_confirm` | confirmation gate | show scope/cost/difference, wait | bypass user | confirm/modify/interrupt |
| `executing` | preconditions satisfied | call tool, record run | duplicate non-idempotent call | success/failure/interrupt |
| `validating` | tool returned | inspect asset and state | trust success wording alone | pass/fail |
| `retrying` | recoverable failure | retry within policy | infinite retry | success/limit |
| `completed` | all completion checks pass | report and hand off | mutate confirmed asset | new change/handoff |
| `failed` | unrecoverable/limit | explain and offer recovery | pretend success | retry/end |
| `interrupted` | user interrupted | stop new calls, preserve progress | silent paid continuation | resume/end |
| `handoff` | payload complete | deliver references and unresolved items | drop dependencies | recipient accepts |

The diagram must show normal, modification, failure, retry, interruption, and handoff paths. Unknown product behavior remains unknown; robust additions are `【建议规则】`.

## Rule classes

- `【事实规则】`: directly supported behavior to preserve.
- `【推断规则】`: necessary explanation of stable visible behavior.
- `【建议规则】`: added for reliability, safety, recovery, or clarity.
- `【未知】`: not enforceable as a product fact.

Rules should cover identity, goal, boundary, inputs, context reads/writes, workflow, tools, preconditions, confirmation, validation, modification, rollback, failure, retry, interruption, idempotency, billing, handoff, completion, and output format.

## Prompt structure

1. Agent name.
2. Role.
3. Core goal.
4. Task boundary.
5. Input contract.
6. Global-context protocol.
7. Workflow.
8. Tool-use rules.
9. User-confirmation rules.
10. Result validation.
11. Modification and rollback.
12. Error, retry, interruption, and billing.
13. State machine.
14. Downstream handoff.
15. Completion conditions.
16. Output formats.

Unknown fields use semantic placeholders labeled `推导设计`. Unknown tools use `<功能性名称>` and `非官方工具名`.

## Completion conditions

The Agent may not enter completed merely because it said so. Require, as applicable:

- required inputs and confirmations recorded;
- required assets exist, are viewable, and have stable references;
- tool result agrees with page/task/asset state;
- global-context write succeeded or is explicitly unknown;
- user constraints can be validated against the result;
- downstream payload is complete and accepted;
- unresolved items are carried forward visibly.

## Minimum behavioral tests

| Test | Input | Initial state | Expected judgment | Expected tool action | Expected state | Forbidden behavior |
|---|---|---|---|---|---|---|
| Complete normal input |  |  |  |  |  |  |
| Missing required input |  |  |  |  |  |  |
| Local modification |  |  |  |  |  |  |
| Tool failure |  |  |  |  |  |  |
| User interruption |  |  |  |  |  |  |
| Page/context conflict |  |  |  |  |  |  |
| Duplicate request |  |  |  |  |  |  |
| Downstream cannot start |  |  |  |  |  |  |

## Output order

Evidence range → boundary interview → input contract → output contract → tool contract → state machine → rule register → functional-equivalent prompt → rule/evidence traceability → tests → unknowns.

## Gate

- each important rule is traceable to evidence or a design rationale;
- fact and design are not mixed;
- paid, destructive, overwriting, publishing, batch, and downstream actions have explicit gates;
- validation does not trust the Agent or tool alone;
- upstream edits preserve versions and invalidate/recompute the correct scope when supported or recommended;
- failure, balance, safety, state-write failure, interruption, duplicate request, and downstream failure are handled;
- work stops after this one Agent until the architecture stage is authorized.
