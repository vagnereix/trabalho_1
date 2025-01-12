Observando os dados dos 50 casos, vemos que:

1. **Custo Uniforme (Uniform)** sempre retorna caminhos compatíveis (por vezes ótimos em termos de custo de caminho para aquela função de custo específica), mas visita consideravelmente mais nós do que o A\* em boa parte das execuções (visivelmente, `visited` e `generated` costumam ser maiores em Uniform).
2. **A\*** invariavelmente encontra o mesmo caminho (ou um caminho de mesmo custo) que o Uniform para cada função de custo, mas com um número de nós visitados e gerados geralmente menor (isto significa que a heurística ajuda a “guiar” a busca).
3. Em algumas poucas situações, o Custo Uniforme e o A* encontram não só o mesmo custo de caminho mas também chegam a visitar um número até parecido de nós — porém, no geral, o A* visita (e gera) significativamente menos estados, confirmando que a heurística está acelerando a busca na maior parte dos casos.
4. Para C1, C2, C3, C4 — quando comparados, cada função de custo produz diferentes valores de caminho, mas a tendência é que o A\* encontre a mesma rota do Custo Uniforme (quando a heurística não subestima).
5. As heurísticas (H1 e H2) fazem diferença no **número de nós visitados/gerados** (em especial H2 tende a ser mais “agressiva” em algumas execuções, visitando menos nós). O custo total, em contrapartida, permanece igual ao do Uniform para a mesma função de custo, desde que a heurística seja admissível.

**Conclusão**

- Os resultados (caminhos com custo igual / coerente em ambos algoritmos) e a diferença de desempenho (A\* visitando menos nós que o Uniform na maior parte dos testes) indicam que as implementações de **Custo Uniforme** e **A\*** (bem como as heurísticas) estão se comportando como esperado.
- Onde A\* encontra o mesmo custo, mas expande bem menos nós que o Uniform, confirma que a heurística está ajudando.
- Nas execuções onde se vê um aumento significativo de nós visitados/gerados em Uniform, enquanto A\* faz a mesma rota com menos expansões, reforça a ideia de que a heurística está “direcionando” a busca e não está superestimando custos (ou seja, continua sendo admissível).

Em resumo, os resultados batem exatamente com o comportamento teórico esperado, o que sugere que **ambas as implementações (Uniform e A\*) estão corretas**.

_Os arquivos considerados para análise estão em `./at1/experiments/experiment_2_files`._
