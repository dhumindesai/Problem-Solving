# def find_missing_number(nums):
#   l = len(nums)
#   expected_total = (l-1)*(l) // 2
#   total = 0
#   for n in nums:
#     if n != l:
#       total += n
#   return expected_total - total

def find_missing_number(nums):
    for i in range(len(nums)):
        while nums[i] != i and nums[i] != len(nums):
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]

    for i in range(len(nums)):
        if nums[i] != i:
            return i

print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number([4, 0, 3, 1]))