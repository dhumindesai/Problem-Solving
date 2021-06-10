from collections import deque


def is_it_a_tree(node_count, edge_start, edge_end):
    if node_count < 1:
        return False

    # bfs
    def isCycleBfs(root):
        q = deque()
        q.append(root)
        visited[root] = 1

        while q:
            node = q.popleft()
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    q.append(neighbor)
                    parent[neighbor] = node
                else:
                    # check if neighbor is not parent (cross edge detection)
                    if parent[node] != neighbor:
                        return True
        return False

    # build graph
    adjList = [[] for _ in range(node_count)]
    visited = [-1 for _ in range(node_count)]
    parent = [-1 for _ in range(node_count)]

    for i in range(len(edge_start)):
        adjList[edge_start[i]].append(edge_end[i])
        adjList[edge_end[i]].append(edge_start[i])

    # outer loop
    component = 0
    for i in range(node_count):
        if component > 1:
            return False
        if visited[i] == -1:
            component += 1
            if isCycleBfs(i):
                return False

    return True

print(is_it_a_tree(4, [0,0, 0], [1,2,3]))