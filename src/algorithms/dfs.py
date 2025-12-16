import time

def dfs(problem):
    """
    DFS to explore deepest nodes first using a stack LIFO
    """
    start_time = time.time()
    stack = [(problem.initial_state, [])]

    visited = set()
    nodes_expanded = 0

    while stack:
        current_state , path = stack.pop() #POP
        # for optimization make a limit for moves as some will be too long
        if len(path) > 5000:
            continue
        if current_state in visited:
            continue
        visited.add(current_state)
        nodes_expanded += 1

        if problem.is_goal(current_state):
            end_time = time.time()
            return {
                "success" : True
                , "path" : path
                , "time" : end_time - start_time
                , "nodes_explained" : nodes_expanded
                , "cost" : len(path)
            }
        
        # neighbours for revresing stack
        neighbours = problem.get_successors(current_state)
        for action , next_state , cost in reversed( neighbours):
            if next_state not in visited:
                stack.append((next_state, path + [action]))

    return {"success" : False}