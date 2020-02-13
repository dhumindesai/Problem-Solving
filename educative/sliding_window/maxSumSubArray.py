'''
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

'''
def max_sub_array_of_size_k(k, arr):
  winStart = 0
  winEnd = k - 1
  maxSum = 0
  winSum = 0
  for i in range(len(arr)):
    winSum += arr[i]
    if i == winEnd:
      maxSum = max(maxSum, winSum)
      winSum -= arr[winStart]
      winStart += 1
      winEnd += 1
  return maxSum

print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))