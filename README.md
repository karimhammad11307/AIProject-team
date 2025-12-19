# 8-Puzzle Solver: AI Search Algorithms
**Artificial Intelligence Course Project**

## 👥 Team Members
| Name | Student ID |
|------|------------|
| كريم محمد سعيد حماد | 2023157 |
| محمود محمد السيد عمر الشوريجي | 2023394 |
| احمد محمد عبدالرؤوف الخولي | 2023282 |
| مؤمن علاء نصر الجزار | 2023235 |
| عبدالرحمن ايمن فتوج الشريف | 2023128 |
| محمد عادل علي ناصف | 2023370 |
| حاتم ايمن فضل علي | 2023066 |
| يوسف محمد شرف الخولي | 2023257 |
| علي اشرف علي مهنا | 2023623 |

## 📌 Project Overview
This project implements a comprehensive framework for solving the classic **8-Puzzle** game using various Artificial Intelligence search strategies. 

The primary objective is to provide hands-on experience in implementing and evaluating fundamental search algorithms. By applying these algorithms to the 8-Puzzle, we gain a deeper understanding of their theoretical underpinnings, practical applications, and performance trade-offs.

We have successfully applied the required algorithms to the chosen problem domain and conducted a comparative analysis focusing on key metrics such as **time complexity**, **space complexity**, **solution optimality**, and **path cost**.

---

## 🧩 The Problem: 8-Puzzle
The **8-puzzle** is a sliding puzzle that consists of a 3x3 frame of numbered square tiles (1-8) in random order with one tile missing. 

* **Objective:** Place the tiles in the correct order by making sliding moves that use the empty space.
* **Goal State:** `(1, 2, 3, 4, 5, 6, 7, 8, 0)`
* **Significance:** This problem presents a manageable yet non-trivial state space, ideal for analyzing and comparing search algorithm performance.

---

## 🚀 Features & Algorithms Implemented
This framework implements all the required search strategies as outlined in the project proposal.

### Uninformed Search Strategies
1.  **Breadth-First Search (BFS):** * Explores the shallowest nodes first using a FIFO queue.
    * Guarantees an optimal (shortest-move) solution.
2.  **Depth-First Search (DFS):** * Explores as far as possible along each branch before backtracking using a LIFO stack.
    * Memory efficient but not guaranteed to find the shortest path.
3.  **Iterative Deepening Search (IDS):** * Runs depth-limited searches repeatedly, increasing the depth limit with each iteration.
    * Combines the benefits of BFS (completeness, optimality) with the memory efficiency of DFS.
4.  **Uniform-Cost Search (UCS):** * Expands the least-cost unexpanded node using a priority queue. 
    * For the 8-puzzle (where all moves cost 1), UCS behaves identically to BFS but is structured to handle variable costs.

### Informed Search Strategies
5.  **A* Search (A-Star):** * Uses a heuristic function to guide the search for the optimal path.
    * **Heuristic Used:** *Manhattan Distance* – The sum of the vertical and horizontal distances of each tile from its goal position.
6.  **Hill Climbing:** * A local search algorithm that continuously moves to the neighbor state with the lowest heuristic cost (steepest descent). 
    * Serves as a practical example of greedy, heuristic-driven search (though it may get stuck in local optima).

---

## 📊 Performance Analysis & Results
Our comprehensive analysis compares the algorithms based on the required metrics. Key findings include:

| Metric | BFS / UCS | DFS | IDS | A* (Manhattan) | Hill Climbing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Optimality** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | ❌ No |
| **Completeness**| ✅ Yes | ⚠️ Risk | ✅ Yes | ✅ Yes | ⚠️ Risk |
| **Speed** | Slow | Fast | Medium | ⚡ Very Fast | ⚡ Instant |
| **Memory** | High | Low | Low | Medium | Low |

* **Trade-offs:** BFS/UCS are optimal but memory-heavy. DFS/IDS are memory-efficient but DFS isn't optimal.
* **Efficiency:** A* is typically the most efficient, finding the optimal path while expanding significantly fewer nodes than BFS.
* **Local Optima:** Hill Climbing is very fast per step but may fail to solve the puzzle entirely if it hits a plateau.

---

## 📂 Project Structure

```text
8-puzzle-ai-project/
├── src/
│   ├── eight_puzzle.py        # Core `EightPuzzle` class (State, Goal Check, Successors)
│   ├── bfs.py                 # Breadth-First Search Implementation
│   ├── dfs.py                 # Depth-First Search Implementation
│   ├── ids.py                 # Iterative Deepening Search Implementation
│   ├── ucs.py                 # Uniform-Cost Search Implementation
│   ├── astar.py               # A* Search with Manhattan Distance
│   └── hill_climbing.py       # Hill Climbing Implementation
└── README.md                  # Project Documentation
