
def letter_case_permutations(s):
    result = []
    def helper(s, i, slate):
        #Leaf nodes
        if i == len(s):
            result.append("".join(slate))
            return
        #Internal nodes
        if s[i].isdigit():
            slate.append(s[i])
            helper(s, i+1, slate)
            slate.pop()
        else:
            slate.append(s[i].upper())
            helper(s, i+1, slate)
            slate.pop()
            slate.append(s[i].lower())
            helper(s, i+1, slate)
            slate.pop()

    helper(s, 0, [])
    return result

print(letter_case_permutations("111"))
print(letter_case_permutations("a1z"))
print(letter_case_permutations("a1b2"))