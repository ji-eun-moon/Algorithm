import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

Max = 0
while q:
    y, x = q.popleft()
    for iy, ix in ((-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)):
        dy = y + iy
        dx = x + ix
        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] == 0:
                arr[dy][dx] = arr[y][x] + 1
                Max = max(Max, arr[dy][dx])
                q.append((dy, dx))

print(Max - 1)
