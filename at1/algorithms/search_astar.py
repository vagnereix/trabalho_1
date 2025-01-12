import heapq

def a_star_search(start, goal, get_neighbors, cost_function, heuristic):
    """
    A* Search.
    - num_visited: quantos nós foram removidos da fronteira (expandidos).
    - num_generated: quantos nós novos foram efetivamente adicionados à fronteira.
    f(n) = g(n) + h(n).
    """
    # frontier: (f_value, state, path, depth, cost_so_far)
    frontier = []
    h_value = heuristic(start, goal)
    heapq.heappush(frontier, (h_value, start, [start], 0, 0))

    best_cost = {start: 0}

    num_visited = 0
    num_generated = 0

    while frontier:
        f_value, state, path, depth, cost_so_far = heapq.heappop(frontier)
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

        # Se o custo atual não é o melhor custo, ignore
        if cost_so_far > best_cost.get(state, float('inf')):
            continue

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            g_new = cost_so_far + cost_function(state, neighbor, depth+1)
            if g_new < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = g_new
                num_generated += 1  # só conta se for efetivamente adicionado
                new_path = path + [neighbor]
                h_new = heuristic(neighbor, goal)
                f_new = g_new + h_new
                heapq.heappush(frontier, (f_new, neighbor, new_path, depth+1, g_new))

    return None
