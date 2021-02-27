def how_construct(targetStr, words):
    dp = [[] for _ in range(len(targetStr) + 1)]
    dp[0] = [[]]
    for i in range(len(targetStr)):
        for word in words:
            if dp[i] and (i + len(word)) < len(dp) and targetStr[i:i + len(word)] == word:
                for comb in dp[i]:
                    new_comb = list(comb)
                    new_comb.append(word)
                    dp[i + len(word)].append(new_comb)
    return dp[-1]

print(how_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))
print(how_construct("dhrumin", ["d", "h", "r", "u", "m", "i", "n", "dh", "ru"]))
print(how_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(how_construct("enterapotentpot", ["a", "p", "ent", "enter", "o", "t", "ot"]))
