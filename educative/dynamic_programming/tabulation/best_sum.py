def best_sum(target, arr):
    dp = [None] * (target+1)
    dp[0] = []

    for i in range(target):
        for num in arr:
            if dp[i] is not None and i + num <= target:
                combination = dp[i] + [num]
                if dp[i + num] is None or len(dp[i + num]) > len(combination):
                    dp[i + num] = combination

    return dp[target]

print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(7, [2, 3]))
print(best_sum(2, [5, 3]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(100, [1, 2, 5, 25]))