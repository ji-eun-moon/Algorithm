from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
used = [[0]*M for _ in range(N)]
def bfs(i, j):
    cnt = 0
    q = deque()
    q.append((i, j))
    while q:
        cnt += 1
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 1 and used[dy][dx] == 0:
                    q.append((dy, dx))
                    used[dy][dx] = 1
    return cnt

Max = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and used[i][j] == 0:
            cnt += 1
            used[i][j] = 1
            Max = max(Max, bfs(i, j))

print(cnt)
print(Max)