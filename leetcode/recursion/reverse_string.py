def reverseStringHelper(s, start, end):
    if start >= end:
        return
    s[start], s[end] = s[end], s[start]
    reverseStringHelper(s, start + 1, end - 1)


def reverseString(s):
    n = len(s)
    reverseStringHelper(s, 0, n - 1)


s = ['h', 'e', 'l', 'l', 'o']

reverseString(s)

print(s)