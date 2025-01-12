import math

def h1_euclidean_10(current_state, goal_state):
    """
    H1: 10 * distancia euclidiana
    """
    x1, y1 = current_state
    x2, y2 = goal_state
    return 10 * math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def h2_manhattan_10(current_state, goal_state):
    """
    H2: 10 * distancia Manhattan
    """
    x1, y1 = current_state
    x2, y2 = goal_state
    return 10 * (abs(x1 - x2) + abs(y1 - y2))

heuristics = [
    ('H1', h1_euclidean_10),
    ('H2', h2_manhattan_10),
]
