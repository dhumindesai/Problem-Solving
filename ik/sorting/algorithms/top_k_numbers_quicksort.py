import random
def top_k_numbers(nums, k):

    def quickselect(start, end, i, k):

        if i > k:
            return

        # find the pivot index
        pivot_index = random.randint(start,end)

        # bring pivot to the beginning
        nums[pivot_index], nums[start] = nums[start], nums[pivot_index]

        # lamuto's partitioning
        left = pivot_index
        right = left + 1

        while right <= end:
            if nums[right] >= nums[pivot_index]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
            right += 1

        nums[start], nums[left] = nums[left], nums[start]

        k += 1



    quickselect(0, len(nums) - 1, 1, k)

    return nums[:k]

print(top_k_numbers([3, 5, 1, 8, 3, 4, 9], 7))