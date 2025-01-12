import random
import os
from datetime import datetime

# Ajuste se necessário o caminho de import:
from ..utils.city import get_neighbors, MAX_X, MAX_Y
from ..utils.costs import cost_functions
from ..utils.heuristics import h1_euclidean_10, h2_manhattan_10

from ..algorithms.search_uniform import uniform_cost_search
from ..algorithms.search_astar import a_star_search


def main(output_folder="./at1/experiments/experiment_2_files"):
    """
    Executa 50 repetições, gerando pares aleatórios de estados (x1, y1) e (x2, y2),
    e comparando o desempenho das buscas:
      i)   Custo Uniforme (funções de custo c1, c2, c3, c4)
      ii)  A* (funções de custo c1..c4 combinadas com heurísticas h1, h2)
    Os resultados são salvos em um arquivo de texto na pasta 'experiment_2_files'.
    """
    
    # Lista de heurísticas (para A*)
    heur_functions = [
        ('H1', h1_euclidean_10),
        ('H2', h2_manhattan_10),
    ]
    
    # Gera um nome de arquivo único baseado na data e hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = os.path.join(output_folder, f"results_2_{timestamp}.txt")
    
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
            
            # (opcional) Evitar start == goal
            # while goal_state == start_state:
            #     x2 = random.randint(0, MAX_X)
            #     y2 = random.randint(0, MAX_Y)
            #     goal_state = (x2, y2)
            
            # Escreve informações iniciais
            f.write(f"=== Execução {i} ===\n")
            f.write(f"Estado Inicial: {start_state}\n")
            f.write(f"Objetivo:       {goal_state}\n\n")
            
            #####################################
            # i) Custo Uniforme (c1..c4)
            #####################################
            f.write("--- Custo Uniforme ---\n")
            for (cost_name, cf) in cost_functions:
                result = uniform_cost_search(start_state, goal_state, get_neighbors, cf)
                if result is not None:
                    f.write(f"  Uniform + {cost_name}: ")
                    f.write(f"Caminho={result['path']}, ")
                    f.write(f"Custo={result['cost']}, ")
                    f.write(f"Visitados={result['visited']}")
                    f.write(f", Gerados={result['generated']}")
                    f.write("\n")
                else:
                    f.write(f"  Uniform + {cost_name}: SEM SOLUÇÃO\n")
            
            #####################################
            # ii) A* (c1..c4) + (h1..h2)
            #####################################
            f.write("\n--- A* ---\n")
            for (cost_name, cf) in cost_functions:
                for (heur_name, hf) in heur_functions:
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
            
            f.write("\n")  # quebra de linha após cada bateria de testes

    print(f"Execução concluída! Resultados salvos em '{output_filename}'.")


if __name__ == "__main__":
    main()
