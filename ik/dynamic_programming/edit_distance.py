def edit_distance_rec(s1, s2):

    def helper(s1, s2, i, j):

        #base case
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i
        if s1[i] == s2[j]:
            return helper(s1, s2, i+1, j+1)

        #iterative case
        return 1 + min(helper(s1, s2, i, j + 1), helper(s1, s2, i+1, j+1), helper(s1, s2, i+1, j))

    return helper(s1, s2, 0, 0)

#TODO: improve space complexity
def edit_distance(strWord1, strWord2):
    m = len(strWord1)
    n = len(strWord2)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(m):
        dp[n][i] = m - i

    for j in range(n):
        dp[j][m] = n - j

    for i in range(n-1, -1, -1): # n-1 to 0
        for j in range(m-1, -1, -1): # m-1 to 0
            if strWord1[j] == strWord2[i]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j+1], dp[i+1][j])

    return dp[0][0]

print(edit_distance("fifsmivvlq", "fpypvzeidrssnwlxss"))
print(edit_distance("ball", "bcl"))
print(edit_distance("ab", "ab"))