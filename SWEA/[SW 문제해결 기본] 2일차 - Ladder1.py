T = 10

for test_case in range(1, T + 1):

    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착 좌표 찾기
    for i in range(100):
        if ladder[99][i] == 2:
            y = 99
            x = i
            break

    direct_y = [0, 0, -1]
    direct_x = [-1, 1, 0]

    # 도착 좌표를 시작으로 1이 있는 곳을 따라 위로 올라가며 좌표찾기
    while True:
        if y == 0:  # y 좌표가 0이 되면 break
            break
        for k in range(3):
            dy = y + direct_y[k]
            dx = x + direct_x[k]
            if 0 > dy or 0 > dx or 99 < dy or 99 < dx:
                continue
            if ladder[dy][dx] == 1:
                y = dy
                x = dx
                ladder[dy][dx] = 0  # 왔던 길 되돌아가지 않도록 지난자리 0으로 바꿈
                break

    print(f'#{tc} {x}')