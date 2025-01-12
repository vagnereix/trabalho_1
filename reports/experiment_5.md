A partir dessa amostra de execuções, podemos observar **padrões** relevantes ao comparar os resultados (custo total, número de nós visitados/gerados etc.) entre as diferentes combinações de custo (C1–C4) e heurística (H1, H2). Em particular:

1. **Diferença de custos entre as funções**

   - Em muitas execuções, notamos que a combinação com a função de custo **C4** (seja com H1 ou H2) costuma gerar **custos mais baixos** (ou um dos mais baixos) quando comparada a C1, C2 e C3.
   - A função C2, por outro lado, tende a apresentar custos mais elevados em várias execuções.

2. **Número de nós visitados e gerados**

   - De modo geral, usar a heurística **H2** (Manhattan) frequentemente resulta em **menos nós visitados** e **menos nós gerados** do que a H1, embora isso não seja uma regra rígida em todos os casos. Podemos ver exemplos em que (C4 + H2) apresenta valores bem baixos de “Visitados” e “Gerados”, indicando que a busca ficou mais “focada”.
   - Quando o custo total e a expansão de nós não estão alinhados (por exemplo, um custo menor mas com maior expansão), isso indica que a heurística pode ter influenciado fortemente o “caminho” durante a busca.

3. **Influência das farmácias**

   - Como o experimento exige passar em pelo menos uma farmácia, há casos em que o trajeto “sai do caminho” para incluir esses pontos. Isso pode elevar o custo ou fazer com que surjam grandes sequências de movimentos de “ida e volta” entre as farmácias e o caminho principal.
   - Algumas vezes a farmácia está quase na rota direta, então o custo extra é pequeno; em outras, a farmácia força um desvio considerável.

4. **Tendências de desempenho**

   - **C4 + H2** desponta em várias execuções como uma das melhores combinações (custo final baixo e menos nós visitados/gerados).
   - Em alguns cenários, **C1** também gera soluções de custo relativamente baixo, mas normalmente expande mais nós (ou tem resultados mais inconsistentes) em relação ao C4.
   - **C3** costuma ficar intermediário, com custo final próximo ao C1/C4, porém com maior número de nós visitados.

5. **Conclusão resumida**
   - Em termos de **eficiência** (menos nós visitados/gerados) e **custo do caminho**, **C4** parece ser uma função de custo que se adapta bem à heurística H2, reduzindo tanto o custo final quanto o esforço de busca na maioria das execuções.
   - A heurística H2 (Manhattan) — possivelmente por ser “mais fiel” à distância em grade — costuma orientar a busca para expandir menos nós, sobretudo quando combinada com C4.
   - Já a C2 frequentemente resulta em caminhos mais caros, e a H1 (Euclidiana) muitas vezes explora mais nós em cenários onde o percurso exige mudança de eixos frequente (subidas/descidas e deslocamento horizontal).

Essas observações servem como **tendência**. Se quisermos “bater o martelo” de que _uma_ combinação é definitivamente melhor, precisaríamos de mais análises estatísticas (por exemplo, médias de custo, desvios padrão, gráficos comparativos etc.). Mas pelos dados brutos apresentados, as combinações de **C4 + H2** costumam aparecer com destaque, tanto em economia de custo quanto em nós gerados/visitados.

_Os arquivos considerados para análise estão em `./at1/experiments/experiment_5_files`._
