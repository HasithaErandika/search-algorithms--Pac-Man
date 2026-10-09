# Individual Contribution and AI Usage Declaration

## Individual contribution

| Student ID | Name | Questions and tasks contributed | Contribution summary |
| --- | --- | --- | --- |
| IT24101081 | Seneja Ramanayake | Q1 — `depthFirstSearch`; Q7 — `foodHeuristic` | Worked on the depth-first graph search and the food-search heuristic. Q1 covers exploring the deepest available state first while avoiding repeated state expansion and reconstructing the action path. Q7 covers estimating the remaining cost to collect all food while keeping the heuristic admissible and consistent for A*. |
| IT24101186 | Guruge J (Jayashan Guruge) | Q2 — `breadthFirstSearch`; Q6 — `cornersHeuristic` | Implemented BFS in `search.py` using the provided FIFO `util.Queue`, tracking discovered states and returning a shortest-step path. Implemented the corners heuristic in `searchAgents.py` using the Manhattan distance to the farthest unvisited corner as a non-negative lower bound. Checked BFS and heuristic behavior with the focused autograder questions. |

## AI usage declaration


| Student Name | IT Number | Assignment | AI Tool | AI Usage / Prompt |
| --- | --- | --- | --- | --- |
| **Jayashan Guruge** | IT24101186 | **Q2 – Breadth-First Search** | ChatGPT | • Explain the concepts I need to learn before implementing Q2.<br>• Explain Breadth-First Search and graph search.<br>• Explain how I can implement it.<br>• How can I test Q2 using the Pac-Man project and autograder to make sure my Breadth-First Search implementation works correctly? |
| **Jayashan Guruge** | IT24101186 | **Q6 – Corners Heuristic** | ChatGPT | • What should I know before starting Q6?<br>• How does A* search work?<br>• What is a heuristic?<br>• How does Manhattan distance work?<br>• What do admissibility and consistency mean?<br>• How does the Corners Problem work?<br>• How should I implement and test `cornersHeuristic`? |
| **Seneja Ramanayake** | IT24101081 | **Q1 – Depth-First Search** | ChatGPT | • Explain the concepts needed before implementing Q1.<br>• How does depth-first graph search work, and how should a stack and explored set be used?<br>• How can the action path be tracked and returned when the goal is found?<br>• How should I test `depthFirstSearch` with the Pac-Man project autograder? |
| **Seneja Ramanayake** | IT24101081 | **Q7 – Food Heuristic** | ChatGPT | • Explain the Food Search Problem and how A* uses a heuristic.<br>• What makes a food heuristic admissible and consistent?<br>• How can distances between Pac-Man and remaining food be used to estimate the cost of collecting all food?<br>• How should I implement and test `foodHeuristic` for optimality and node expansion? |



