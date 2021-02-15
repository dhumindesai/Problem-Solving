def gcd_iterative(n1, n2):
    while True:
        if n1 == n2:
            return n1
        if n1 < n2:
            n2 = n2 - n1
        else:
            n1 = n1 - n2
    return 0

def gcd_recursive(n1, n2):
    if n1 == n2:
        return n1
    if n1 < n2:
        return gcd_recursive(n1, n2 - n1)
    else:
        return gcd_recursive(n1 - n2, n2)

print(gcd_iterative(12, 21))
print(gcd_recursive(12, 21))