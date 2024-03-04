class Solution:
    def coinChange(self, coins, amount):

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}
        def dp(amount):
            if amount == 0:
                return 0

            result = []
            for coin in coins:
                if amount-coin >= 0:
                    if amount-coin not in memo:
                        memo[amount-coin] = dp(amount-coin)
                    if memo[amount-coin] != -1:
                        result.append(memo[amount-coin])

            return min(result)+1 if result else -1

        return dp(amount)