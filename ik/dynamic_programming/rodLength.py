# def get_maximum_profit(price):
#     rodLen = len(price)
#     maxProfit = [0]
#
#     def helper(prices, rodLen, total):
#         # Base
#         if rodLen == 0:
#             maxProfit[0] = max(maxProfit[0], total)
#             return
#
#         if rodLen < 0:
#             return
#
#         # Recursive
#         for i in range(len(prices)):
#             helper(prices, rodLen - i -1, total + prices[i])
#            # helper(prices[:i] + prices[i + 1:], rodLen, total)
#
#     helper(price, rodLen, 0)
#     return maxProfit[0]

def get_maximum_profit(price):
    dp = [ 0 for _ in range(len(price) + 1)]

    #base
    dp[1] = price[0]

    for i in range(2, len(dp)):
        dp[i] = price[i-1]
        for rodLen in range(i):
            dp[i] = max(dp[i], dp[i-rodLen] + dp[rodLen])

    return dp[-1]

print(get_maximum_profit([1,5,8,9]))
print(get_maximum_profit([1, 1, 9, 3, 8, 9, 11]))