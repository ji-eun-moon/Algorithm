from collections import deque

arr = [list(map(int, input().split())) for _ in range(4)]

q = deque()
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    y, x = q.popleft()
    for iy, ix in ((-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)):
        dy = y + iy
        dx = x + ix
        if 0 <= dy < 4 and 0 <= dx < 5:
            if arr[dy][dx] == 0:
                arr[dy][dx] += arr[y][x] + 1
                q.append((dy, dx))

print(arr[y][x]-1)