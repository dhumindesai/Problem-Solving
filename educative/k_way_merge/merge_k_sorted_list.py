from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


'''
T = O(N*logN)
S = O(1)
'''
def merge_lists_brutforce(lists):
    resultHead = None
    minHeap = []

    for l in lists:
        currentNode = l
        while currentNode:
            heappush(minHeap, currentNode.value)
            currentNode = currentNode.next

    resultHead = ListNode(heappop(minHeap))
    currentNode = resultHead
    while minHeap:
        currentNode.next = ListNode(heappop(minHeap))
        currentNode = currentNode.next
    return resultHead


'''
T- O(N∗logK)
S- O(K)
'''
def merge_lists(lists):
    resultHead = None
    minHeap = []

    for i in range(len(lists)):
        if lists[i]:
            heappush(minHeap, lists[i])

    lastNode, resultHead = None, None

    while minHeap:
        node = heappop(minHeap)
        if not lastNode:
            resultHead = node
            lastNode = resultHead
        else:
            lastNode.next = node
            lastNode = lastNode.next
        if node.next:
            heappush(minHeap, node.next)

    return resultHead

def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


main()

