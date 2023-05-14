import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())  # 노드 개수, 간선 개수
start = int(input())  # 시작 노드

graph = [[] for _ in range(V+1)]  # 노드 정보
distance = [INF] * (V+1)  # 최단 경로
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 거리, 노드
        if distance[now] < dist:  # 저장된 최단 경로 정보가 이미 더 작으면 넘어가기
            continue
        for i in graph[now]:  # 인접한 노드 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost  # 최단 경로 갱신
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])