from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
a, b = map(int, input().split())

direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]
def bfs():
    q = deque()
    q.append((a, b))
    arr[a][b] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 0:
                    arr[dy][dx] += arr[y][x] + 1
                    q.append((dy, dx))
    return arr[y][x]

print(bfs()-1)