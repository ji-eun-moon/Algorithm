import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

N = int(input())  # 도시 개수
M = int(input())  # 버스 개수

arr = [[] for _ in range(N+1)]

# 인접리스트
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

st, ed = map(int, input().split())
result = dijkstra(st)
print(result[ed])