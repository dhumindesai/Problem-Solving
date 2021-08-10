# def number_of_ways(coins, amount):
#     table = [0 for _ in range(amount + 1)]
#
#     # base case
#     table[0] = 0
#
#     for i in range(1, len(table)):
#         for c in coins:
#             if i - c >= 0:
#                 table[i] += 1 + table[i - c]
#
#     return table[-1]

def number_of_ways(coins, amount):
    ways = [0]
    def helper(coins, target):
        if target == 0:
            ways[0] += 1
            return
        if target < 0:
            return

        for i in range(len(coins)):
            helper(coins, target - coins[i])

    helper(coins, amount)

    return ways[0]



print(number_of_ways([1,2], 4))