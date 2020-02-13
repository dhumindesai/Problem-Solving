'''
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
'''

def find_averages_of_subarrays(K, arr):
    winSum = 0.0
    winStart = 0
    winEnd = K - 1
    result = []
    for i in range(len(arr)):
        winSum += arr[i]
        if i == winEnd:
            result.append(winSum/K)
            winSum -= arr[winStart]
            winStart += 1
            winEnd += 1
    return result

print(find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
print(find_averages_of_subarrays(1, [1]))
