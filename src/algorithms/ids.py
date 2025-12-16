import time

def ids(problem):
    """
    IDS: Iterative Deepening Search.
    Repeatedly runs Depth-Limited Search (DLS) with increasing depth limits.
    """
    start_time = time.time()
    depth_limit = 0
    total_nodes_expanded = 0

    while True:
        # Run DLS with the current depth limit
        result = dls(problem, depth_limit)
        
        # Add nodes from this iteration to the total count
        total_nodes_expanded += result["nodes_expanded"]

        if result["success"]:
            # Goal found! Return the full stats
            end_time = time.time()
            return {
                "success": True,
                "path": result["path"],
                "time": end_time - start_time,
                "nodes_expanded": total_nodes_expanded,  # Total across all iterations
                "cost": len(result["path"])
            }
        
        # If not found, increase depth and try again
        depth_limit += 1
        
        # Safety break: If depth gets too crazy (e.g., > 100), stop.
        if depth_limit > 100:
            return {"success": False}

def dls(problem, limit):
    """
    Helper: Depth-Limited Search (DFS with a depth limit)
    """
    # Stack stores: (current_state, path)
    stack = [(problem.initial_state, [])]
    
    # Track visited states *at specific depths* to optimize
    visited_at_depth = {}
    nodes_expanded = 0

    while stack:
        current_state, path = stack.pop() # LIFO

        # Optimization: If we found this state at a shallower depth before, skip
        if current_state in visited_at_depth and visited_at_depth[current_state] <= len(path):
            continue
        visited_at_depth[current_state] = len(path)
        
        nodes_expanded += 1

        if problem.is_goal(current_state):
            return {
                "success": True, 
                "path": path, 
                "nodes_expanded": nodes_expanded
            }
        
        # Only add neighbors if we are below the depth limit
        if len(path) < limit:
            neighbours = problem.get_successors(current_state)
            # Reversed to match your DFS style (optional, but consistent)
            for action, next_state, cost in reversed(neighbours):
                stack.append((next_state, path + [action]))

    return {"success": False, "nodes_expanded": nodes_expanded}