#TODO: need optimization in space
def numberOfPaths(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        if matrix[0][i] == 0:
            break
        dp[0][i] = 1

    for j in range(m):
        if matrix[j][0] == 0:
            break
        dp[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


print(numberOfPaths([[1,1,0,1], [1,1,1,1]]))