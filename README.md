# Trabalho 1 – Inteligência Artificial

Este repositório contém implementações de algoritmos de busca e scripts de experimentos para avaliá-los.

## Estrutura de Pastas

```
at1/
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── ...
│   └── ...
├── experiments/
│   ├── experiment_1_script.py
│   ├── experiment_2_script.py
│   └── ...
├── utils/
│   ├── ...
│   └── ...
├── main.py
└── README.md
```

- **`algorithms/`**: Implementações de algoritmos de busca (por exemplo, BFS, DFS, A\*).
- **`experiments/`**: Scripts para rodar diferentes experimentos e comparar resultados.
- **`utils/`**: Funções de suporte (utilitários) que podem ser usadas pelos algoritmos e experimentos.
- **`main.py`**: Arquivo principal que recebe parâmetros para executar os algoritmos ou experimentos.
- **`README.md`**: Este arquivo de instruções.

## Requisitos do Ambiente

- **Python 3.x**
  - [Download](https://www.python.org/downloads/).

## Como Executar os Algoritmos/Experimentos

1. **Entre no diretório principal do trabalho** (nomeado de `trabalho_1`).
2. **Execute o arquivo main** com argumentos que indiquem qual experimento você deseja rodar. Por exemplo:

   ```bash
   # No diretório /trabalho_1
   # Caso esteja no Windows, substitua `python3` por `py`
   $ python3 -m at1.main --experiment 1
   ```

   Ajuste o número do experimento conforme desejado.

3. **Verifique os resultados**:

   - Ao rodar cada experimento, pode ser gerada uma pasta dentro de `experiments` no formato `experiments_{n}_files` contendo registros (arquivos `.txt`).
   - Analise esses arquivos para conferir o comportamento dos algoritmos, comparação de custo, número de nós expandidos, etc.

4. **Para executar de forma customizada** qualquer um dos algoritmos:

   ```bash
   # Ou apenas `python3 -m at1.main` para ver as opções disponíveis
   $ python3 -m at1.main <ALG> <COST> <HEUR> <start_x> <start_y> <goal_x> <goal_y>
   ```

   - **BFS** sem heurística, usando custo C1, partindo de (0,0) até (3,4):
     ```bash
     $ python3 -m at1.main BFS C1 none 0 0 3 4
     ```
   - **DFS** com custo C2, partindo de (0,0) até (3,4):
     ```bash
     $ python3 -m at1.main DFS C2 none 0 0 3 4
     ```
   - **Uniform** Cost Search (Dijkstra) com custo C3, start (1,1) até (10,5):
     ```bash
     $ python3 -m at1.main UNIFORM C3 none 1 1 10 5
     ```
   - **Greedy** com custo C1, heurística H1, start (0,0) até (30,30):
     ```bash
     $ python3 -m at1.main GREEDY C1 H1 0 0 30 30
     ```
   - **A\*** com custo C2, heurística H2, start (2,2) até (5,5):
     ```bash
     $ python3 -m at1.main ASTAR C2 H2 2 2 5 5
     ```

5. O programa exibirá:

   - O estado inicial e o objetivo
   - O caminho completo (lista de estados)
   - O custo total calculado
   - A quantidade de nós visitados (ou expandidos)

6. **Para trocar as funções de custo** (por exemplo, entre C1, C2, C3, C4) basta modificar o parâmetro COST no comando de execução.

7. **Para trocar as heurísticas** (apenas para Greedy ou A\*) ajuste o parâmetro HEUR para H1 ou H2.
