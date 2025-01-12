import random
import os
from datetime import datetime

from ..utils.city import get_neighbors, MAX_X, MAX_Y
from ..utils.costs import cost_c1, cost_c2, cost_c3, cost_c4
from ..utils.heuristics import h1_euclidean_10, h2_manhattan_10

from ..algorithms.search_greedy import greedy_search
from ..algorithms.search_astar import a_star_search

def main(output_folder="./at1/experiments/experiment_3_files"):
    """
    Executa 50 vezes (em um loop), gerando pares (x1,y1) e (x2,y2).
    Para cada par gerado:
      i)  Faz a Busca Gulosa com custo f1..f4 + heurística H1,
          e custo f1..f4 + heurística H2.
      ii) Faz a Busca A* com custo f1..f4 + heurística H1,
          e custo f1..f4 + heurística H2.

    Guarda os resultados em um arquivo .txt, incluindo caminho, custo,
    nós visitados/gerados etc.
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
    
    # Gera um nome de arquivo único baseado na data/hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = os.path.join(output_folder, f"results_{timestamp}.txt")

    # Cria a pasta de saída se não existir
    os.makedirs(output_folder, exist_ok=True)

    with open(output_filename, "w", encoding="utf-8") as f:
        # Loop de 50 repetições (ou quantas quiser)
        for i in range(1, 51):
            # Gera aleatoriamente coordenadas do estado inicial (x1, y1) e objetivo (x2, y2)
            x1 = random.randint(0, MAX_X)
            y1 = random.randint(0, MAX_Y)
            x2 = random.randint(0, MAX_X)
            y2 = random.randint(0, MAX_Y)

            start_state = (x1, y1)
            goal_state  = (x2, y2)

            f.write(f"=== Execução {i} ===\n")
            f.write(f"Estado Inicial: {start_state}\n")
            f.write(f"Objetivo:       {goal_state}\n\n")
            
            ##################################
            # i) Busca Gulosa (f1..f4 + H1,H2)
            ##################################
            f.write("--- BUSCA GULOSA ---\n")
            for (cost_name, cf) in cost_functions:
                for (heur_name, hf) in heuristics:
                    result = greedy_search(start_state, goal_state, get_neighbors, cf, hf)
                    if result is not None:
                        f.write(f"  Greedy + {cost_name} + {heur_name}: ")
                        f.write(f"Caminho={result['path']}, ")
                        f.write(f"Custo={result['cost']}, ")
                        f.write(f"Visitados={result['visited']}")
                        f.write(f", Gerados={result['generated']}")
                        f.write("\n")
                    else:
                        f.write(f"  Greedy + {cost_name} + {heur_name}: SEM SOLUÇÃO\n")
            
            f.write("\n")
            
            ##################################
            # ii) A* (f1..f4 + H1,H2)
            ##################################
            f.write("--- A* ---\n")
            for (cost_name, cf) in cost_functions:
                for (heur_name, hf) in heuristics:
                    result = a_star_search(start_state, goal_state, get_neighbors, cf, hf)
                    if result is not None:
                        f.write(f"  A* + {cost_name} + {heur_name}: ")
                        f.write(f"Caminho={result['path']}, ")
                        f.write(f"Custo={result['cost']}, ")
                        f.write(f"Visitados={result['visited']}")
                        f.write(f", Gerados={result['generated']}")
                        f.write("\n")
                    else:
                        f.write(f"  A* + {cost_name} + {heur_name}: SEM SOLUÇÃO\n")
            
            f.write("\n")  # quebra de linha após cada execução

    print(f"Execução concluída! Resultados salvos em '{output_filename}'.")


if __name__ == "__main__":
    main()
