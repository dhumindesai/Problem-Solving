def get_subsets_with_duplicates(s):
    result = []

    def helper(s, i, slate):

        # For leaf nodes
        if i == len(s):
            result.append("".join(slate))
            return

        # For internal  nodes
        else:
            counter = 1
            while i < len(s) - 1 and s[i] == s[i+1]:
                counter += 1
            for _ in range(0, counter):
                slate.append(s[i])
                helper(s, i + 1, slate)
                slate.pop()
                helper(s, i + 1, slate)

    helper(s, 0, [])
    return result

print(get_subsets_with_duplicates("abc"))
print(get_subsets_with_duplicates("aaa"))