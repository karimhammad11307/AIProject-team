import time

def get_heuristic(state):
    """
    Heuristic: Counts misplaced tiles.
    Goal state assumed: (1, 2, 3, 4, 5, 6, 7, 8, 0)
    """
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    count = 0
    for i in range(9):
        # Check if tile is not empty (0) and not in correct spot
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def hill_climbing(problem):
    """
    Hill Climbing: Greedy local search.
    Moves to the neighbor with the lowest heuristic cost.
    """
    start_time = time.time()
    current_state = problem.initial_state
    path = []
    nodes_expanded = 0
    
    while True:
        nodes_expanded += 1

        # Check if current state is goal
        if problem.is_goal(current_state):
            end_time = time.time()
            return {
                "success": True,
                "path": path,
                "time": end_time - start_time,
                "nodes_expanded": nodes_expanded,
                "cost": len(path)
            }
        
        # Get neighbors
        neighbours = problem.get_successors(current_state)
        
        # Find the Best Neighbor
        best_neighbor = None
        best_neighbor_score = get_heuristic(current_state) # Start with current score
        best_action = None
        
        # Evaluate all neighbors
        for action, neighbor_state, cost in neighbours:
            score = get_heuristic(neighbor_state)
            
            # Strict Hill Climbing: Only move if the neighbor is STRICTLY better (<)
            if score < best_neighbor_score:
                best_neighbor = neighbor_state
                best_neighbor_score = score
                best_action = action
        
        # If no neighbor is better, we are stuck (Local Maxima)
        if best_neighbor is None:
            return {
                "success": False,
                "reason": "Stuck in local optimum"
            }
        
        # Move to the best neighbor
        current_state = best_neighbor
        path.append(best_action)
        
        # Safety limit to prevent infinite loops on plateaus
        if len(path) > 5000:
             return {"success": False, "reason": "Path too long"}