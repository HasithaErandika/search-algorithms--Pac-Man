"""Generic search algorithms for the Pac-Man project.

Q1-Q3 are reserved for their assigned owners. Hasitha's Q4 implementation is
added in a separate commit so the ownership boundaries remain visible.
"""

from util import PriorityQueue, raiseNotDefined


def depthFirstSearch(problem):
    raiseNotDefined()


def breadthFirstSearch(problem):
    raiseNotDefined()


def uniformCostSearch(problem):
    raiseNotDefined()


def nullHeuristic(state, problem=None):
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Return an optimal action sequence using graph-search A*."""
    start = problem.getStartState()
    frontier = PriorityQueue()
    frontier.push((start, [], 0), heuristic(start, problem))
    expanded = set()

    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()
        if state in expanded:
            continue
        if problem.isGoalState(state):
            return actions

        expanded.add(state)
        for successor, action, step_cost in problem.getSuccessors(state):
            if successor in expanded:
                continue
            next_actions = actions + [action]
            next_cost = cost + step_cost
            priority = next_cost + heuristic(successor, problem)
            frontier.push((successor, next_actions, next_cost), priority)

    return []


# Berkeley Pac-Man accepts these conventional aliases.
dfs = depthFirstSearch
bfs = breadthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch
