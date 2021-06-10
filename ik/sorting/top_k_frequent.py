from heapq import *


def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []
    freq = {}
    for n in arr:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    min_heap = []
    for num, count in freq.items():
        if len(min_heap) < k:
            heappush(min_heap, (count, num))
        else:
            if min_heap[0][0] < count:
                heappop(min_heap)
                heappush(min_heap, (count, num))

    while min_heap:
        result.append(heappop(min_heap)[1])

    return result

print(find_top_k_frequent_elements([1, 2, 3, 2, 4, 3, 1,3, 4,4,4,4],2))


def find_top_k_frequent_elements_with_countsort(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    freq = {}

    for n in arr:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    group = [[] for _ in range(len(arr) + 1)]

    for num, count in freq.items():
        group[count].append(num)

    result = []
    i = len(group) - 1
    while i >= 0:
        for num in group[i]:
            if len(result) < k:
                result.append(num)
            else:
                break
        i -= 1

    return result

print(find_top_k_frequent_elements_with_countsort([6, 1, 2 ,1, 2, 3,1],2))