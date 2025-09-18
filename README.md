## Python CSP Solver for Sudoku
This project provides a Python-based Constraint Satisfaction Problem (CSP) solver and a set of Sudoku puzzle instances to demonstrate its functionality. The solver uses a backtracking algorithm and is extended with the Minimum Remaining Values (MRV) heuristic to improve performance on complex problems.

## Contents
This repository includes the following files:

cs4300_csp.py: Contains the core CSP solver logic, including a baseline backtracking solver and an optimized version implementing the MRV heuristic.

cs4300_csp_parser.py: A parser that reads and interprets problem instances from .csp files.

run_csp.py: A command-line script to run the solvers on a specified .csp problem file.

send_more_money_strict_add10.csp: The original example cryptarithmetic puzzle.

sudoku_*.csp: A set of 4x4 Sudoku puzzles (easy, medium, hard).

sudoku_9x9_*.csp: A set of 9x9 Sudoku puzzles (easy, medium, hard) to test the solver on a larger scale.

csp_report.md: The final project report detailing the problem formalization, heuristic implementation, and results.

## How to Run the Solver
You can run the solver from your terminal. You must provide the path to a .csp file. You can also specify which solver to use (the baseline or the MRV-enhanced version).

## Basic Usage
```bash
To solve a puzzle using the baseline solver:

python3 run_csp.py <path_to_puzzle_file.csp>

Example:

python3 run_csp.py sudoku_medium.csp
python3 run_csp.py sudoku_9x9_hard.csp

Using the MRV Heuristic
To solve a puzzle using the MRV solver for better performance:

python3 run_csp.py <path_to_puzzle_file.csp> --solver mrv

Example:

python3 run_csp.py sudoku_medium.csp --solver mrv
python3 run_csp.py sudoku_9x9_hard.csp --solver mrv
```
Problem Instances
The repository includes several Sudoku puzzle files to demonstrate and test the solver's capabilities:

4x4 Puzzles: sudoku_4x4_easy.csp, sudoku_4x4_medium.csp, sudoku_4x4_hard.csp

These are small-scale puzzles, solvable by both the baseline and MRV solvers.

9x9 Puzzles: sudoku_9x9_easy.csp, sudoku_9x9_medium.csp, sudoku_9x9_hard.csp

These are standard, full-sized Sudoku puzzles. The hard version serves as an excellent test case to highlight the dramatic performance improvement gained from the MRV heuristic.