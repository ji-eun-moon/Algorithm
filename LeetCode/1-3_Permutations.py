# https://leetcode.com/problems/permutations/

# 35 ms

class Solution:
    def permute(self, nums):
        N = len(nums)
        path = [0] * N
        used = [0] * N
        result = []

        def dfs(level):
            if level == N:
                result.append(path[:])
                return
            for i in range(N):
                if used[i] == 0:
                    used[i] = 1
                    path[level] = nums[i]
                    dfs(level+1)
                    used[i] = 0
                    path[level] = 0

        dfs(0)
        return result

result = Solution()
print(result.permute(nums = [1, 2, 3]))