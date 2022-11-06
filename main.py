# Blibiotecas responsaveis para importacao do arquivo via Explorer

from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename

from simples import vef_simples
from grau import grau, arestas, regular
from completo import completo
# Modulos responsaveis para determinacao das caracteristicas do grafo

x =[[0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]]


print(grau(x),
      arestas(x),
      regular(x),
      completo(x),sep="\n")


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
    janela.attributes('-topmost',False)
    janela.withdraw()

    diretorio = askopenfilename(filetypes=(("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv")))
    arquivo = open(diretorio, "r")
    janela.destroy()
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


pega_arquivo()
