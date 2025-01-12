**Comparando as Execuções BFS vs. DFS**

A partir da listagem de caminhos, custos e estatísticas (nós visitados/gerados) de cada execução, podemos observar alguns pontos principais:

1. **Características dos Caminhos Encontrados**

   - **BFS (Breadth-First Search)**, em geral, encontra caminhos de menor profundidade (ou menor número de passos), especialmente quando o grafo é não-ponderado. Observamos que, em todos os pares (start, goal), o BFS encontra caminhos com um número de saltos relativamente pequeno (e de forma consistente).
   - **DFS (Depth-First Search)**, por sua vez, pode fazer “desvios” bem grandes no grafo, visitando muitos nós “desnecessários” antes de encontrar a solução. Isso fica nítido pelos comprimentos de caminho muito maiores e também pelos custos f1, f2, f3, f4 frequentemente elevados em algumas execuções do DFS.

2. **Custos e Funções de Avaliação (f1, f2, f3, f4)**

   - Notamos que, nas estatísticas de custos, o BFS tende a ter valores (f1, f2, f3, f4) consideravelmente **mais baixos** (ou pelo menos mais consistentes) do que o DFS em muitas das execuções.
   - No DFS, é comum surgir caminhos com custo bem maior (por exemplo, valores de f1 chegando a 1000+, 2000+ em alguns casos), enquanto no BFS esse custo raramente passa de alguns poucos centenas de unidades. Isso indica que o **DFS explora muito** do grafo antes de finalmente chegar à meta.

3. **Consistência dos Caminhos**

   - O BFS apresenta **pouca variação** entre as diferentes runs (execuções) no mesmo par (start, goal). Por exemplo, para o Par 4 ou Par 7, o BFS praticamente sempre retorna uma variação do mesmo caminho, e as estatísticas de custo f1, f2 etc. são muito semelhantes.
   - O DFS, por outro lado, pode ter runs que encontram caminhos razoavelmente “bons” (com custo não tão alto), mas também pode ter runs bastante “ruins” (com custo enorme, caminhos com voltas extensas etc.).

4. **Observação sobre a “vizinhança randomizada”**

   - Nos experimentos relatados, parece que tanto BFS quanto DFS recebem alguma **ordem de vizinhos randomizada** (aleatória). Então, cada “run” pode gerar uma permutação diferente do grafo e, consequentemente, um caminho ligeiramente diferente.
   - Entretanto, a **BFS** invariavelmente encontra um caminho curto (tende a ser ótimo ou próximo do ótimo em número de passos), mesmo com a ordem de vizinhos randomizada.
   - Já a **DFS** pode variar muito conforme muda a ordem em que os vizinhos são visitados. Em alguns runs, o DFS até encontra um caminho relativamente curto; em outros, percorre boa parte do grafo antes de chegar ao objetivo.

5. **Conclusão: BFS vs. DFS**  
   Em termos de **qual é o melhor caminho** (isto é, menor número de passos ou menor custo nos termos f1, f2, f3, f4), **a BFS** tende a produzir **caminhos muito mais consistentes e de menor custo** para todas as funções, enquanto **a DFS** frequentemente resulta em caminhos muito mais extensos, com custo total elevado e visitando mais nós do que o necessário. Isso reforça a ideia geral de que BFS encontra soluções ótimas em termos de profundidade (quando não há pesos) e DFS é altamente dependente de sorte/ordem de vizinhança, podendo encontrar soluções boas em alguns casos, mas também soluções bem ruins em outras execuções.

_Os arquivos considerados para análise estão em `./at1/experiments/experiment_4_files`._
