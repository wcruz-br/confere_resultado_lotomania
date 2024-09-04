# Quer saber se ganhou na Lotomania?

Esse script Python verifica os resultados de apostas da [Lotomania](https://loterias.caixa.gov.br/Paginas/Lotomania.aspx) em relação a uma lista de resultados de sorteio informados.

## Como usar

Defina as apostas na lista `meus_numeros_apostas`, onde cada sublista representa uma aposta separada.

Em seguida, defina a lista de resultados de sorteios na lista `concursos_e_resultados`. Cada elemento nesta lista é uma sublista, contendo o número do sorteio e os números vencedores codificados (tudo grudadinho em uma string de pares de dígitos). Fiz dessa forma para facilitar o copy/paste dos resultados na [página de resultdos da Lotomania](https://loterias.caixa.gov.br/Paginas/Lotomania.aspx).

O script então verifica os acertos de cada aposta em cada concurso, dizendo quantos números você acertou.

Por fim, verifica se alguma das apostas ganhou em algum dos sorteios. Pelas regras da Lotomania, você ganha se acertar pelo menos 15 números - ou se não acertar nenhum.

## Melhorias futuras

Melhorias que eu quero fazer nesse script, mas não sei quando vou ter tempo (honestamente ele não é minha prioridade). Se quiser ajudar com isso, seria ótimo!

1. Baixar automaticamente do site da Caixa o xls com os resultados, bastando informar então um range de concursos. Infelizmente eles não disponibilzam uma API. Esse xls pode ser baixado manualmente na página de resultados (perto do final da página), mas não há uma URL direta para fazer isso. Parece que complicaram de propósito.
2. Atender a regras de várias loterias, como Mega-Sena, Lotofácil, etc.
3. Montar uma interface gráfica (web, talvez) para o usuário escolher com o mouse os números que compõem cada aposta.

---

Versão original por [wcruz-br](https://github.com/wcruz-br)