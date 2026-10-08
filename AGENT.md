# Agent and Contributor Guide

This file describes the working agreement for contributors and coding agents in the Pac-Man search project.

## Scope

The starter project must retain the expected Berkeley Pac-Man interfaces. Do not rename files, functions, classes, or command-line arguments used by the autograder.

Primary implementation files:

- `search.py`: DFS, BFS, UCS, and A* (Q1–Q4).
- `searchAgents.py`: `CornersProblem`, corners heuristic, and food heuristic (Q5–Q7).
- `util.py`: provided `Stack`, `Queue`, and `PriorityQueue`; use these data structures.

## Team ownership

| Member | Questions | Main files |
| --- | --- | --- |
| Seneja Ramanayake | Q1, Q7 | `search.py`, `searchAgents.py` |
| Jayashan Guruge | Q2, Q6 | `search.py`, `searchAgents.py` |
| Nipuna Bhanuka | Q3 | `search.py` |
| Hasitha Erandika | Q4, Q5 | `search.py`, `searchAgents.py` |

Ownership identifies the primary implementer and reviewer. It does not limit anyone from reviewing, testing, or helping with another question.

## Implementation rules

1. Preserve the starter API and existing function signatures.
2. Use graph search: maintain an expanded/visited set and do not expand a state twice.
3. Return a list of actions, or the starter project's expected failure value when no path exists.
4. Use `util.Stack` for DFS, `util.Queue` for BFS, and `util.PriorityQueue` for UCS and A*.
5. Keep problem states small, immutable/hashable, and independent of the complete `GameState`.
6. For Q6 and Q7, heuristics must be non-negative, admissible, and consistent. A heuristic must return `0` at a goal state.
7. Avoid unrelated refactors and do not commit generated caches, local environments, or IDE files.

## Workflow

Before editing, read the relevant starter implementation and its neighboring helper methods. Make focused commits using imperative messages, for example `feat: implement breadth-first search` or `test: verify corners heuristic`.

Before opening a pull request or handing off work:

```bash
python autograder.py -q q1
python autograder.py -q q2
python autograder.py -q q3
python autograder.py -q q4
python autograder.py -q q5
python autograder.py -q q6
python autograder.py -q q7
```

Also run `python pacman.py` for a manual smoke test when the starter files are available. Record meaningful test results in the contribution or report notes.

## Viva preparation

Each member should be able to explain the complete search skeleton, frontier behavior, duplicate-state handling, path-cost calculation, heuristic admissibility/consistency, and the state representation used by the corners and food problems.

## Agent behavior

Agents should inspect existing work before modifying files, make the smallest safe change, explain assumptions, and verify changes with the narrowest relevant tests. Never replace unrelated user work or alter assignment interfaces for convenience.
