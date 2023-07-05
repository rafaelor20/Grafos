import tkinter as tk
import math

from grafoListaAdjacencia import GrafoListaAdjacencia
from grafoMatrizAdjacencia import GrafoMatrizAdjacencia


class GraphVisualizer:
    def __init__(self, grafo):
        self.grafo = grafo

        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()

        self.vertex_radius = 20
        self.vertex_positions = self.calculate_vertex_positions()

        self.draw_graph()

        self.window.mainloop()

    def calculate_vertex_positions(self):
        num_vertices = len(self.grafo.vertices)
        positions = []

        for i in range(num_vertices):
            angle = 2 * i * math.pi / num_vertices
            x = 200 + 150 * math.cos(angle)
            y = 200 + 150 * math.sin(angle)
            positions.append((x, y))

        return positions

    def draw_graph(self):
        for i, vertice in enumerate(self.grafo.vertices):
            x, y = self.vertex_positions[i]
            self.canvas.create_oval(
                x - self.vertex_radius,
                y - self.vertex_radius,
                x + self.vertex_radius,
                y + self.vertex_radius,
                fill="lightblue",
            )
            self.canvas.create_text(x, y, text=vertice.rotulo)

        for i in range(len(self.grafo.vertices)):
            for j in self.grafo.adjacencia[i]:
                start_x, start_y = self.vertex_positions[i]
                end_x, end_y = self.vertex_positions[j]

                # Calculate the unit vector pointing from start to end
                dx, dy = end_x - start_x, end_y - start_y
                length = math.sqrt(dx**2 + dy**2)

                if length > 0:
                    unit_dx, unit_dy = dx / length, dy / length

                    # Calculate the adjusted start and end points
                    adjusted_start_x = start_x + self.vertex_radius * unit_dx
                    adjusted_start_y = start_y + self.vertex_radius * unit_dy
                    adjusted_end_x = end_x - self.vertex_radius * unit_dx
                    adjusted_end_y = end_y - self.vertex_radius * unit_dy

                    self.canvas.create_line(
                        adjusted_start_x,
                        adjusted_start_y,
                        adjusted_end_x,
                        adjusted_end_y,
                    )


def createCompleteKnGraph(number):
    grafoKn = GrafoMatrizAdjacencia(number)
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


def creaeKRegularGraph(n, k):
    # Check if k is valid for a regular graph
    if k >= n or k % 2 != 0:
        raise ValueError("Invalid degree for a regular graph")

    grafo = GrafoMatrizAdjacencia(n)

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


# Exemplo createCompleteKnGraph
n = 5
graphKn = createCompleteKnGraph(5)
visualizer = GraphVisualizer(graphKn)

# Exemplo creaeKRegularGraph
n = 8
k = 4
grafoKRegular = creaeKRegularGraph(n, k)
grafoKRegular.imprimir_grafo()
visualizer = GraphVisualizer(grafoKRegular)
