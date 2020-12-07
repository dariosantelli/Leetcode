def climbStairs(self, n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 2

    for i in range(n - 2):
        dp[i + 2] = dp[i + 1] + dp[i]

    return dp[n - 1]