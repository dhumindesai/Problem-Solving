


# def maxLength(arr):
#     def is_unique(s):
#         if len(s) < 2:
#             return True
#         s = sorted(s)
#         p1 = 0
#         p2 = 1
#
#         while p2 < len(s):
#             if s[p1] == s[p2]:
#                 return False
#             p1 += 1
#             p2 += 1
#         return True
#
#     dp = ["" for _ in range(len(arr))]
#     dp[-1] = arr[-1] if is_unique(arr[-1]) else ""
#
#     for i in range(len(arr) - 2, -1, -1):
#         if is_unique(arr[i]) and len(arr[i]) > len(dp[i+1]):
#             dp[i] = arr[i]
#             continue
#
#         dp[i] = arr[i] + dp[i+1] if is_unique(arr[i] + dp[i+1]) else dp[i+1]
#
#     return len(dp[0])



# print(maxLength(["un","iq","ue"]))
# print(maxLength(["cha","r","act","ers"]))
# print(maxLength(["abcdefghijklmnopqrstuvwxyz"]))
# print(maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))
# print(maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]))
def maxLength(arr):

    def is_unique(s):
        if len(s) < 2:
            return True
        s = sorted(s)
        p1 = 0
        p2 = 1

        while p2 < len(s):
            if s[p1] == s[p2]:
                return False
            p1 += 1
            p2 += 1

        return True

    def helper(i):
        #leaf node
        if i == len(arr):
            return ""
        if not is_unique(arr[i]):
            return ""

        #internal nodes
        result = arr[i]
        for j in range(i + 1, len(arr)):
            temp1 = arr[i] + arr[j]
            temp2 = arr[i] + helper(j)
            if is_unique(temp1) and len(temp1) > len(result):
                result = temp1
            if is_unique(temp2)and len(temp2) > len(result):
                result = temp2
            if is_unique(arr[j]) and len(arr[j]) > len(result):
                result = arr[j]

        return result

    return helper(0)




print(maxLength(["un","iq","ue"]))
print(maxLength(["cha","r","act","ers"]))
print(maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))
print(maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]))
print(maxLength(["a", "abc", "d", "de", "def"]))


