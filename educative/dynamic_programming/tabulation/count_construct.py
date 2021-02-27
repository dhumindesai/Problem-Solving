def count_construct(targetStr, words, memo=None):
    dp = [0] * (len(targetStr) + 1)
    dp[0] = 1

    for i in range(len(targetStr)):
        for word in words:
            if dp[i] > 0 and (i + len(word)) < len(dp) and targetStr[i:i + len(word)] == word:
                dp[i + len(word)] += dp[i]

    return dp[-1]

print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "o", "t", "ot"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeef",
                      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeeee"]))