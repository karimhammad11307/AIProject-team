import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.problems.puzzle_8 import EightPuzzle
from src.algorithms.bfs import bfs
from src.algorithms.dfs import dfs
from src.algorithms.ids import ids
from src.algorithms.hill_climbing import hill_climbing

def main():
    print(" === 8-Puzzle AI solver === ")
    # test cases
    initial_state = (1,2,3,4,5,6,7,0,8)
    print (f"Initial state : {initial_state}")

    #setup problem 
    problem = EightPuzzle(initial_state)
    #1 Run BFS
    print("\n--- Running BFS ")
    bfs_result = bfs(problem)
    if bfs_result ['success']:
        print(f'solution found: {bfs_result["path"]}')
        print(f'Moves: {bfs_result["cost"]}')
        print(f'Time: {bfs_result["time"]:.5f}s')
    else:
        print("BFS Failed to find a solution")

    #2 Run DFS
    print("\n--- Running DFS ")
    dfs_result = dfs(problem)
    if dfs_result ['success']:
        print(f'solution found: {dfs_result["path"]}')
        print(f'Moves: {dfs_result["cost"]}')
        print(f'Time: {dfs_result["time"]:.5f}s')
    else:
        print("DFS Failed to find a solution")

        # 3. Run IDS (Iterative Deepening Search)
    print("\n--- Running IDS ---")
    if 'ids' in globals(): # Checks if import worked
        ids_result = ids(problem)
        if ids_result['success']:
            print(f'Solution found: {ids_result["path"]}')
            print(f'Moves: {ids_result["cost"]}')
            print(f'Time: {ids_result["time"]:.5f}s')
        else:
            print("IDS Failed to find a solution")
    else:
        print("IDS function not available.")

        # 4. Run Hill Climbing
    print("\n--- Running Hill Climbing ---")
    if 'hill_climbing' in globals(): # Checks if import worked
        hc_result = hill_climbing(problem)
        if hc_result['success']:
            print(f'Solution found: {hc_result["path"]}')
            print(f'Moves: {hc_result["cost"]}')
            print(f'Time: {hc_result["time"]:.5f}s')
        else:
            print("Hill Climbing Failed.")
            if 'reason' in hc_result:
                print(f"Reason: {hc_result['reason']}")
    else:
        print("Hill Climbing function not available.")
if __name__ == "__main__":
    main()
