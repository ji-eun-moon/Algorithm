# https://leetcode.com/problems/network-delay-time/description/

import heapq
class Solution:
    def networkDelayTime(self, times, n, k):

        # 가중치 그래프 만들기
        graph = {i: [] for i in range(1, n + 1)}
        for time in times:
            graph[time[0]].append((time[1], time[2]))

        # 다익스트라 알고리즘
        distance = [float("inf")] * (n+1)
        distance[k] = 0
        q = []
        heapq.heappush(q, (0, k))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for v, w in graph[now]:
                cost = distance[now] + w
                if cost < distance[v]:
                    distance[v] = cost
                    heapq.heappush(q, (cost, v))

        # distance 의 최댓값이 inf 이면 불가능, 그렇지 않으면 최댓값이 정답
        ret = max(distance[1:])
        answer = -1 if ret == float("inf") else ret
        return answer


solve = Solution()
print(solve.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(solve.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(solve.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))