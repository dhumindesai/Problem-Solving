import random


def quick_sort(nums):
    # Quick-sort using Lomuto's partitionig
    def helper(nums, start, end):
        if start >= end:
            return

        #Choose pivot
        pivotIndex = random.randint(start, end)

        # partitioning
        nums[pivotIndex], nums[start] = nums[start], nums[pivotIndex]

        p1 = start

        for p2 in range(start + 1, end + 1):
            if nums[start] > nums[p2]:
                p1 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]

        nums[start], nums[p1] = nums[p1], nums[start]

        # recursive calls
        helper(nums, start, p1 - 1)
        helper(nums, p1 + 1, end)

    helper(nums, 0, len(nums) - 1)
    return nums

print(quick_sort([5,2,3,1]))
print(quick_sort([0,1,2,3]))