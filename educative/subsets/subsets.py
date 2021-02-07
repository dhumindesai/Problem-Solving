'''
Time : O(N*2^N)
Space : O(N*2^N)
'''
def find_subsets(nums):
  subsets = [[]]
  for num in nums:
    for i in range(len(subsets)):
      new_set = list(subsets[i])
      new_set.append(num)
      subsets.append(new_set)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
