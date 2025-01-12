import random
import os
from datetime import datetime

# Imports do seu projeto (semelhantes aos do experimento 3):
from ..utils.city import get_neighbors, MAX_X, MAX_Y
from ..utils.costs import cost_c1, cost_c2, cost_c3, cost_c4
from ..utils.heuristics import h1_euclidean_10, h2_manhattan_10

from ..algorithms.search_astar import a_star_search
# Se quiser usar a busca gulosa também, você pode importar, mas aqui vamos focar em A*:
# from ..algorithms.search_greedy import greedy_search


def generate_unique_points(n=6):
    """
    Gera n pontos distintos dentro dos limites [0..MAX_X] e [0..MAX_Y].
    Retorna uma lista de tuplas (x, y).
    """
    points_set = set()
    while len(points_set) < n:
        px = random.randint(0, MAX_X)
        py = random.randint(0, MAX_Y)
        points_set.add((px, py))
    return list(points_set)


def a_star_with_at_least_one_pharmacy(start, goal, pharmacies, neighbor_func, cost_func, heuristic_func):
    """
    Exemplo de função que garante que o caminho passe em pelo menos
    uma farmácia, fazendo A* em duas etapas: 
      1) start -> farmácia 
      2) farmácia -> goal
    Combina o resultado de menor custo total (se houver caminhos viáveis).
    """
    best_path = None
    best_cost = float('inf')
    total_visited = 0
    total_generated = 0

    for pharm in pharmacies:
        # A* do início para esta farmácia
        res1 = a_star_search(start, pharm, neighbor_func, cost_func, heuristic_func)
        if res1 is None:
            continue

        # A* da farmácia para o objetivo
        res2 = a_star_search(pharm, goal, neighbor_func, cost_func, heuristic_func)
        if res2 is None:
            continue

        # Concatena os caminhos (removendo a posição duplicada da farmácia)
        combined_path = res1['path'] + res2['path'][1:]
        combined_cost = res1['cost'] + res2['cost']
        combined_visited = res1['visited'] + res2['visited']
        combined_generated = res1['generated'] + res2['generated']

        if combined_cost < best_cost:
            best_cost = combined_cost
            best_path = combined_path
            total_visited = combined_visited
            total_generated = combined_generated

    if best_path is None:
        return None

    return {
        'path': best_path,
        'cost': best_cost,
        'visited': total_visited,
        'generated': total_generated
    }


def main(output_folder="./at1/experiments/experiment_5_files"):
    """
    Executa 25 vezes (em um loop), gerando:
      - (x1,y1): endereço do trabalho do agente (estado inicial)
      - (x2,y2): endereço da casa do agente (estado objetivo)
      - (x3,y3)...(x6,y6): endereços das 4 farmácias (sem repetição)

    Para cada conjunto de pontos, faz:
      i)  A* (f1=cost_c1, h1=h1_euclidean_10) obrigando passar em >=1 farmácia.
      ii) A* para as combinações de f2,f3,f4 com h1 e h2, também passando em >=1 farmácia.

    Guarda os resultados (caminho, custo, nós visitados, gerados etc.) em um .txt.
    """

    # Lista das funções de custo
    cost_functions = [
        ('C1', cost_c1),
        ('C2', cost_c2),
        ('C3', cost_c3),
        ('C4', cost_c4),
    ]
    
    # Lista das heurísticas
    heuristics = [
        ('H1', h1_euclidean_10),
        ('H2', h2_manhattan_10),
    ]
    
    # Gera um nome de arquivo único baseado em data/hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = os.path.join(output_folder, f"results_5_{timestamp}.txt")

    # Cria a pasta de saída, se não existir
    os.makedirs(output_folder, exist_ok=True)

    with open(output_filename, "w", encoding="utf-8") as f:
        # Loop de 25 repetições
        for i in range(1, 26):
            # Gera 6 pontos aleatórios e distintos
            pts = generate_unique_points(6)
            # Atribui cada um dos pontos
            start_state = pts[0]   # trabalho
            goal_state  = pts[1]   # casa
            pharmacies  = pts[2:]  # quatro farmácias

            f.write(f"=== Execução {i} ===\n")
            f.write(f"Trabalho (início): {start_state}\n")
            f.write(f"Casa (objetivo):   {goal_state}\n")
            f.write(f"Farmácias:         {pharmacies}\n\n")

            ###########################################
            # i) A* usando cost_c1 + h1_euclidean_10
            #    (passando por pelo menos 1 farmácia)
            ###########################################
            (cost_name, cf) = cost_functions[0]  # 'C1', cost_c1
            (heur_name, hf) = ('H1', h1_euclidean_10)

            result = a_star_with_at_least_one_pharmacy(
                start_state, goal_state, pharmacies,
                get_neighbors, cf, hf
            )
            f.write(f"--- A* + {cost_name} + {heur_name} (>=1 farmácia) ---\n")
            if result is not None:
                f.write(f"  Caminho={result['path']}, ")
                f.write(f"Custo={result['cost']}, ")
                f.write(f"Visitados={result['visited']}, ")
                f.write(f"Gerados={result['generated']}\n")
            else:
                f.write("  SEM SOLUÇÃO (não há trajeto que passe em farmácia)\n")

            f.write("\n")

            ###################################################
            # ii) A* com as combinações (f2,f3,f4) × (H1,H2)
            #     também passando em pelo menos 1 farmácia
            ###################################################
            for (cost_name, cf) in cost_functions[1:]:  # pular cost_c1
                for (heur_name, hf) in heuristics:
                    result = a_star_with_at_least_one_pharmacy(
                        start_state, goal_state, pharmacies,
                        get_neighbors, cf, hf
                    )
                    f.write(f"--- A* + {cost_name} + {heur_name} (>=1 farmácia) ---\n")
                    if result is not None:
                        f.write(f"  Caminho={result['path']}, ")
                        f.write(f"Custo={result['cost']}, ")
                        f.write(f"Visitados={result['visited']}, ")
                        f.write(f"Gerados={result['generated']}\n")
                    else:
                        f.write("  SEM SOLUÇÃO (não há trajeto que passe em farmácia)\n")

                    f.write("\n")

            f.write("\n")  # quebra de linha após cada iteração

    print(f"Experimento 5 concluído! Resultados salvos em '{output_filename}'.")


if __name__ == "__main__":
    main()
