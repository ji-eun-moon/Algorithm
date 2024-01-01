# https://leetcode.com/problems/subsets/

# 53 ms
class Solution:
    def subsets(self, nums):
        N = len(nums)
        path = []
        result = []
        def dfs(level, start):
            result.append(path[:])
            if level == N:
                return
            for i in range(start, N):
                path.append(nums[i])
                dfs(level+1, i+1)
                path.pop()

        dfs(0, 0)
        return result

solve = Solution()
print(solve.subsets(nums=[1, 2, 3]))
