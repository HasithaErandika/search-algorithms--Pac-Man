# Testing and Verification

Run commands from the repository root with the Miniforge environment activated, or with `.venv` activated.

## Focused tests

```bash
python autograder.py -q q1
python autograder.py -q q2
python autograder.py -q q3
python autograder.py -q q4
python autograder.py -q q5
python autograder.py -q q6
python autograder.py -q q7
```

Run the focused test after changing its implementation. Q6 and Q7 must be checked for both optimal paths and expansion thresholds; a fast but inadmissible heuristic is not acceptable.

## Full verification

```bash
python autograder.py
python pacman.py
```

For manual algorithm checks, use the starter project's documented `pacman.py` options and compare DFS, BFS, UCS, and A* on the same layout. Confirm that the returned action sequence reaches the goal and that costs match the problem's cost function.

## Before integration

- Confirm no debug prints or temporary changes remain.
- Confirm all seven focused tests pass.
- Inspect `git diff` and `git status`.
- Confirm no `.venv`, `__pycache__`, editor files, or generated output is staged.
- Record the exact test commands and results for the group report.
