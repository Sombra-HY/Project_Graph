def vef_simples(matriz):
    # Verifica se existe valores maiores que 1 na matriz, se tiver nao é um Grafo simples
    #
    # logica: intero nas linhas, acho o maior numero da linha da matriz e verifico se é maior que 1,
    # se tiver qualquer linha maior que 1, logo ela nao e simples.
    # o any recebera a vereficacao anterior, em conjunto com o not any retornara TRUE ou FALSE
    # RESUMO: grafo simples retorna TRUE e nao simples FALSE

    simples = not any([(max(linha) > 1) for linha in matriz])



    simples1 = []
    for x in range(len(matriz)):
        simples1.append(matriz[x][x])

    # vef linhas diagonais sao iguais a 0, ou seja os lacos

    simples1 = max(simples1)==0

    # para ser simples nao poder ter lacos e nao poder ter numeros maior que 1
    simples = True if simples and simples1 else False

    # LACOS:
    #
    # Um laco em uma matriz de adjacencia e basicamente a prensenca de algun valor maior que 0
    # na diagonal de uma matriz de adjacencia,diagonal, matriz[0][0],matriz[1][1],matriz[2][2]...
    # RESUMO: logo e possivel saber se tem lacos, se tem um numero maior que 0 na diagonal e sua posicao é a vertice + 1
    # (visto que uma lista comeca com 0, sendo inviavel representar o vertice 0, V0)
    # "lacos" sera uma lista com as vertices que tem lacos, por exemplo , ['V1','v2','V5']

    lacos = []
    for x in range(len(matriz)):
        if (matriz[x][x] > 0):
            lacos.append("V%d" % (x+1))

    # PARALELAS OU MUTIPLAS
    #
    # A presenca de mutiplas em matriz adjacente é a presenca um valor maior que um,
    # exceto na diagonal da matriz, que é um laco.
    # entao basta vereficar se existe valores maior que 1, exceto na diagonal, a posicao
    # sera o numero da coluna e da linha, ambos + 1, (lista comeca  com [0]).
    # LOGICA: nao e ncessario correr a lista, matriz, inteira pois ela e simetrica, a
    # utilizacao do 'contador' ira ajudar a nao vereficar m[x][y] e o m[y][x], visto que sao iguais...
    #
    # o 'mutiplas' contem as posicoes onde e paralelo, por exemplo, ['v1 v2', 'v3 v4' ]

    contador = 0
    mutiplas = []
    for linha in range(len(matriz)):
        contador += 1
        for coluna in range(len(matriz[0])):
            if coluna + contador >= len(matriz):
                break
            if matriz[linha][coluna + contador] > 1:
                mutiplas.append("V%d V%d" % (linha + 1, coluna + contador + 1))

    return simples, lacos, mutiplas

