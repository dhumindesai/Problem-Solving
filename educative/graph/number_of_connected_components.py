from collections import deque


def number_of_connected_components(n, edges):
    # 2. BFS/DFS
    def bfs(root):
        q = deque()
        q.append(root)
        visited[root] = True

        while q:
            node = q.popleft()
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True

    # 1. build an adjacencyList
    adjList = [[] for _ in range(n)]
    visited = [False for _ in range(n)]

    for src, dst in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)

    # 3. outerloop
    components = 0
    for v in range(len(visited)):
        if not visited[v]:
            components += 1
            bfs(v)

    return components

n = 5

edges = [[0 , 1],[1 , 2],[0 , 2],[3 , 4]]

print(number_of_connected_components(n ,edges))

import math
math.pow(2,4)