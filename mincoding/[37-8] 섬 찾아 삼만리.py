from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    q.append((dy, dx))

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)
            cnt += 1

print(cnt)
