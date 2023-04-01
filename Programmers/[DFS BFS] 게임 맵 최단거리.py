def solution(maps):
    global Min
    N = len(maps)
    M = len(maps[0])
    used = [[0]*M for _ in range(N)]
    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]
    Min = 21e8
    def bfs(y, x):
        global Min
        q = []
        q.append((y, x))

        while q:
            y, x = q.pop(0)
            if y == N-1 and x == M-1:
                return used[y][x] + 1
            for i in range(4):
                dy = y + direct_y[i]
                dx = x + direct_x[i]
                if 0 <= dy < N and 0 <= dx < M:
                    if used[dy][dx] == 0 and maps[dy][dx] == 1:
                        used[dy][dx] = used[y][x] + 1
                        q.append((dy, dx))

        return -1

    answer = bfs(0, 0)

    return answer
