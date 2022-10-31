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
def bipartido(matriz):

    # arestas sera a lista como citado na linha 16, tera o par ordenado entre vertices
    arestas =[]

    for linha in range(len(matriz)):

        for colunha in range(len(matriz[linha])):
            # aqui faco a vereficacao se cada elemento da matriz e maior que 0
            # caso seja adiciono na lista o par ordenado (ij) linha coluna

            if matriz[linha][colunha] > 0:
                arestas.append([linha+1, colunha+1])
    print(arestas)

    # essa parte sera dedicada para formatacao da lista
    # no caso a lista atualmente esta nesse formato = [[1,2],[2,1],[3,1]...]
    # entao, deve se colocar os elementos da lista em orden
    # e adicionar no conjunto que eliminara elementos repetidos

    lista_ordenada = [sorted(z) for z in arestas]
    lista_ordenada = [("%d-%d" % (x, y)) for x, y in lista_ordenada]

    # os elementos repetidos serao eliminados com o tipo de variavel set
    # similiar como funciona os conjuntos na matematica
    # por exemplo, lista=[1,1,3,5] o conjunto seria (1,3,5)

    conjunto = set()
    conjunto.update(lista_ordenada)

    print(lista_ordenada)
    print(conjunto)
    print(len(conjunto))

    if len(conjunto)%2 == 0:
        return True
    else:
        return False



