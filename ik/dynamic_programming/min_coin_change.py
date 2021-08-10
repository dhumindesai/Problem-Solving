def minimum_coins(coins, value):
    dp = [float('inf') for _ in range(value + 1)]
    dp[0] = 0

    for i in range(1, len(dp)):
        for c in coins:
            if i - c >= 0:
                dp[i] = 1 + min(dp[i], dp[i - c])

    return dp[-1]

print(minimum_coins([67], 9))