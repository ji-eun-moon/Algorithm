def bfs(sty, stx):
    q = []
    q.append((sty, stx))
    visited[sty][stx] = 1
    while q:
        y, x = q.pop(0)
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] == 0 and visited[dy][dx] == 0:
                    visited[dy][dx] += visited[y][x] + 1
                    q.append((dy, dx))
                if arr[dy][dx] == 3:
                    return visited[y][x] - 1
    return 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sty = i
                stx = j

    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]

    print(f'#{test_case} {bfs(sty, stx)}')
