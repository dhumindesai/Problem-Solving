def trimPrefix(prefix, word):
    return word[len(prefix):]


def count_construct(targetStr, words, memo=None):
    if memo is None:
        memo = {}
    if targetStr in memo:
        return memo[targetStr]
    if not targetStr:
        return 1

    result = 0
    for word in words:
        if targetStr.startswith(word):
            newStr = trimPrefix(word, targetStr)
            result += count_construct(newStr, words, memo)

    memo[targetStr] = result
    return result

print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "o", "t", "ot"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeef",
                      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeeee"]))