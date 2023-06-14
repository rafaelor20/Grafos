#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Estrutura para representar um vértice
typedef struct
{
    int index;
    char label[20];
    int degree;
} Vertex;

// Estrutura para a Estrutura de Adjacência
typedef struct
{
    int maxVertices;
    int numVertices;
    int numEdges;
    Vertex **vertices;
    bool **adjacencyMatrix;
} Graph;

// Função para criar um grafo
Graph *createGraph(int maxVertices)
{
    Graph *graph = (Graph *)malloc(sizeof(Graph));
    graph->maxVertices = maxVertices;
    graph->numVertices = 0;
    graph->numEdges = 0;

    graph->vertices = (Vertex **)malloc(maxVertices * sizeof(Vertex *));
    graph->adjacencyMatrix = (bool **)malloc(maxVertices * sizeof(bool *));

    for (int i = 0; i < maxVertices; i++)
    {
        graph->vertices[i] = NULL;
        graph->adjacencyMatrix[i] = (bool *)malloc(maxVertices * sizeof(bool));

        for (int j = 0; j < maxVertices; j++)
        {
            graph->adjacencyMatrix[i][j] = false;
        }
    }

    return graph;
}

// Função para adicionar um vértice ao grafo
void addVertex(Graph *graph, int index, const char *label)
{
    if (index < 0 || index >= graph->maxVertices)
    {
        printf("Erro: Índice de vértice inválido.\n");
        return;
    }

    if (graph->vertices[index] != NULL)
    {
        printf("Erro: Já existe um vértice com esse índice.\n");
        return;
    }

    Vertex *vertex = (Vertex *)malloc(sizeof(Vertex));
    vertex->index = index;
    snprintf(vertex->label, sizeof(vertex->label), "%s", label);
    vertex->degree = 0;

    graph->vertices[index] = vertex;
    graph->numVertices++;
}

// Função para criar uma aresta entre dois vértices
void addEdge(Graph *graph, int index1, int index2)
{
    if (index1 < 0 || index1 >= graph->maxVertices || index2 < 0 || index2 >= graph->maxVertices)
    {
        printf("Erro: Índice de vértice inválido.\n");
        return;
    }

    if (graph->vertices[index1] == NULL || graph->vertices[index2] == NULL)
    {
        printf("Erro: Um dos vértices não existe.\n");
        return;
    }

    if (graph->adjacencyMatrix[index1][index2])
    {
        printf("Erro: A aresta já existe.\n");
        return;
    }

    graph->adjacencyMatrix[index1][index2] = true;
    graph->adjacencyMatrix[index2][index1] = true;
    graph->numEdges++;

    graph->vertices[index1]->degree++;
    graph->vertices[index2]->degree++;
}

// Função para remover uma aresta entre dois vértices
void removeEdge(Graph *graph, int index1, int index2)
{
    if (index1 < 0 || index1 >= graph->maxVertices || index2 < 0 || index2 >= graph->maxVertices)
    {
        printf("Erro: Índice de vértice inválido.\n");
        return;
    }

    if (graph->vertices[index1] == NULL || graph->vertices[index2] == NULL)
    {
        printf("Erro: Um dos vértices não existe.\n");
        return;
    }

    if (!graph->adjacencyMatrix[index1][index2])
    {
        printf("Erro: A aresta não existe.\n");
        return;
    }

    graph->adjacencyMatrix[index1][index2] = false;
    graph->adjacencyMatrix[index2][index1] = false;
    graph->numEdges--;

    graph->vertices[index1]->degree--;
    graph->vertices[index2]->degree--;
}

// Função para calcular o grau de um vértice
int calculateDegree(Graph *graph, int index)
{
    if (index < 0 || index >= graph->maxVertices)
    {
        printf("Erro: Índice de vértice inválido.\n");
        return -1;
    }

    if (graph->vertices[index] == NULL)
    {
        printf("Erro: O vértice não existe.\n");
        return -1;
    }

    return graph->vertices[index]->degree;
}

// Função para verificar se dois vértices são vizinhos
bool areNeighbors(Graph *graph, int index1, int index2)
{
    if (index1 < 0 || index1 >= graph->maxVertices || index2 < 0 || index2 >= graph->maxVertices)
    {
        printf("Erro: Índice de vértice inválido.\n");
        return false;
    }

    if (graph->vertices[index1] == NULL || graph->vertices[index2] == NULL)
    {
        printf("Erro: Um dos vértices não existe.\n");
        return false;
    }

    return graph->adjacencyMatrix[index1][index2];
}

// Função para imprimir o grafo
void printGraph(Graph *graph)
{
    printf("Número de vértices: %d\n", graph->numVertices);
    printf("Número de arestas: %d\n", graph->numEdges);
    printf("Arestas:\n");

    for (int i = 0; i < graph->maxVertices; i++)
    {
        for (int j = i + 1; j < graph->maxVertices; j++)
        {
            if (graph->adjacencyMatrix[i][j])
            {
                printf("%s -- %s\n", graph->vertices[i]->label, graph->vertices[j]->label);
            }
        }
    }

    printf("Graus dos vértices:\n");

    for (int i = 0; i < graph->maxVertices; i++)
    {
        if (graph->vertices[i] != NULL)
        {
            printf("%s: %d\n", graph->vertices[i]->label, graph->vertices[i]->degree);
        }
    }
}

// Função de exemplo para utilizar o grafo
void exampleUsage()
{
    Graph *graph = createGraph(10);

    addVertex(graph, 0, "A");
    addVertex(graph, 1, "B");
    addVertex(graph, 2, "C");
    addVertex(graph, 3, "D");
    addVertex(graph, 4, "E");

    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 2, 4);
    addEdge(graph, 3, 4);

    printf("Grau do vértice C: %d\n", calculateDegree(graph, 2));
    printf("A e C são vizinhos? %s\n", areNeighbors(graph, 0, 2) ? "Sim" : "Não");

    removeEdge(graph, 1, 2);
    printf("Grau do vértice B após remover a aresta: %d\n", calculateDegree(graph, 1));

    printGraph(graph);
}

int main()
{
    exampleUsage();

    return 0;
}
