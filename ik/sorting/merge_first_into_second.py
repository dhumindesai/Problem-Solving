def merger_first_into_second(arr1, arr2):
    #
    # Write your code here.
    #
    p1, p2 = len(arr1) - 1, len(arr1) - 1
    p3 = len(arr2) - 1

    while p3 >= 0:
        if p1 < 0:
            break
        if p2 < 0:
            while p1 >= 0:
                arr2[p3] = arr1[p1]
                p1 -= 1
                p3 -= 1
        elif arr1[p1] >= arr2[p2]:
            arr2[p3] = arr1[p1]
            p1 -= 1
            p3 -= 1
        else:
            arr2[p3], arr2[p2] = arr2[p2], arr2[p3]
            p2 -= 1
            p3 -= 1

arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 0, 0, 0]
merger_first_into_second(arr1, arr2)
print(arr2)