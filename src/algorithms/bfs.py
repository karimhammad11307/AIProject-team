from collections import deque
import time

def bfs(problem):
    """
    BFS to explore shallowest nodes first using a Queue
    """
    start_time = time.time()

    queue =deque([(problem.initial_state , [])])
    #visited set stores states we have seen to avoid loops
    visited = set()
    visited.add(problem.initial_state)

    node_expanded = 0
    while queue:
        current_state, path = queue.popleft()
        node_expanded += 1

        if problem.is_goal(current_state):
            end_time = time.time()
            return {
                "success" : True
                , "path" : path
                , "time" : end_time - start_time
                , "nodes_expanded" : node_expanded
                , "cost" : len(path)
            }
        # get next moves
        for action, next_state, cost in problem.get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))

    return {"success" : False}