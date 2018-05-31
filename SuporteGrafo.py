'''

    Módulo com classes auxiliares ao TAD Grafo.

'''

# pylint: disable=C0103
# pylint: disable=R0903
class Aresta:
    ''' Classe que representa uma aresta '''

    def __init__(self, v1, v2, peso):
        self.v1 = v1
        self.v2 = v2
        self.peso = peso

class Celula:
    ''' Classe que representa uma célula '''

    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

# pylint: enable=R0903
# pylint: enable=C0103
