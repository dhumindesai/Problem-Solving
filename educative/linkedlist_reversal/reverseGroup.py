class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()
def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """

    if k < 2:
        return head

    size = 0
    node = head
    while node:
        size += 1
        node =node.next

    left_link = None

    prev = None
    current = head

    i = 1

    while i <= (size // k):
        current_count = 1
        left = current
        while current and current_count <= k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            current_count += 1

        if left_link:
            left_link.next = prev
        else:
            head = prev
        left.next = current
        left_link =left
        i += 1

    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
# head.next.next.next.next.next.next.next.next = Node(9)

reverseKGroup(head, 3).print_list()
