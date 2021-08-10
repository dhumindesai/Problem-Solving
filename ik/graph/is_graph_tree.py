# from collections import deque
#
#
# def is_it_a_tree(node_count, edge_start, edge_end):
#     if node_count < 1:
#         return False
#
#     # bfs
#     def isCycleBfs(root):
#         q = deque()
#         q.append(root)
#         visited[root] = 1
#
#         while q:
#             node = q.popleft()
#             for neighbor in adjList[node]:
#                 if visited[neighbor] == -1:
#                     visited[neighbor] = 1
#                     q.append(neighbor)
#                     parent[neighbor] = node
#                 else:
#                     # check if neighbor is not parent (cross edge detection)
#                     if parent[node] != neighbor:
#                         return True
#         return False
#
#     # build graph
#     adjList = [[] for _ in range(node_count)]
#     visited = [-1 for _ in range(node_count)]
#     parent = [-1 for _ in range(node_count)]
#
#     for i in range(len(edge_start)):
#         adjList[edge_start[i]].append(edge_end[i])
#         adjList[edge_end[i]].append(edge_start[i])
#
#     # outer loop
#     component = 0
#     for i in range(node_count):
#         if component > 1:
#             return False
#         if visited[i] == -1:
#             component += 1
#             if isCycleBfs(i):
#                 return False
#
#     return True


# Complete the function below
# The function accepts an INTEGER node_count, two INTEGER_ARRAYs edge_start and edge_end as parameters and
# is expected to return a BOOLEAN
def is_it_a_tree(n, edge_start, edge_end):
    # 2. dfs
    def is_cycle_in_dfs(root):
        visited[root] = True
        for neighbor in adjList[root]:
            if not visited[neighbor]:
                # tree edge
                visited[neighbor] = True
                parent[neighbor] = root
                if is_cycle_in_dfs(neighbor):
                    return True
            else:
                # check for the backedge
                if neighbor is not parent[root]:
                    return True
        return False

    # 1. create a graph
    adjList = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    components = 0

    for i in range(len(edge_start)):
        adjList[edge_start[i]].append(edge_end[i])  # i = 1 => edgList[0].append(2)
        adjList[edge_end[i]].append(edge_start[i])

    # 3. outer loop
    for vertex in range(n):
        if not visited[vertex]:
            components += 1
            if components > 1:
                return False
            if is_cycle_in_dfs(vertex):
                return False
    return True


print(is_it_a_tree(4, [0,0], [1,2]))