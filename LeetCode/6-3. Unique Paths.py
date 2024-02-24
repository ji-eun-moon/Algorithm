# https://leetcode.com/problems/unique-paths/description/

# Top down
class Solution:
    def uniquePaths(self, m, n):

        memo = [[-1] * n for _ in range(m)]

        def dp(y, x):
            if y == 0 or x == 0:
                memo[y][x] = 1
            elif memo[y][x] == -1:
                memo[y][x] = dp(y-1, x) + dp(y, x-1)
            return memo[y][x]

        return dp(m-1, n-1)

# Bottom up
class Solution:
    def uniquePaths(self, m, n):

        dp = [[1] * n for _ in range(m)]

        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

        return dp[m-1][n-1]

solve = Solution()
print(solve.uniquePaths(m = 3, n = 7))
print(solve.uniquePaths(m = 3, n = 2))
