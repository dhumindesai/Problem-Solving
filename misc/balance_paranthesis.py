def balanced(s):
    count = 0
    for c in s:
        if count < 0:
            return False
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
    return count == 0

print(balanced(")("))