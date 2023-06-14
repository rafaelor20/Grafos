#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VERTICES 100

// Estrutura para representar um vértice
typedef struct
{
    int index;
    char label[100];
    int degree;
} Vertex;

// Estrutura para representar um grafo
typedef struct
{
    int numVertices;
    int numEdges;
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
    vertex.degree = 0;

    graph->vertices[graph->numVertices] = vertex;
    graph->numVertices++;
}

// Método para criar uma aresta entre dois vértices
void addEdge(Graph *graph, int index1, int index2)
{
    if (index1 < 0 || index1 >= graph->numVertices || index2 < 0 || index2 >= graph->numVertices)
    {
        printf("Índice inválido!\n");
        return;
    }

    graph->adjMatrix[index1][index2] = 1;
    graph->adjMatrix[index2][index1] = 1;

    graph->vertices[index1].degree++;
    graph->vertices[index2].degree++;

    graph->numEdges++;
}

// Método para remover uma aresta entre dois vértices
void removeEdge(Graph *graph, int index1, int index2)
{
    if (index1 < 0 || index1 >= graph->numVertices || index2 < 0 || index2 >= graph->numVertices)
    {
        printf("Índice inválido!\n");
        return;
    }

    graph->adjMatrix[index1][index2] = 0;
    graph->adjMatrix[index2][index1] = 0;

    graph->vertices[index1].degree--;
    graph->vertices[index2].degree--;

    graph->numEdges--;
}

// Método para calcular o grau de um vértice
int calculateDegree(Graph *graph, int index)
{
    if (index < 0 || index >= graph->numVertices)
    {
        printf("Índice inválido!\n");
        return -1;
    }

    return graph->vertices[index].degree;
}

// Método para imprimir o grafo
void printGraph(Graph *graph)
{
    printf("Número de vértices: %d\n", graph->numVertices);
    printf("Número de arestas: %d\n", graph->numEdges);

    printf("Lista de arestas:\n");
    for (int i = 0; i < graph->numVertices; i++)
    {
        for (int j = i + 1; j < graph->numVertices; j++)
        {
            if (graph->adjMatrix[i][j] == 1)
            {
                printf("(%s, %s)\n", graph->vertices[i].label, graph->vertices[j].label);
            }
        }
    }

    printf("Grau de cada vértice:\n");
    for (int i = 0; i < graph->numVertices; i++)
    {
        printf("%s: %d\n", graph->vertices[i].label, graph->vertices[i].degree);
    }
}

// Método para criar um grafo
Graph createGraph(int maxVertices)
{
    Graph graph;
    graph.numVertices = 0;
    graph.numEdges = 0;
    memset(graph.adjMatrix, 0, sizeof(graph.adjMatrix));
    memset(graph.vertices, 0, sizeof(graph.vertices));
    return graph;
}

// Função de exemplo para utilizar o grafo
void exampleUsage()
{
    int maxVertices = 10;
    Graph graph = createGraph(maxVertices);

    addVertex(&graph, 0, "A");
    addVertex(&graph, 1, "B");
    addVertex(&graph, 2, "C");

    addEdge(&graph, 0, 1);
    addEdge(&graph, 1, 2);

    printGraph(&graph);
}

int main()
{
    exampleUsage();

    return 0;
}
