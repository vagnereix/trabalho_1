import random
import os
from datetime import datetime

from ..algorithms.search_bfs import bfs
from ..algorithms.search_dfs import dfs
from ..utils.city import get_neighbors_random, MAX_X, MAX_Y
from ..utils.costs import cost_c1, cost_c2, cost_c3, cost_c4


def main(output_folder="./at1/experiments/experiment_4_files"):
    """
    Executa o experimento 4 conforme descrito:
      - 20 pares iniciais/finais aleatórios
      - Para cada par:
          * BFS 10x (vizinhos gerados em ordem aleatória)
          * DFS 10x (idem)
        Em cada execução, calcular e salvar resultados com f1, f2, f3, f4.
    """

    # Gera um nome de arquivo único baseado na data/hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = os.path.join(output_folder, f"results_4_{timestamp}.txt")

    # Cria a pasta de saída se não existir
    os.makedirs(output_folder, exist_ok=True)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write("# Experimento 4: BFS e DFS com vizinhança randomizada\n\n")
        
        # Repetir 20 vezes
        for i in range(1, 21):
            # Gera (x1, y1) e (x2, y2) aleatórios
            x1 = random.randint(0, MAX_X)
            y1 = random.randint(0, MAX_Y)
            x2 = random.randint(0, MAX_X)
            y2 = random.randint(0, MAX_Y)
            start = (x1, y1)
            goal  = (x2, y2)

            outfile.write(f"## Par {i}: start={start}, goal={goal}\n")

            # BFS 10 vezes
            for run_bfs in range(1, 11):
                # Roda BFS com get_neighbors_random
                result_bfs = bfs(start, goal, get_neighbors_random, cost_function=cost_c1)
                # result_bfs é um dict com {start, goal, path, cost, visited, generated}

                if result_bfs is None:
                    outfile.write(f"BFS run={run_bfs} -> NENHUM CAMINHO ENCONTRADO!\n")
                else:
                    path = result_bfs['path']
                    visited = result_bfs['visited']
                    generated = result_bfs['generated']
                    
                    # Calcula custos com f1, f2, f3, f4
                    cost_f1 = result_bfs['cost']  # pois já usamos cost_c1
                    cost_f2 = _calc_cost_for_path(path, cost_c2) 
                    cost_f3 = _calc_cost_for_path(path, cost_c3)
                    cost_f4 = _calc_cost_for_path(path, cost_c4)

                    outfile.write(
                        f"BFS rodada={run_bfs} Caminho={path} "
                        f"Visitados={visited} Gerados={generated} "
                        f"Custo_C1={cost_f1} Custo_C2={cost_f2} "
                        f"Custo_C3={cost_f3} Custo_C4={cost_f4}\n"
                    )

            # DFS 10 vezes
            for run_dfs in range(1, 11):
                result_dfs = dfs(start, goal, get_neighbors_random, cost_function=cost_c1)
                if result_dfs is None:
                    outfile.write(f"DFS run={run_dfs} -> NENHUM CAMINHO ENCONTRADO!\n")
                else:
                    path = result_dfs['path']
                    visited = result_dfs['visited']
                    generated = result_dfs['generated']

                    # Custos com f1, f2, f3, f4
                    cost_f1 = result_dfs['cost']  # pois já usamos cost_c1
                    cost_f2 = _calc_cost_for_path(path, cost_c2) 
                    cost_f3 = _calc_cost_for_path(path, cost_c3)
                    cost_f4 = _calc_cost_for_path(path, cost_c4)

                    outfile.write(
                        f"DFS rodada={run_dfs} path={path} "
                        f"Visitados={visited} Gerados={generated} "
                        f"Custo_C1={cost_f1} Custo_C2={cost_f2} "
                        f"Custo_C3={cost_f3} Custo_C4={cost_f4}\n"
                    )

            outfile.write("\n")  # separa blocos

    print(f"Resultados salvos em: {output_filename}")


def _calc_cost_for_path(path, cost_func):
    """
    Função auxiliar: dada uma lista de (x, y) e uma cost_func,
    soma o custo passo a passo.
    """
    if not path or len(path) < 2:
        return 0
    total = 0
    for i in range(len(path) - 1):
        curr = path[i]
        nxt = path[i+1]
        depth = i + 1  # ou alguma convenção de profundidade
        total += cost_func(curr, nxt, depth)
    return total


if __name__ == "__main__":
    main()
