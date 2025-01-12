**Análise geral comparando BFS, DFS e Custo Uniforme (Uniform Cost) nos cenários apresentados**:

1. **BFS (Busca em Largura)**

   - De modo geral, o BFS encontra **caminhos com menor número de passos** (ou menor profundidade) para chegar ao objetivo, pois sua estratégia de expansão em “camadas” prioriza sempre os nós mais próximos do estado inicial.
   - Observando as tabelas, percebe-se que, quase sempre, o **custo total** encontrado pelo BFS é competitivo ou pelo menos razoável (principalmente quando o custo está diretamente relacionado à quantidade de passos).
   - O BFS, porém, costuma ter um **número considerável de nós gerados e visitados** (às vezes bastante alto), já que ele expande em largura e não “pula” camadas.

2. **DFS (Busca em Profundidade)**

   - O DFS pode se alongar bastante pelo espaço de busca (indo “fundo” antes de testar alternativas), o que faz com que o **caminho encontrado seja, em geral, mais longo** que o de outros algoritmos (quando não há um bom critério de corte ou heurística).
   - Em vários cenários, o DFS gera caminhos com custos elevados (às vezes muito maiores que BFS ou Custo Uniforme), pois ele tende a “descer” por caminhos que nem sempre são promissores.
   - O DFS costuma expandir muitos nós em profundidade, mas dependendo da ordem de geração (ou do critério de parada) pode terminar rápido _se_ o objetivo for encontrado precocemente. Entretanto, quando não encontra rapidamente, a **quantidade de nós visitados e gerados** também pode ficar muito grande.

3. **Custo Uniforme (Uniform Cost Search)**
   - O Custo Uniforme prioriza, a cada etapa, expandir o nó de **menor custo acumulado**. Quando o custo por passo é uniforme ou correlacionado à quantidade de passos, ele se assemelha ao BFS. Entretanto, quando cada ação tem um custo diferente ou quando existem várias funções de custo (C1, C2, C3, C4), a busca de custo uniforme consegue, em geral, caminhos de **custo total mais baixo** que BFS/DFS, pois privilegia expandir o caminho de menor custo acumulado, não necessariamente o de menor profundidade.
   - Dependendo do cenário (e da função de custo utilizada), o Uniform pode visitar mais nós que o BFS ou, às vezes, até menos — mas de forma geral, tende a expandir bastantes nós também (porque precisa manter filas de prioridade e analisar custos cumulativos).
   - Pelos dados, nota-se que, em boa parte das situações, o **custo encontrado pelo Uniform tende a ser um dos menores** (ou empatando com BFS, se o custo for basicamente a “contagem de passos” igual para todas as ações).

### Principais conclusões gerais

- **BFS**:

  - Traz caminhos curtos em número de ações (passos), mas nem sempre com menor “custo” se o problema penaliza ou valoriza cada passo de forma diferente.
  - De forma consistente, percorre muitos nós, pois expande tudo em “camadas”.

- **DFS**:

  - Costuma apresentar caminhos bem mais longos, pois desce a árvore de busca até o fundo antes de voltar;
  - Frequentemente encontra soluções de **custo muito alto**, especialmente sem heurísticas ou sem um limite de profundidade;
  - Pode visitar (e gerar) uma quantidade enorme de nós, dependendo da profundidade.

- **Custo Uniforme**:
  - Quando existe uma função de custo diferenciada por ação ou por passo, tende a encontrar **soluções de menor custo total** (pelo menos, quando o custo é condizente com as arestas).
  - Em muitas execuções, é competitivo com BFS (quando os custos são uniformes ou muito parecidos).
  - Em geral, consome mais memória e tempo que o BFS/DFS simples, pois precisa gerenciar prioridades (mas garante o menor custo, se cada passo tiver um custo adequado).

Em resumo, **se a preocupação for só a quantidade de passos**, o BFS (ou DFS, com muito cuidado) pode ser suficiente; **se o objetivo é garantir o caminho de menor custo (soma de pesos)**, o Custo Uniforme é mais apropriado. O DFS puro, por sua vez, muitas vezes **não é indicado** para problemas em que se deseja um custo (ou caminho) minimizado, pois tende a achar qualquer solução, sem garantia de ser boa.

_Os arquivos considerados para análise estão em `./at1/experiments/experiment_1_files`._
