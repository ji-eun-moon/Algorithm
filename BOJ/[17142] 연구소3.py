import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
labMap = [list(map(int, input().split())) for _ in range(N)]
virus_list = []

# virus_list 만들기
for i in range(N):
    for j in range(N):
        if labMap[i][j] == 2:
            virus_list.append([i, j])


# 4. bfs - 플로이드 워셜로 바이러스 시간 퍼지도록 하기
def bfs(newMap):
    global minTime

    maxTime = 0

    while acitveVirus:
        y, x = acitveVirus.popleft()
        for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny = y + iy
            nx = x + ix
            if 0 <= ny < N and 0 <= nx < N:
                if newMap[ny][nx] == 0:
                    newMap[ny][nx] = 3
                    time[ny][nx] = time[y][x] + 1
                    maxTime = max(maxTime, time[ny][nx])
                    acitveVirus.append((ny, nx))
                elif newMap[ny][nx] == 2:
                    newMap[ny][nx] = 3
                    time[ny][nx] = time[y][x] + 1
                    acitveVirus.append((ny, nx))


    for i in range(N):
        for j in range(N):
            if newMap[i][j] == 0:
                return

    minTime = min(maxTime, minTime)
    return


# 활성화 할 virus M 개의 조합 만들기
virusCombi = combinations(virus_list, M)

minTime = 100000000
for combi in virusCombi:
    newMap = [arr[:] for arr in labMap]
    acitveVirus = deque()
    time = [[0] * N for _ in range(N)]
    for i in range(M):
        acitveVirus.append(combi[i])
        newMap[combi[i][0]][combi[i][1]] = 3
    bfs(newMap)


if minTime == 100000000:
    print(-1)
else:
    print(minTime)