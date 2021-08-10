class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def middleNode(head):
    if not head:
        return None

    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Middle Node: " + str(middleNode(head).value))

head.next.next.next.next.next = Node(6)
print("Middle Node: " + str(middleNode(head).value))

head.next.next.next.next.next.next = Node(7)
print("Middle Node: " + str(middleNode(head).value))