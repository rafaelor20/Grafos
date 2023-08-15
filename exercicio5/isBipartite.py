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
