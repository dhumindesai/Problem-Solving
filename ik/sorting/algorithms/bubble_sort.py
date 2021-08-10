def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

print(bubble_sort([5, 4, 3, 2, 1, 0]))
print(bubble_sort([5,2,4,1,7,0,6, 1]))