'''

    Módulo que contém método para leitura de um arquivo txt
    descritivo de um grafo por matriz de adjacência.

'''

import re
from Grafo import GrafoTAD

# pylint: disable=C0103

def grafoSimplesSemPeso(path):
    ''' Lê do arquivo em path um grafo simples sem peso nas arestas. '''
    fileGrafo = open(path, "r")

    numVertice = int(fileGrafo.readline())

    grafo = GrafoTAD(numVertice)

    # Criação de matriz NxN vazia.
    matriz = [[0 for x in range(numVertice)] for y in range(numVertice)]

    linhas = fileGrafo.readlines()
    for i in range(numVertice):
        linha = re.split(r'\s', linhas[i])
        for j in range(numVertice):
            try:
                if re.match(r'\s', linha[j]):
                    raise "Matriz incompleta!"
                matriz[i][j] = linha[j]
            except IndexError:
                raise "Matriz incompleta!"

    for i in range(numVertice):
        for j in range(numVertice):
            if matriz[i][j] != matriz[j][i]:
                raise "Grafo dirigido não suportado!"
            elif matriz[i][j] == "1":
                if not grafo.existeAresta(i, j):
                    grafo.insereAresta(i, j)

    return grafo

# pylint: enable=C0103
