import math


class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.grau = 0
        self.profundidade_entrada = None
        self.profundidade_saida = None


class GrafoListaAdjacencia:
    def __init__(self, max_vertices):
        self.max_vertices = max_vertices
        self.vertices = []
        self.num_arestas = 0
        self.adjacencia = [[] for _ in range(max_vertices)]

    def adicionar_vertice(self, rotulo):
        indice = len(self.vertices)
        vertice = Vertice(indice, rotulo)
        self.vertices.append(vertice)

    def adicionar_aresta(self, indice_vertice1, indice_vertice2):
        if (
            indice_vertice1 < 0
            or indice_vertice1 >= len(self.vertices)
            or indice_vertice2 < 0
            or indice_vertice2 >= len(self.vertices)
        ):
            raise IndexError("Índice de vértice inválido")

        self.adjacencia[indice_vertice1].append(indice_vertice2)
        self.adjacencia[indice_vertice2].append(indice_vertice1)

        self.vertices[indice_vertice1].grau += 1
        self.vertices[indice_vertice2].grau += 1
        self.num_arestas += 1

    def remover_aresta(self, indice_vertice1, indice_vertice2):
        if (
            indice_vertice1 < 0
            or indice_vertice1 >= len(self.vertices)
            or indice_vertice2 < 0
            or indice_vertice2 >= len(self.vertices)
        ):
            raise IndexError("Índice de vértice inválido")

        self.adjacencia[indice_vertice1].remove(indice_vertice2)
        self.adjacencia[indice_vertice2].remove(indice_vertice1)

        self.vertices[indice_vertice1].grau -= 1
        self.vertices[indice_vertice2].grau -= 1
        self.num_arestas -= 1

    def calcular_grau(self, indice_vertice):
        if indice_vertice < 0 or indice_vertice >= len(self.vertices):
            raise IndexError("Índice de vértice inválido")

        return self.vertices[indice_vertice].grau

    def sao_vizinhos(self, indice_vertice1, indice_vertice2):
        if (
            indice_vertice1 < 0
            or indice_vertice1 >= len(self.vertices)
            or indice_vertice2 < 0
            or indice_vertice2 >= len(self.vertices)
        ):
            raise IndexError("Índice de vértice inválido")

        return indice_vertice2 in self.adjacencia[indice_vertice1]

    def imprimir_grafo(self):
        print("Número de vértices:", len(self.vertices))
        print("Número de arestas:", self.num_arestas)

        print("Arestas:")
        for i in range(len(self.vertices)):
            for j in self.adjacencia[i]:
                if i < j:
                    print(f"{self.vertices[i].rotulo} - {self.vertices[j].rotulo}")

        print("Graus dos vértices:")
        total_grau = 0
        num_vertices_impar = 0
        num_vertices_par = 0

        for vertice in self.vertices:
            total_grau += vertice.grau
            print(f"{vertice.rotulo}: {vertice.grau}")

            if vertice.grau % 2 == 0:
                num_vertices_par += 1
            else:
                num_vertices_impar += 1

        print("Somatório do grau dos vértices:", total_grau)
        print("Número de vértices de grau ímpar:", num_vertices_impar)
        print("Número de vértices de grau par:", num_vertices_par)

    def busca_em_profundidade_imprimir_rotulo(self, indice_vertice):
        visitados = [False] * len(self.vertices)

        self._dfs_imprimir_rotulo(indice_vertice, visitados)

    def _dfs_imprimir_rotulo(self, indice_vertice, visitados):
        visitados[indice_vertice] = True
        print(self.vertices[indice_vertice].rotulo)

        for vizinho in self.adjacencia[indice_vertice]:
            if not visitados[vizinho]:
                self._dfs_imprimir_rotulo(vizinho, visitados)

    def busca_em_profundidade(self, indice_vertice):
        visitados = [False] * len(self.vertices)
        tempo = 0

        for indice_vertice in range(len(self.vertices)):
            if not visitados[indice_vertice]:
                tempo = self._dfs(indice_vertice, visitados, tempo)

    def _dfs(self, indice_vertice, visitados, tempo):
        visitados[indice_vertice] = True
        tempo += 1
        self.vertices[indice_vertice].profundidade_entrada = tempo

        for vizinho in self.adjacencia[indice_vertice]:
            if not visitados[vizinho]:
                tempo = self._dfs(vizinho, visitados, tempo)

        tempo += 1
        self.vertices[indice_vertice].profundidade_saida = tempo

        return tempo

    def subgrafo(self, vertices, arestas):
        subgrafo = GrafoListaAdjacencia(len(vertices))

        vertex_mapping = (
            {}
        )  # To store the mapping from old graph indices to subgraph indices

        for index, indice_vertice in enumerate(vertices):
            subgrafo.adicionar_vertice(self.vertices[indice_vertice].rotulo)
            vertex_mapping[indice_vertice] = index

        for aresta in arestas:
            indice_vertice1, indice_vertice2 = aresta
            if (
                indice_vertice1 in vertex_mapping and indice_vertice2 in vertex_mapping
            ):  # Ensure both vertices are part of the subgraph
                subgrafo.adicionar_aresta(
                    vertex_mapping[indice_vertice1], vertex_mapping[indice_vertice2]
                )

        return subgrafo

    def subtrair_vertices(self, vertices):
        # Create a copy of the original graph
        subtracao_grafo = GrafoListaAdjacencia(self.max_vertices)

        # Map vertices from the original graph to the subgraph
        vertex_mapping = {}
        for index, vertice in enumerate(self.vertices):
            if index not in vertices:
                new_index = len(vertex_mapping)
                vertex_mapping[index] = new_index
                subtracao_grafo.adicionar_vertice(vertice.rotulo)

        # Remove the vertices from the copied graph
        for indice_vertice in vertices:
            # Ignore the vertex if it's not present in the subgraph
            if indice_vertice not in vertex_mapping:
                continue

            for vizinho in self.adjacencia[indice_vertice]:
                # Check if the neighbor is also removed before removing the edge
                if vizinho in vertex_mapping:
                    subtracao_grafo.remover_aresta(
                        vertex_mapping[indice_vertice], vertex_mapping[vizinho]
                    )

        return subtracao_grafo

    def subgrafo_induzido(self, vertices):
        subgrafo = GrafoListaAdjacencia(len(vertices))

        # Create a mapping from original graph indices to subgraph indices
        vertex_mapping = {}
        for index, indice_vertice in enumerate(vertices):
            vertex_mapping[indice_vertice] = index

        for indice_vertice in vertices:
            subgrafo.adicionar_vertice(self.vertices[indice_vertice].rotulo)

        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                indice_vertice1, indice_vertice2 = vertices[i], vertices[j]
                if self.sao_vizinhos(indice_vertice1, indice_vertice2):
                    subgrafo.adicionar_aresta(
                        vertex_mapping[indice_vertice1], vertex_mapping[indice_vertice2]
                    )

        return subgrafo

    def subtrair_vertices(self, vertices):
        # Create a copy of the original graph
        subtracao_grafo = GrafoListaAdjacencia(self.max_vertices)

        # Map vertices from the original graph to the subgraph
        vertex_mapping = {}
        for index, vertice in enumerate(self.vertices):
            if index not in vertices:
                new_index = len(vertex_mapping)
                vertex_mapping[index] = new_index
                subtracao_grafo.adicionar_vertice(vertice.rotulo)

        # Create a new adjacency list for the subtracted graph
        subtracao_grafo.adjacencia = [[] for _ in range(len(vertex_mapping))]
        subtracao_grafo.num_arestas = 0

        # Reconstruct the adjacency list without the edges connected to removed vertices
        for indice_vertice in range(len(self.vertices)):
            if indice_vertice not in vertices:
                new_index_vertice = vertex_mapping[indice_vertice]
                for vizinho in self.adjacencia[indice_vertice]:
                    if vizinho not in vertices:
                        new_index_vizinho = vertex_mapping[vizinho]
                        subtracao_grafo.adjacencia[new_index_vertice].append(
                            new_index_vizinho
                        )
                        subtracao_grafo.num_arestas += 1

        return subtracao_grafo

    def subgrafo_aresta_induzido(self, arestas):
        subgrafo = GrafoListaAdjacencia(len(self.vertices))

        vertex_mapping = {}
        for index, vertice in enumerate(self.vertices):
            subgrafo.adicionar_vertice(vertice.rotulo)
            vertex_mapping[vertice.indice] = index

        for aresta in arestas:
            indice_vertice1, indice_vertice2 = aresta
            if indice_vertice1 in vertex_mapping and indice_vertice2 in vertex_mapping:
                subgrafo.adicionar_aresta(
                    vertex_mapping[indice_vertice1], vertex_mapping[indice_vertice2]
                )

        return subgrafo

    def subtrair_arestas(self, arestas):
        subtraido_grafo = GrafoListaAdjacencia(self.max_vertices)

        vertex_mapping = {}
        for index, vertice in enumerate(self.vertices):
            subtraido_grafo.adicionar_vertice(vertice.rotulo)
            vertex_mapping[vertice.indice] = index

        for indice_vertice in range(len(self.vertices)):
            for vizinho in self.adjacencia[indice_vertice]:
                aresta = (indice_vertice, vizinho)
                if aresta not in arestas and (vizinho, indice_vertice) not in arestas:
                    subtraido_grafo.adicionar_aresta(
                        vertex_mapping[indice_vertice], vertex_mapping[vizinho]
                    )

        return subtraido_grafo


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


