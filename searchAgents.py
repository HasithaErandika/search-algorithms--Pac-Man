"""Search problems and agents for the Pac-Man project.

Only the Q5 corners representation is owned by Hasitha in this repository.
The remaining assignment functions stay explicit placeholders for their owners.
"""

from game import Directions
from util import raiseNotDefined


class CornersProblem:
    """State space for visiting each of the four maze corners."""

    def __init__(self, startingGameState):
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        width = self.walls.width
        height = self.walls.height
        self.corners = ((1, 1), (1, height - 2),
                        (width - 2, 1), (width - 2, height - 2))
        self._expanded = 0

    def getStartState(self):
        visited = ()
        if self.startingPosition in self.corners:
            visited = (self.startingPosition,)
        return self.startingPosition, visited

    def isGoalState(self, state):
        _, visited = state
        return len(visited) == len(self.corners)

    def getSuccessors(self, state):
        position, visited = state
        successors = []
        x, y = position
        moves = ((Directions.NORTH, (x, y + 1)),
                 (Directions.SOUTH, (x, y - 1)),
                 (Directions.EAST, (x + 1, y)),
                 (Directions.WEST, (x - 1, y)))
        for action, next_position in moves:
            next_x, next_y = next_position
            if self.walls[next_x][next_y]:
                continue
            next_visited = visited
            if next_position in self.corners and next_position not in visited:
                next_visited = visited + (next_position,)
            successors.append(((next_position, next_visited), action, 1))
        self._expanded += 1
        return successors

    def getCostOfActions(self, actions):
        if actions is None:
            return 999999
        return len(actions)


def cornersHeuristic(state, problem):
    raiseNotDefined()


def foodHeuristic(state, problem):
    raiseNotDefined()
