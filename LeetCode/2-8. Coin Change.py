# https://leetcode.com/problems/coin-change/description/

# DP
class Solution:
    def coinChange(self, coins, amount):

        coins.sort()
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


solve = Solution()
print(solve.coinChange(coins = [1,2,5], amount = 11))
print(solve.coinChange(coins = [2], amount = 3))
print(solve.coinChange(coins = [1], amount = 0))