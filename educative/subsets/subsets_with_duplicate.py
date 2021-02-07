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
    # sort the numbers to handle duplicates
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        # if current and the previous elements are same, create new subsets only from the subsets
        # added in the previous step
        if i > 0 and nums[i] == nums[i - 1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex+1):
            # create a new subset from the existing subset and add the current element to it
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets
def main():

  print("Here is the list of subsets: " + str(subsets_with_duplicates_2([1, 3, 3])))
  print("Here is the list of subsets: " + str(subsets_with_duplicates_2([1, 5, 3, 3])))
  print("Here is the list of subsets: " + str(subsets_with_duplicates_2([3,3])))


main()