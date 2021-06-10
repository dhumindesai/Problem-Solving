from heapq import *


def kth_largest(k, initial_stream, append_stream):
    result = []
    min_heap = []

    for n in initial_stream:
        heappush(min_heap, n)
        if len(min_heap) > k:
            heappop(min_heap)

    for n in append_stream:
        heappush(min_heap, n)
        if len(min_heap) > k:
            heappop(min_heap)
        result.append(min_heap[0])

    return result

print(kth_largest(2, [4, 6], [5, 2, 20]))