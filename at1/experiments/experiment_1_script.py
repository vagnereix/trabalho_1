import random
import os
from datetime import datetime

from ..utils.city import get_neighbors, MAX_X, MAX_Y
from ..utils.costs import cost_c1, cost_c2, cost_c3, cost_c4
from ..algorithms.search_bfs import bfs
from ..algorithms.search_dfs import dfs
from ..algorithms.search_uniform import uniform_cost_search


def main(output_folder="./at1/experiments/experiment_1_files"):
    # Lista das funções de custo
    cost_functions = [
        ('C1', cost_c1),
        ('C2', cost_c2),
        ('C3', cost_c3),
        ('C4', cost_c4),
    ]
    
    # Gerar um nome de arquivo único baseado na data e hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = os.path.join(output_folder, f"results_{timestamp}.txt")
    
    # Cria a pasta de saída se não existir
    os.makedirs(output_folder, exist_ok=True)
    
    with open(output_filename, "w", encoding="utf-8") as f:
        # Loop de 50 repetições
        for i in range(1, 51):
            # Gera aleatoriamente coordenadas do estado inicial (x1, y1) e objetivo (x2, y2)
            x1 = random.randint(0, MAX_X)
            y1 = random.randint(0, MAX_Y)
            x2 = random.randint(0, MAX_X)
            y2 = random.randint(0, MAX_Y)
            
            start_state = (x1, y1)
            goal_state  = (x2, y2)
            
            # Para evitar o caso (opcional) de início == objetivo:
            # while goal_state == start_state:
            #     x2 = random.randint(0, MAX_X)
            #     y2 = random.randint(0, MAX_Y)
            #     goal_state = (x2, y2)
            
            # Escreve informações iniciais
            f.write(f"=== Execução {i} ===\n")
            f.write(f"Estado Inicial: {start_state}\n")
            f.write(f"Objetivo:       {goal_state}\n")
            
            #####################
            # i) BFS (c1..c4)
            #####################
            f.write("--- BFS ---\n")
            for (cost_name, cf) in cost_functions:
                result = bfs(start_state, goal_state, get_neighbors, cf)
                if result is not None:
                    f.write(f"  BFS + {cost_name}: ")
                    f.write(f"Caminho={result['path']}, ")
                    f.write(f"Custo={result['cost']}, ")
                    f.write(f"Visitados={result['visited']}")
                    f.write(f", Gerados={result['generated']}")
                    f.write("\n")
                else:
                    f.write(f"  BFS + {cost_name}: SEM SOLUÇÃO\n")
            
            #####################
            # ii) DFS (c1..c4)
            #####################
            f.write("--- DFS ---\n")
            for (cost_name, cf) in cost_functions:
                result = dfs(start_state, goal_state, get_neighbors, cf)
                if result is not None:
                    f.write(f"  DFS + {cost_name}: ")
                    f.write(f"Caminho={result['path']}, ")
                    f.write(f"Custo={result['cost']}, ")
                    f.write(f"Visitados={result['visited']}")
                    f.write(f", Gerados={result['generated']}")
                    f.write("\n")
                else:
                    f.write(f"  DFS + {cost_name}: SEM SOLUÇÃO\n")
            
            #####################
            # iii) Custo Uniforme (c1..c4)
            #####################
            f.write("--- Custo Uniforme ---\n")
            for (cost_name, cf) in cost_functions:
                result = uniform_cost_search(start_state, goal_state, get_neighbors, cf)
                if result is not None:
                    f.write(f"  Uniform + {cost_name}: ")
                    f.write(f"Caminho={result['path']}, ")
                    f.write(f"Custo={result['cost']}, ")
                    f.write(f"Visitados={result['visited']}")
                    if 'generated' in result:
                        f.write(f", Gerados={result['generated']}")
                    f.write("\n")
                else:
                    f.write(f"  Uniform + {cost_name}: SEM SOLUÇÃO\n")
            
            f.write("\n")  # quebra de linha após cada bateria de testes

    print(f"Execução concluída! Resultados salvos em '{output_filename}'.")


if __name__ == "__main__":
    main()
