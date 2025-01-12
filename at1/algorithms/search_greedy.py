import heapq

def greedy_search(start, goal, get_neighbors, cost_function, heuristic):
    """
    Busca Gulosa.
    - num_visited: quantos nós foram removidos da fronteira (expandidos).
    - num_generated: quantos nós novos foram efetivamente adicionados à fronteira.
    """
    # frontier: min-heap (h_value, state, path, depth, cost_so_far)
    frontier = []
    h_value = heuristic(start, goal)
    heapq.heappush(frontier, (h_value, start, [start], 0, 0))

    visited = set([start])

    num_visited = 0
    num_generated = 0

    while frontier:
        _, state, path, depth, cost_so_far = heapq.heappop(frontier)
        num_visited += 1  # nó expandido

        if state == goal:
            return {
                'start': start,
                'goal': goal,
                'path': path,
                'cost': cost_so_far,
                'visited': num_visited,
                'generated': num_generated
            }

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                num_generated += 1  # só conta se for realmente adicionado
                new_cost = cost_so_far + cost_function(state, neighbor, depth+1)
                new_path = path + [neighbor]
                new_h = heuristic(neighbor, goal)
                heapq.heappush(frontier, (new_h, neighbor, new_path, depth+1, new_cost))

    return None
