import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, Y, X = map(int, input().split())

q = deque()

for n in range(1, K+1):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == n:  # 숫자 순서대로 큐에 넣기
                q.append((i, j, 0))

while q:
    y, x, time = q.popleft()
    if time == S:
        break
    for iy, ix in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        dy = iy + y
        dx = ix + x
        if 0 <= dy < N and 0 <= dx < N:
            if arr[dy][dx] == 0:
                arr[dy][dx] = arr[y][x]
                q.append((dy, dx, time+1))

print(arr[Y-1][X-1])



