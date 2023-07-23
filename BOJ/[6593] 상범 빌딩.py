import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    q = deque()
    q.append((stz, sty, stx))
    visited[stz][sty][stx] = 1

    while q:
        z, y, x = q.popleft()
        if (z, y, x) == (edz, edy, edx):
            return visited[z][y][x] - 1
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C:
                if visited[nz][ny][nx] == 0 and arr[nz][ny][nx] != '#':
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    q.append((nz, ny, nx))

    return 0

while True:
    L, R, C = map(int, input().split())  # 층 수, 한 층의 행, 열

    # 0, 0, 0 입력받으면 종료
    if (L, R, C) == (0, 0, 0):
        break

    # 건물 정보 입력 받기
    arr = []
    for _ in range(L):
        temp = [list(input().strip()) for _ in range(R)]
        blank = input()
        arr.append(temp)

    # 출발, 도착 지점 찾기
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    stz, sty, stx = i, j, k
                elif arr[i][j][k] == 'E':
                    edz, edy, edx = i, j, k

    result = bfs()

    if result:
        print(f'Escaped in {result} minute(s).')
    else:
        print('Trapped!')