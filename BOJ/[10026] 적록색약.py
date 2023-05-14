from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]

def bfs(y, x, color):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + iy, x + ix
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0:
                    if arr[ny][nx] in color:
                        visited[ny][nx] = 1
                        q.append((ny, nx))

visited = [[0]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j, [arr[i][j]])
            cnt += 1

print(cnt, end=' ')

visited = [[0]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            if arr[i][j] == 'R' or arr[i][j] == 'G':
                bfs(i, j, ['R', 'G'])
            else:
                bfs(i, j, [arr[i][j]])
            cnt += 1
print(cnt)