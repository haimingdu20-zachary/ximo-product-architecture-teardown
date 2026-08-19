# Evidence protocol

Read this reference for every teardown.

## Scope register

| Source ID | File/page | Apparent stage | Readability | Access status | Timestamp | Notes |
|---|---|---|---|---|---|---|

Use stable IDs. Preserve original paths and filenames, but never infer chronology from their lexical order alone.

## Atomic evidence ledger

| Evidence ID | Time/order | Source/surface | Actor/Agent | User action or intent | Visible response | Asset/state delta | Level | Exact evidence | Conflict |
|---|---|---|---|---|---|---|---|---|---|

The exact-evidence cell should contain a short page quote, component label, Agent label, asset/version, task status, error, model/price, or official statement. One screenshot may support several records, but each conclusion still needs its own row.

## Evidence levels

- `【已确认】`: directly visible in an in-scope UI, artifact, result, official source, or reproducible state.
- `【合理推断】`: supported by two or more compatible confirmed facts or a necessary relation between visible states.
- `【建议设计】`: a proposed robust implementation or product improvement; never present it as observed behavior.
- `【未知】`: missing, cropped, ambiguous, inaccessible, contradictory, or only narrated without a result surface.

For source paths, technology names, tool names, schemas, and implementation details, absence of evidence means unknown—not a license to use a conventional guess.

## Evidence strength and conflict handling

Compare, in descending practical strength:

1. asset that can be opened, played, or inspected;
2. canvas and asset-library state;
3. task/run state;
4. buttons, forms, warnings, errors, model and billing surfaces;
5. Agent natural-language claims;
6. filenames, analyst notes, and marketing language.

This order helps describe strength; it does not erase conflicts. Preserve both sides and classify the reconciliation as `一致`, `冲突`, or `无法比较`.

| Surface | What to verify |
|---|---|
| Chat | claim, plan, confirmation request, error explanation |
| Task/run | queued, running, success, failed, interrupted, retry |
| Canvas | node/card existence, references, connections, stale state |
| Asset/history | actual file, version, stable reference, timestamp |
| Preview/editor | viewable/playable result, completeness, edit/export entry |
| Account/billing | permission, balance, estimate, debit, refund, restriction |

## Completion verification

Do not mark a stage complete from chat or a tool success message alone. Check, when applicable:

- required assets exist and are viewable;
- tasks are successful, not queued/running/failed/interrupted;
- global/canvas state resolves to the current asset version;
- downstream references are not stale;
- required user confirmation is recorded;
- preview/editor/export contains the required components;
- quality constraints can actually be compared with the user’s request;
- downstream handoff was accepted.

If quality or state cannot be inspected, say compliance is unverified.

## Failure, interruption, and billing

For each event record exact text, affected operation/asset, task state, whether any asset was produced, whether balance may have changed, recovery actions, retry behavior, duplicate results, and whether execution continued after interruption.

Never infer that an unobserved branch exists. Draw it as a dashed `【未知】` branch only when the requested report requires the category.

## Safety boundary

Default to read-only inspection. Navigation and opening public or already-authorized views are allowed. Obtain or rely on explicit authority before state-changing operations, and confirm immediately before sensitive transmission, purchases, deletion, publication, uploads, microphone/camera/location access, or other consequential actions.

Do not inspect cookies, storage, credentials, authentication headers, private logs, or unrelated accounts. If authentication is needed, hand control to the user or request the minimum supported action.

## Evidence gaps section

Always list inaccessible or unreadable sources, cropped controls, stages supported only by narration, missing official names, missing failure/billing/retry examples, quality attributes that cannot be judged, and unresolved surface conflicts.
