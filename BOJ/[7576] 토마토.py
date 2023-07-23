import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    q = deque()

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
            elif arr[i][j] == 1:
                q.append((i, j))

    while q:
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 0:
                    arr[dy][dx] = arr[y][x] + 1
                    q.append((dy, dx))
                    cnt -= 1

    if cnt == 0:
        return arr[y][x] - 1
    else:
        return -1

print(bfs())