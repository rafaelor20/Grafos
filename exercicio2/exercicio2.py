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


def is_bipartite(graph, X, Y):
    color = {}  # Dictionary to store the color of each vertex

    # Assign initial colors to the vertices in X and Y
    for vertex in X:
        color[vertex] = "X"
    for vertex in Y:
        color[vertex] = "Y"

    # Perform graph coloring
    for vertex in graph.vertices:
        if vertex.rotulo in X:
            current_color = "X"
        else:
            current_color = "Y"

        for neighbor in graph.adjacencia[vertex.indice]:
            if color.get(neighbor) == current_color:
                return False  # Adjacent vertices have the same color, not bipartite

    return True  # No adjacent vertices have the same color, bipartite


# Exemplo createCompleteKnGraph
def exemploCreateCompleteKnGraph():
    grafoKn = createCompleteKnGraph(5)
    grafoKn.imprimir_grafo()
    visualizer = GraphVisualizer(grafoKn)


# Exemplo creaeKRegularGraph
def exemploCreaeKRegularGraph():
    n = 8
    k = 4
    grafoKRegular = creaeKRegularGraph(n, k)
    grafoKRegular.imprimir_grafo()
    visualizer = GraphVisualizer(grafoKRegular)


# Exemplo is_bipartite
def exemploIsBipartite():
    # Create the graph
    grafo = GrafoMatrizAdjacencia(6)
    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_vertice("C")
    grafo.adicionar_vertice("D")
    grafo.adicionar_vertice("E")
    grafo.adicionar_vertice("F")

    # Add edges
    grafo.adicionar_aresta(0, 1)
    grafo.adicionar_aresta(0, 2)
    grafo.adicionar_aresta(1, 3)
    grafo.adicionar_aresta(2, 4)
    grafo.adicionar_aresta(3, 5)
    grafo.adicionar_aresta(4, 5)

    # Define the sets X and Y
    X = {"A", "C", "E"}
    Y = {"B", "D", "F"}

    # Check if the graph is bipartite
    is_bipartite_graph = is_bipartite(grafo, X, Y)
    print(is_bipartite_graph)  # Output: True


exemploCreateCompleteKnGraph()
exemploCreaeKRegularGraph()
exemploIsBipartite()
