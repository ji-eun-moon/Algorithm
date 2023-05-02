from collections import deque

arr = [[0, 0, 0, 0],
       [1, 1, 0, 1],
       [0, 0, 0, 0],
       [1, 0, 1, 0]]

visited = [[0]*4 for _ in range(4)]

sty, stx = map(int, input().split())
edy, edx = map(int, input().split())

def bfs():
    q = deque()
    q.append((sty, stx))
    visited[sty][stx] = 1
    while q:
        y, x = q.popleft()
        if y == edy and x == edx:
            return visited[y][x] - 1
        for iy, ix in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < 4 and 0 <= dx < 4:
                if arr[dy][dx] == 0 and visited[dy][dx] == 0:
                    visited[dy][dx] += visited[y][x] + 1
                    q.append((dy, dx))

print(f'{bfs()}회')