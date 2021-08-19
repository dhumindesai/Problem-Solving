def minimumTotal(triangle):
    rows = len(triangle)

    table = [triangle[0]]

    # fill walls
    for i in range(1, rows):
        table.append([0 for _ in range(len(triangle[i]))])
        table[i][0] = triangle[i][0] + table[i - 1][0]
        table[i][i] = triangle[i][i] + table[i - 1][i - 1]

    #fill table from top to bottom
    for i in range(1, rows):
        for j in range(1, i):
            table[i][j] = triangle[i][j] + min(table[i-1][j], table[i-1][j-1])

    return min(table[-1])

print(minimumTotal([[1],[-5,-2],[3,6,1],[-1,2,4,-3]]))