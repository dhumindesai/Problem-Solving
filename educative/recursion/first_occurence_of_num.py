def firstIndex(arr, testVariable, currentIndex) :
    if currentIndex == len(arr):
        return -1
    if arr[currentIndex] == testVariable:
        return currentIndex
    return firstIndex(arr, testVariable, currentIndex + 1)

print(firstIndex([9, 8, 1, 8, 1, 7], 21, 0))