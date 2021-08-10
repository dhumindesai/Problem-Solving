def canReach(self, arr, start):
    """
    :type arr: List[int]
    :type start: int
    :rtype: bool
    """

    def get_neighbors(node):
        result = []
        if node + arr[node] < len(arr):
            result.append(node + arr[node])
        if node - arr[node] >= 0:
            result.append(node - arr[node])
        return result

    def dfs(node):
        visited[node] = True
        if arr[node] == 0:
            return True
        for neighbor in get_neighbors(node):
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        return False

    visited = [False for _ in range(len(arr))]
    return dfs(start)
