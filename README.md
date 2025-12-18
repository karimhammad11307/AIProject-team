8-Puzzle Solver: AI Search Algorithms
Artificial Intelligence Course Project

📌 Project Overview
This project implements a comprehensive framework for solving the classic 8-Puzzle game using various Artificial Intelligence search strategies. The primary objective is to provide hands-on experience in implementing and evaluating fundamental search algorithms. By applying these algorithms to the 8-Puzzle, we gain a deeper understanding of their theoretical underpinnings, practical applications, and performance trade-offs.

We have successfully applied the required algorithms to the chosen problem domain and conducted a comparative analysis focusing on key metrics such as time complexity, space complexity, solution optimality, and path cost.

🧩 The Problem: 8-Puzzle
The 8-puzzle is a sliding puzzle that consists of a 3x3 frame of numbered square tiles (1-8) in random order with one tile missing. The object of the puzzle is to place the tiles in the correct order (goal state: (1, 2, 3, 4, 5, 6, 7, 8, 0)) by making sliding moves that use the empty space. This problem presents a manageable yet non-trivial state space ideal for analyzing and comparing search algorithm performance.

🚀 Features & Algorithms Implemented
This framework implements all the required search strategies as outlined in the project proposal:

Uninformed Search Strategies
Breadth-First Search (BFS): Explores the shallowest nodes first using a FIFO queue. Guarantees an optimal (shortest-move) solution.

Depth-First Search (DFS): Explores as far as possible along each branch before backtracking using a LIFO stack.

Iterative Deepening Search (IDS): A state space search strategy in which a depth-limited search is run repeatedly, increasing the depth limit with each iteration until the goal is found. It combines the benefits of BFS (completeness, optimality) with the memory efficiency of DFS.

Uniform-Cost Search (UCS): Expands the least-cost unexpanded node using a priority queue. For the 8-puzzle where all moves have a uniform cost of 1, UCS behaves identically to BFS.

Informed Search Strategies
A* Search (A-Star): An informed search algorithm that uses a heuristic function to guide its search for the optimal path. We have implemented it with the following admissible and consistent heuristic:

Heuristic Used: Manhattan Distance – The sum of the vertical and horizontal distances of each tile from its goal position.

Hill Climbing: A local search algorithm that continuously moves to the neighbor state with the lowest heuristic cost (steepest descent). While not guaranteed to find a solution due to local optima, it serves as a practical example of greedy, heuristic-driven search.

📊 Performance Analysis & Results
Our comprehensive analysis compares the algorithms based on the metrics required by the proposal. Key findings include:

Optimality: BFS, UCS, and A* successfully find the shortest path to the goal. DFS and Hill Climbing do not guarantee optimal solutions.

Completeness: BFS, UCS, IDS, and A* are complete (will find a solution if one exists). DFS and Hill Climbing can get stuck in infinite loops or local optima without additional safeguards (which we have implemented, e.g., visited sets and depth limits).

Time & Space Efficiency: There is a clear trade-off:

BFS/UCS are optimal but can consume significant memory.

DFS/IDS are memory-efficient but may be slower or not find the optimal path.

A*, with a good heuristic like Manhattan Distance, is typically the most efficient, finding the optimal path while expanding far fewer nodes than BFS.

Hill Climbing is very fast per step but may fail to solve the puzzle entirely.

Project Structure & How to Run

8-puzzle-ai-project/
├── src/
│   ├── eight_puzzle.py        # Core `EightPuzzle` class with state representation, goal check, and successor generation.
│   ├── bfs.py                 # Implementation of Breadth-First Search.
│   ├── dfs.py                 # Implementation of Depth-First Search.
│   ├── ids.py                 # Implementation of Iterative Deepening Search.
│   ├── ucs.py                 # Implementation of Uniform-Cost Search.
│   ├── astar.py               # Implementation of A* Search with Manhattan Distance heuristic.
│   └── hill_climbing.py       # Implementation of Hill Climbing.
├── tests/
│   └── test_puzzles.py        # Scripts with predefined puzzle states for testing and comparison.
├── analysis/
│   └── results_analysis.md    # Detailed write-up of our comparative analysis and results.
├── README.md                  # This file.
└── requirements.txt           # Python dependencies (if any).
Prerequisites
Python 3.7+

Installation & Execution
Clone the repository: git clone [Your-Repository-Link-Here]

Navigate to the project directory: cd 8-puzzle-ai-project

Run any solver on a sample puzzle. For example, to run A*:

python src/astar.py
