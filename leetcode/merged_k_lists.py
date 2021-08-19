class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from heapq import *


class Solution(object):
    def mergeKLists(self, lists):
        min_heap = []
        k = len(lists)

        for i in range(k):
            heappush(min_heap, (lists[i].val, lists[i]))

        result_head = None
        result_tail = None

        while min_heap:
            next_node = heappop(min_heap)[1]
            print(next_node.val)
            if not result_head:
                result_head = next_node
                result_tail = next_node
            else:
                result_tail.next = next_node

            if next_node.next:
                heappush(min_heap, (next_node.next.val, next_node.next))

        return result_head

l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

s = Solution()
s.mergeKLists([l1,l2,l3])