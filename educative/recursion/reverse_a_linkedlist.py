class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseHelper(current, next, head):
    if not next:
        head.next = None
        head = current
        return head
    temp = next.next
    next.next = current
    return reverseHelper(next, temp, head)


def reverse(head):
    return reverseHelper(head, head.next, head)

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    printList(head)

    printList(reverse(head))


def printList(head):
    node = head
    while node:
        print(node.value, end=" ")
        node = node.next
    print()

main()