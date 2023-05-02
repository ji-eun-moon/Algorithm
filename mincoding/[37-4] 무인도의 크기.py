from collections import deque

arr = [list(map(int, input().split())) for _ in range(4)]
visited = [[0]*4 for _ in range(4)]

q = deque()
q.append((0, 0))
visited[0][0] = 1
cnt = 1
while q:
    y, x = q.popleft()
    for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        dy = y + iy
        dx = x + ix
        if 0 <= dy < 4 and 0 <= dx < 4:
            if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                q.append((dy, dx))
                cnt += 1

print(cnt)