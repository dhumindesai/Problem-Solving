def insertAtBottom(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = stack.pop()
    insertAtBottom(stack, item)
    stack.append(temp)

def reverse(stack):
    if not stack:
        return

    temp = stack.pop()
    reverse(stack)
    insertAtBottom(stack, temp)

def main():
    stack = [1, 2, 3, 4, 5]

    print(stack)
    reverse(stack)
    print(stack)

main()