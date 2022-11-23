# Blibiotecas responsaveis para pegar o arquivo
from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename

def main():
    # _____________ SECUNDARIO___________________________________________________
    var = '1'
    def pega_arquivo():
        # O "pega_arquivo"
        #
        # Alem do pega arquivo abrir o explore para a escolha do arquivo
        # ele tambem tratara o conteudo do arquivo
        # colocar em uma lista a linha remover os espacos e quebras de linha
        # e tranforma os chars em inteiro "1" --> 1
        # alocando em uma lista cada linha para quer fique no formato ( representacao visual apenas )
        #
        #  [[ 1, 0, 1 ],
        #   [ 1, 0, 1 ],
        #   [ 1, 0, 1 ]]
        #

        janela = tk()
        # Selecao de arquivo/ diretorio onde se encontra
        janela.lift()
        janela.attributes('-topmost', False)
        janela.withdraw()

        diretorio = askopenfilename(filetypes=(("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv")))
        arquivo = open(diretorio, "r")
        janela.destroy()

        try:
            if arquivo:

                dados = []

                for x in arquivo.readlines():
                    # A retirada dos espacoes e "\n" é feito aqui e a dos valores em int
                    # 3 linhas abaixo de codigo.

                    var = x.replace("\n", "").split(" ")
                    var = [int(x) for x in var]
                    dados.append(var)

            arquivo.close()

            # Mostrando a Matriz
            print("\nMatriz Selecionada: \n\n---------------------------------------------------------")
            for x in range(len(dados)):
                print("\t", end="")
                for y in range(len(dados)):
                    print("%d" % (dados[x][y]), end="\t")
                print("\n")
            print("---------------------------------------------------------\nCaracterística  da Matriz: ")
            return dados # <--------- Matriz de retorno
        except:

            arquivo.close()
            return

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

        simples1 = max(simples1) == 0

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
                lacos.append("V%d" % (x + 1))

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
                    mutiplas.append("V%d-V%d" % (linha + 1, coluna + contador + 1))

        return simples, lacos, mutiplas

    # GRAUS EM GRAFOS
    #
    # A quantidade de graus de uma vertice, matriz de adjacencia, pode ser representado pela
    # soma da primeira coluna sendo que a diagonal da matriz mutiplicado por 2
    # por exemplo,
    #                    [ 1, 0, 1 ]
    # segue a matriz G = [ 0, 0, 1 ]
    #                    [ 1, 1, 1 ]
    # o grau da vertice 1 é ( G[0][0] * 2 ) + G[1][0] + G[2][0]
    # o grau da vertice 2 é ( G[1][1] * 2 ) + G[0][1] + G[2][1]
    # o grau da vertice 3 é ( G[2][2] * 2 ) + G[0][2] + G[1][2]
    #
    # Diagonal que sera mutiplicada por 2
    #  [*2 ,  ,  ]
    #  [  , *2,  ]
    #  [  ,  , *2]

    # LOGICA: intero a matriz inteira, verefico se a linha e coluna sao iguais,
    # sem sim, mutiplico por 2 e armazeno, se nao armazeno o valor daquele indice e colunha somando isto
    # com todos valores da coluna, apos terminar de ler a coluna toda so reseto o "soma".
    def grau(matriz):
        graus_vertices = []

        for coluna in range(len(matriz)):
            soma = 0

            for linha in range(len(matriz)):
                if linha == coluna:
                    soma += matriz[linha][coluna] * 2

                else:
                    soma += matriz[linha][coluna]

            graus_vertices.append(soma)

        return graus_vertices

    # ARESTAS
    #
    # As quantidade de arestas esta associada aos graus de uma matriz
    # equacao SOMATORIA de graus(v) = 2|E|; |E| = Quantidade de arestas
    # como ja existe a funcao que retorna uma lista de vertices
    # basta somar os valores da lista e divir por dois
    # SOMATORIA de graus(V)/2 = |E|

    def arestas(matriz):
        Qarestas = sum(grau(matriz)) / 2
        return Qarestas

    # GRAFO REGULAR
    #
    # um grafo regular e dito como um que todas vertices tem a mesma quantidade de graus

    def regular(matriz):
        matriz = grau(matriz)
        return not any([(v != matriz[0]) for v in matriz])

    # COMPLETO
    #
    # Para ser completo o quantidade de vertices -1 tem que ser igual
    # ao soma de elemento da linha,
    #  [0,1,1] = 3 -1 =2 == sum(0,1,1)
    #  [1,0,1] = 3 -1 =2 == sum(1,0,1)
    #  [1,1,0] = 3 -1 =2 == sum(1,1,0)

    def completo(m):
        var = 0

        if vef_simples(m)[0] == True:
            var = 1

            for x in m:
                if sum(x) != (len(x) - 1):
                    var = 0

        return True if var == 1 else False

    # BIPARTIDO
    #
    # Para um grafo ser bipartido o comprimento de ciclos dele nao
    # pode ser impar, se nao ele nao e bipartido
    # por exemplo, na matriz de adjacencia
    #
    #         v1 v2 v3
    #     v1 [0, 1, 0]
    # M = v2 [1, 0, 1]
    #     v3 [0, 1, 0]
    #
    # em todos os valores diferentes de 0, existe uma
    # aresta associada as vertices, pegando os valores da linha e
    # e coluna, fazendo um par ordenado, onde tem um valor > 0 temos a
    #
    # lista =( v1v2 , v2v1 , v2v3 , v3v2)
    #
    # considerando que os elementos com vertices repetidas sao iguais
    # temos o conjunto = ( v1v2 , v2v3 )
    #
    #
    # o comprimento do conjunto e dois, len(conjunto) sendo par
    # sendo um grafo bipartido


    #_____________________________   PRINCIPAL   _______________________________________________
    # chamada das funcoes

    # VERIFICACAO SIMPLES
    MATRIZ = pega_arquivo() # retorno da linha 55 (MATRIZ)
    DADOS = vef_simples(MATRIZ)

    if (DADOS[0]):
        print("\nO grafo é simples, pois ele nao tem nem lacos ou arestas mutiplas")
    else:
        print("\nO grafo nao é simples, pois ele tem", end=" ")
        if (any(DADOS[1])):
            print(" laco(s) na(s) vertices:")
            for vertice in DADOS[1]: #todas as vertices serao printadas aqui
                print(vertice, end=" ")
        # arestas paralelas
        if (any(DADOS[2])):
            print("\n\nArestas paralelas nos vertices")
            for vertice in DADOS[2]:  # todas as vertices serao printadas aqui
                print(vertice, end=" ")

    # VERIFICACAO DE GRAUS
    GRAUS = grau(MATRIZ)
    print("\n\nO grau do grafo é em orden nao crescente:", sorted(GRAUS))

    # QUANT. ARESTAS
    print("A quantidade de arestas do grafo é %d" % arestas(MATRIZ))

    # GRAFO COMPLETO

    print("O grafo %s e completo" % ("" if completo(MATRIZ) else "nao"))

    # GRAFO REGULAR

    print("O grafo %s e regular" % ("" if regular(MATRIZ) else "nao"))

main()