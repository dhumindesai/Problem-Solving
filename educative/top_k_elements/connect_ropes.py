'''
Time O(Nlogn)
Space O(N)
'''
from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    result = 0
    minHeap = []

    for num in ropeLengths:  # nlogn
        heappush(minHeap, num)

    while len(minHeap) > 1:
        temp = heappop(minHeap) + heappop(minHeap)  # nlogn
        heappush(minHeap, temp)  # nlogn
        result += temp

    return result


def main():
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 2, 1, 4, 2])))


main()

