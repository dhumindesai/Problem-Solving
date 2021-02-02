from __future__ import print_function


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


def reverse_sub_list(head, p, q):
    previous, current, next = None, head, None

    i = 1
    while i < p:
        previous = current
        current = current.next
        if current is None:
            raise Exception("p is out of bound")
        i += 1

    next = current.next
    first_node_of_sublist = current

    while i < q:
        temp = next.next
        next.next = current
        current = next
        next = temp
        i += 1

    first_node_of_sublist.next = next
    if previous is not None:
        previous.next = current
    else:
        head = current

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 3, 5)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
