def jobScheduling(startTime, endTime, profit):

    dp = [0 for _ in range(max(endTime) + 1)]



    for i in endTime:
        dp[i] = profit[i] + dp[i - startTime[i]]

    return max(dp)

print(jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))

