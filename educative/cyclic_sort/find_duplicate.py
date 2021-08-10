def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    for i in range(len(nums)):
        while nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] == nums[j]:
                return nums[i]
            else:
                nums[i], nums[j] = nums[j], nums[i]

    return -1

print(findDuplicate([1,3,4,2,2]))
print(findDuplicate([2,2,2,2]))
print(findDuplicate([1, 3, 4, 2, 1]))
print(findDuplicate([1,4,3,4,4]))