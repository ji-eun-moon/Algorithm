T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direct_y = [0, 0, -1, 1]
    direct_x = [-1, 1, 0, 0]
    Max = 0
    for i in range(N):
        for j in range(M):
            Sum = arr[i][j]
            X = arr[i][j]
            for n in range(1, X+1):
                for k in range(4):
                    dy = i + n*direct_y[k]
                    dx = j + n*direct_x[k]
                    if 0 <= dy < N and 0 <= dx < M:
                        Sum += arr[dy][dx]
            Max = max(Max, Sum)
    print(f'#{test_case} {Max}')