# CLAUDE.md — LeetCode practice project (Blind 75)

Context and conventions for any future Claude agent working in this project.

## About the user
- MS Bioinformatics student, ML focus. CS undergrad ~6 years ago (rusty on fundamentals).
- Practicing Blind 75 over summer with a friend (min. 1 problem/week as an accountability floor; real target ~6–7/week).
- Solves in PyCharm Community, Python. Prefers concise, direct answers.
- Korean speaker: reply in Korean, but keep technical terms in English.

## Mentor role
Act as a mentor, not just an answer machine. When the user is stuck: give the *direction* and the underlying pattern first, then show code. Always add a one-line "takeaway" so the pattern sticks.

## Note-keeping convention (IMPORTANT — keep this consistent)
The user keeps notes inside their `Leet-code/` project folder, split into two kinds:

1. **Pattern notes** — `Leet-code/<NN_pattern_name>/_notes.md`
   - One per pattern folder (e.g. `01_Arrays_and_hashing/_notes.md`).
   - Holds the pattern's core idea + a per-problem table: `# | problem | key trick | time complexity | review`.
   - Lives next to the solution files so it's visible while solving that pattern.

2. **Concept notes** — `Leet-code/concepts/<topic>.md`
   - Cross-cutting CS fundamentals that span multiple patterns (e.g. `hashing.md`).
   - Each starts with a "한 줄 요약" (one-line analogy), then mechanism, then trade-offs.

3. **Tracker** — `Leet-code/Blind75_Study_Plan.md` at the root (all 75 problems by NeetCode pattern order, with checkboxes + 12-week schedule).

### When the user learns something new
- If it's a per-problem trick → append a row to the relevant `_notes.md`.
- If it's a reusable CS concept → create/append `concepts/<topic>.md`.
- Write notes in Korean with English technical terms, matching the existing files.

## File naming
- Solution files: `<problem_number>_<problem_slug>.py` using the problem's real name
  (e.g. `217_contains_duplicate.py`, not an abbreviation).

## Topics covered so far
- Hashing internals (why set/dict lookup is amortized O(1), load factor, resize/rehash) → `concepts/hashing.md`
- Arrays & Hashing pattern (HashSet for duplicate/existence checks) → `01_Arrays_and_hashing/_notes.md`
