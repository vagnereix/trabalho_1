Com base nos **dados** do arquivo de resultados (com as 50 execuções e as diversas combinações de Custo e Heurística), é possível **destacar** alguns pontos importantes na comparação entre a **Busca Gulosa** (Greedy) e o **A\***:

1. **Custo do Caminho Encontrado**

   - Em praticamente todas as instâncias, o **custo** final obtido pelo **A\*** foi **igual ou menor** que o custo encontrado pela Busca Gulosa.
   - A Gulosa, por priorizar somente a heurística para avançar, muitas vezes “despreza” o custo acumulado, o que faz com que ela encontre trajetos **mais longos** (ou seja, custo maior). Já o A\* equilibra heurística e custo acumulado, garantindo caminhos de menor (ou igual) custo.

2. **Nós Visitados e Gerados**

   - Embora a Busca Gulosa possa, em algumas execuções, parecer mais “rápida” (com menos nós visitados/gerados no início), o fato de **não** levar em conta o custo real pode levá-la a expandir ou revisitar caminhos errados e acabar, em certos casos, gerando mais nós no total.
   - O A\*, por outro lado, tende a expandir mais nós que a Gulosa, mas **garante** um melhor resultado em termos de solução final (caminho). Nos logs, vê-se que A\* usualmente mantém as expansões controladas (principalmente quando a heurística é boa), sem perder de vista o custo acumulado.

3. **Influencia das Heurísticas**

   - Em todos os testes, quando a heurística **H1** ou **H2** é “admissível/consistente”, o A\* encontra o caminho **ótimo** (ou muito próximo) com custo menor (ou igual) que o da Gulosa.
   - A Gulosa se beneficia de uma heurística muito boa (que “aponta” direto para o objetivo), mas quando a heurística é menos direcional, ela pode se perder e pagar caro em custo total.
   - Observando as linhas com combinações de **C4 + H1** ou **C4 + H2**, por exemplo, há casos em que a Gulosa até sai com custo relativamente menor que em outras combinações, mas **ainda** não chega no custo tão baixo quanto o A\* em boa parte das execuções.

4. **Diferença entre as Funções de Custo (C1, C2, C3, C4)**

   - Analisando linhas como “Greedy + C1 + H1” vs. “Greedy + C2 + H1” ou “A* + C3 + H2” vs. “A* + C4 + H2”, percebe-se que algumas funções de custo geram caminhos ligeiramente diferentes, mas ainda assim a Gulosa não se aproxima do custo ótimo em boa parte dos casos.
   - O A\* ajusta-se melhor a quaisquer das quatro funções de custo, pois “compensa” a variação do custo real com a heurística.

5. **Conclusão Geral**
   - Dos registros acima, fica claro que a **Busca Gulosa** acaba sendo mais “arriscada”: se a heurística **não** for altamente precisa em apontar o caminho certo, ela tende a produzir caminhos de custo elevado.
   - O **A\*** se mostra **mais robusto**: embora possa visitar alguns nós a mais, entrega soluções de **custo** final consistentemente **menor** (ou igual) ao da Gulosa.
   - Portanto, considerando os 50 experimentos, a **A\*** se sai melhor em termos de qualidade de solução (custo do percurso), enquanto a Gulosa, mesmo rápida em alguns cenários, não garante bom desempenho no que diz respeito ao custo final.

_Os arquivos considerados para análise estão em `./at1/experiments/experiment_3_files`._