def main():
    grafo = createGraph()

    # Exercise 4.4: Subgrafo aresta-induzido G[E1]
    arestas_induzidas = [(0, 1), (0, 2), (1, 3), (2, 6)]
    subgrafo_aresta_induzido = grafo.subgrafo_aresta_induzido(arestas_induzidas)
    print("Subgrafo aresta-induzido G[E1]:")
    subgrafo_aresta_induzido.imprimir_grafo()
    print()

    # Exercise 4.5: G - {1, 3}
    vertices_subtrair = [1, 3]
    subtracao_grafo = grafo.subtrair_arestas(
        [(1, 3), (3, 1)]
    )  # For an undirected graph, we add both (u, v) and (v, u)
    print("G - {1, 3}:")
    subtracao_grafo.imprimir_grafo()
    print()

    # Exercise 4.6:
    # a) Gerar um subgrafo próprio (subgraph)
    subgrafo_vertices_a = [0, 1, 3, 4]
    subgrafo_a = grafo.subgrafo(subgrafo_vertices_a, [(0, 1), (1, 3), (1, 4)])
    print("Subgrafo próprio:")
    subgrafo_a.imprimir_grafo()
    print()

    # b) Gerar um subgrafo gerador (spanning tree)
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

    # c) Seja X1 = {y, v, x, u}, gerar o subgrafo induzido G[X1]
    subgrafo_induzido_vertices = [1, 3, 4, 5]
    subgrafo_c = grafo.subgrafo_induzido(subgrafo_induzido_vertices)
    print("Subgrafo induzido G[X1]:")
    subgrafo_c.imprimir_grafo()
    print()

    # d) Seja X2 = {u, w}, gerar G - X
    vertices_para_subtrair_d = [0, 1, 2, 3, 4, 5, 6]
    subtracao_grafo_d = grafo.subtrair_vertices(vertices_para_subtrair_d)
    print("G - X2:")
    subtracao_grafo_d.imprimir_grafo()
    print()

    # e) Seja E1 = {a, c, e, g}, gerar o subgrafo aresta-induzido G[E1]
    arestas_induzidas_e = [(0, 1), (0, 2), (1, 3), (1, 4)]
    subgrafo_aresta_induzido_e = grafo.subgrafo_aresta_induzido(arestas_induzidas_e)
    print("Subgrafo aresta-induzido G[E1]:")
    subgrafo_aresta_induzido_e.imprimir_grafo()
    print()

    # f) Seja E2 = {a, b, f}, gerar G - E2
    vertices_subtrair_f = [1, 3, 4]
    subtracao_grafo_f = grafo.subtrair_arestas([(1, 3), (1, 4), (3, 1), (4, 1)])
    print("G - E2:")
    subtracao_grafo_f.imprimir_grafo()
    print()


if __name__ == "__main__":
    main()
