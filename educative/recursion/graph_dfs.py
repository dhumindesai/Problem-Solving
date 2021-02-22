from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


def dfs(graph):
    visited = set()
    for v in graph.vertices:
        dfsHelper(v, visited, graph.graph)

def dfsHelper(vertex, visited, edges):
    if vertex in visited:
        return
    print(vertex)
    visited.add(vertex)

    for node in edges[vertex]:
        dfsHelper(node, visited, edges)


def main():
    myGraph = Graph([0, 1, 2, 3, 4, 5, 6])
    myGraph.addEdge(0, 1)
    myGraph.addEdge(1, 2)
    myGraph.addEdge(1, 3)
    myGraph.addEdge(2, 4)
    myGraph.addEdge(3, 4)
    myGraph.addEdge(3, 5)

    dfs(myGraph)

main()