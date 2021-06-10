def is_palindrome(soln):
    for s in soln.split("|"):
        p1 = 0
        p2 = len(s) -1

        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
    return True


def generate_palindromic_decompositions(s):
    result = []

    def helper(s, i, slate):

        # leaf nodes
        if len(s) == i:
            soln = "".join(slate)
            if is_palindrome(soln):
                result.append(soln)
            return

        # internal nodes
        else:
            # choice-1
            slate.append("|" + s[i])
            helper(s, i + 1, slate)
            slate.pop()

            # choice-2
            slate.append(s[i])
            helper(s, i + 1, slate)
            slate.pop()


    helper(s, 1, [s[0]])
    return result

print(generate_palindromic_decompositions("abba"))
print(generate_palindromic_decompositions("a"))
# print(generate_palindromic_decompositions(""))