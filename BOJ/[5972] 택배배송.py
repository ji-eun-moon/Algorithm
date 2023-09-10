import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())  # 노드, 간선
graph = [[] for _ in range(N+1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a 부터 b 까지 소 c 마리
    graph[b].append((a, c))
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

print(distance[N])