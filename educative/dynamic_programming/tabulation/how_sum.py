def how_sum(target, arr):
    dp = [None] * (target+1)
    dp[0] = []

    for i in range(target):
        for num in arr:
            if dp[i] is not None and i + num <= target:
                dp[i + num] = dp[i] + [num]

    return dp[target]

print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 3]))
print(how_sum(2, [5, 3]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
print(how_sum(100, [1,2, 5, 25]))