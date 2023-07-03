import tkinter as tk
import math

class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.grau = 0

class Grafo:
    def __init__(self, estrutura_dados, max_vertices):
        self.estrutura_dados = estrutura_dados
        self.max_vertices = max_vertices
        self.vertices = []
        self.num_arestas = 0

        if estrutura_dados == "matriz_adjacencia":
            self.adjacencia = [[0] * max_vertices for _ in range(max_vertices)]
        elif estrutura_dados == "lista_adjacencia":
            self.adjacencia = [[] for _ in range(max_vertices)]

    def adicionar_vertice(self, rotulo):
        indice = len(self.vertices)
        vertice = Vertice(indice, rotulo)
        self.vertices.append(vertice)

    def adicionar_aresta(self, indice_vertice1, indice_vertice2):
        if indice_vertice1 < 0 or indice_vertice1 >= len(self.vertices) or indice_vertice2 < 0 or indice_vertice2 >= len(self.vertices):
            raise IndexError("Índice de vértice inválido")

        if self.estrutura_dados == "matriz_adjacencia":
            self.adjacencia[indice_vertice1][indice_vertice2] = 1
            self.adjacencia[indice_vertice2][indice_vertice1] = 1
        elif self.estrutura_dados == "lista_adjacencia":
            self.adjacencia[indice_vertice1].append(indice_vertice2)
            self.adjacencia[indice_vertice2].append(indice_vertice1)

        self.vertices[indice_vertice1].grau += 1
        self.vertices[indice_vertice2].grau += 1
        self.num_arestas += 1

    def remover_aresta(self, indice_vertice1, indice_vertice2):
        if indice_vertice1 < 0 or indice_vertice1 >= len(self.vertices) or indice_vertice2 < 0 or indice_vertice2 >= len(self.vertices):
            raise IndexError("Índice de vértice inválido")

        if self.estrutura_dados == "matriz_adjacencia":
            self.adjacencia[indice_vertice1][indice_vertice2] = 0
            self.adjacencia[indice_vertice2][indice_vertice1] = 0
        elif self.estrutura_dados == "lista_adjacencia":
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
        if indice_vertice1 < 0 or indice_vertice1 >= len(self.vertices) or indice_vertice2 < 0 or indice_vertice2 >= len(self.vertices):
            raise IndexError("Índice de vértice inválido")

        if self.estrutura_dados == "matriz_adjacencia":
            return self.adjacencia[indice_vertice1][indice_vertice2] == 1
        elif self.estrutura_dados == "lista_adjacencia":
            return indice_vertice2 in self.adjacencia[indice_vertice1]

    def imprimir_grafo(self):
        print("Número de vértices:", len(self.vertices))
        print("Número de arestas:", self.num_arestas)

        print("Arestas:")
        if self.estrutura_dados == "matriz_adjacencia":
            for i in range(len(self.vertices)):
                for j in range(i+1, len(self.vertices)):
                    if self.adjacencia[i][j] == 1:
                        print(f"{self.vertices[i].rotulo} - {self.vertices[j].rotulo}")
        elif self.estrutura_dados == "lista_adjacencia":
            for i in range(len(self.vertices)):
                for j in self.adjacencia[i]:
                    if i < j:
                        print(f"{self.vertices[i].rotulo} - {self.vertices[j].rotulo}")

        print("Graus dos vértices:")
        for vertice in self.vertices:
            print(f"{vertice.rotulo}: {vertice.grau}")

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
            self.canvas.create_oval(x - self.vertex_radius, y - self.vertex_radius,
                                    x + self.vertex_radius, y + self.vertex_radius,
                                    fill="lightblue")
            self.canvas.create_text(x, y, text=vertice.rotulo)

        for i in range(len(self.grafo.vertices)):
            for j in self.grafo.adjacencia[i]:
                start_x, start_y = self.vertex_positions[i]
                end_x, end_y = self.vertex_positions[j]

                # Calculate the unit vector pointing from start to end
                dx, dy = end_x - start_x, end_y - start_y
                length = math.sqrt(dx ** 2 + dy ** 2)

                if length > 0:
                    unit_dx, unit_dy = dx / length, dy / length

                    # Calculate the adjusted start and end points
                    adjusted_start_x = start_x + self.vertex_radius * unit_dx
                    adjusted_start_y = start_y + self.vertex_radius * unit_dy
                    adjusted_end_x = end_x - self.vertex_radius * unit_dx
                    adjusted_end_y = end_y - self.vertex_radius * unit_dy

                    self.canvas.create_line(adjusted_start_x, adjusted_start_y, adjusted_end_x, adjusted_end_y)


def createCompleteKnGraph(number):
  grafoKn =  Grafo("matriz_adjacencia", number)
  i = 0
  while i < number:
    grafoKn.adicionar_vertice( "V" + str(i) )
    i = i + 1
  i = 0
  j = i+1
  while i < number - 2:
    grafoKn.adicionar_aresta(i, j)
    print(i)
    print(j)
    i = i + 1
    j = i + 1
    
  if i>0:
    grafoKn.adicionar_aresta(j, 0)
  return grafoKn

#Exemplo createCompleteKnGraph
graphKn = createCompleteKnGraph(5)
visualizer = GraphVisualizer(graphKn)
