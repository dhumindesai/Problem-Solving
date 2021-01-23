from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  cycle_length = find_cycle_length(head)
  p1, p2 = head, head
  p1 = move_pointer_at_cycle_len(p1, cycle_length)
  while p1 is not p2:
    p1 = p1.next
    p2 = p2.next
  return p1

def move_pointer_at_cycle_len(p, n):
  for _ in range(n):
    p = p.next
  return p

def find_cycle_length(head):
  fast, slow = head, head
  result = 1

  while fast is not None and fast.next.next is not None:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      offset = slow
      slow = slow.next
      while slow is not offset:
        result += 1
        slow = slow.next
      return result


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
