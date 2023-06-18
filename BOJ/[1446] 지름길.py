# 푸는 중


import heapq
INF = int(1e8)

N, D = map(int, input().split())

graph = [[] for _ in range(D+2)]

for _ in range(N):
    st, ed, dist = map(int, input().split())
    graph[st].append((ed, dist))

distance = [INF]*(D+2)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)

print(distance)