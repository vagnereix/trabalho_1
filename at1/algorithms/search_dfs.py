def dfs(start, goal, get_neighbors, cost_function):
    """
    Busca em Profundidade (DFS).
    - num_visited: quantos nós foram retirados da pilha (expandidos).
    - num_generated: quantos nós novos foram efetivamente adicionados à pilha.
    """
    stack = []
    visited = set()

    # (state, path, depth, cost_so_far)
    stack.append((start, [start], 0, 0))
    visited.add(start)

    num_visited = 0
    num_generated = 0

    while stack:
        state, path, depth, cost_so_far = stack.pop()
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
                stack.append((neighbor, new_path, depth+1, new_cost))

    return None
