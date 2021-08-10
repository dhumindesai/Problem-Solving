def min_steps_balance(piles):
    piles.sort(reverse=True)
    result = 0
    min_height = float("inf")
    max_height = float("-inf")
    sum = 0

    for p in piles:
        min_height = min(min_height, p)
        max_height = max(max_height, p)
        sum += p

    while sum != (min_height * len(piles)):
        for i in range(len(piles)):
            if piles[i] == max_height and i < len(piles) - 1 and piles[i] > piles[i+1]:
                sum = sum - (piles[i] - piles[i+1])
                piles[i] = piles[i+1]
                result += 1
                max_height = max(piles)
                break

    return result

print(min_steps_balance([50]) == 0)
print(min_steps_balance([10, 10]) == 0)
print(min_steps_balance([5, 2, 1]) == 3)
print(min_steps_balance([4, 2, 1]) == 3)
print(min_steps_balance([4, 5, 5, 4, 2]) == 6)
print(min_steps_balance([4, 8, 16, 32]) == 6)
print(min_steps_balance([4, 8, 8]) == 2)
print(min_steps_balance([4, 4, 8, 8]) == 2)
print(min_steps_balance([1, 2, 2, 3, 3, 4]) == 9)
print(min_steps_balance([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)
print(min_steps_balance([5, 5, 5, 3, 3, 2, 2, 1]))
print(min_steps_balance([5, 5, 5, 3, 3]))
