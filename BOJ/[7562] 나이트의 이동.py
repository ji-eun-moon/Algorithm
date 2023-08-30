from collections import deque

T = int(input())

direct_y = [2, 1, 2, 1, -2, -1, -2, -1]
direct_x = [-1, -2, 1, 2, -1, -2, 1, 2]

def bfs(l, nowy, nowx, targety, targetx):
    visited = [[0] * l for _ in range(l)]
    q = deque()
    q.append((nowy, nowx))
    visited[nowy][nowx] = 1
    while q:
        y, x = q.popleft()
        if (y, x) == (targety, targetx):
            return visited[targety][targetx] - 1
        for i in range(8):
            ny = y + direct_y[i]
            nx = x + direct_x[i]
            if 0 <= ny < l and 0 <= nx < l:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

for test_case in range(T):

    l = int(input())  # 체스판의 길이
    nowy, nowx = map(int, input().split())  # 현재 위치
    targety, targetx = map(int, input().split())  # 목표 위치

    print(bfs(l, nowy, nowx, targety, targetx))