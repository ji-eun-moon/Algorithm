T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for i in range(N)]
    # 우, 하, 좌, 상 순서
    direct_y = [0, 1, 0, -1]
    direct_x = [1, 0, -1, 0]
    i = 0  # 처음 방향

    # 시작점
    stx = sty = 0
    num = 1
    arr[stx][sty] = num

    while True:
        if num == N*N:
            break
        dy = sty + direct_y[i]
        dx = stx + direct_x[i]
        # 막다른길에 가면 방향 전환
        if 0 > dy or dy >= N or 0 > dx or dx >= N or arr[dy][dx] != 0:
            i = (i + 1) % 4
            continue
        num += 1
        arr[dy][dx] = num
        sty = dy
        stx = dx

    print(f'#{test_case}')
    for a in arr:
        for b in a:
            print(b, end=' ')
        print()


