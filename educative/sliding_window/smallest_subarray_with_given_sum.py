# def smallest_subarray_with_given_sum(s, arr):
#     if not arr:
#         return 0
#     winStart = winEnd = 0
#     minLen = float('inf')
#     winSum = 0
#
#     while winEnd < len(arr):
#         if winSum < s:
#             winSum += arr[winEnd]
#         if winSum >= s:
#             print(winStart, winEnd, winSum)
#             minLen = min(minLen, winEnd - winStart + 1)
#             winSum -= arr[winStart]
#             winStart += 1
#         if winSum < s:
#             winEnd += 1
#
#     return minLen
#
# #print(smallest_subarray_with_given_sum(7, [2,1,5,2,3,2]))
# print(smallest_subarray_with_given_sum(7, [2,1,5,2,8]))

'''
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
'''
import math


def smallest_subarray_with_given_sum(s, arr):
    minWinSize = math.inf
    winStart, winEnd = 0, 0
    currentWinSum = arr[0]

    while winEnd < len(arr):
        if currentWinSum >= s:
            minWinSize = min(minWinSize, winEnd - winStart + 1)
            currentWinSum -= arr[winStart]
            winStart += 1
        else:
            winEnd += 1
            if winEnd < len(arr):
                currentWinSum += arr[winEnd]
    if minWinSize == math.inf:
        return 0
    return minWinSize

print(smallest_subarray_with_given_sum(7, [2,1,5,2,3,2]))
print(smallest_subarray_with_given_sum(7, [2,1,5,2,8]))
