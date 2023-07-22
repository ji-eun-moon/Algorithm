# DFS - recursion Error
import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000000)

N, A, B = map(int, input().split())  # 방(노드)의 개수, 로봇 A 위치, 로봇 B 위치

# 인접 리스트 만들기
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 방문 배열
visited = [0]*(N+1)

# 출발지에서 도착지까지의 총 비용을 구한 후, 가장 큰 비용 하나 빼기
max_total = 0
def dfs(now, max_cost, total):
    global max_total
    if now == B:
        max_total = total - max_cost
    for n, cost in graph[now]:
        if visited[n] == 0:
            visited[n] = 1
            dfs(n, max(max_cost, cost), total+cost)

visited[A] = 1
dfs(A, 0, 0)
print(max_total)

# BFS

import sys
from collections import deque
input = sys.stdin.readline

N, A, B = map(int, input().split())  # 방(노드)의 개수, 로봇 A 위치, 로봇 B 위치

# 인접 리스트 만들기
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs():
    visited = [0]*(N+1)
    q = deque()
    q.append((A, 0, 0))
    visited[A] = 1
    while q:
        now, max_cost, total = q.popleft()
        if now == B:
            return total - max_cost
        for nxt, cost in graph[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, max(max_cost, cost), total+cost))

print(bfs())