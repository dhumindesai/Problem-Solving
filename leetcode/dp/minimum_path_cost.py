def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    table = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        if i == 0:
            table[i][0] = grid[i][0]
            continue
        table[i][0] = grid[i][0] + table[i - 1][0]

    for j in range(n):
        if j == 0:
            table[0][j] = grid[0][j]
            continue
        table[0][j] = grid[0][j] + table[0][j - 1]

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = grid[i][j] + min(table[i - 1][j], table[i][j - 1])

    print(table)

    return table[-1][-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))