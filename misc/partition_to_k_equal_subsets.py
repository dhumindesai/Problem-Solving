def canPartitionKSubsets(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    sum = 0
    for num in nums:
        sum += num

    if sum % k != 0:
        return False

    def helper(i, target_sum, current_sum, slate):
        # base
        if target_sum == current_sum:
            counter[0] += 1
            for i in slate:
                visited.add(i)
            print(slate)
            return True
        if i == len(nums):
            return False

        # internal
        if i not in visited:
            slate.append(i)
            helper(i + 1, target_sum, current_sum + nums[i], slate)  # include
            slate.pop()

        helper(i + 1, target_sum, current_sum, slate)  # exclude


    counter = [0]
    visited = set()
    helper(0, sum // k, 0, [])

    if counter[0] == k:
        return True
    else:
        return False

#print(canPartitionKSubsets([4,3,2,3,5,2,1], 4))
# print(canPartitionKSubsets([1,2,3,4], 3))
print(canPartitionKSubsets([1,1,1,1,2,2,2,2], 2))