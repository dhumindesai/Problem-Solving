def how_sum(target, arr, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in arr:
        rem = target - num
        result = how_sum(rem, arr, memo)
        memo[target] = result
        if result is not None:
            result.append(num)
            return result
    memo[target] = None
    return None

print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 3]))
print(how_sum(2, [5, 3]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
print(how_sum(100, [1, 2, 5, 25]))