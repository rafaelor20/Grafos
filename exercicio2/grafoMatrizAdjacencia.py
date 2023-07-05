import tkinter as tk
import math


class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.grau = 0


class GrafoMatrizAdjacencia:
    def __init__(self, max_vertices):
        self.max_vertices = max_vertices
        self.vertices = []
        self.num_arestas = 0
        self.adjacencia = [[0] * max_vertices for _ in range(max_vertices)]

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

        self.adjacencia[indice_vertice1][indice_vertice2] = 1
        self.adjacencia[indice_vertice2][indice_vertice1] = 1

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

        self.adjacencia[indice_vertice1][indice_vertice2] = 0
        self.adjacencia[indice_vertice2][indice_vertice1] = 0

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

        return self.adjacencia[indice_vertice1][indice_vertice2] == 1

    def imprimir_grafo(self):
        print("Número de vértices:", len(self.vertices))
        print("Número de arestas:", self.num_arestas)

        print("Arestas:")
        for i in range(len(self.vertices)):
            for j in range(i + 1, len(self.vertices)):
                if self.adjacencia[i][j] == 1:
                    print(f"{self.vertices[i].rotulo} - {self.vertices[j].rotulo}")

        print("Graus dos vértices:")
        for vertice in self.vertices:
            print(f"{vertice.rotulo}: {vertice.grau}")
