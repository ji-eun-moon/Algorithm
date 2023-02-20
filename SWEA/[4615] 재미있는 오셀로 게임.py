# 풀이중
def rule(y, x, dol):
    direct_y = [-1, -1, -1, 0, 0, 1, 1, 1]
    direct_x = [-1, 0, 1, -1, 1, -1, 1, 0]
    for i in range(8):
        dy = y + direct_y[i]  # dol 과 다른 돌이어야 함
        dx = x + direct_x[i]
        mdy = y + 2 * direct_y[i]  # 돌과 같은 돌이어야 함
        mdx = x + 2 * direct_x[i]
        if 0 <= dy < N and 0 <= dx < N and 0 <= mdy < N and 0 <= mdx < N:
            if arr[dy][dx] != 0 and arr[dy][dx] != dol:
                if arr[mdy][mdx] == dol:
                    arr[dy][dx] = dol
                    arr[y][x] = dol
                    break


T = int(input())
for test_case in range(1, T + 1):
    # 1 흑돌 2 백돌
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    # 시작 돌 놓기
    arr[N // 2 - 1][N // 2 - 1], arr[N // 2][N // 2] = 2, 2
    arr[N // 2][N // 2 - 1], arr[N // 2 - 1][N // 2] = 1, 1

    for _ in range(M):
        a, b, dol = map(int, input().split())
        rule(b - 1, a - 1, dol)

    black, white = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            if arr[i][j] == 2:
                white += 1

    print(f'#{test_case} {black} {white}')