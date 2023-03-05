T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # + 형태로 파리 퇴치
    def spray_1(y, x):
        cnt = arr[y][x]
        direct_y = [0, 0, 1, -1]
        direct_x = [-1, 1, 0, 0]
        for n in range(1, M):
            for i in range(4):
                dy = y + n*direct_y[i]
                dx = x + n*direct_x[i]
                if 0 <= dy < N and 0 <= dx < N:
                    cnt += arr[dy][dx]
        return cnt

    # X 형태로 파리 퇴치
    def spray_2(y, x):
        cnt = arr[y][x]
        direct_y = [-1, -1, 1, 1]
        direct_x = [-1, 1, -1, 1]
        for n in range(1, M):
            for i in range(4):
                dy = y + n*direct_y[i]
                dx = x + n*direct_x[i]
                if 0 <= dy < N and 0 <= dx < N:
                    cnt += arr[dy][dx]
        return cnt

    Max = 0
    for i in range(N):
        for j in range(N):
            tmp = max(spray_1(i, j), spray_2(i, j))
            Max = max(Max, tmp)

    print(f'#{test_case} {Max}')