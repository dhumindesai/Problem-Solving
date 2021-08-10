import random


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    targetIndex = len(nums) - k
    result = [None]

    def quick_select(nums, start, end):
        # choose pivot
        pivotIndex = random.randint(start, end)

        # Partitioning
        nums[pivotIndex], nums[start] = nums[start], nums[pivotIndex]

        p1 = start

        for p2 in range(start + 1, end + 1):
            if nums[p2] < nums[start]:
                p1 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]

        nums[start], nums[p1] = nums[p1], nums[start]

        # recursive call
        if p1 == targetIndex:
            result[0] = nums[p1]
            return
        elif p1 > targetIndex:
            quick_select(nums, start, p1 - 1)
        else:
            quick_select(nums, p1 + 1, end)

    quick_select(nums, 0, len(nums) - 1)

    return result[0]

print(findKthLargest([3, 2, 1, 5, 6, 4], 2))