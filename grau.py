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
    graus_vertices =[]

    for coluna in range(len(matriz)):
        soma = 0

        for linha in range(len(matriz)):
            if linha == coluna:
                soma += matriz[linha][coluna]*2

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
    Qarestas = sum(grau(matriz))/2
    return Qarestas
