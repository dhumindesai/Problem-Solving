'''
nlogn
1
'''
def solution(nums):
    if len(nums) < 2:
        return 0

    nums.sort()
    first = 0
    last = len(nums) - 1

    while first < last and nums[first] < 0 and nums[last] > 0:
        if abs(nums[first]) == nums[last]:
            return nums[last]
        if abs(nums[first]) > nums[last]:
            first += 1
        else:
            last -= 1

    return 0

'''
O(n)
O(n)
'''
def solution_2(nums):
    if len(nums) < 2:
        return 0
    seen = set()
    for num in nums:
        seen.add(num)

    result = 0
    for num in nums:
        if num < 0 and abs(num) in seen:
            result = max(result, abs(num))
        if num > 0 and -num in seen:
            result = max(result, num)

    return result

print(solution([3, 2, -2, 5, -3]))
print(solution([1, 2, 3, -4]))
print(solution([100, 100, -100, -2, -2, 2, 1, -1]))
print()
print(solution_2([3, 2, -2, 5, -3]))
print(solution_2([1, 2, 3, -4]))
print(solution_2([100, 100, -100, -2, -2, 2, 1, -1]))