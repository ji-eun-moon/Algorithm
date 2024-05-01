import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
def bfs(si, sj):

    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    union = [(si, sj)]
    total = arr[si][sj]

    while q:
        y, x = q.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            dy = y + iy
            dx = x + ix
            if 0 <= dy < N and 0 <= dx < N:
                if visited[dy][dx] == 0:
                    if L <= abs(arr[y][x] - arr[dy][dx]) <= R:
                        q.append((dy, dx))
                        visited[dy][dx] = 1
                        union.append((dy, dx))
                        total += arr[dy][dx]

    if len(union) > 1:
        avg = total // len(union)
        for y, x in union:
            arr[y][x] = avg
        return 1
    return 0


while True:
    visited = [[0]*N for _ in range(N)]
    flag = 0  # 인구 이동 확인 플래그
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                flag = max(flag, bfs(i, j))

    if flag == 0:  # 인구 이동이 없었으면 종료
        break
    answer += 1

print(answer)