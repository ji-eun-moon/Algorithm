import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

def dijkstra(start):

    distance = [INF]*(N+1)
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
                parents[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

    return distance

st, ed = map(int, input().split())
parents = [st]*(N+1)
result = dijkstra(st)
print(result[ed])  # 최소 비용

path = []
temp = ed
while True:
    path.append(temp)
    if temp == parents[temp]:
        break
    temp = parents[temp]
print(len(path))
path.reverse()
print(*path)