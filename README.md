Este script verifica os resultados de apostas da Lotomania em relação a uma lista de resultados de sorteio informados.

Defina as apostas na lista `meus_numeros_apostas`, onde cada sublista representa uma aposta separada.

Em seguida, defina a lista de resultados de sorteios na lista `concursos_e_resultados`. Cada elemento nesta lista
é uma sublista contendo o número do sorteio e os números vencedores codificados como uma string de pares de dígitos.
Fiz dessa forma para facilitar o copy/paste dos resultados na página https://loterias.caixa.gov.br/Paginas/Lotomania.aspx

O script então verifica os acertos de cada aposta em cada concurso, dizendo quantos números você acertou.
Por fim, verifica se alguma das apostas ganhou em algum dos sorteios (pelas regras da Lotomania, você ganha
se acertar pelo menos 15 números ou se não acertar nenhum).

TODO: baixar automaticamente do site da Caixa o xls com os resultados, bastando informar então um range de concursos
