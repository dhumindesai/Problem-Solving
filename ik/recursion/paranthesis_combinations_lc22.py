def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []

    def helper(slate, open, close):
        # Backtrack
        if open > close:
            return

        # base
        if open == 0 and close == 0:
            result.append("".join(slate[:]))

        # recursive
        if open > 0:
            slate.append("(")
            helper(slate, open - 1, close)
            slate.pop()

        slate.append(")")
        helper(slate, open, close - 1)
        slate.pop()

    helper([], n, n)

    return result

print(generateParenthesis(3))
print(generateParenthesis(2))