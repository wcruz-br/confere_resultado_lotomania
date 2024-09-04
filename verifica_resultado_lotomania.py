# Números que apostei
meus_numeros_apostas = [
    [
        1,  3,  4,  6,  8, 13,
        15, 16, 21, 23, 25, 27,
        28, 31, 34, 36, 39, 40,
        41, 42, 45, 46, 48, 49,
        50, 56, 58, 59, 60, 61,
        65, 66, 69, 71, 72, 73,
        74, 76, 77, 83, 84, 85,
        86, 87, 88, 91, 92, 97,
        98, 0
    ],
    [
        3, 4, 5, 7, 8,10,
        11,12,15,18,21,22,
        24,27,28,29,30,33,
        35,36,37,40,42,44,
        45,51,53,59,60,61,
        65,66,67,68,69,70,
        71,72,73,74,75,78,
        80,83,86,89,90,92,
        95,98
    ],
]

# Resultados dos concursos
concursos_e_resultados = [
    [2661, '1011142227283233384244465051565879809197'],
    [2662, '0205091521283138465258606365737482899197'],
    [2663, '0005070817242629303235394043455765688392'],
    [2664, '0309121719222325353650515357676972788994'],
]

def numeros_sorteados(resultados_string):
    """Converte uma lista de strings de resultados em uma lista bidimensional de inteiros.

    Esta função recebe uma lista de strings, onde cada string representa os resultados de um sorteio da loteria,
    com os números codificados como pares de dígitos.
    Por exemplo: "07101522313845525860687279818895".

    Args:
        resultados_string: Uma lista de strings, onde cada string contém os números sorteados em um concurso.

    Returns:
        Uma lista bidimensional de inteiros. Cada sublista representa os números sorteados em um concurso,
        convertidos para inteiros.
    """
    return [[int(resultado[i:i+2]) for i in range(0, len(resultado), 2)] for resultado in resultados_string]

def verifica_resultado(sorteados, meus_numeros_apostas):
    """Verifica os acertos entre os números jogados (em várias apostas) e os sorteados para vários jogos.

    Args:
        sorteados: Uma lista bidimensional de inteiros, onde cada sublista representa os números sorteados em um concurso.
        meus_numeros_apostas: Uma lista bidimensional de inteiros, onde cada sublista representa os números jogados em uma aposta.

    Returns:
        Uma lista tridimensional de inteiros.
        - O primeiro nível representa os concursos.
        - O segundo nível representa as apostas feitas para aquele concurso.
        - O terceiro nível (uma lista) contém os números que foram acertados naquela aposta, para aquele concurso.
    """
    return [[list(set(sorteado) & set(meus_numeros)) for meus_numeros in meus_numeros_apostas] for sorteado in sorteados]

def main():
    """
    Este script verifica os resultados de apostas da Lotomania em relação a uma lista de resultados de sorteio informados.

    Defina as apostas na lista `meus_numeros_apostas`, onde cada sublista representa uma aposta separada.

    Em seguida, defina a lista de resultados de sorteios na lista `concursos_e_resultados`. Cada elemento nesta lista
    é uma sublista contendo o número do sorteio e os números vencedores codificados como uma string de pares de dígitos.
    Fiz dessa forma para facilitar o copy/paste dos resultados na página https://loterias.caixa.gov.br/Paginas/Lotomania.aspx

    O script então verifica os acertos de cada aposta em cada concurso, dizendo quantos números você acertou.
    Por fim, verifica se alguma das apostas ganhou em algum dos sorteios (pelas regras da Lotomania, você ganha
    se acertar pelo menos 15 números ou se não acertar nenhum).

    TODO: baixar automaticamente do site da Caixa o xls com os resultados, bastando informar então um range de concursos
    """

    concursos = [concurso[0] for concurso in concursos_e_resultados]
    resultados_jogos = [concurso[1] for concurso in concursos_e_resultados]

    # Obtém os números sorteados para cada jogo
    sorteados = numeros_sorteados(resultados_jogos)

    # Verifica os acertos para cada jogo e cada aposta
    acertos = verifica_resultado(sorteados, meus_numeros_apostas)

    # Imprime apostas
    print("")
    print("Apostas:")
    for aposta in meus_numeros_apostas:
        print(" ", ' '.join(map(str, aposta)))

    # Imprime os resultados para cada jogo e cada aposta
    print("")
    for i, resultado in enumerate(sorteados):
        print(f"----- Concurso {concursos[i]} -----")
        print("Números sorteados:", ' '.join(map(str, resultado)))
        for j, acertos_aposta in enumerate(acertos[i]):
            print(f"Aposta {j+1} acertou {len(acertos_aposta)} números:", ' '.join(map(str, acertos_aposta)))
        print("")

    # Verifica se houve premiação em algum dos jogos, para alguma aposta
    ganhou = False
    for i, acertos_jogo in enumerate(acertos):
        if any(len(acerto) >= 15 for acerto in acertos_jogo) or any(len(acerto) == 0 for acerto in acertos_jogo):
            print(f"\nParabéns! Você ganhou no Concurso {concursos[i]} com pelo menos uma das apostas!")
            ganhou = True

    if not ganhou:
        print("Que pena, não ganhou nada...")

    print("")

if __name__ == "__main__":
    main()
