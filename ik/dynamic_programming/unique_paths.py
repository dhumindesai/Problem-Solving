#TODO: need optimization in space
def count_unique_paths(m,n):

    table = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        table[i][0] = 1

    for j in range(n):
        table[0][j] = 1

    for i in range(1,m):
        for j in range(1,n):
            table[i][j] = table[i-1][j] + table[i][j-1]

    return table[m-1][n-1]

print(count_unique_paths(3,3))