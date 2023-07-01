import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 최단 거리 구하는 bfs 함수
def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy = iy + y
            dx = ix + x
            if 0 <= dy < N and 0 <= dx < M:
                if visited[dy][dx] == 0 and arr[dy][dx] == 'L':
                    visited[dy][dx] = visited[y][x] + 1
                    q.append((dy, dx))

    return visited[y][x] - 1

# 각 점마다 육지인 경우 bfs 함수 -> 최단 거리 구하기
Max = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = bfs(i, j)
            Max = max(result, Max)  # 최단 거리 중에서 최댓값 구하기

print(Max)