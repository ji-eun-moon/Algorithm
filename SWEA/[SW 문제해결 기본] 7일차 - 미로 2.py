def bfs(sty, stx):
    q = []
    q.append((sty, stx))
    visited[sty][stx] = 1
    while q:
        y, x = q.pop(0)
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < 100 and 0 <= dx < 100:
                if arr[dy][dx] == 0 and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    q.append((dy, dx))
                if arr[dy][dx] == 3:
                    return 1
    return 0

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    sty, stx = 1, 1
    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]

    print(f'#{test_case} {bfs(sty, stx)}')