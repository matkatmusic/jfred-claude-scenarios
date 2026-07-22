# s88-multi-source-two-roots — capture notes (run 20260722-142525, ACCEPTED)

Status: **PASSES task-171 verification** — same-folder restructured scenario
(user directive 2026-07-22; see the note atop
`plans/170-s88-ground-truth-design.md`), all 26 steps completed, all four s87
mechanisms present. Two earlier failed runs are preserved in
`../s88-multi-source-two-roots-run1-failed/` (permission stalls; deviations in
its capture-notes.md).

## Sessions (both cwd = /private/tmp/scen88-alpha — ONE shared root)

- a1 `190e9da4-7a79-4fa0-a747-ac96b6ee83ab` (326 records, 21:25:29–21:34:55 UTC)
- a2 `38a3d7f8-159c-409d-89a0-ee152d26b646` (113 records, 21:30:30–21:34:50 UTC)

Multi-source shape: `source-a1/` and `source-a2/` each hold `projects/…/<one
session>.jsonl` + `file-history/<session>/` — the replica-sync shape (two
sources declaring the SAME root); the flat files at the capture root are the
run-all-scenarios auto-capture of the workspace tree (incl. `.git`,
`.step_states`).

## Four s87 mechanisms

1. **cwd remap** — records carry `/private/tmp/scen88-alpha` for declared root `/tmp/scen88-alpha`.
2. **time-aware indirection** — a2 ran `ctx_execute("exec(open('rename_map.py').read())")`
   TWICE (21:31:41, 21:32:22); the script content differed at each run instant
   (1 tuple → 2 tuples via the step-13 out-of-band edit), and neither sandbox
   call embeds the rename list.
3. **result-instant rename stamping** — step-3 `perl -pi -e 's/\bqty_chk\b/check_quantity/g'`
   whole-word Bash rename over both files, no Edit/Write tool.
4. **git-INDEX staged-blob evidence** — `git add` 21:34:02 (step 18) then commit
   21:34:32 (step 20): commits `ace7dfa` baseline → `a13f392` final.

## Ground-truth revision ladders (sha256/12; .step_states snapshot = alpha root per step)

`inventory.py` (one shared cross-session stream):

| step | actor | size | sha | change |
|---|---|---|---|---|
| 1 | a1 Write | 518B | 4bed4c2d0b85 | add_item / qty_chk / find_item |
| 3 | a1 Bash perl | 525B | 2f9d3b0f6c92 | qty_chk → check_quantity |
| 4 | runner user-edit | 543B | 8515b609e592 | + `# reviewed by ops` |
| 10 | a2 MCP sandbox | 546B | 145a23fb7c20 | add_item → insert_item |
| 12 | a1 Edit | 959B | 727b9a870e66 | + restock (uses check_quantity + insert_item) |
| 14 | a2 MCP sandbox | 963B | b04aab403539 | find_item → lookup_item (over a1's restock) |

Final functions: insert_item, check_quantity, lookup_item, restock.

`tests/test_inventory.py` (a1 + runner): step 1 594B 0ecc11956020 → step 3
622B 8ed947eadb52 (perl rename) → step 7 802B 6a9a244e5604 (check_quantity
zero-stock test) → step 15 1046B 7a521ce35953 (restock test) → step 16 1062B
0985c4af78a4 (`# tests updated` user-edit stamp).

`rename_map.py` (a2 + runner): step 8 248B ab13c2e9c794 (1 tuple) → step 13
282B a464732290b1 (runner user-edit adds `("find_item", "lookup_item"),`).

File-history sidecars: a1 `a07691c51891380c@v2–v5` (inventory 518/543/546/963),
`cc14ea01eae31bca@v2–v5` (tests 594/622/802/1062); a2 `e34327bd3a9ff6ca@v2–v3`
(rename_map 248/282). Note a1's inventory backups skip the step-3 perl state
(525B) — no tool-triggered backup for a Bash substitution, as designed.

Cross-session interleave on the one file: a1(1) → a1(3) → runner(4) → a2(10)
→ a1(12) → a2(14) — the alternating same-folder stream this scenario exists
to exercise. Stale sessions from the two failed runs were pruned from this
capture (they remain in the live projects folder and the run1-failed copy).
