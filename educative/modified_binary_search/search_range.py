def search_range(nums, target):
    result = [-1, -1]

    left = 0
    right = len(nums) - 1
    mid = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = [mid, mid]
            break
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    left_start, left_end = 0, mid - 1
    while left_start <= left_end:
        left_mid = (left_start + left_end) // 2
        if nums[left_mid] == target and left_mid < result[0]:
            result[0] = left_mid
            left_end = left_mid - 1
            continue
        elif target > nums[left_mid]:
            left_start = left_mid + 1
        else:
            left_end = left_mid - 1

    right_start, right_end = mid + 1, len(nums) - 1
    while right_start <= right_end:
        right_mid = (right_start + right_end) // 2
        if nums[right_mid] == target and right_mid > result[1]:
            result[1] = right_mid
            right_start = right_mid + 1
            continue
        elif target > nums[right_mid]:
            right_start = right_mid + 1
        else:
            right_end = right_mid - 1

    return result

# print(search_range([5,7,7,8,8,10], 8))
# print(search_range([1,2,2], 2))
print(search_range([1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8], 8))
