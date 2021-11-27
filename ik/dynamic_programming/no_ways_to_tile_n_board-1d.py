#recursive
def no_ways(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    result = no_ways(n-1) + no_ways(n-2) + no_ways(n-3)
    memo[n] = result
    return result

print(no_ways(4))