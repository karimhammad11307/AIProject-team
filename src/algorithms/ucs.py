import heapq
import time

def ucs(problem):
    """
    Uniform Cost Search algorithm
    Returns a dictionary with success status, path, cost, and time
    """
    start_time = time.time()
    
    # Priority queue: (cost, state, path)
    frontier = [(0, problem.initial_state, [])]
    explored = set()
    
    while frontier:
        cost, state, path = heapq.heappop(frontier)
        
        # Check if goal reached
        if problem.is_goal(state):
            end_time = time.time()
            return {
                'success': True,
                'path': path,
                'cost': cost,
                'time': end_time - start_time
            }
        
        # Skip if already explored
        if state in explored:
            continue
        
        explored.add(state)
        
        # Expand successors
        for action, next_state, step_cost in problem.get_successors(state):
            if next_state not in explored:
                new_cost = cost + step_cost
                new_path = path + [action]
                heapq.heappush(frontier, (new_cost, next_state, new_path))
    
    # No solution found
    end_time = time.time()
    return {
        'success': False,
        'path': [],
        'cost': 0,
        'time': end_time - start_time
    }