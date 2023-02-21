# import sys
# sys.stdin = open("sample_input(1).txt", "r")

def rule(y, x, dol):
    direct_y = [-1, -1, -1, 0, 0, 1, 1, 1]
    direct_x = [-1, 0, 1, -1, 1, -1, 1, 0]
    arr[y][x] = dol
    for i in range(8):
        lst = []  # 내가 따먹을수 있는 돌
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < N and 0 <= dx < N:
            if arr[dy][dx] == 0 or arr[dy][dx] == dol:
                continue
            elif arr[dy][dx] != dol:  # 다른 돌을 만났을 경우
                lst.append((dy, dx))
                while True:
                    # 범위 벗어날때까지 내 돌 못만나면 리스트 초기화하고 break
                    if 0 > dy or dy >= N or dx >= N or 0 > dx:
                        lst = []
                        break
                    if arr[dy][dx] == 0:
                        lst = []
                        break
                    dy += direct_y[i]
                    dx += direct_x[i]
                    if 0 <= dy < N and 0 <= dx < N:
                        if arr[dy][dx] != dol:  # 다른돌이면 lst에 좌표 append
                            lst.append((dy, dx))
                        elif arr[dy][dx] == dol:  # 내돌을 만나면 break
                            break

        for j in range(len(lst)):
            if dol == 1:
                arr[lst[j][0]][lst[j][1]] = 1
            elif dol == 2:
                arr[lst[j][0]][lst[j][1]] = 2

T = int(input())
for test_case in range(1, T + 1):
    # 1 = 흑돌 2 = 백돌
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    # 초기 돌 설정
    center = N // 2
    arr[center][center], arr[center-1][center-1] = 2, 2
    arr[center-1][center], arr[center][center-1] = 1, 1

    for _ in range(M):
        a, b, dol = map(int, input().split())  # x+1, y+1, 돌 색깔
        if arr[b-1][a-1] == 0:
            rule(b-1, a-1, dol)

    black, white = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print(f'#{test_case} {black} {white}')