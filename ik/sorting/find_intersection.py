def find_intersection(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
            continue

        max_n = max(arr1[p1], arr2[p2], arr3[p3])

        if arr1[p1] < max_n:
            p1 += 1
        if arr2[p2] < max_n:
            p2 += 1
        if arr3[p3] < max_n:
            p3 += 1

    if not result:
        return [-1]
    else:
        return result


print(find_intersection([2, 5, 10],[2, 3, 4, 10], [2, 4, 10]))