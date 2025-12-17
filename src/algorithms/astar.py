import heapq
import time

def manhattan_distance(state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """
    Calculate Manhattan distance heuristic
    Sum of distances of each tile from its goal position
    """
    distance = 0
    for i in range(9):
        if state[i] != 0:  # Skip the empty tile
            # Find goal position of current tile
            goal_index = goal_state.index(state[i])
            # Convert indices to (row, col)
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            # Add Manhattan distance
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def misplaced_tiles(state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """
    Alternative heuristic: count misplaced tiles
    """
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal_state[i])

def astar(problem, heuristic=manhattan_distance):
    """
    A* Search algorithm
    Returns a dictionary with success status, path, cost, and time
    """
    start_time = time.time()
    
    # Priority queue: (f_cost, g_cost, state, path)
    # f_cost = g_cost + h_cost
    h_cost = heuristic(problem.initial_state, problem.goal_state)
    frontier = [(h_cost, 0, problem.initial_state, [])]
    explored = set()
    
    # Track best cost to reach each state
    best_cost = {problem.initial_state: 0}
    
    while frontier:
        f_cost, g_cost, state, path = heapq.heappop(frontier)
        
        # Check if goal reached
        if problem.is_goal(state):
            end_time = time.time()
            return {
                'success': True,
                'path': path,
                'cost': g_cost,
                'time': end_time - start_time
            }
        
        # Skip if already explored
        if state in explored:
            continue
        
        explored.add(state)
        
        # Expand successors
        for action, next_state, step_cost in problem.get_successors(state):
            new_g_cost = g_cost + step_cost
            
            # Only add if we found a better path or haven't seen this state
            if next_state not in explored and (next_state not in best_cost or new_g_cost < best_cost[next_state]):
                best_cost[next_state] = new_g_cost
                h_cost = heuristic(next_state, problem.goal_state)
                new_f_cost = new_g_cost + h_cost
                new_path = path + [action]
                heapq.heappush(frontier, (new_f_cost, new_g_cost, next_state, new_path))
    
    # No solution found
    end_time = time.time()
    return {
        'success': False,
        'path': [],
        'cost': 0,
        'time': end_time - start_time
    }