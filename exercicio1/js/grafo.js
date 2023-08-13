class GraphAdjacencyList {
  constructor() {
    this.vertices = new Map();
  }

  addVertex(index, label) {
    this.vertices.set(index, { index, label, edges: new Set() });
  }

  addEdge(vertex1, vertex2) {
    const v1 = this.vertices.get(vertex1);
    const v2 = this.vertices.get(vertex2);
    v1.edges.add(vertex2);
    v2.edges.add(vertex1);
  }

  removeEdge(vertex1, vertex2) {
    const v1 = this.vertices.get(vertex1);
    const v2 = this.vertices.get(vertex2);
    v1.edges.delete(vertex2);
    v2.edges.delete(vertex1);
  }

  getDegree(vertex) {
    return this.vertices.get(vertex).edges.size;
  }

  areAdjacent(vertex1, vertex2) {
    const v1 = this.vertices.get(vertex1);
    return v1.edges.has(vertex2);
  }

  printGraph() {
    console.log("Number of vertices:", this.vertices.size);
    let edgeCount = 0;

    for (const [vertex, data] of this.vertices) {
      for (const edge of data.edges) {
        if (edge > vertex) {
          console.log("Edge:", vertex, "<->", edge);
          edgeCount++;
        }
      }
    }

    console.log("Number of edges:", edgeCount);

    for (const [vertex, data] of this.vertices) {
      console.log("Degree of vertex", vertex, ":", this.getDegree(vertex));
    }
  }
}

// Exemplo de uso:
const graphAdjList = new GraphAdjacencyList();
graphAdjList.addVertex(0, "A");
graphAdjList.addVertex(1, "B");
graphAdjList.addVertex(2, "C");
graphAdjList.addVertex(3, "D");
graphAdjList.addVertex(4, "E");
graphAdjList.addEdge(0, 1);
graphAdjList.addEdge(1, 2);
graphAdjList.addEdge(2, 3);
graphAdjList.addEdge(3, 4);
graphAdjList.printGraph();
