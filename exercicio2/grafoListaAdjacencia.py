import tkinter as tk
import math


class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.grau = 0


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
