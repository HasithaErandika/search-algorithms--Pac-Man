# Assignment Plan

## Objective

Implement DFS, BFS, UCS, and A*, then implement the corners problem representation and admissible/consistent heuristics for corners and food search.

## Question allocation

| Question | Deliverable | Marks | Primary owner | Review focus |
| --- | --- | ---: | --- | --- |
| Q1 | `depthFirstSearch` | 4 | Seneja Ramanayake | graph search and stack behavior |
| Q2 | `breadthFirstSearch` | 4 | Jayashan Guruge | queue behavior and shortest steps |
| Q3 | `uniformCostSearch` | 4 | Nipuna Bhanuka | varying costs and priority updates |
| Q4 | `aStarSearch` | 4 | Hasitha Erandika | `g + h` ordering and null heuristic |
| Q5 | `CornersProblem` | 8 | Hasitha Erandika | compact state and successor bookkeeping |
| Q6 | `cornersHeuristic` | 8 | Jayashan Guruge | admissibility, consistency, node count |
| Q7 | `foodHeuristic` | 8 | Seneja Ramanayake | lower bound, consistency, node count |

The autograder allocation totals 40 marks. The remaining assessment is the group report (10), individual Git contribution (10), and individual viva (40).

## Suggested milestones

1. Confirm the extracted starter files and environment.
2. Read `util.py`, `search.py`, `searchAgents.py`, and the autograder tests as a group.
3. Implement and test Q1–Q4 in parallel, with one peer review per question.
4. Integrate Q5, then test the corners representation with BFS before tuning Q6.
5. Implement Q7 and test both optimality and expansion counts.
6. Run the complete autograder, capture results, review the Git history, and rehearse viva questions.

## Report checklist

- [ ] State the objective and environment.
- [ ] Explain the common graph-search skeleton.
- [ ] Describe the frontier used by DFS, BFS, UCS, and A*.
- [ ] Explain the corners state representation.
- [ ] Justify the admissibility and consistency of both heuristics.
- [ ] Include autograder results for Q1–Q7.
- [ ] Include individual contribution screenshots and commit evidence.
- [ ] Include each member's understanding of the full solution.

## Collaboration expectations

Use small focused commits, review each other's code, and keep the default branch runnable. Individual ownership is evidence of contribution, not a substitute for shared understanding.
