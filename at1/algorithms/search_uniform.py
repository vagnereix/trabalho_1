import heapq

def uniform_cost_search(start, goal, get_neighbors, cost_function):
    """
    Dijkstra / Busca de Custo Uniforme.
    - num_visited: quantos nós foram removidos da fronteira (expandidos).
    - num_generated: quantos nós novos foram efetivamente adicionados à fronteira.
    """
    # frontier: min-heap com (cost_so_far, state, path, depth)
    frontier = []
    heapq.heappush(frontier, (0, start, [start], 0))

    # Armazena o melhor custo encontrado até cada estado
    best_cost = {start: 0}

    num_visited = 0
    num_generated = 0

    while frontier:
        cost_so_far, state, path, depth = heapq.heappop(frontier)
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

        # Se o custo sacado da fila não é o melhor custo atual, ignoramos
        if cost_so_far > best_cost.get(state, float('inf')):
            continue

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            new_cost = cost_so_far + cost_function(state, neighbor, depth+1)
            # Só adicionamos se for um custo melhor do que o melhor conhecido
            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                new_path = path + [neighbor]
                num_generated += 1  # só conta se for de fato adicionar à fronteira
                heapq.heappush(frontier, (new_cost, neighbor, new_path, depth+1))

    return None
