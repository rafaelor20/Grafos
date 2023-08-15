from grafoListaAdjacencia import GrafoListaAdjacencia


def createCompleteKnGraph(number):
    grafoKn = GrafoListaAdjacencia(number)
    i = 0
    while i < number:
        grafoKn.adicionar_vertice("V" + str(i))
        i = i + 1
    i = 0
    j = i + 1
    while i < number - 2:
        grafoKn.adicionar_aresta(i, j)
        print(i)
        print(j)
        i = i + 1
        j = i + 1

    if i > 0:
        grafoKn.adicionar_aresta(j, 0)
    return grafoKn
