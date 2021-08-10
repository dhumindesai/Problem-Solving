def subsets_with_duplicates_1(nums):
    subsets = [[]]
    num_freq = {}
    for num in nums:
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
        for i in range(len(subsets)):
            if is_freq_matching(subsets[i], num, num_freq[num]):
                new_set = list(subsets[i])
                new_set.append(num)
                subsets.append(new_set)
    return subsets

def is_freq_matching(current_set, num,  freq):
    counter = 0
    for n in current_set:
        if n == num:
            counter += 1
    if counter == freq-1:
        return True
    else:
        return False

#########From Educative###########

def subsets_with_duplicates_2(nums):
    result = []

    def helper(i, slate):

        # base case
        if i == len(nums):
            result.append(slate[:])
            return

        # recursive case
        count = 1

        # include
        # count number of repeated characters
        j = i
        while j < len(nums) - 1 and nums[j] == nums[j + 1]:
            count += 1
            j += 1

        for _ in range(count):
            slate.append(nums[i])
            helper(i + count, slate)

        for _ in range(count):
            slate.pop()

        # exclude
        helper(i + count, slate)

    helper(0, [])

    return result

def main():

  print("Here is the list of subsets: " + str(subsets_with_duplicates_2([1, 3, 3])))
  print("Here is the list of subsets: " + str(subsets_with_duplicates_2([1, 5, 3, 3])))
  print("Here is the list of subsets: " + str(subsets_with_duplicates_2([3,3])))


main()