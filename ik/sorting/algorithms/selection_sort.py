def selection_sort(arr):

    for i in range(len(arr)):
        min_ele_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ele_index]:
                min_ele_index = j
        arr[i], arr[min_ele_index] = arr[min_ele_index], arr[i]

    return arr


print(selection_sort([5,2,4,1,7,0,6, 1]))
