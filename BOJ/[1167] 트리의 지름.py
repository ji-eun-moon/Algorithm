from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]

# 인접리스트 - (정점, 거리) 저장
Max, idx = 0, 0
for _ in range(N):
    lst = list(map(int, input().split()))
    n = lst[0]
    for i in range(1, len(lst), 2):
        if lst[i] == -1:
            break
        arr[n].append((lst[i], lst[i+1]))


def bfs(now):
    q = deque()
    q.append(now)
    visited[now] = 1
    while q:
        now = q.popleft()
        for i in arr[now]:
            if visited[i[0]] == 0:
                visited[i[0]] = visited[now] + i[1]
                q.append(i[0])

visited = [0] * (N + 1)
bfs(1)
idx = visited.index(max(visited))  # 가장 거리가 긴 간선 찾기

# 그 간선이 포함된 최대 거리 찾기
visited = [0] * (N + 1)
bfs(idx)
print(max(visited) - 1)
