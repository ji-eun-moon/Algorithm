# https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        answer = 0.0
        return answer

solve = Solution()
print(solve.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
print(solve.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node = 0, end_node = 2))
print(solve.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2))
