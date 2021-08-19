def addTwoNumbers(l1, l2):
    carry_over = 0
    result_head = None

    val_1 = l1.val
    val_2 = l2.val
    while l1 or l2:
        new_val = val_1 + val_2 + carry_over
        carry_over = new_val // 10

        l3 = ListNode(new_val % 10)
        if not result_head:
            result_head = l3
        else:
            result_head.next = l3

        l1 = l1.next
        l2 = l2.next

        if not l1:
            val_1 = 0
        else:
            val_1 = l1.val

        if not l2:
            val_2 = 0
        else:
            val_2 = l2.val

    return result_head