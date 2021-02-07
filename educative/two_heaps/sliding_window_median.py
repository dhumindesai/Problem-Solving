'''
Time complexity #
The time complexity of our algorithm is O(N*K)O(N∗K) where ‘N’ is the total number of elements in the input array and ‘K’ is the size of the sliding window. This is due to the fact that we are going through all the ‘N’ numbers and, while doing so, we are doing two things:

Inserting/removing numbers from heaps of size ‘K’. This will take O(logK)O(logK)
Removing the element going out of the sliding window. This will take O(K)O(K) as we will be searching this element in an array of size ‘K’ (i.e., a heap).
Space complexity #
Ignoring the space needed for the output array, the space complexity will be O(K)O(K) because, at any time, we will be storing all the numbers within the sliding window.
'''

from heapq import *
import heapq


def find_sliding_window_median(nums, k):
    result = []
    max_heap, min_heap = [], []
    first, second = 0, 0

    # calculate the median for the first window
    for i in range(k):
        insert(max_heap, min_heap, nums[i])
        second += 1
    result.append(findMedian(max_heap, min_heap))

    # slide the window and calculate medians
    while second < len(nums):
        insert(max_heap, min_heap, nums[second])
        if nums[first] in min_heap:
            removeFirstElement(min_heap, nums[first])
        else:
            removeFirstElement(max_heap, -nums[first])

        rebalance_heaps(max_heap, min_heap)
        result.append(findMedian(max_heap, min_heap))
        first += 1
        second += 1

    return result


def rebalance_heaps(max_heap, min_heap):
    if len(min_heap) > len(max_heap):
        heappush(max_heap, -heappop(min_heap))
    if len(max_heap) > len(min_heap) + 2:
        heappush(min_heap, -heappop(max_heap))


def insert(max_heap, min_heap, num):
    if not max_heap or -max_heap[0] > num:
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)
    rebalance_heaps(max_heap, min_heap)


def findMedian(max_heap, min_heap):
    if len(max_heap) == len(min_heap):
        return (-max_heap[0] + min_heap[0]) / 2
    else:
        return -max_heap[0]


def removeFirstElement(heap, element):
    ind = heap.index(element)  # find the element
    # move the element to the end and delete it
    heap[ind] = heap[-1]
    del heap[-1]
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
        heapq._siftup(heap, ind)
        heapq._siftdown(heap, 0, ind)


print(find_sliding_window_median([1, 2, -1, 3, 5], 2))