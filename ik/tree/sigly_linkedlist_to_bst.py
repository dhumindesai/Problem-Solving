from ik.tree.ds import TreeNode, SinglyLinkedListNode


def findMid(l_head):
    if not l_head or not l_head.next:
        return l_head

    fast, slow = l_head, l_head
    slow_prev = None

    while fast and fast.next:
        fast = fast.next.next
        slow_prev = slow
        slow = slow.next

    slow_prev.next = None

    return slow

def sorted_list_to_bst(head):
    """
        Args:
         head(SinglyLinkedListNode_int32)
        Returns:
         TreeNode_in32
    """

    if not head:
        return None

    def convert(l_head):
        if not l_head:
            return None
        if not l_head.next:
            return TreeNode(l_head.data)
        mid = findMid(l_head)
        root = TreeNode(mid.data)

        left_head = l_head
        right_head = mid.next
        root.left_ptr = convert(left_head)
        root.right_ptr = convert(right_head)

        mid.next = None

        return root

    return convert(head)

head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(2)
head.next.next = SinglyLinkedListNode(3)
head.next.next.next = SinglyLinkedListNode(4)
head.next.next.next.next = SinglyLinkedListNode(5)
head.next.next.next.next.next = SinglyLinkedListNode(6)
head.next.next.next.next.next.next = SinglyLinkedListNode(7)

result = sorted_list_to_bst(head)
print(result)
