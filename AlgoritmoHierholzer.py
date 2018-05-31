'''

    Módulo que implementa o algoritmo de Hierholzer.

'''

from Grafo import GrafoTAD
from PasseioGrafo import PasseioGrafo

#pylint: disable=C0103
class Heierholzer:
    ''' Classe que implementa o algoritmo de Hierholzer. '''
    def __init__(self):
        self.tourEuler = []
        self.tourEulerVertices = []
        self.ciclo = []
        self.passeio = PasseioGrafo()
        self.grafoAux = GrafoTAD(0)
        self.check = False
        self.verticeCiclo = 0

    def adicionarArestas(self, conjunto):
        ''' Adiciona o conjunto de arestas conjunto ao
        Tour de Euler sendo gerado. '''
        print("--------------------")
        print("Ciclo: " + self.stringCiclo(conjunto))

        if len(self.tourEulerVertices) > 0: #pylint: disable=C1801
            if conjunto[0] == self.tourEulerVertices[len(self.tourEulerVertices) - 1]:
                # Se o novo ciclo tiver como nó raiz o mesmo do antigo ciclo.
                for aresta in conjunto:
                    self.tourEuler.append(aresta)
                    self.tourEulerVertices.append(aresta.v1)
            else:
                index = 0
                concluido = False
                for arestaEuler in self.tourEuler:
                    for elemento in conjunto:
                        if arestaEuler.v2 == elemento.v1:

                            # Procura um canto onde possa inserir o novo ciclo, ou seja, uma aresta
                            # que liga um vertice do ciclo antigo com o novo.
                            # Os fors abaixo servem pra reordenar o ciclo de forma possa ser
                            # adicionado no tour.

                            for indexConjuntoI in range(conjunto.index(elemento), len(conjunto)):
                                index += 1
                                self.tourEuler.insert(index, conjunto[indexConjuntoI])
                                self.tourEulerVertices.insert(index, conjunto[indexConjuntoI].v1)

                            for indexConjuntoF in range(0, conjunto.index(elemento)):
                                index += 1
                                self.tourEuler.insert(index, conjunto[indexConjuntoF])
                                self.tourEulerVertices.insert(index, conjunto[indexConjuntoF].v1)

                            concluido = True
                            break

                    if concluido:
                        break

                    index += 1
        else:
            # Se o tour estiver vazio adiciona sem checagem de nada.
            for aresta in conjunto:
                self.tourEuler.append(aresta)
                self.tourEulerVertices.append(aresta.v1)

        print("Tour: " + self.stringCiclo(self.tourEuler))


    def obterTourEuler(self, grafo, verticeRoot):
        ''' Método que gera o Tour de Euler, se disponível
        no grafo grafo a partir do vértice verticeRoot. '''
        self.grafoAux = grafo
        self.tourEuler = []
        self.tourEulerVertices = []
        self.verticeCiclo = verticeRoot

        self.ciclo = self.passeio.geraCiclo(self.grafoAux, self.verticeCiclo)
        # Gera um ciclo com o nó passado por parametro como nó inicio/fim.

        if len(self.ciclo) == 0: #pylint: disable=C1801
            # Se não retornar um ciclo significa que o grafo
            # não é Euleriano.
            return None

        self.adicionarArestas(self.ciclo)
        # Adicionar as arestas no tour de Euler.

        for aresta in self.ciclo:
            # Remove as arestas que foram pro tour do grafo,
            # para calculo de novos ciclos.
            self.grafoAux.retiraAresta(aresta.v1, aresta.v2)

        while not self.grafoAux.isNulo():
            # Roda enquanto o grafo tiver alguma aresta.

            self.check = False

            for vertice in self.tourEulerVertices:
                if not self.grafoAux.isListAdjVazia(vertice):
                    # Pega o primeiro vizinho para gerar o novo ciclo.
                    self.verticeCiclo = self.grafoAux.primeiroListaAdj(vertice).v2

                    # Check representa se há algum nó que pode ser
                    # utilizado como nó raiz.
                    self.check = True
                    break

            if not self.check:
                # Se não existir um possivel nó raiz o grafo
                # não é Euleriano.
                return None

            self.ciclo = self.passeio.geraCiclo(self.grafoAux, self.verticeCiclo)

            if len(self.ciclo) == 0: #pylint: disable=C1801
                return None

            self.adicionarArestas(self.ciclo)

            for aresta in self.ciclo:
                self.grafoAux.retiraAresta(aresta.v1, aresta.v2)

        return self.tourEuler

    def stringCiclo(self, ciclo): #pylint: disable=R0201
        ''' Imprime o ciclo ciclo. '''
        toPrint = ""
        for aresta in ciclo:
            toPrint += "(" + str(aresta.v1) + ", " + str(aresta.v2) + ") "
        return toPrint

#pylint: enable=C0103
