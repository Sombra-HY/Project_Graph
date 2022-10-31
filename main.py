# Blibiotecas responsaveis para importacao do arquivo via Explorer

from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename

# Modulos responsaveis para determinacao das caracteristicas do grafo

from grau import arestas, regular, grau
from simples import vef_simples
from bipartido import bipartido
from completo import completo

x =[[0, 0, 0],
    [0, 0, 1],
    [0, 1, 0]]

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
    tk().withdraw()

    # Selecao de arquivo/ diretorio onde se encontra

    diretorio = askopenfilename(filetypes=(("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv")))
    arquivo = open(diretorio, "r")

    try:
        if arquivo:
            print("rodando...")

            dados = []

            for x in arquivo.readlines():
                # A retirada dos espacoes e "\n" é feito aqui e a dos valores em int
                # 3 linhas abaixo de codigo.

                var = x.replace("\n", "").split(" ")
                var = [int(x) for x in var]
                dados.append(var)
                print(dados)

        arquivo.close()
        return dados
    except:
        arquivo.close()
        return


while var!='0':
    var = input("\nDigite uma das opcoes abaixo:\n\n1 - Analisar um grafo, apartir de uma matriz adjacente\n0 - Sair \n")
    if var == "1":
        print("s")
        pega_arquivo()

