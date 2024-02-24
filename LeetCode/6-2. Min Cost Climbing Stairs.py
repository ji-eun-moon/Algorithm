# https://leetcode.com/problems/min-cost-climbing-stairs/description/\

class Solution:
    def minCostClimbingStairs(self, cost):

        n = len(cost)
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]

class Solution:
    def minCostClimbingStairs(self, cost):

        # memo 초기화
        n = len(cost)
        memo = [-1] * (n + 1)
        def dp(n):
            # base case
            if n == 0 or n == 1:
                return 0
            # 아직 경우의 수가 정해지지 않은 경우
            if memo[n] == -1:
                # 재귀 호출
                memo[n] = min(dp(n - 1) + cost[n-1], dp(n-2) + cost[n-2])
            # 현재 계단에 도달하는 총 경우의 수 반환
            return memo[n]

        return dp(n)

solve = Solution()
print(solve.minCostClimbingStairs(cost = [10,15,20]))
print(solve.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))