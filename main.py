'''

    Módulo executável.

'''

from sys import argv

import ReadFileGrafo
from AlgoritmoHierholzer import Heierholzer

if len(argv) > 1:
    PATH = argv[1]
else:
    PATH = str(input("Digite o caminho para o arquivo do grafo ou deixe em braco para o grafo padrão: "))
    if len(PATH) == 0:
        PATH = "./GrafoAnotado.txt"

grafo = ReadFileGrafo.grafoSimplesSemPeso(PATH) # pylint: disable=C0103

grafo.imprimeSemPeso()

euler = Heierholzer() # pylint: disable=C0103

tour = euler.obterTourEuler(grafo, 0) # pylint: disable=C0103

if tour == None: # pylint: disable=C0121
    print("--------------------") # pylint: disable=C0325
    print("Não existe um tour de Euler.") # pylint: disable=C0325
