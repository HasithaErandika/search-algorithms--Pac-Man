# Search Algorithms in Pac-Man

This repository is the group workspace for the Pac-Man search assignment. The project implements depth-first search (DFS), breadth-first search (BFS), uniform-cost search (UCS), and A* search, then applies them to the corners and food-search problems.

The assignment brief, architecture, environment setup, question ownership, testing workflow, and collaboration rules are documented in [`docs/`](docs/).

## Team

| Member | Assigned questions |
| --- | --- |
| Seneja Ramanayake | Q1 — Depth First Search; Q7 — Food Heuristic |
| Jayashan Guruge | Q2 — Breadth First Search; Q6 — Corners Heuristic |
| Nipuna Bhanuka | Q3 — Uniform Cost Search |
| Hasitha Erandika | Q4 — A* Search; Q5 — Finding All the Corners |

Every member is responsible for understanding the complete solution, not only the questions assigned above.

## Quick start

The recommended environment is Miniforge/Conda. A standard Python `venv` setup is also documented for systems without Conda.

```bash
conda create -n cs188 python=3.11
conda activate cs188
python -m pip install -r requirements.txt
```

After extracting the Pac-Man starter files into this repository, verify the game and run the relevant autograder question:

```bash
python pacman.py
python autograder.py -q q1
```

See [`docs/setup.md`](docs/setup.md) for the full setup and verification procedure.

## Documentation

- [`docs/architecture.md`](docs/architecture.md) — system architecture and search design.
- [`docs/assignment-plan.md`](docs/assignment-plan.md) — requirements, ownership, milestones, and marking checklist.
- [`docs/setup.md`](docs/setup.md) — Miniforge and `venv` setup instructions.
- [`docs/testing.md`](docs/testing.md) — autograder and manual verification commands.
- [`AGENT.md`](AGENT.md) — contribution and implementation guidance for the team.
