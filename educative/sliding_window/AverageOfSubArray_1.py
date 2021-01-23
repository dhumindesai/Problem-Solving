'''
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
'''


def calculateFirstWindowSum(K, arr):
    result = 0.0
    for i in range(K):
        result += arr[i]
    return result


def findAverageOfSubArray(K, arr):
    result = []
    windowSum = calculateFirstWindowSum(K, arr)
    result.append(windowSum/K)

    winStart = 1
    winEnd = K

    while winEnd < len(arr):
        windowSum = windowSum - arr[winStart - 1] + arr[winEnd]
        result.append(windowSum/K)
        winStart += 1
        winEnd += 1

    return result

print(findAverageOfSubArray(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))



# def find_averages_of_subarrays(K, arr):
#     winSum = 0.0
#     winStart = 0
#     winEnd = K - 1
#     result = []
#     for i in range(len(arr)):
#         winSum += arr[i]
#         if i == winEnd:
#             result.append(winSum/K)
#             winSum -= arr[winStart]
#             winStart += 1
#             winEnd += 1
#     return result
#
# print(find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
# print(find_averages_of_subarrays(1, [1]))