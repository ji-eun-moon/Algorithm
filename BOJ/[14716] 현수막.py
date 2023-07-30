from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        y, x = q.popleft()
        for iy, ix in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < M and 0 <= dx < N:
                if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    q.append((dy, dx))
cnt = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)