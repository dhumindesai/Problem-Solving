def longestOnes(nums, k):
    zeros = 0
    start, end = 0, 0
    max_so_far = 0

    while end < len(nums):
        if nums[end] == 0:
            zeros += 1

        if zeros <= k:
            end +=1
            max_so_far = max(max_so_far, end - start)
            continue


        if nums[start] == 0:
            zeros -= 1

        start += 1
        end += 1

    return max_so_far

print(longestOnes([0,1,1,0,0], 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(longestOnes([0,0,0,1], 3))
