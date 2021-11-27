def subarraySum(nums, k):
    prefix_sum = 0
    prefix_sum_freq = {0: 1}
    result = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum - k in prefix_sum_freq:
            result += prefix_sum_freq[prefix_sum - k]

        if prefix_sum in prefix_sum_freq:
            prefix_sum_freq[prefix_sum] += 1
        else:
            prefix_sum_freq[prefix_sum] = 1

    return result

print(subarraySum([1,1,1], 2))