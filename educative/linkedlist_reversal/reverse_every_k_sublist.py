#######NOT COMPLETED#######

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


def reverse_every_k_elements(head, k):
    current, next = head, head.next
    last_node_of_prev_list = None

    while current != None:
        first_node_of_current_list = current
        for _ in range(k - 1):
            if next is None:
                break
            temp = next.next
            next.next = current
            current = next
            next = temp

        # Link last node of previous list
        if last_node_of_prev_list is None:
            head = current
        else:
            last_node_of_prev_list.next = current

        # Link last node of current list
        first_node_of_current_list.next = next

        # go forward

        last_node_of_prev_list = current
        current = next
        if next is not None:
            next = next.next

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()







