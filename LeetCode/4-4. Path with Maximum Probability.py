# https://leetcode.com/problems/path-with-maximum-probability/

import heapq

class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):

        graph = {i : [] for i in range(n)}
        # 그래프 만들기 - 무방향
        for i in range(len(edges)):
            st, ed, v = edges[i][0], edges[i][1], succProb[i]
            graph[st].append([ed, v])
            graph[ed].append([st, v])

        probability = [0.0]*n
        probability[start_node] = 1.0
        q = []
        heapq.heappush(q, (1.0, start_node))

        while q:
            prob, now = heapq.heappop(q)

            if probability[now] > prob:
                continue

            for vv, ww in graph[now]:
                new_prob = probability[now] * ww
                if new_prob > probability[vv]:
                    probability[vv] = new_prob
                    heapq.heappush(q, (new_prob, vv))


        return probability[end_node]

solve = Solution()
print(solve.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
print(solve.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node = 0, end_node = 2))
print(solve.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2))
