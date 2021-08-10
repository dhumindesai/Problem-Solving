class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def print_list(self):
      temp = self
      while temp is not None:
          print(str(temp.val) + " ", end='')
          temp = temp.next
      print()

def reorderList(head):
    # find the middle
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    middle = slow

    # reverse the second half
    prev = None
    current = middle

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    second_half_current = prev
    first_half_current = head

    while second_half_current:
        temp_1 = first_half_current.next
        temp_2 = second_half_current.next

        first_half_current.next = second_half_current
        second_half_current.next = temp_1

        first_half_current = temp_1
        second_half_current = temp_2

    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(reorderList(head).print_list())