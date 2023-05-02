from collections import deque

N = int(input())
arr = [[0]*N for _ in range(N)]
y1, x1, y2, x2 = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()
q.append((y1, x1))
q.append((y2, x2))
arr[y1][x1] = 1
arr[y2][x2] = 1
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[ny][nx] == 0:
                arr[ny][nx] += (arr[y][x] + 1)
                q.append((ny, nx))

for a in arr:
    for b in a:
        print(b, end='')
    print()