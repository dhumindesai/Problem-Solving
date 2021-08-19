def combinations(n, k):
    result = []

    def helper(i, slate):
        # base
        if len(slate) == k:
            result.append(slate[:])

        # recursive
        for j in range(i, n+1):
            slate.append(j)
            helper(j + 1, slate)
            slate.pop()

    helper(1, [])

    return result


print(combinations(5,3))