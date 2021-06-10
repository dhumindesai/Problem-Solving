from collections import deque

def number_of_connected_components(n, edges):
    # dfs
    def dfs(node):
        visited[node] = 1
        for neighbor in adjList[node]:
            if visited[neighbor] == -1:
                dfs(neighbor)

    #bfs
    def bfs(node):
        q = deque()
        q.append(node)
        visited[node] = 1

        while q:
            current = q.popleft()
            for neighbor in adjList[current]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    q.append(neighbor)


    # build a graph
    adjList = [[] for _ in range(n)]
    visited = [-1 for _ in range(n)]

    for src, dst in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)

    components = 0
    # outer loop
    for i in range(n):
        if visited[i] == -1:
            components += 1
            bfs(i)

    return components

n = 5

edges = [[0 , 1],[1 , 2],[0 , 2],[3 , 4]]

print(number_of_connected_components(n ,edges))