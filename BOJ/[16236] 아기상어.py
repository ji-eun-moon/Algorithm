from collections import deque


def bfs(sty, stx):
    global size

    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    q = deque()
    q.append((sty, stx))

    candi = []
    visited[sty][stx] = 1

    while q:
        y, x = q.popleft()

        for iy, ix in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            dy, dx = y + iy, x + ix
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] <= size and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    distance[dy][dx] = distance[y][x] + 1
                    q.append((dy, dx))

                    if arr[dy][dx] < size and arr[dy][dx] != 0:
                        candi.append((dy, dx, distance[dy][dx]))

    return sorted(candi, key= lambda x: (x[2], x[0], x[1]))


N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
sty, stx = 0, 0
answer = 0
size = 2

# 상여 위치
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sty, stx = i, j


eat = 0
while True:

    fish = bfs(sty, stx)

    if len(fish) == 0:
        break

    y, x, time = fish[0]

    answer += time
    eat += 1
    arr[sty][stx], arr[y][x] = 0, 0
    sty, stx = y, x

    if size == eat:
        eat = 0
        size += 1

print(answer)