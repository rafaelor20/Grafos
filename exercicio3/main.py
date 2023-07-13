import math
from grafoListaAdjacencia import GrafoListaAdjacencia


def example(numberOfVertices=7):
    grafo = GrafoListaAdjacencia(numberOfVertices)

    for i in range(numberOfVertices):
        grafo.adicionar_vertice(chr(ord("v") + i))

    grafo.adicionar_aresta(0, 1)
    grafo.adicionar_aresta(0, 2)
    grafo.adicionar_aresta(1, 3)
    grafo.adicionar_aresta(1, 4)
    grafo.adicionar_aresta(2, 5)
    grafo.adicionar_aresta(2, 6)
    grafo.adicionar_aresta(3, 1)
    grafo.adicionar_aresta(4, 1)
    grafo.adicionar_aresta(5, 2)
    grafo.adicionar_aresta(6, 2)

    grafo.busca_em_profundidade(1)

    arestas_arvore = []
    arestas_retorno = []

    for u in range(len(grafo.adjacencia)):
        for v in grafo.adjacencia[u]:
            if (
                grafo.vertices[u].profundidade_entrada
                < grafo.vertices[v].profundidade_entrada
            ) or (
                grafo.vertices[u].profundidade_saida
                > grafo.vertices[v].profundidade_saida
                and grafo.sao_vizinhos(v, u)
            ):
                arestas_arvore.append((u, v))
            else:
                arestas_retorno.append((u, v))

    print("Arestas da árvore:")
    for u, v in arestas_arvore:
        print(f"{grafo.vertices[u].rotulo} - {grafo.vertices[v].rotulo}")

    print("Arestas de retorno:")
    for u, v in arestas_retorno:
        print(f"{grafo.vertices[u].rotulo} - {grafo.vertices[v].rotulo}")

    for vertice in grafo.vertices:
        print(f"Vértice: {vertice.rotulo}")
        print(f"Profundidade de entrada: {vertice.profundidade_entrada}")
        print(f"Profundidade de saída: {vertice.profundidade_saida}")
        print()


example()
