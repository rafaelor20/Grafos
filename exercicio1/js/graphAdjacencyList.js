// Arquivo: graphAdjacencyList.js

class GraphAdjacencyList {
  constructor() {
    this.vertices = new Map();
  }

  addVertex(index, label) {
    this.vertices.set(index, {
      index,
      label,
      neighbors: new Set(),
    });
  }

  removeVertex(index) {
    this.vertices.delete(index);
    // Remover todas as arestas relacionadas ao vértice removido
    for (const vertex of this.vertices.values()) {
      vertex.neighbors.delete(index);
    }
  }

  addEdge(index1, index2) {
    const vertex1 = this.vertices.get(index1);
    const vertex2 = this.vertices.get(index2);

    if (vertex1 && vertex2) {
      vertex1.neighbors.add(index2);
      vertex2.neighbors.add(index1);
    }
  }

  removeEdge(index1, index2) {
    const vertex1 = this.vertices.get(index1);
    const vertex2 = this.vertices.get(index2);

    if (vertex1 && vertex2) {
      vertex1.neighbors.delete(index2);
      vertex2.neighbors.delete(index1);
    }
  }

  getDegree(index) {
    const vertex = this.vertices.get(index);
    return vertex ? vertex.neighbors.size : 0;
  }

  areNeighbors(index1, index2) {
    const vertex1 = this.vertices.get(index1);
    return vertex1 ? vertex1.neighbors.has(index2) : false;
  }

  printGraph() {
    console.log(`Número de vértices: ${this.vertices.size}`);
    let totalEdges = 0;

    for (const [index, vertex] of this.vertices) {
      totalEdges += vertex.neighbors.size;
      console.log(`Grau do vértice ${index}: ${vertex.neighbors.size}`);
      for (const neighborIndex of vertex.neighbors) {
        console.log(`Aresta: ${index} - ${neighborIndex}`);
      }
    }

    console.log(`Número de arestas: ${totalEdges / 2}`);
  }
}

