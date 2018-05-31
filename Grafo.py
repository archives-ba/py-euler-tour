'''

    Módulo do TAD Grafo por Lista de Adjacência.
    Contém também classe geradora de passeios.

'''

from SuporteGrafo import Aresta
from SuporteGrafo import Celula

# pylint: disable=C0103

class GrafoTAD:
    ''' Classe que representa um grafo por lista de adjacência. '''

    def __init__(self, numVertices):
        self.indice = []
        self.adj = []
        self.numVertices = numVertices
        self.arestas = []
        for i in range(self.numVertices): # pylint: disable=W0612
            self.indice.append(0)
            self.adj.append([])

    def insereAresta(self, v1, v2, peso=0):
        ''' Insere a aresta (v1, v2) no grafo com o peso especificado '''
        cell_to_add = Celula(v2, peso)
        self.adj[v1].append(cell_to_add)
        cell_to_add2 = Celula(v1, peso)
        self.adj[v2].append(cell_to_add2)

        for arestaI in self.arestas:
            if arestaI.v1 == v1 and arestaI.v2 == v2:
                return
            if arestaI.v2 == v1 and arestaI.v1 == v2:
                return

        self.arestas.append(Aresta(v1, v2, peso))

    def existeAresta(self, v1, v2):
        ''' Retorna se existe uma aresta entre v1 -> v2 '''
        for v in self.adj[v1]:
            if v.vertice == v2:
                return True

        for v22 in self.adj[v2]:
            if v22.vertice == v1:
                return True

        return False

    def isNulo(self):
        ''' Retorna se o grafo é nulo. '''
        for v in range(self.numVertices):
            if not self.isListAdjVazia(v):
                return False
        return True

    def isListAdjVazia(self, v):
        ''' Retorna verdadeiro se a lista adjunta de v for vazia '''
        lenght = len(self.adj[v])
        if lenght == 0:
            return True
        return False

    def primeiroListaAdj(self, v):
        ''' Retorna a primeira aresta da lista adjunta de v '''
        self.indice[v] = 0
        if not self.isListAdjVazia(v):
            item = self.adj[v][self.indice[v]]
            if item != None:
                return Aresta(v, item.vertice, item.peso)
            return None
        return None

    def proxAdj(self, v):
        ''' Retorna, se houver, a próxima aresta da lista adjunta de v '''
        self.indice[v] += 1
        if len(self.adj[v]) == self.indice[v]:
            return None
        item = self.adj[v][self.indice[v]]
        if item != None:
            return Aresta(v, item.vertice, item.peso)
        return None

    def retiraAresta(self, v1, v2):
        ''' Retorna a aresta v1 -> v2 se ela for removida com sucesso,
            retorna None se ela não existir. '''

        for arestaI in self.arestas:
            if (arestaI.v1 == v1 and arestaI.v2 == v2) or (arestaI.v2 == v1 and arestaI.v1 == v2):
                self.arestas.remove(arestaI)
                break

        for item in self.adj[v1]:
            if item.vertice == v2:
                self.adj[v1].remove(item)

        for item2 in self.adj[v2]:
            if item2.vertice == v1:
                self.adj[v2].remove(item2)
                return Aresta(v1, v2, item2.peso)

        return None

    def imprime(self):
        ''' Imprime a lista adjunta do grafo. '''
        for vertice in range(self.numVertices):
            toPrint = ""
            toPrint = str(vertice) + " -> "
            for celula in self.adj[vertice]:
                toPrint += str(celula.vertice) + "(" + str(celula.peso) + "), "

            print(toPrint)

    def imprimeSemPeso(self):
        ''' Imprime a lista adjunta do grafo. '''
        for vertice in range(self.numVertices):
            toPrint = ""
            toPrint = str(vertice) + " -> "
            for celula in self.adj[vertice]:
                toPrint += str(celula.vertice) + ", "

            print(toPrint)

# pylint: enable=C0103
