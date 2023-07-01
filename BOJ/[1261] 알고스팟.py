from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < N and 0 <= dx < M:
                if visited[dy][dx] == 0:
                    if arr[dy][dx] == 0:  # 벽이 아니라면 이동 가능
                        visited[dy][dx] = visited[y][x]
                        q.appendleft((dy, dx))  # 벽인 아닌 경우 우선으로 탐색
                    else:  # 벽이라면 부수고 이동 가능
                        visited[dy][dx] = visited[y][x] + 1
                        q.append((dy, dx))

    return visited[N-1][M-1] - 1  # 시작할 때 1이었으므로

print(bfs(0, 0))

