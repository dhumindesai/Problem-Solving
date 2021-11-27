def maximalSquare(matrix):
    # def min_neighbor(x,y):
    #     return min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1])


    m = len(matrix)
    n = len(matrix[0])
    result = 0
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        dp[i][0] = int(matrix[i][0])
        result = max(result, dp[i][0])

    for j in range(n):
        dp[0][j] = int(matrix[0][j])
        result = max(result, dp[0][j])

    for i in range(1, m):
        for j in range(1, n):
            if int(matrix[i][j]) != 0:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                result = max(result, dp[i][j])

    return result**2

# print(maximalSquare([["1","0","1","0","0"],
#                      ["1","0","1","1","1"],
#                      ["1","1","1","1","1"],
#                      ["1","0","0","1","0"]]))
print(maximalSquare([["1","1","1","1","0"],
                     ["1","1","1","1","0"],
                     ["1","1","1","1","1"],
                     ["1","1","1","1","1"],
                     ["0","0","1","1","1"]]))
