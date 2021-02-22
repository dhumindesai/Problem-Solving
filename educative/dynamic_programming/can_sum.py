def can_sum(target, arr, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in arr:
        rem = target - num
        result = can_sum(rem, arr, memo)
        if result:
            memo[target] = True
            return True

    memo[target] = False
    return False

print(can_sum(10, [5, 3, 4, 7, 2]))
print(can_sum(300, [7, 14]))