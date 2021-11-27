def count_possible_dial_nums_rec(n):
    result = [0]
    neighbors = {
        0: [4,6],
        1: [8,6],
        2: [7,9],
        3: [8,4],
        4: [3,9,0],
        5: [],
        6: [0,1,7],
        7: [2,6],
        8: [1,3],
        9: [2,4]
    }

    def helper(i, num):

        # base
        if i == n -1 :
            result[0] += 1
            return

        #recursive
        for neighbor in neighbors[num]:
            helper(i + 1, neighbor)

    for num in range(10):
        helper(0, num)

    return result[0]

print(count_possible_dial_nums_rec(3))

def count_possible_dial_nums_dp(n):
    neighbors = {
        0: [4,6],
        1: [8,6],
        2: [7,9],
        3: [8,4],
        4: [3,9,0],
        5: [],
        6: [0,1,7],
        7: [2,6],
        8: [1,3],
        9: [2,4]
    }

    dp = [[0 for _ in range(10)] for _ in range(2)]

    #init the first row with 1
    for j in range(10):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(10):
            dp[i%2][j] = 0
            for nbr in neighbors[j]:
                dp[i%2][j] += dp[(i-1)%2][nbr]

    return sum(dp[(n-1)%2])


print(count_possible_dial_nums_dp(4))