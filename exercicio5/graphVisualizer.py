import tkinter as tk
import math


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
