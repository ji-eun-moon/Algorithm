import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())  # 세로, 가로
board = [list(input().strip()) for _ in range(N)]  # 보드

# R 구슬과 B 구슬 위치 저장
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            ry, rx = i, j
        elif board[i][j] == 'B':
            by, bx = i, j

# 구슬 이동 함수
def move(y, x, dy, dx):
    cnt = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

def bfs():
    q = deque()
    visited = set()
    q.append((ry, rx, by, bx, 0))
    visited.add((ry, rx, by, bx))

    while q:
        cry, crx, cby, cbx, cnt = q.popleft()
        # cnt 가 10 보다 크면 break
        if cnt > 10:
            break
        # 빨간 구슬이 구멍에 들어간 경우
        if board[cry][crx] == 'O':
            return 1
        # 현재 구슬들 위치에서 4 방향으로 이동
        for iy, ix in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nry, nrx, rmove = move(cry, crx, iy, ix)
            nby, nbx, bmove = move(cby, cbx, iy, ix)
            # 파란 구슬이 구멍에 들어간 경우 - 탐색할 필요 없음
            if board[nby][nbx] == 'O':
                continue
            # 중복 체크
            if (nry, nrx, nby, nbx) in visited:
                continue
            # 파란 구슬의 위치와 빨간 구슬의 위치가 같다면, 더 멀리서 온 구슬을 한 칸 이전 칸으로 이동
            if (nry, nrx) == (nby, nbx):
                if rmove > bmove:
                    nry -= iy
                    nrx -= ix
                else:
                    nby -= iy
                    nbx -= ix
            # 이동한 좌표 q, visited 배열에 추가
            q.append((nry, nrx, nby, nbx, cnt + 1))
            visited.add((nry, nrx, nby, nbx))

    return 0

print(bfs())


