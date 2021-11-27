def no_ways(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = no_ways(n-1, memo) + no_ways(n-2, memo)
    memo[n] = result
    return result

print(no_ways(10))

