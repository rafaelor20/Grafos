from grafoListaAdjacencia import GrafoListaAdjacencia


def createKRegularGraph(n, k):
    # Check if k is valid for a regular graph
    if k >= n or k % 2 != 0:
        raise ValueError("Invalid degree for a regular graph")

    grafo = GrafoListaAdjacencia(n)

    # Add vertices
    for i in range(n):
        grafo.adicionar_vertice(str(i + 1))

    # Connect vertices to create a k-regular graph
    for i in range(n):
        for j in range(1, k // 2 + 1):
            vertice1 = i
            vertice2 = (i + j) % n
            grafo.adicionar_aresta(vertice1, vertice2)

    return grafo
