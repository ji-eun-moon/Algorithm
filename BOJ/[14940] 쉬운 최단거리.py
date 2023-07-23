import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = [[-1]*M for _ in range(N)]
def bfs():
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
                result[i][j] = 0
            if arr[i][j] == 0:
                result[i][j] = 0

    while q:
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < N and 0 <= dx < M:
                if visited[dy][dx] == 0 and arr[dy][dx] != 0:
                    visited[dy][dx] = visited[y][x] + 1
                    result[dy][dx] = visited[y][x]
                    q.append((dy, dx))

bfs()
for r in result:
    print(*r)