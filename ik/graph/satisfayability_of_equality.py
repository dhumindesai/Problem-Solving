from collections import deque
def equationsPossible(equations):
    """
    :type equations: List[str]
    :rtype: bool

    a --- b
        c
    """

    def bfs(root, component):
        q = deque()
        q.append(root)
        visited[root] = component

        while q:
            node = q.popleft()
            for neighbor in adjList[node]:
                if not neighbor in visited:
                    visited[neighbor] = component
                    q.append(neighbor)

    adjList = {}

    for eq in equations:
        if "==" in eq:
            var_1 = eq.split("==")[0]
            var_2 = eq.split("==")[1]
            if not var_1 in adjList:
                adjList[var_1] = [var_2]
            else:
                adjList[var_1].append(var_2)
            if not var_2 in adjList:
                adjList[var_2] = [var_1]
            else:
                adjList[var_2].append(var_1)

    visited = {}
    component = 0

    for k in adjList.keys():
        if not k in visited:
            component += 1
            bfs(k, component)

    for eq in equations:
        if "!=" in eq:
            var_1 = eq.split("!=")[0]
            var_2 = eq.split("!=")[1]
            if var_1 in visited and var_2 in visited and visited[var_1] == visited[var_2]:
                return False

    return True

print(equationsPossible(["c==c","b==d","x!=z"]))