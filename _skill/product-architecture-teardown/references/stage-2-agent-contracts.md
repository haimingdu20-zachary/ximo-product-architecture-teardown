# Stage 2 — Observable Agent contracts

Use this stage only after the user journey is stable. Discover the Agent roster from explicit labels or repeated observable functional boundaries; never assume a conventional roster or fixed count.

## Roster discovery

| Agent/candidate | First appearance | Trigger | Follows/replaces | Downstream handoff | Re-entry evidence | Confidence | Evidence |
|---|---|---|---|---|---|---|---|

If a label might be a UI role, task category, or orchestrator rather than an independent Agent, retain the ambiguity. Put expected-but-absent functions in an omissions list, not the actual roster. When no name is visible, use a neutral functional label such as `<角色设计职能>`.

## Six input sources

For each Agent inspect all six, even when the answer is `【未知】`:

1. Current user input: requirements, choices, feedback, modifications, confirmations, interruptions, uploads.
2. Long-term user information: language, plan, balance, permissions, preferences, saved assets, project history.
3. Project context: configuration, scripts, entities, assets, references, models, states, confirmations, errors, versions.
4. Upstream Agent output: producer, fields/assets, start conditions, rerun consequences.
5. Platform knowledge/assets: libraries, templates, model limits, domain knowledge, safety, copyright, billing rules.
6. Tool/runtime results: assets, task status, errors, safety blocks, balance, interruption, retry, context-write result.

## Observable judgments

Summarize functions, never hidden reasoning:

- problem solved and takeover boundary;
- required information and completeness checks;
- automatic continuation versus user confirmation;
- stop, modification, invalidation, retry, and rollback conditions;
- completion criteria and actual quality validation;
- downstream handoff conditions.

## I/O contract card

```text
Agent: <name or functional label>
1. Core goal
2. Trigger and takeover boundary
3. Inputs — mark the six sources and required/optional/unknown
4. Observable judgments
5. Tools
6. Outputs — mark the five output classes
7. Global context reads/writes
8. Completion conditions
9. Failure, retry, interruption, and idempotency
10. Unconfirmed questions
```

### Input table

| Input | Source type | Required/optional/unknown | Use | Level | Evidence |
|---|---|---|---|---|---|

### Five output classes

1. User reply.
2. Page component: form, button, confirmation, task, error, preview/editor entry.
3. Asset: text, image, video, audio, version/history.
4. Global context write: field, state, reference, relationship, confirmation, error.
5. Downstream handoff: recipient, payload, start condition, unresolved items.

### Context table

| Field/object | Read/write | Producer | Consumer | Update time | Version/invalidation | Level | Evidence |
|---|---|---|---|---|---|---|---|

## Tool contract

Do not invent an official name. Use `<functional name>` and label it `功能命名，非官方工具名`.

| Tool | Official/functional | Caller | Preconditions | Required inputs | Confirmation gate | Observable execution | Success validation | Failure/retry | State write | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|

An Agent plan is not execution. Confirm execution only through a result surface, task state, asset delta, runtime result, or context/state change. When the action succeeded but the state write is not visible, record tool success and state unknown separately.

## Cross-Agent and global outputs

Produce:

- tool master table;
- global-context field table;
- producer–consumer table;
- Agent input → judgment → tool → output → handoff diagram;
- fact/inference/design/unknown register.

Explicitly inspect versions, stable asset references, upstream edits and downstream invalidation, orphan assets, write-only/read-only fields, duplicate calls, billing effects, and chat/task/canvas/asset/preview conflicts.

## Output order

1. Scope and gaps.
2. Roster and omissions.
3. One contract card per evidenced Agent.
4. Tool master table.
5. Global-context table.
6. Producer–consumer table.
7. Cross-Agent flow diagram.
8. Evidence-level register.
9. Five most valuable validation questions.

## Gate

- no unsupported Agent is in the actual roster;
- every Agent has appearance, trigger, boundary, and handoff evidence;
- six input sources and five output classes were checked;
- plans and calls are distinct;
- context producers, consumers, versions, and invalidation are traceable;
- modification, failure, interruption, balance, retry, idempotency, and conflicts are addressed or unknown;
- no full System Prompt has been drafted yet.

Do not proceed to the functional prompt until this gate passes and the target Agent is selected.
