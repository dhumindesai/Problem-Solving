def merge(string1, string2) :

    if not string1:
        return string2

    if not string2:
        return string1

    if string1[0] <= string2[0]:
        return string1[0] + merge(string1[1:], string2)
    else:
        return string2[0] + merge(string1, string2[1:])


print(merge("acu", "bst"))