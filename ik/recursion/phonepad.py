def getWordsFromPhoneNumber(phoneNumber):
    # Write your code here
    result = []

    numpad = {"2": "abc", "3": "def",
              "4": "ghi", "5": "jkl", "6": "mno",
              "7": "pqrs", "8": "tuv", "9": "wxyz"
              }

    def helper(i, slate):

        # leaf node
        if i == 7:
            if slate:
                result.append("".join(slate))
            return

        if phoneNumber[i] in "01":
            helper(i + 1, slate)
            return

        # internal nodes
        for c in numpad[phoneNumber[i]]:
            slate.append(c)
            helper(i + 1, slate)
            slate.pop()

    helper(0, [])

    if not result:
        return ["-1"]

    return result

print(getWordsFromPhoneNumber("11001010"))