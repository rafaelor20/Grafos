#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VERTICES 100

// Estrutura para representar um vértice
typedef struct
{
    int index;
    char label[100];
} Vertex;

// Estrutura para representar um grafo
typedef struct
{
    int numVertices;
    int adjMatrix[MAX_VERTICES][MAX_VERTICES];
    Vertex vertices[MAX_VERTICES];
} Graph;

// Método para adicionar um vértice ao grafo
void addVertex(Graph *graph, int index, const char *label)
{
    if (graph->numVertices >= MAX_VERTICES)
    {
        printf("Número máximo de vértices excedido!\n");
        return;
    }

    Vertex vertex;
    vertex.index = index;
    strcpy(vertex.label, label);

    graph->vertices[graph->numVertices] = vertex;
    graph->numVertices++;
}

// Método para criar um grafo
Graph createGraph(int maxVertices)
{
    Graph graph;
    graph.numVertices = 0;
    memset(graph.adjMatrix, 0, sizeof(graph.adjMatrix));
    memset(graph.vertices, 0, sizeof(graph.vertices));
    return graph;
}

int main()
{
    int maxVertices = 10;
    Graph graph = createGraph(maxVertices);

    addVertex(&graph, 0, "A");
    addVertex(&graph, 1, "B");
    addVertex(&graph, 2, "C");

    // Exemplo de acesso aos vértices do grafo
    for (int i = 0; i < graph.numVertices; i++)
    {
        Vertex vertex = graph.vertices[i];
        printf("Index: %d, Label: %s\n", vertex.index, vertex.label);
    }

    return 0;
}
