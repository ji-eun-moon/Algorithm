# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/description/

'''
1. 다익스트라 알고리즘을 통해 각 노드까지 드는 비용 distance 배열 완성하기
2. maxMoves 이내에 도달 가능한 노드의 수 확인하기
    1-1. distance 배열 값이 maxMoves 이내이면 도달 가능한 노드
3. maxMoves 이내에 도달 가능한 세분화된 노드의 수 확인하기
    3-1. 세분화된 노드의 개수 중에서, maxMoves - distance 값 만큼 더 이동할 수 있다.
    3-2. 양방향과 겹치는 부분 고려해야 한다.
'''

import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        answer = 0

        # 가중치 그래프 만들기 - 양방향 그래프
        # u, v 사이를 cnt만큼 나눌 수 있다면, u -> v 비용은 cnt + 1
        graph = {i: [] for i in range(n)}
        for u, v, cnt in edges:
            graph[u].append([v, cnt+1])
            graph[v].append([u, cnt+1])

        # 다익스트라 알고리즘으로 비용 계산
        distance = [float("inf")] * n
        distance[0] = 0
        q = []
        heapq.heappush(q, (0, 0))

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for v, w in graph[now]:
                cost = distance[now] + w
                if cost < distance[v]:
                    distance[v] = cost
                    heapq.heappush(q, (cost, v))

        # 이동 가능한 노드 수 계산
        for d in distance:
            if d <= maxMoves:
                answer += 1

        # 이동 가능한 서브 노드 계산
        for u, v, cnt in edges:
            a, b = 0, 0
            if distance[u] < maxMoves:  # 아직 더 이동할 수 있으면
                a = min(maxMoves-distance[u], cnt)  # 이동 가능한 서브노드 계산
            # 양방향 확인
            if distance[v] < maxMoves:
                b = min(maxMoves-distance[v], cnt)
            # 겹치는 부분 있는지 확인하고 더하기
            answer += min(a+b, cnt)

        return answer

solve = Solution()
print(solve.reachableNodes(edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3))
print(solve.reachableNodes(edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4))
print(solve.reachableNodes(edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5))
