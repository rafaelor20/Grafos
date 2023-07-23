import math
from grafoListaAdjacencia import GrafoListaAdjacencia


def createGraph(numberOfVertices=8):
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

    """
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
    """
    return grafo


def exercicio4_4(grafo):
    print("Exercício 4.4:")
    # Exercise 4.4: Subgrafo aresta-induzido G[E1]
    arestas_induzidas = [(0, 1), (0, 2), (1, 3), (2, 6)]
    subgrafo_aresta_induzido = grafo.subgrafo_aresta_induzido(arestas_induzidas)
    print("Subgrafo aresta-induzido G[E1]:")
    # subgrafo_aresta_induzido.imprimir_grafo()
    print()


def exercicio4_5(grafo):
    print("Exercício 4.5:")
    vertices_subtrair = [1, 3]
    subtracao_grafo = grafo.subtrair_arestas(
        [(1, 3), (3, 1)]
    )  # For an undirected graph, we add both (u, v) and (v, u)
    print("G - {1, 3}:")
    # subtracao_grafo.imprimir_grafo()
    print()


def exercicio4_6_a(grafo):
    print("Exercício 4.6.a:")
    subgrafo_vertices_a = [0, 1, 3, 4]
    subgrafo_a = grafo.subgrafo(subgrafo_vertices_a, [(0, 1), (1, 3), (1, 4)])
    print("Subgrafo próprio:")
    subgrafo_a.imprimir_grafo()
    print()


def exercicio4_6_b(grafo):
    print("Exercício 4.6.b:")
    # For simplicity, let's just consider the first component of the spanning forest.
    arestas_arvore = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 6),
    ]  # Use the variable arestas_arvore instead of component_edges
    component_vertices = set()
    for edge in arestas_arvore:
        component_vertices.add(edge[0])
        component_vertices.add(edge[1])
    subgrafo_b = grafo.subgrafo(list(component_vertices), arestas_arvore)
    print("Subgrafo gerador (spanning tree):")
    subgrafo_b.imprimir_grafo()
    print()


def exercicio4_6_c(grafo):
    print("Exercício 4.6.c:")
    subgrafo_induzido_vertices = [1, 3, 4, 5]
    subgrafo_c = grafo.subgrafo_induzido(subgrafo_induzido_vertices)
    print("Subgrafo induzido G[X1]:")
    subgrafo_c.imprimir_grafo()
    print()


def exercicio4_6_d(grafo):
    print("Exercício 4.6.d:")
    vertices_para_subtrair_d = [0, 1, 2, 3, 4, 5, 6]
    subtracao_grafo_d = grafo.subtrair_vertices(vertices_para_subtrair_d)
    print("G - X2:")
    subtracao_grafo_d.imprimir_grafo()
    print()


def exercicio4_6_e(grafo):
    print("Exercício 4.6.e:")
    arestas_induzidas_e = [(0, 1), (0, 2), (1, 3), (1, 4)]
    subgrafo_aresta_induzido_e = grafo.subgrafo_aresta_induzido(arestas_induzidas_e)
    print("Subgrafo aresta-induzido G[E1]:")
    subgrafo_aresta_induzido_e.imprimir_grafo()
    print()


def exercicio4_6_f(grafo):
    print("Exercício 4.6.f:")
    vertices_subtrair_f = [1, 3, 4]
    subtracao_grafo_f = grafo.subtrair_arestas([(1, 3), (1, 4), (3, 1), (4, 1)])
    print("G - E2:")
    subtracao_grafo_f.imprimir_grafo()
    print()


def main():
    grafo = createGraph()

    # Exercise 4.4: Subgrafo aresta-induzido G[E1]
    exercicio4_4(grafo)

    # Exercise 4.5: G - {1, 3}
    exercicio4_5(grafo)

    # Exercise 4.6:
    # a) Gerar um subgrafo próprio (subgraph)
    exercicio4_6_a(grafo)

    # b) Gerar um subgrafo gerador (spanning tree)
    exercicio4_6_b(grafo)

    # c) Seja X1 = {y, v, x, u}, gerar o subgrafo induzido G[X1]
    exercicio4_6_c(grafo)

    # d) Seja X2 = {u, w}, gerar G - X
    exercicio4_6_d(grafo)

    # e) Seja E1 = {a, c, e, g}, gerar o subgrafo aresta-induzido G[E1]
    exercicio4_6_e(grafo)

    # f) Seja E2 = {a, b, f}, gerar G - E2
    exercicio4_6_f(grafo)


if __name__ == "__main__":
    main()
