import random

MAX_X = 30
MAX_Y = 30

def get_neighbors(state):
    """
    Retorna os estados (x, y) vizinhos de 'state', considerando
    ações que movem o agente para cima, baixo, esquerda ou direita,
    respeitando as fronteiras [0..MAX_X, 0..MAX_Y].
    """
    x, y = state
    neighbors = []
    
    # Ação: mover para cima (x, y+1)
    if y + 1 <= MAX_Y:
        neighbors.append((x, y+1))
    
    # Ação: mover para baixo (x, y-1)
    if y - 1 >= 0:
        neighbors.append((x, y-1))
    
    # Ação: mover para a direita (x+1, y)
    if x + 1 <= MAX_X:
        neighbors.append((x+1, y))
    
    # Ação: mover para a esquerda (x-1, y)
    if x - 1 >= 0:
        neighbors.append((x-1, y))
    
    return neighbors

def get_neighbors_random(state):
    """
    Retorna os estados (x, y) vizinhos em ordem aleatória.
    """
    neighbors = get_neighbors(state)

    # Embaralha a lista de vizinhos
    random.shuffle(neighbors)

    return neighbors
