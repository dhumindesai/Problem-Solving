def max_product_from_cut_pieces(n):
    #
    # Write your code here.
    #
    dp = [0 for _ in range(n + 1)]

    dp[1] = 0
    dp[2] = 1

    for i in range(3, n + 1):
        for cut in range(1, i):
            dp[i] = max(dp[i], cut * (i - cut), cut * dp[i - cut])

    return dp[-1]

print(max_product_from_cut_pieces(4))

