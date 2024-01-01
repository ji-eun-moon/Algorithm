# https://leetcode.com/problems/combinations/

# 1087 ms
class Solution:
    def combine(self, n, k):
        nums = list(range(1, n+1))
        path = [0] * k
        result = []
        def dfs(level, start):
            if level == k:
                result.append(path[:])
                return
            for i in range(start, n):
                path[level] = nums[i]
                dfs(level+1, i+1)
                path[level] = 0

        dfs(0, 0)
        return result

solve = Solution()
print(solve.combine(4, 2))
