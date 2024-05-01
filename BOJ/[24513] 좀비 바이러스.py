import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = [0]*4

q = deque()
for i in range(N):
    for j in range(M):
        # 바이러스가 있으면 큐에 담기
        if town[i][j] > 0:
            q.append((town[i][j], i, j))

while q:
    virus, y, x = q.popleft()
    if town[y][x] == 3:  # 이미 3으로 감염되었을 경우 더이상 퍼지지 않음
        continue
    for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        dy = y + iy
        dx = x + ix
        if 0 <= dy < N and 0 <= dx < M:
            if town[dy][dx] == -1:  # 치료제가 있는 경우
                continue
            if town[dy][dx] == 0:  # 아직 감염되지 않은 경우 감염
                town[dy][dx] = virus
                visited[dy][dx] = visited[y][x] + 1
                q.append((virus, dy, dx))
            # 이미 다른 바이러스에 감염 되었지만 다른 바이러스와 동시에 도착했을 경우
            elif town[dy][dx] != virus and visited[dy][dx] == visited[y][x] + 1:
                town[dy][dx] = 3  # 3으로 감염되고 더이상 감염 퍼지지 않음


for i in range(N):
    for j in range(M):
        if town[i][j] == -1:
            continue
        answer[town[i][j]] += 1

print(*answer[1:])
