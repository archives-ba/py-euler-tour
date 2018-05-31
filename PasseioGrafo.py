'''

    Módulo que implementa a classe que realiza passeios em grafos.

'''

from enum import Enum

# pylint: disable=C0103
# pylint: disable=R0902

class PasseioGrafo:
    ''' Classe que realiza os passeios no grafo. '''

    class Cor(Enum):
        ''' Enumeração das cores para controle de visitação. '''
        BRANCO = 0
        CINZA = 1
        PRETO = 2

    def __init__(self):

        self.cor = []
        self.pai = []
        self.d = []
        self.f = []
        self.tempo = 0
        self.arvores = ""
        self.ciclo = []
        self.verticeRoot = 0
        self.breakoutTime = False


    def geraCiclo(self, grafo, vertice):
        ''' Gera um ciclo do grafo '''
        self.cor = []
        self.pai = []
        self.d = []
        self.f = []
        self.tempo = 0
        self.arvores = ""
        self.ciclo = []
        self.verticeRoot = 0
        self.breakoutTime = False

        for v in range(grafo.numVertices): # pylint: disable=W0612
            self.cor.append(PasseioGrafo.Cor.BRANCO)
            self.pai.append(None)
            self.d.append(0)
            self.f.append(0)

        self.verticeRoot = vertice
        self.visitaGeraCiclo(vertice, grafo)

        return self.ciclo

    def visitaGeraCiclo(self, vertice, grafo):
        ''' Visita da busca em profundidade modificada para geração de ciclos. '''
        self.breakoutTime = False
        self.cor[vertice] = PasseioGrafo.Cor.CINZA
        self.tempo += 1
        self.d[vertice] = self.tempo

        v_adjacente = grafo.primeiroListaAdj(vertice)
        while v_adjacente != None:
            if self.cor[v_adjacente.v2] == PasseioGrafo.Cor.CINZA:
                # Checa se o vértice é cinza, pois a raiz já é cinza.
                if self.pai[v_adjacente.v1] != self.verticeRoot:
                    # Checa se não é o nó seguinte após a raiz.
                    if v_adjacente.v2 == self.verticeRoot:
                        # Entra aqui se a aresta leva até a origem da árvore (Ciclo)
                        self.ciclo.append(v_adjacente)
                        self.breakoutTime = True
                        # Para, de forma que o nó adicionado
                        # não seja removido da lista contendo o ciclo.
                        break

            if self.cor[v_adjacente.v2] == PasseioGrafo.Cor.BRANCO:
                self.pai[v_adjacente.v2] = vertice
                self.ciclo.append(v_adjacente)
                # Vai adicionando o caminho ao ciclo.
                self.visitaGeraCiclo(v_adjacente.v2, grafo)

            if self.breakoutTime:
                # Caso já tenha achado o ciclo, não é necessário continuar visitando os vizinhos.
                break

            v_adjacente = grafo.proxAdj(vertice)

        if not self.breakoutTime:
            # Chegando aqui, pode-se dizer que este nó não tem mais vizinhos.
            if len(self.ciclo) > 0: # pylint: disable=C1801
                self.ciclo.pop()
            # Logo, retrocede-se para tentar outro caminho, pois este vértice não pertence ao ciclo.

        self.cor[vertice] = PasseioGrafo.Cor.PRETO
        self.tempo += 1
        self.f[vertice] = self.tempo

    def imprimirCiclo(self):
        ''' Imprime o ciclo encontrado. '''
        toPrint = ""
        for aresta in self.ciclo:
            toPrint += "(" + str(aresta.v1) + ", " + str(aresta.v2) + ") "
        print(toPrint)

# pylint: enable=R0902
# pylint: enable=C0103
