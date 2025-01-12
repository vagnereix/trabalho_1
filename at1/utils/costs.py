# costs.py

def cost_c1(current_state, next_state, depth):
    """
    C1: Todas as ações têm custo 10.
    O 'depth' pode ser o número de arestas no caminho até este estado,
    mas não influencia no custo aqui.
    """
    return 10

def cost_c2(current_state, next_state, depth):
    """
    C2: Ações na vertical (y muda) custam 10,
        Ações na horizontal (x muda) custam 15.
    """
    x1, y1 = current_state
    x2, y2 = next_state
    if x1 == x2:
        # Mudou y => vertical
        return 10
    else:
        # Mudou x => horizontal
        return 15

def cost_c3(current_state, next_state, depth):
    """
    C3: Ações na vertical custam 10.
        Ações na horizontal custam 10 + ((depth - 1) mod 6).
    """
    x1, y1 = current_state
    x2, y2 = next_state
    if x1 == x2:
        # vertical
        return 10
    else:
        # horizontal
        return 10 + ((depth - 1) % 6)

def cost_c4(current_state, next_state, depth):
    """
    C4: Ações na vertical custam 10.
        Ações na horizontal custam 5 + (10 - (depth mod 11)).
    """
    x1, y1 = current_state
    x2, y2 = next_state
    if x1 == x2:
        # vertical
        return 10
    else:
        # horizontal
        return 5 + (10 - (depth % 11))
