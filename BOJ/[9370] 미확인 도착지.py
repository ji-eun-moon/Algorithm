import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijakstra(start):
    distance = [INF] * (n+1)

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

T = int(input())

for test_case in range(1, T+1):

    n, m, t = map(int, input().split())  # 교차로, 도로, 목적지 후보 수
    s, g, h = map(int, input().split())  # 출발지, 거쳐야 하는 교차로 g, h

    arr = [[] for _ in range(n+1)]  # 인접 리스트
    for _ in range(m):
        a, b, d = map(int, input().split())
        arr[a].append((b, d))  # a -> b 비용 d
        arr[b].append((a, d))  # 양방향이므로

    s_distance = dijakstra(s)
    h_distance = dijakstra(h)
    g_distance = dijakstra(g)

    result = []
    for _ in range(t):
        x = int(input())

        # s -> h -> g -> x
        result1 = s_distance[h] + h_distance[g] + g_distance[x]
        # s -> g -> h -> x
        result2 = s_distance[g] + g_distance[h] + h_distance[x]

        if s_distance[x] == result1 or s_distance[x] == result2:
            result.append(x)

    result.sort()
    print(*result)





