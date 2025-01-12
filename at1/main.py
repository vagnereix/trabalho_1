import sys
import importlib
import os

from .utils.city import get_neighbors
from .utils.costs import cost_c1, cost_c2, cost_c3, cost_c4
from .utils.heuristics import h1_euclidean_10, h2_manhattan_10

from .algorithms.search_bfs import bfs
from .algorithms.search_dfs import dfs
from .algorithms.search_uniform import uniform_cost_search
from .algorithms.search_greedy import greedy_search
from .algorithms.search_astar import a_star_search

def run_experiment(experiment_number):
    """
    Executa o experimento especificado pelo número.
    """
    try:
        # Construir o nome do módulo do experimento
        module_name = f"at1.experiments.experiment_{experiment_number}_script"
        
        # Importar o módulo dinamicamente
        experiment_module = importlib.import_module(module_name)
        
        # Verificar se o módulo possui a função 'main'
        if hasattr(experiment_module, 'main'):
            experiment_module.main()
        else:
            print(f"O script do experimento {experiment_number} não possui uma função 'main()'.")
    except ModuleNotFoundError:
        print(f"Experimento {experiment_number} não encontrado. Verifique se o script 'experiment_{experiment_number}_script.py' existe em 'experiments/'.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar o Experimento {experiment_number}: {e}")

def main():
    """
    Executa o programa principal, que pode rodar algoritmos de busca ou experimentos.
    """
    if '--experiment' in sys.argv:
        try:
            # Obter o índice de '--experiment' e o número do experimento
            exp_index = sys.argv.index('--experiment')
            experiment_number = int(sys.argv[exp_index + 1])
        except (ValueError, IndexError):
            print("Uso correto para experimento: python3 -m at1.main --experiment <NUM_EXPERIMENTO>")
            sys.exit(1)
        
        # Executar o experimento solicitado
        run_experiment(experiment_number)
        sys.exit(0)  # Encerrar após rodar o experimento

    if len(sys.argv) < 8:
        print("Uso: python3 -m at1.main <ALG> <COST> <HEUR> <start_x> <start_y> <goal_x> <goal_y>")
        print("Exemplo: python3 -m at1.main BFS C1 none 0 0 3 4")
        print("Algoritmos (ALG): BFS | DFS | UNIFORM | GREEDY | ASTAR")
        print("Funções de custo (COST): C1 | C2 | C3 | C4")
        print("Heurísticas (HEUR): H1 | H2 | none (para BFS, DFS, Uniform)")
        print("---------------------------------------------------------")
        print("Executar experimentos da Seção 5: python3 -m at1.main --experiment <NUM_EXPERIMENTO>")
        sys.exit(1)
    
    alg = sys.argv[1].upper()
    cost_choice = sys.argv[2].upper()
    heur_choice = sys.argv[3].upper()
    
    try:
        start_x = int(sys.argv[4])
        start_y = int(sys.argv[5])
        goal_x = int(sys.argv[6])
        goal_y = int(sys.argv[7])
    except ValueError:
        print("As coordenadas de início e objetivo devem ser inteiros.")
        sys.exit(1)
    
    start_state = (start_x, start_y)
    goal_state = (goal_x, goal_y)
    
    # Seleciona função de custo
    if cost_choice == 'C1':
        cost_fn = cost_c1
    elif cost_choice == 'C2':
        cost_fn = cost_c2
    elif cost_choice == 'C3':
        cost_fn = cost_c3
    elif cost_choice == 'C4':
        cost_fn = cost_c4
    else:
        print("Função de custo inválida. Escolha entre C1, C2, C3, C4.")
        sys.exit(1)
    
    # Seleciona função de heurística
    if heur_choice == 'H1':
        heur_fn = h1_euclidean_10
    elif heur_choice == 'H2':
        heur_fn = h2_manhattan_10
    elif heur_choice == 'NONE':
        heur_fn = None
    else:
        print("Heurística inválida. Escolha entre H1, H2, none.")
        sys.exit(1)
    
    result = None
    
    # Escolhe algoritmo
    if alg == 'BFS':
        result = bfs(start_state, goal_state, get_neighbors, cost_fn)
    elif alg == 'DFS':
        result = dfs(start_state, goal_state, get_neighbors, cost_fn)
    elif alg == 'UNIFORM':
        result = uniform_cost_search(start_state, goal_state, get_neighbors, cost_fn)
    elif alg == 'GREEDY':
        if heur_fn is None:
            print("Para busca Gulosa, forneça uma heurística (H1 ou H2).")
            sys.exit(1)
        result = greedy_search(start_state, goal_state, get_neighbors, cost_fn, heur_fn)
    elif alg == 'ASTAR':
        if heur_fn is None:
            print("Para A*, forneça uma heurística (H1 ou H2).")
            sys.exit(1)
        result = a_star_search(start_state, goal_state, get_neighbors, cost_fn, heur_fn)
    else:
        print("Algoritmo inválido. Escolha entre BFS, DFS, UNIFORM, GREEDY, ASTAR.")
        sys.exit(1)
    
    # Exibe resultado
    if result is None:
        print("Caminho não encontrado.")
    else:
        print("=== RESULTADO ===")
        print(f"Estado Inicial: {result['start']}")
        print(f"Objetivo:       {result['goal']}")
        print(f"Caminho:        {result['path']}")
        print(f"Custo total:    {result['cost']}")
        print(f"Nós visitados:  {result['visited']}")
        print(f"Nós gerados:    {result['generated']}")

if __name__ == "__main__":
    main()
