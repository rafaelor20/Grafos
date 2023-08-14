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


def exercicio5_9(grafo):
    # Exercise 5.2
    passeio = Passeio()
    passeio.adicionar_vertice(1)
    passeio.adicionar_vertice(3)
    passeio.adicionar_vertice(2)
    passeio.adicionar_vertice(5)
    passeio.adicionar_vertice(4)
    passeio.imprimir_passeio()

    # Exercise 5.3
    passeio.imprimir_reverso()

    # Exercise 5.4
    secao = passeio.obter_secao(1, 3)
    secao.imprimir_passeio()

    # Exercise 5.5
    passeio_v_x = Passeio()
    busca_em_profundidade_passeio(
        grafo, 1, 5, [False] * len(grafo.vertices), passeio_v_x
    )
    passeio_v_x.imprimir_passeio()

    # Exercise 5.6
    caminho_v_x = Passeio()
    busca_em_profundidade_caminho(
        grafo, 1, 5, [False] * len(grafo.vertices), caminho_v_x
    )
    caminho_v_x.imprimir_passeio()

    # Exercise 5.7
    ciclo = busca_ciclo(grafo)
    if ciclo is not None:
        print("O grafo possui um ciclo:")
        for vertice in ciclo:
            print(vertice, end=" ")
        print()
    else:
        print("O grafo não possui ciclo.")

    # Exercise 5.8
    ciclo_g_v_maior_igual_2 = buscar_ciclo_com_g_v_maior_igual_2(grafo)
    if ciclo_g_v_maior_igual_2 is not None:
        print("Ciclo com grau >= 2 encontrado:")
        for vertice in ciclo_g_v_maior_igual_2:
            print(vertice, end=" ")
        print()
    else:
        print("Nenhum ciclo com grau >= 2 encontrado.")

    # Exercise E.1
    # Test find_cycle_with_edge with grafo edges
    edge_to_find = (2, 3)
    result_cycle = find_cycle_with_edge(grafo.vertices, edge_to_find)
    print("Cycle with edge a:", result_cycle)

    # Exercise E.2
    walk_between_u_and_v = [1, 3, 4, 2, 5]
    u_vertex = 1
    v_vertex = 2
    result_path = walk_to_path(walk_between_u_and_v, u_vertex, v_vertex)
    if result_path is None:
        print("No valid path between u and v found.")
    else:
        print("Path between u and v:", result_path)


def main():
    grafo = createGraph()

    exercicio5_9(grafo)


if __name__ == "__main__":
    main()
