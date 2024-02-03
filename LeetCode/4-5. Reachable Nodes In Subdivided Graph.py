# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/description/

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        answer = 0
        return answer

solve = Solution()
print(solve.reachableNodes(edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3))
print(solve.reachableNodes(edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4))
print(solve.reachableNodes(edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5))
