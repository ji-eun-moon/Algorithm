
# Top down
class Solution:
    def rob(self, nums):
        n = len(nums)

        memo = {}
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2)+nums[i])

            return memo[i]

        return dp(n-1)

# Bottom up
class Solution:
    def rob(self, nums):
        n = len(nums)

        dp = [-1]*n
        dp[0] = nums[0]

        if n > 1:
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[n-1]


solve = Solution()
print(solve.rob(nums = [1,2,3,1]))
print(solve.rob(nums = [2,7,9,3,1]))