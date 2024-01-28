import sys
input = sys.stdin.readline
from collections import deque

global fuel, canPickUp, canArrive, fuel, ty, tx

N, M, fuel = map(int, input().split())  # 격자 한변, 손님 수, 초기 연료
load = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(int, input().split())  # 택시 위치
# 좌표 조정
ty -= 1
tx -= 1
canPickUp, canArrive = 0, 0

# 승객 정보 저장 - 출발지 : 목적지
passenger = {}
for i in range(M):
    p_sty, p_stx, p_edy, p_edx = map(int, input().split())
    passenger[(p_sty-1, p_stx-1)] = (p_edy-1, p_edx-1)

# 출발 : 가장 가까운 승객 찾기
def departure(sty, stx):
    global canPickUp
    canPickUp = 0
    Min = 100000000
    visited = set()
    q = deque()

    temp = []  # 태울 승객 후보
    visited.add((sty, stx))
    q.append((sty, stx, 0))

    while q:
        y, x, cur_dist = q.popleft()
        # 현재 위치에 승객이 있는 경우
        if (y, x) in passenger:
            if Min >= cur_dist:
                Min = cur_dist
                temp.append([y, x])
        for iy, ix in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = y + iy
            nx = x + ix
            if 0 <= ny < N and 0 <= nx < N:
                if (ny, nx) in visited:
                    continue
                if load[ny][nx] != 1:
                    visited.add((ny, nx))
                    q.append((ny, nx, cur_dist + 1))

    if temp:
        canPickUp = 1
        temp.sort(key= lambda x: (x[0], x[1]))
        p_sty, p_stx = temp[0]
        return p_sty, p_stx, Min
    else:
        canPickUp = 0
        return 0, 0, 0


# 도착 : 승객을 데려다 주는 데 드는 연료의 양
def arrive(sty, stx, edy, edx):
    global canArrive
    canArrive = 0
    visited = set()

    q = deque()
    visited.add((sty, stx))
    q.append((sty, stx, 0))

    while q:
        y, x, cur_dist = q.popleft()
        # 현재 위치에 승객이 있는 경우
        if (y, x) == (edy, edx):
            canArrive = 1
            return y, x, cur_dist
        for iy, ix in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = y + iy
            nx = x + ix
            if 0 <= ny < N and 0 <= nx < N:
                if (ny, nx) in visited:
                    continue
                if load[ny][nx] != 1:
                    visited.add((ny, nx))
                    q.append((ny, nx, cur_dist + 1))

    return 0, 0, 0

def solve():
    global canPickUp, canArrive, fuel, ty, tx

    # 연료와 남아있는 승객이 있는 경우
    while fuel > 0 and passenger:
        # 가장 가까운 승객 찾기
        p_sty, p_stx, need_fuel = departure(ty, tx)
        # 찾을 수 있는 승객이 없는 경우
        if not canPickUp:
            return -1
        # 승객을 태우러 갈 수 없는 경우
        if need_fuel > fuel:
            return -1
        # 승객 태우러 갈 때까지 소비한 연료
        fuel -= need_fuel
        # 승객의 목적지 찾기
        p_edy, p_edx = passenger[(p_sty, p_stx)]
        # 목적지 까지 이동
        t_edy, t_edx, need_fuel = arrive(p_sty, p_stx, p_edy, p_edx)
        # 도착할 수 없는 경우
        if not canArrive:
            return -1
        # 연료가 모자란 경우
        if need_fuel > fuel:
            return -1
        # 데려다 준 손님 목록에서 제거
        del passenger[(p_sty, p_stx)]
        # 연료, 좌표 갱신
        fuel += need_fuel
        ty, tx = t_edy, t_edx

    return fuel

print(solve())
