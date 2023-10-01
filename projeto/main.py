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
    return grafo


class Passeio:
    def __init__(self):
        self.vertices = []

    def adicionar_vertice(self, vertice):
        self.vertices.append(vertice)

    def imprimir_passeio(self):
        print("Passeio:")
        for vertice in self.vertices:
            print(vertice, end=" ")
        print()

    def imprimir_arestas_do_passeio(self, grafo):
        print("Arestas do passeio:")
        for i in range(len(self.vertices) - 1):
            u = self.vertices[i]
            v = self.vertices[i + 1]
            if grafo.sao_vizinhos(u, v):
                print(f"Aresta: {u} - {v}")
        print()

    def imprimir_reverso(self):
        print("Reverso do passeio:")
        for vertice in reversed(self.vertices):
            print(vertice, end=" ")
        print()

    def obter_secao(self, i, j):
        if i < 0 or j >= len(self.vertices) or i > j:
            raise ValueError("Posições inválidas para a seção")

        secao = Passeio()
        for idx in range(i, j + 1):
            secao.adicionar_vertice(self.vertices[idx])
        return secao


def busca_em_profundidade_passeio(
    grafo, vertice_atual, vertice_destino, visitados, passeio
):
    visitados[vertice_atual] = True
    passeio.adicionar_vertice(vertice_atual)

    if vertice_atual == vertice_destino:
        return True

    for vizinho in grafo.adjacencia[vertice_atual]:
        if not visitados[vizinho]:
            if busca_em_profundidade_passeio(
                grafo, vizinho, vertice_destino, visitados, passeio
            ):
                return True

    passeio.vertices.pop()
    return False


def busca_em_profundidade_caminho(
    grafo, vertice_atual, vertice_destino, visitados, caminho
):
    visitados[vertice_atual] = True
    caminho.adicionar_vertice(vertice_atual)

    if vertice_atual == vertice_destino:
        return True

    for vizinho in grafo.adjacencia[vertice_atual]:
        if not visitados[vizinho]:
            if busca_em_profundidade_caminho(
                grafo, vizinho, vertice_destino, visitados, caminho
            ):
                return True

    caminho.vertices.pop()
    return False


def busca_em_profundidade_ciclo(grafo, vertice_atual, visitados, stack, ciclo):
    visitados[vertice_atual] = True
    stack.append(vertice_atual)

    for vizinho in grafo.adjacencia[vertice_atual]:
        if not visitados[vizinho]:
            if busca_em_profundidade_ciclo(grafo, vizinho, visitados, stack, ciclo):
                return True
        elif vizinho in stack:
            ciclo.extend(stack[stack.index(vizinho) :])
            return True

    stack.pop()
    return False


def busca_ciclo(grafo):
    visitados = [False] * len(grafo.vertices)
    ciclo = []

    for vertice in range(len(grafo.vertices)):
        if not visitados[vertice] and busca_em_profundidade_ciclo(
            grafo, vertice, visitados, [], ciclo
        ):
            return ciclo

    return None


def buscar_ciclo_com_g_v_maior_igual_2(grafo):
    for vertice in range(len(grafo.vertices)):
        if grafo.calcular_grau(vertice) >= 2:
            ciclo = []
            visitados = [False] * len(grafo.vertices)
            stack = []

            if busca_em_profundidade_ciclo(grafo, vertice, visitados, stack, ciclo):
                return ciclo


def find_cycle_with_edge(trail, edge_a):
    cycle = []
    a, b = edge_a  # Assuming edge_a is represented as a tuple (a, b)

    # Find the position of edge 'a' in the trail
    index_a = -1
    for i in range(len(trail)):
        if (trail[i] == a and trail[(i + 1) % len(trail)] == b) or (
            trail[i] == b and trail[(i + 1) % len(trail)] == a
        ):
            index_a = i
            break

    # If edge 'a' is not found in the trail, return an empty cycle
    if index_a == -1:
        return cycle

    # Extract the cycle starting from edge 'a'
    for i in range(index_a, index_a + len(trail) + 1):
        cycle.append(trail[i % len(trail)])

        # Stop when we complete the cycle
        if (trail[i % len(trail)] == a and trail[(i + 1) % len(trail)] == b) or (
            trail[i % len(trail)] == b and trail[(i + 1) % len(trail)] == a
        ):
            break

    return cycle


def walk_to_path(walk, u, v):
    path = []
    u_found = False
    v_found = False

    for vertex in walk:
        if vertex == u:
            u_found = True
        if u_found:
            path.append(vertex)
        if vertex == v:
            v_found = True
            break

    if not (u_found and v_found):
        return None  # Either u or v wasn't found in the walk

    return path


def find_walk(grafo, vertice_atual, vertice_destino, visitados, walk):
    visitados[vertice_atual] = True
    walk.append(vertice_atual)

    if vertice_atual == vertice_destino:
        return True

    for vizinho in grafo.adjacencia[vertice_atual]:
        if not visitados[vizinho]:
            if find_walk(grafo, vizinho, vertice_destino, visitados, walk):
                return True

    walk.pop()
    return False


def main():
    grafo = GrafoListaAdjacencia(4)

    # Adicione os vértices
    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_vertice("C")
    grafo.adicionar_vertice("D")

    # Defina as capacidades das arestas (representando rotas e suas capacidades)
    grafo.definir_capacidade_aresta(0, 1, 10)  # Rota de A para B com capacidade 10
    grafo.definir_capacidade_aresta(0, 2, 5)  # Rota de A para C com capacidade 5
    grafo.definir_capacidade_aresta(1, 2, 15)  # Rota de B para C com capacidade 15
    grafo.definir_capacidade_aresta(1, 3, 10)  # Rota de B para D com capacidade 10
    grafo.definir_capacidade_aresta(2, 3, 10)  # Rota de C para D com capacidade 10

    # Calcule o fluxo máximo de A para D
    fluxo_maximo = grafo.calcular_fluxo_maximo(0, 3)
    capacidade_residual = grafo.capacidade_residual(0, 3)
    capacidade_da_aresta = grafo.capacidade_da_aresta(0, 3)
    print("Capacidade residual: ", capacidade_residual)
    print("capacidade da aresta: ", capacidade_da_aresta)
    print("Fluxo Máximo de A para D:", fluxo_maximo)


if __name__ == "__main__":
    main()
