// Arquivo: graphMatrix.js

class GraphMatrix {
  constructor(maxVertices) {
    this.maxVertices = maxVertices;
    this.adjMatrix = [];

    for (let i = 0; i < maxVertices; i++) {
      this.adjMatrix[i] = [];
      for (let j = 0; j < maxVertices; j++) {
        this.adjMatrix[i][j] = 0;
      }
    }
  }

  addVertex(index, label) {
    // Verificar se o índice está dentro do limite máximo de vértices
    if (index >= 0 && index < this.maxVertices) {
      this.adjMatrix[index][index] = label;
    }
  }

  removeVertex(index) {
    // Verificar se o índice está dentro do limite máximo de vértices
    if (index >= 0 && index < this.maxVertices) {
      this.adjMatrix[index][index] = 0;
      // Remover todas as arestas relacionadas ao vértice removido
      for (let i = 0; i < this.maxVertices; i++) {
        this.adjMatrix[index][i] = 0;
        this.adjMatrix[i][index] = 0;
      }
    }
  }

  addEdge(index1, index2) {
    // Verificar se os índices estão dentro do limite máximo de vértices
    if (
      index1 >= 0 &&
      index1 < this.maxVertices &&
      index2 >= 0 &&
      index2 < this.maxVertices
    ) {
      this.adjMatrix[index1][index2] = 1;
      this.adjMatrix[index2][index1] = 1;
    }
  }

  removeEdge(index1, index2) {
    // Verificar se os índices estão dentro do limite máximo de vértices
    if (
      index1 >= 0 &&
      index1 < this.maxVertices &&
      index2 >= 0 &&
      index2 < this.maxVertices
    ) {
      this.adjMatrix[index1][index2] = 0;
      this.adjMatrix[index2][index1] = 0;
    }
  }

  getDegree(index) {
    // Verificar se o índice está dentro do limite máximo de vértices
    if (index >= 0 && index < this.maxVertices) {
      let degree = 0;
      for (let i = 0; i < this.maxVertices; i++) {
        if (this.adjMatrix[index][i] === 1) {
          degree++;
        }
      }
      return degree;
    }
    return 0;
  }

  areNeighbors(index1, index2) {
    // Verificar se os índices estão dentro do limite máximo de vértices
    if (
      index1 >= 0 &&
      index1 < this.maxVertices &&
      index2 >= 0 &&
      index2 < this.maxVertices
    ) {
      return this.adjMatrix[index1][index2] === 1;
    }
    return false;
  }

  printGraph() {
    console.log(`Número de vértices: ${this.maxVertices}`);
    let totalEdges = 0;

    for (let i = 0; i < this.maxVertices; i++) {
      let degree = 0;
      let neighbors = [];
      for (let j = 0; j < this.maxVertices; j++) {
        if (this.adjMatrix[i][j] === 1) {
          degree++;
          neighbors.push(j);
        }
      }
      totalEdges += degree;
      console.log(`Grau do vértice ${i}: ${degree}`);
      neighbors.forEach((neighbor) => {
        console.log(`Aresta: ${i} - ${neighbor}`);
      });
    }

    console.log(`Número de arestas: ${totalEdges / 2}`);
  }
}


