def generate_palindromic_decompositions(string):
    if not string or len(string) == 1:
        return [string]

    output = []
    n = len(string)

    def _palindromic_decomposition(so_far, start):
        # base case
        if start == n:
            output.append('|'.join(so_far))
            return

        # take every possible string from the current position and
        # if it's palndromic go forward, and if it's not prune
        for i in range(start+1, n+1):
            curr = string[start:i]
            if is_palindrome(curr):
                so_far.append(curr)
                _palindromic_decomposition(so_far, i)
                # at the end of dfs remove what was appended to
                so_far.pop()

    _palindromic_decomposition([], 0)
    return output


def is_palindrome(string):
    if not string or len(string) == 1:
        return True

    low, high = 0, len(string) - 1
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1

    return True

print(generate_palindromic_decompositions("abba"))
print(generate_palindromic_decompositions("a"))
print(generate_palindromic_decompositions(""))