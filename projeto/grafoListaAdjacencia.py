import math
from vertice import Vertice


class GrafoListaAdjacencia:
    def __init__(self, max_vertices):
        self.max_vertices = max_vertices
        self.vertices = []
        self.num_arestas = 0
        self.adjacencia = [[] for _ in range(max_vertices)]
        self.capacidades = [[0] * max_vertices for _ in range(max_vertices)]
        self.fluxo = [[0] * max_vertices for _ in range(max_vertices)]

    def calcular_fluxo_maximo(self, indice_origem, indice_destino):
        self.inicializar_fluxo()  # Inicializa a matriz de fluxo
        max_fluxo = 0  # Inicializa o fluxo máximo

        while True:
            # Encontra um caminho aumentante usando a busca em largura
            caminho_aumentante = self.encontrar_caminho_aumentante(
                indice_origem, indice_destino
            )

            if not caminho_aumentante:
                break  # Se não há mais caminhos aumentantes, saia do loop

            # Encontra a capacidade mínima residual ao longo do caminho
            capacidade_residual_minima = float("inf")

            for i in range(len(caminho_aumentante) - 1):
                u = caminho_aumentante[i]
                v = caminho_aumentante[i + 1]
                capacidade_residual = 0

                # Encontra a capacidade residual da aresta (u, v)
                for j in range(len(self.adjacencia[u])):
                    if self.adjacencia[u][j] == v:
                        capacidade_residual = 1  # Supomos capacidade unitária

                capacidade_residual_minima = min(
                    capacidade_residual_minima, capacidade_residual
                )

            # Atualiza o fluxo ao longo do caminho
            for i in range(len(caminho_aumentante) - 1):
                u = caminho_aumentante[i]
                v = caminho_aumentante[i + 1]

                # Incrementa o fluxo da aresta (u, v) e decrementa o fluxo da aresta (v, u)
                self.adicionar_fluxo(u, v, capacidade_residual_minima)
                self.adicionar_fluxo(v, u, -capacidade_residual_minima)

            # Atualiza o fluxo máximo
            max_fluxo += capacidade_residual_minima

        return max_fluxo

    def encontrar_caminho_aumentante(self, indice_origem, indice_destino):
        visitados = [False] * len(self.vertices)
        pais = [-1] * len(self.vertices)  # Rastreia os pais dos vértices no caminho
        capacidade_minima = [float("inf")] * len(self.vertices)

        fila = [indice_origem]
        visitados[indice_origem] = True

        while fila:
            vertice_atual = fila.pop(0)

            for vizinho in self.adjacencia[vertice_atual]:
                if not visitados[vizinho]:
                    capacidade_residual = self.capacidade_residual(
                        vertice_atual, vizinho
                    )

                    if capacidade_residual > 0:
                        capacidade_minima[vizinho] = min(
                            capacidade_minima[vertice_atual], capacidade_residual
                        )
                        pais[vizinho] = vertice_atual
                        visitados[vizinho] = True
                        fila.append(vizinho)

        if not visitados[indice_destino]:
            return None  # No augmenting path found

        caminho = []
        vertice_atual = indice_destino
        while vertice_atual != -1:
            caminho.insert(0, vertice_atual)
            vertice_atual = pais[vertice_atual]

        return caminho

    def capacidade_residual(self, u, v):
        return self.capacidades[u][v] - self.fluxo[u][v]

    def capacidade_da_aresta(self, u, i):
        # Verifica se u é um índice de vértice válido
        if 0 <= u < self.max_vertices:
            # Verifica se i é um índice de vizinho válido
            if 0 <= i < len(self.adjacencia[u]):
                v = self.adjacencia[u][i]
                # Verifica se v é um índice de vértice válido
                if 0 <= v < self.max_vertices:
                    # Retorna a capacidade da aresta (u, v)
                    return self.capacidades[u][v]

        # Se algum dos índices for inválido ou a conexão não existir, retorne 0 ou outro valor padrão
        return 0

    def definir_capacidade_aresta(self, u, v, capacidade):
        if 0 <= u < self.max_vertices and 0 <= v < self.max_vertices:
            self.capacidades[u][v] = capacidade
        else:
            raise IndexError("Índices de vértice inválidos")

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

    def inicializar_fluxo(self):
        self.fluxo = [[0] * len(self.vertices) for _ in range(len(self.vertices))]

    def adicionar_fluxo(self, indice_vertice1, indice_vertice2, valor):
        self.fluxo[indice_vertice1][indice_vertice2] += valor
