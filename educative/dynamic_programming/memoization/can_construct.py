def trimPrefix(prefix, word):
    return word[len(prefix):]


def can_construct(targetStr, words, memo=None):
    if memo is None:
        memo = {}
    if targetStr in memo:
        return memo[targetStr]
    if not targetStr:
        return True
    for word in words:
        if targetStr.startswith(word):
            newStr = trimPrefix(word, targetStr)
            currentResult = can_construct(newStr, words, memo)
            memo[newStr] = currentResult
            if currentResult:
                return True
    memo[word] = False
    return False

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeef",
                    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeeeef"]))