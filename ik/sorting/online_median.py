from heapq import *


def online_median(stream):
    result = []
    min_heap = []
    max_heap = []

    if len(stream) <= 1:
        return stream

    result.append(stream[0])
    if stream[0] <= stream[1]:
        heappush(max_heap, -stream[0])
        heappush(min_heap, stream[1])
    else:
        heappush(max_heap, -stream[1])
        heappush(min_heap, stream[0])
    result.append((stream[0] + stream[1]) // 2)

    for i in range(2, len(stream)):
        if stream[i] > -max_heap[0]:
            heappush(min_heap, stream[i])
        else:
            heappush(max_heap, -stream[i])

        # Balance
        if (len(max_heap) > len(min_heap) + 1):
            heappush(min_heap, -heappop(max_heap))
        if (len(min_heap) > len(max_heap)):
            heappush(max_heap, -heappop(min_heap))

        if ((len(min_heap) + len(max_heap)) % 2 == 0):
            result.append((min_heap[0] + (-max_heap[0])) // 2)
        else:
            result.append(-max_heap[0])

    return result

print(online_median([3, 8, 5, 2]))
print(online_median([1, 1, 1, 1, 1]))