def min_steps(num, memo=None):
    if memo is None:
        memo = {}
    if num in memo:
        return memo[num]
    if num == 1:
        return 0

    results = []
    results.append(1 + min_steps(num - 1, memo))
    if num%2 == 0:
        results.append(1 + min_steps(num / 2, memo))
    if num%3 == 0:
        results.append(1 + min_steps(num / 3, memo))
    result = min(results)
    memo[num] = result
    return result

print(min_steps(6))
print(min_steps(8))
print(min_steps(10))
print(min_steps(15))
print(min_steps(300))