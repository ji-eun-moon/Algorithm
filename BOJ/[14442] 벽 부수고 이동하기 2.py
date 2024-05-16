from collections import deque
N, M, K = map(int, input().split())  # 행렬 세로, 가로, 부술 수 있는 벽의 개수
maps = [list(input()) for _ in range(N)]

def bfs(sty, stx, cnt):
    q = deque()
    q.append((sty, stx, cnt))
    visited = [[[0]*M for _ in range(N)] for _ in range(K+1)]
    visited[cnt][sty][stx] = 1

    while q:
        y, x, cnt = q.popleft()
        if y == N-1 and x == M-1:
            return visited[cnt][y][x]
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy, dx = y + iy, x + ix
            if 0 <= dy < N and 0 <= dx < M:
                # 벽이 아닌 경우 - 방문하지 않은 경우 방문
                if maps[dy][dx] == '0' and visited[cnt][dy][dx] == 0:
                    visited[cnt][dy][dx] = visited[cnt][y][x] + 1
                    q.append((dy, dx, cnt))
                # 벽인 경우 - 부술 수 있는 횟수가 남았고, 방문하지 않은 경우
                elif maps[dy][dx] == '1' and cnt < K and visited[cnt+1][dy][dx] == 0:
                    visited[cnt+1][dy][dx] = visited[cnt][y][x] + 1
                    q.append((dy, dx, cnt+1))

    return -1

print(bfs(0, 0, 0))

