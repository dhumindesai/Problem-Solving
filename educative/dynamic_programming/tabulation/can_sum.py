def can_sum(target, arr):
    dp = [False for _ in range(target + 1)]
    dp[0] = True

    for i in range(target):
        for num in arr:
            if dp[i] and i + num <= target:
                dp[i + num] = True
    print(dp)
    return dp[target]

print(can_sum(7, [3, 4, 5]))
print(can_sum(10, [5, 3, 4, 7, 2]))
print(can_sum(300, [7, 14]))