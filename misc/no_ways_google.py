
def no_ways(m, n):
    def get_neighbors(x, y):
        neighbors = []
        dirs = [(-1, -1), (-1, 0), (-1, 1)]
        for r, c in dirs:
            new_r = x + r
            new_c = y + c
            if 0 <= new_r < m and 0 <= new_c < n:
                neighbors.append((new_r, new_c))
        return neighbors
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1

    for i in range(1, m):
        for j in range(0, n):
            for x, y in get_neighbors(i, j):
                dp[i][j] += dp[x][y]

    return dp[m - 1][0]

print(no_ways(3,3))