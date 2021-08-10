'''

Given a two-dimensional boolean matrix, find the number of islands.

An island is a group of connected 1s or a standalone 1.
 A cell in the matrix can be connected to up to 8 neighbors: 2 vertical, 2 horizontal and 4 diagonal.
'''
def count_islands(matrix):
    # dfs
    def get_neighbors(i, j):
        result = []
        if i > 0:
            result.append((i - 1, j))
        if j > 0:
            result.append((i, j - 1))
        if i < rows - 1:
            result.append((i + 1, j))
        if j < cols - 1:
            result.append((i, j + 1))
        if i > 0 and j > 0:
            result.append((i - 1, j - 1))
        if i > 0 and j < cols - 1:
            result.append((i - 1, j + 1))
        if i < rows - 1 and j > 0:
            result.append((i + 1, j - 1))
        if i < rows - 1 and j < cols - 1:
            result.append((i + 1, j + 1))

        return result

    def dfs(i, j):

        visited[i][j] = True

        for neighbor in get_neighbors(i, j):
            x, y = neighbor[0], neighbor[1]
            if matrix[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                dfs(x, y)

    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    islands = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                islands += 1
                dfs(i, j)
    return islands

matrix = [

    [1, 1, 0, 0, 0],

    [0, 1, 0, 0, 1],

    [1, 0, 0, 1, 1],

    [0, 0, 0, 0, 0],

    [1, 0, 1, 0, 1]

]
print(count_islands(matrix))