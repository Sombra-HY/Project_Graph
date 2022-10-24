from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename
var = '1'

def pega_arquivo():
    janela = tk().withdraw()
    diretorio = askopenfilename(filetypes=(("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv")))
    arquivo = open(diretorio, "r")
    try:
        if arquivo:
            print("rodando...")
    except:
        return

while var!='0':
    var = input("\nDigite uma das opcoes abaixo:\n\n1 - Analisar um grafo, apartir de uma matriz adjacente\n0 - Sair \n")
    if var == "1": pega_arquivo()