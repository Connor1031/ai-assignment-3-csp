import sys, time
from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking, solve_backtracking_mrv

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run_csp.py <problem.csp> [--solver mrv|base]")
        sys.exit(1)

    filepath = sys.argv[1]
    solver_choice = "base"

    if len(sys.argv) > 3 and sys.argv[2] == "--solver":
        if sys.argv[3] == "mrv":
            solver_choice = "mrv"

    csp = parse_cs4300(filepath)
    
    if solver_choice == "mrv":
        solver_func = solve_backtracking_mrv
    else:
        solver_func = solve_backtracking

    start_time = time.time()
    solutions = list(solver_func(csp))
    end_time = time.time()
    duration = end_time - start_time

    if solutions:
        print(f"Found {len(solutions)} solution(s) in {duration:.4f} seconds.")
        # Just print the first solution to keep the output clean
        print(f"First solution: {solutions[0]}")
    else:
        print(f"No solutions found in {duration:.4f} seconds.")
