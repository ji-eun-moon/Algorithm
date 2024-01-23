import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
labMap = [list(map(int, input().split())) for _ in range(N)]
blanck_list = []  # 빈칸 위치
virus = deque()  # 바이러스 위치 → bfs 로 4 방향 바이러스 퍼지기

# 이중 for 문으로 graph 순회하며 바이러스 위치와 빈칸 위치 담기
for i in range(N):
    for j in range(M):
        if labMap[i][j] == 0:
            blanck_list.append([i, j])
        elif labMap[i][j] == 2:
            virus.append((i, j))


# 바이러스 퍼지기
def bfs(newMap):

    while newVirus:
        y, x = newVirus.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny = y + iy
            nx = x + ix
            if 0 <= ny < N and 0 <= nx < M:
                if newMap[ny][nx] == 0:
                    newMap[ny][nx] = 2
                    newVirus.append((ny, nx))

    # safe area 카운트하기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if newMap[i][j] == 0:
                cnt += 1

    return cnt

Max = 0
# wall_combi 에서 조합 하나씩 확인하며 벽을 세우기
wall_combi = list(combinations(blanck_list, 3))
for combi in wall_combi:
    newMap = [arr[:] for arr in labMap]  # 깊은 복사
    newVirus = deque(arr[:] for arr in virus)
    for i in range(3):
        y, x = combi[i]
        newMap[y][x] = 1
    safe_area = bfs(newMap)
    Max = max(Max, safe_area)


print(Max)