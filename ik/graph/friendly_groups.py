from collections import deque


def can_be_divided(n, dislike1, dislike2):
    # bfs
    def bfs(root):
        q = deque()
        visited[root] = True
        distance[root] = 1
        q.append(root)

        while q:
            node = q.popleft()
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
                    distance[neighbor] = distance[node] + 1
                else:
                    if distance[node] == distance[neighbor]:
                        return False
        return True

    # 1. create an adjacencyList
    adjList = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]

    for i in range(len(dislike1)):
        adjList[dislike1[i]].append(dislike2[i])
        adjList[dislike2[i]].append(dislike1[i])

    # Outer loop
    for vertex in range(n):
        if not visited[vertex]:
            if not bfs(vertex):
                return False
    return True
