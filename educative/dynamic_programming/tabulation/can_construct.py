def can_construct(targetStr, words):
    dp = [False] * (len(targetStr) + 1)
    dp[0] = True

    for i in range(len(targetStr)):
        for word in words:
            if dp[i] and targetStr[i:i+len(word)] == word:
                dp[i+len(word)] = True

    return dp[-1]

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeef",
                    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeeeef"]))