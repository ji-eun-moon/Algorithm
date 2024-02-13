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

        # 다익스트라 알고리즘
        probability = [0.0]*n
        probability[start_node] = 1.0
        q = []
        heapq.heappush(q, (-1.0, start_node))  # 최대 힙

        while q:
            cur_prob, now = heapq.heappop(q)

            # 이미 처리된 노드 제외
            if - probability[now] > cur_prob:
                continue

            for v, prob in graph[now]:
                new_prov = - cur_prob * prob
                # 새로운 경로의 확률이 더 높으면 우선순위큐에 삽입
                if new_prov > probability[v]:
                    probability[v] = new_prov
                    heapq.heappush(q, (-probability[v], v))

        return probability[end_node]

solve = Solution()
print(solve.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
print(solve.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node = 0, end_node = 2))
print(solve.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2))
