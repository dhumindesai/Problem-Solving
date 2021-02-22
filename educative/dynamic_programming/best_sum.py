def best_sum(target, arr, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    minCombination = None
    for num in arr:
        rem = target - num
        result = best_sum(rem, arr, memo)
        if result is not None:
            new_result = result + [num]
            if minCombination is None or len(new_result) < len(minCombination):
                minCombination = new_result

    memo[target] = minCombination
    return minCombination

print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(7, [2, 3]))
print(best_sum(2, [5, 3]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(100, [1, 2, 5, 25]))