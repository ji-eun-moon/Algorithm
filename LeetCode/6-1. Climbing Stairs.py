# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n):

        # memo 초기화
        memo = [-1]*(n+1)
        def dp(n):
            # base case
            if n == 0 or n == 1:
                return 1
            # 아직 경우의 수가 정해지지 않은 경우
            if memo[n] == -1:
                # 재귀 호출
                memo[n] = dp(n-1) + dp(n-2)
            # 현재 계단에 도달하는 총 경우의 수 반환
            return memo[n]

        return dp(n)

class Solution:
    def climbStairs(self, n):

        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


solve = Solution()
print(solve.climbStairs(n = 2))
print(solve.climbStairs(n = 3))