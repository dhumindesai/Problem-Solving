def smallest_subarray_with_given_sum(s, arr):
    if not arr:
        return 0
    winStart = winEnd = 0
    minLen = float('inf')
    winSum = 0

    while winEnd < len(arr):
        if winSum < s:
            winSum += arr[winEnd]
        if winSum >= s:
            print(winStart, winEnd, winSum)
            minLen = min(minLen, winEnd - winStart + 1)
            winSum -= arr[winStart]
            winStart += 1
        if winSum < s:
            winEnd += 1

    return minLen

#print(smallest_subarray_with_given_sum(7, [2,1,5,2,3,2]))
print(smallest_subarray_with_given_sum(7, [2,1,5,2,8]))