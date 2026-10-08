import unittest

from search import aStarSearch
from searchAgents import CornersProblem


class TinyProblem:
    def getStartState(self):
        return "start"

    def isGoalState(self, state):
        return state == "goal"

    def getSuccessors(self, state):
        graph = {
            "start": [("slow", "slow", 5), ("cheap", "cheap", 1)],
            "cheap": [("goal", "finish", 2)],
            "slow": [("goal", "finish", 10)],
            "goal": [],
        }
        return graph[state]


class FakeWalls:
    width = 5
    height = 5

    def __getitem__(self, x):
        return [True, False, False, False, True]


class FakeGameState:
    def getWalls(self):
        return FakeWalls()

    def getPacmanPosition(self):
        return (2, 2)


class SearchTests(unittest.TestCase):
    def test_astar_chooses_lowest_cost_path(self):
        actions = aStarSearch(TinyProblem())
        self.assertEqual(actions, ["cheap", "finish"])

    def test_corners_start_state_is_compact_and_hashable(self):
        problem = CornersProblem(FakeGameState())
        position, visited = problem.getStartState()
        self.assertEqual(position, (2, 2))
        self.assertEqual(visited, frozenset())
        hash((position, visited))

    def test_corner_is_recorded_when_entered(self):
        problem = CornersProblem(FakeGameState())
        state = ((2, 2), frozenset())
        successors = problem.getSuccessors(state)
        positions = {successor[0][0] for successor in successors}
        self.assertIn((1, 2), positions)


if __name__ == "__main__":
    unittest.main()
