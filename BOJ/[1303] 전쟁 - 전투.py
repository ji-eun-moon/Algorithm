from collections import deque

N, M = map(int, input().split())

arr = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

white_power = 0
blue_power = 0
def get_power(color, power):
    global white_power, blue_power
    if color == 'W':
        white_power += power
    if color == 'B':
        blue_power += power
def bfs(color, i, j):
    cnt = 0
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        cnt += 1
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < M and 0 <= dx < N:
                if visited[dy][dx] == 0 and arr[dy][dx] == color:
                    visited[dy][dx] = 1
                    q.append((dy, dx))

    get_power(color, cnt**2)

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            color = arr[i][j]
            bfs(color, i, j)

print(white_power, blue_power)