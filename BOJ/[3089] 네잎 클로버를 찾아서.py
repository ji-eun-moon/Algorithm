import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 네잎클로버 개수, 외게인의 명령 수

clover_y = {}
clover_x = {}
for _ in range(N):
    x, y = map(int, input().split())
    clover_y.setdefault(y, [])
    clover_x.setdefault(x, [])
    clover_y[y].append(x)
    clover_x[x].append(y)

commands = list(input())  # 외계인의 명령

for key in clover_y.keys():
    clover_y[key].sort()
for key in clover_x.keys():
    clover_x[key].sort()

# 명령을 수행한 후 숭이가 있는 곳의 위치
nowx, nowy = 0, 0
for command in commands:
    # y 좌표 동일
    if command == 'R':  # 현재보다 오른쪽 중에서 x 좌표가 가장 큰 것
        tmp = clover_y[nowy]  # y 좌표 동일한 x 좌표 후보
        for t in tmp:
            if t > nowx:
                nowx = t
                break
    elif command == 'L':  # 현재보다 왼쪽 중에서 x 좌표가 가장 큰 것
        tmp = clover_y[nowy]  # y 좌표 동일한 x 좌표 후보
        for t in tmp:
            if t < nowx:
                newx = t
            else:
                nowx = newx
                break
    # x 좌표 동일
    elif command == 'U':  # 현재보다 위쪽 중에서 y 좌표가 가장 작은 것
        tmp = clover_x[nowx]  # x 좌표 동일한 y 좌표 후보
        for t in tmp:
            if t > nowy:
                nowy = t
                break
    elif command == 'D':  # 현재보다 아래쪽 중에서 y 좌표가 가장 큰 것
        tmp = clover_x[nowx]  # x 좌표 동일한 y 좌표 후보
        for t in tmp:
            if t < nowy:
                newy = t
            else:
                nowy = newy
                break

print(nowx, nowy)