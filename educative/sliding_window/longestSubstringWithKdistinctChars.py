def updateFrequencyCounter(freq, c):
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1


def decreaseFrequencyOfChar(freq, c):
    if freq[c] > 1:
        freq[c] -= 1
    else:
        freq.pop(c)

def longest_substring_with_k_distinct_chars(inp_str, k):

    winStart, winEnd = 0, 0
    result = 1
    freq = {}

    for winEnd in range(len(inp_str)):
        updateFrequencyCounter(freq, inp_str[winEnd])
        while len(freq) > k:
            decreaseFrequencyOfChar(freq, inp_str[winStart])
            winStart += 1
        result = max(result, winEnd - winStart + 1)
    return result

print(longest_substring_with_k_distinct_chars("araaci", 2))
print(longest_substring_with_k_distinct_chars("araaci", 1))
print(longest_substring_with_k_distinct_chars("cbbebi", 3))


