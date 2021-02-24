def trimPrefix(prefix, word):
    return word[len(prefix):]


def all_construct(targetStr, words):
    # if memo is None:
    #     memo = {}
    # if targetStr in memo:
    #     return memo[targetStr]
    if targetStr == '':
        return [[]]

    result = []

    for word in words:
        if targetStr.startswith(word):
            newStr = trimPrefix(word, targetStr)
            suffixWays = all_construct(newStr, words)
            targetWays = [[word] + way for way in suffixWays]
            result.append(sum(targetWays, []))
    # memo[targetStr] = result
    return result



print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "o", "t", "ot"]))
print(all_construct("eeeeeeeeeeeeeeeeeeeeef",
                    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeeee"]))