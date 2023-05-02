from collections import deque

N, M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            sty, stx = i, j
        if arr[i][j] == 'D':
            edy, edx = i, j
        if arr[i][j] == 'C':
            cy, cx = i, j
def bfs(sty, stx, edy, edx):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((sty, stx))
    visited[sty][stx] = 1
    while q:
        y, x = q.popleft()
        if y == edy and x == edx:
            return visited[y][x] - 1
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < N and 0 <= dx < M:
                if visited[dy][dx] == 0 and arr[dy][dx] != 'x':
                    visited[dy][dx] += visited[y][x] + 1
                    q.append((dy, dx))


print(bfs(sty, stx, cy, cx) + bfs(cy, cx, edy, edx))
