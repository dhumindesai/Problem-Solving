def two_sum(numbers, target):
    freq = {}
    i = 0
    while i < len(numbers):
        diff = target - numbers[i]
        if diff in freq:
            return [i, freq[diff]]
        freq[numbers[i]] = i
        i += 1
    return [-1, -1]


def pair_sum_sorted_array(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        sum = numbers[p1] + numbers[p2]
        if sum < target:
            p1 += 1
        elif sum > target:
            p2 -= 1
        else:
            return [p1, p2]

    return [-1, -1]

# print(two_sum([4, 1, 5, 0, -1], 10))
print(pair_sum_sorted_array([1, 2, 3, 5, 10], 7))