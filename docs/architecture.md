# Architecture Plan

## 1. System context

The Pac-Man starter project is a small search framework. `pacman.py` runs the game, `game.py` provides the game model, `search.py` provides reusable graph-search algorithms, and `searchAgents.py` adapts those algorithms to concrete Pac-Man problems. The autograder calls the public functions and classes directly.

```text
pacman.py / autograder.py
        |
        v
 searchAgents.py  ---->  search.py
        |                    |
        v                    v
  Problem interface      util.py fringe
        |
        v
   GameState / Grid / Directions (game.py)
```

## 2. Common graph-search contract

Each algorithm follows the same high-level flow:

1. Read the problem's start state and put it on a frontier.
2. Remove one node according to the frontier policy.
3. If it is a goal, return the actions accumulated along the path.
4. If its state has not been expanded, mark it expanded and add its successors.
5. Repeat until a goal is found or the frontier is empty.

The node payload is conceptually `(state, actions, cost)`. DFS and BFS can use the accumulated action list directly; UCS and A* additionally prioritize by path cost.

| Algorithm | Frontier | Priority | Expected property |
| --- | --- | --- | --- |
| DFS | `util.Stack` | newest node first | complete on finite graph with visited states; not optimal |
| BFS | `util.Queue` | oldest node first | optimal when every step has equal cost |
| UCS | `util.PriorityQueue` | `g(n)` | optimal for non-negative step costs |
| A* | `util.PriorityQueue` | `g(n) + h(n)` | optimal with an admissible, consistent heuristic |

## 3. State and ownership boundaries

### `search.py` — Q1–Q4

The algorithms depend only on the problem interface:

- `getStartState()`
- `isGoalState(state)`
- `getSuccessors(state)` returning `(successor, action, stepCost)`
- `getCostOfActions(actions)`

They should not depend on Pac-Man-specific classes.

### `searchAgents.py` — Q5–Q7

`CornersProblem` should represent a state as the current Pac-Man position plus the set of corners already visited. The wall grid and corner coordinates belong to the problem instance, not every state. A tuple such as `(position, visitedCorners)` keeps states hashable and compact.

The food-search heuristic receives a food grid. It should calculate a lower bound on the remaining route while avoiding mutation of the provided grid or problem state.

## 4. Heuristic design constraints

For a heuristic `h`:

- Non-negative: `h(n) >= 0`.
- Goal condition: `h(goal) = 0`.
- Admissibility: `h(n)` never overestimates the true remaining cost.
- Consistency: `h(n) <= cost(n, n') + h(n')` for every successor `n'`.

Safe lower bounds can be built from maze distances or distance estimates that ignore obstacles. Any stronger heuristic must be justified against these properties and tested for optimality before performance tuning.

## 5. Error and compatibility strategy

The autograder is the compatibility boundary. Keep signatures and return types unchanged, use the supplied utility classes, and avoid changing framework files. If a test fails, first identify whether the issue is state identity, duplicate handling, path ordering, cost accumulation, or heuristic validity.

## 6. Verification path

Run the focused question test after each implementation, then run all seven questions before integration. Finally, launch `python pacman.py` and manually verify keyboard control and agent execution. Detailed commands are in [`setup.md`](setup.md) and [`testing.md`](testing.md).
