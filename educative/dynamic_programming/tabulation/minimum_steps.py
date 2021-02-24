import math
def min_steps(num):
    dp = [float(math.inf) for _ in range(num+1)]
    dp[0], dp[1] = 0, 0

    for i in range(1, num):
        dp[i+1] = min(dp[i+1], dp[i] + 1)
        if i*2 <= num:
            dp[i*2] = min(dp[i*2], dp[i] + 1)
        if i*3 <= num:
            dp[i*3] = min(dp[i*3], dp[i] + 1)

    return dp[num]

print(min_steps(6))
print(min_steps(8))
print(min_steps(10))
print(min_steps(15))
print(min_steps(300))