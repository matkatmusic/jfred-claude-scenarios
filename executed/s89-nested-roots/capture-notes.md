# s89-nested-roots — capture notes (run 2026-07-22, ACCEPTED)

Status: **PASSES task-171-style verification** — all 20 steps completed, both
git commits present, and the task-178 coverage gate is FULLY GREEN through the
multi-source engine: `20/20 s89-nested-roots (3 user-edit)` over 391 records
from the two session JSONLs. The task-179 engine-gap prediction (nested-root
rel-path split) stays REFUTED on real data: `tests/test_parser.py` is ONE
merged ladder.

## Sessions (TWO Claude project dirs — the nested-root crux)

- a1 `0c0eb75d-c1fd-4407-8605-44d8c5546b27` (262 records, 02:16:56–02:25:48
  UTC Jul 23), cwd `/private/tmp/scen89-proj`, project dir
  `-private-tmp-scen89-proj`
- a2 `125e3107-a9b4-41ad-9f2c-a52a37640c66` (129 records, 02:18:40–02:24:25
  UTC Jul 23), cwd `/private/tmp/scen89-proj/tests`, project dir
  `-private-tmp-scen89-proj-tests`

Capture layout: `source-0c0eb75d/` and `source-125e3107/` each hold
`projects/<their own project dir>/<session>.jsonl` + `file-history/<session>/`
— the first capture where the source trees carry DIFFERENT project dir names.
Flat files at the capture root are the workspace tree (incl. `.git`,
`.step_states`).

## The crux

The same file reaches the engine under two rel-paths (`tests/test_parser.py`
from a1's root, `test_parser.py` from a2's root) but ONE absolute path
(`/private/tmp/scen89-proj/tests/test_parser.py`). The merged reconstruction
keeps one ladder via absolute-path identity — no rel-path join fires (engine
check: `test_nested_root_sessions_keep_one_ladder_for_one_absolute_path` in
`tests/reconstruction_multi_source.test.ts`).

## Ground-truth revision ladders (sha256/12; `.step_states` = primary root per step)

`parser.py` (a1 + runner, proj root only):

| snapshot | sha256/12 | change |
|---|---|---|
| step-002 | 30c0791d5c9b | a1 Write (step 1): parse_line / count_tokens |
| step-003 | 94b7b07a02fe | runner append `# reviewed by ops` |
| step-005 | 619b32b8c46e | SECOND `# reviewed by ops` (runner re-apply, see deviations) |
| step-008 | bf033cf9d560 | a1 Edit: + strip_comment, removes both dup comment lines |

`tests/test_parser.py` — the cross-root stream:

| snapshot | sha256/12 | actor (root) | change |
|---|---|---|---|
| step-002 | 1fc69bb1fb36 | a1 Write (proj, step 1) | parse_line + count_tokens tests |
| step-007 | 8e85f8a29ac4 | a1 (proj, step 6) + a2 (tests, step 7) | + test_empty_line, + test_count_tokens_multiword (step-6 edit surfaces in this snapshot) |
| step-009 | 778df5761055 | runner append (proj-relative) | + `# tests reviewed` |
| step-010 | 38c9e5ff10fe | a2 Edit (tests) | + TestStripComment (and a second `# tests reviewed`, see deviations) |
| step-011 | fa820053ef70 | a1 Edit (proj) | + TestIntegration strip_then_parse, removes dup comment lines |

Interleave across roots holds: a1 → a1 → a2 → runner → a2 → a1, one ladder.

Git evidence: `a84ffa4` baseline (step 2) → `53bd6c4` "parser tests"
(steps 13–14).

## Deviations from the design-doc ladder (all benign, gate still 20/20)

1. Both runner `Edit:` appends landed TWICE — the second copy appears in the
   snapshot two steps later (step-005 for `# reviewed by ops`, step-010 for
   `# tests reviewed`). The agents' later edits removed the duplicates, and
   the engine reproduces every intermediate state byte-for-byte.
2. a1's step-6 edit (test_empty_line) first shows in the step-007 snapshot —
   snapshot timing, not a lost edit; the gate's semantics ("some engine step
   reproduces this folder") absorb it.
