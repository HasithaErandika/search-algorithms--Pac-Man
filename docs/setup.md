# Environment and Project Setup

## Required starter files

After downloading and extracting `search.zip`, place its contents in this repository. Confirm that these files exist:

`search.py`, `searchAgents.py`, `pacman.py`, `util.py`, `game.py`, and `autograder.py`.

Do not rename the files, functions, or classes expected by the autograder.

## Recommended: Miniforge

Miniforge provides Conda and is the recommended environment manager for this project.

```bash
conda create -n cs188 python=3.11
conda activate cs188
python -m pip install -r requirements.txt
```

If `conda` is not available in a new shell, initialize the shell once with the command provided by your Miniforge installation, then restart the shell. Verify the active interpreter:

```bash
which python
python --version
python -m pip --version
```

The Python version should be 3.9–3.11; Python 3.11 is the team standard.

## Alternative: Python `venv`

Use this only when Conda/Miniforge is unavailable or when a member prefers the standard-library environment tool.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. Leave the environment with `deactivate`. Never commit `.venv/`.

## Verify Pac-Man

From the repository root, with the environment active:

```bash
python pacman.py
```

A playable game window should open. If the project is running in a headless environment, use the autograder commands instead of relying on the graphical smoke test.

## Reproducibility notes

Always install through the active interpreter (`python -m pip`) so packages go into the selected environment. Do not mix a global Python installation with the project environment. Run `conda deactivate` or `deactivate` before switching environment types.
