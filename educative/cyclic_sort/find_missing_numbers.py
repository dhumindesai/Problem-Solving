def find_missing_numbers(nums):
    missingNumbers = []

    for i in range(len(nums)):
        while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            missingNumbers.append(i+1)
    return missingNumbers

print(find_missing_numbers([2, 4, 1, 2]))