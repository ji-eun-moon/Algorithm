from collections import deque

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]
def bfs(y, x):
    cnt = 0
    q = deque()
    q.append((y, x))
    while q:
        cnt += 1
        y, x = q.popleft()
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    q.append((dy, dx))
    return cnt

result = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1 and visited[y][x] == 0:
            visited[y][x] = 1
            result.append(bfs(y, x))

result.sort()
print(len(result))
for a in result:
    print(a)
