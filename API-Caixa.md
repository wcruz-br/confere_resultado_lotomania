# API para obter resultados dos jogos

Pesquisando por aí descobri que há uma API da Caixa para obter os resultados dos jogos das diversas loterias disponíveis. 

No entanto, não há documentação, não há suporte e nenhuma informação oficial sobre ela. Parece ser de uso interno, o que significa que não dá pra confiar que estará sempre no ar, podendo ser desativada a qualquer momento.

Maaaas... como é o que temos para hoje, seguem os links:

https://servicebus2.caixa.gov.br/portaldeloterias/api/quina

https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena

https://servicebus2.caixa.gov.br/portaldeloterias/api/duplasena

https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil

https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania

https://servicebus2.caixa.gov.br/portaldeloterias/api/diadesorte

https://servicebus2.caixa.gov.br/portaldeloterias/api/timemania

https://servicebus2.caixa.gov.br/portaldeloterias/api/federal

https://servicebus2.caixa.gov.br/portaldeloterias/api/loteca

https://servicebus2.caixa.gov.br/portaldeloterias/api/supersete

## Formato

Essas chamadas retornam um JSON. Para obter o resultado de um concurso específico, basta acrescentar o número dele no final da URL, depois de uma barra.

Por exemplo: https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania/2661

```json
{
  "acumulado": true,
  "dataApuracao": "16/08/2024",
  "dataProximoConcurso": "19/08/2024",
  "dezenasSorteadasOrdemSorteio": [
    "27",
    "33",
    "46",
    "44",
    "56",
    "97",
    "79",
    "91",
    "42",
    "38",
    "11",
    "80",
    "14",
    "22",
    "32",
    "58",
    "10",
    "50",
    "28",
    "51"
  ],
  "exibirDetalhamentoPorCidade": true,
  "id": null,
  "indicadorConcursoEspecial": 1,
  "listaDezenas": [
    "10",
    "11",
    "14",
    "22",
    "27",
    "28",
    "32",
    "33",
    "38",
    "42",
    "44",
    "46",
    "50",
    "51",
    "56",
    "58",
    "79",
    "80",
    "91",
    "97"
  ],
  "listaDezenasSegundoSorteio": null,
  "listaMunicipioUFGanhadores": [],
  "listaRateioPremio": [
    {
      "descricaoFaixa": "20 acertos",
      "faixa": 1,
      "numeroDeGanhadores": 0,
      "valorPremio": 0.0
    },
    {
      "descricaoFaixa": "19 acertos",
      "faixa": 2,
      "numeroDeGanhadores": 3,
      "valorPremio": 68006.16
    },
    {
      "descricaoFaixa": "18 acertos",
      "faixa": 3,
      "numeroDeGanhadores": 44,
      "valorPremio": 2897.99
    },
    {
      "descricaoFaixa": "17 acertos",
      "faixa": 4,
      "numeroDeGanhadores": 435,
      "valorPremio": 293.12
    },
    {
      "descricaoFaixa": "16 acertos",
      "faixa": 5,
      "numeroDeGanhadores": 2733,
      "valorPremio": 46.65
    },
    {
      "descricaoFaixa": "15 acertos",
      "faixa": 6,
      "numeroDeGanhadores": 12012,
      "valorPremio": 10.61
    },
    {
      "descricaoFaixa": "0 acertos",
      "faixa": 7,
      "numeroDeGanhadores": 0,
      "valorPremio": 0.0
    }
  ],
  "listaResultadoEquipeEsportiva": null,
  "localSorteio": "ESPAÇO DA SORTE",
  "nomeMunicipioUFSorteio": "SÃO PAULO, SP",
  "nomeTimeCoracaoMesSorte": "\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000",
  "numero": 2661,
  "numeroConcursoAnterior": 2660,
  "numeroConcursoFinal_0_5": 0,
  "numeroConcursoProximo": 2662,
  "numeroJogo": 16,
  "observacao": "",
  "premiacaoContingencia": null,
  "tipoJogo": "LOTOMANIA",
  "tipoPublicacao": 3,
  "ultimoConcurso": true,
  "valorArrecadado": 4202061.0,
  "valorAcumuladoConcurso_0_5": 0.0,
  "valorAcumuladoConcursoEspecial": 0.0,
  "valorAcumuladoProximoConcurso": 3117401.6,
  "valorEstimadoProximoConcurso": 3800000.0,
  "valorSaldoReservaGarantidora": 0.0,
  "valorTotalPremioFaixaUm": 0.0
}
```