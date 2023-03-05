# 내 풀이
def check(y, x):
    direct_y = [-1, 0, 1, 1]
    direct_x = [1, 1, 1, 0]
    for i in range(4):
        flag = 1
        for n in range(1, 5):
            dy = y + n*direct_y[i]
            dx = x + n*direct_x[i]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] == 'o':
                    flag += 1
        if flag == 5:
            return 1
    return 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if check(i, j):
                    result = 'YES'

    print(f'#{test_case} {result}')

# 교수님 풀이
def solve(arr):
    for si in range(1, N+1):
        for sj in range(1, N+1):
            for di, dj in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                for mul in range(5):
                    ni, nj = si + di*mul, sj + dj*mul
                    if arr[ni][nj] != 'o':
                        break
                else:
                    return 'YES'
    return 'NO'

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = ['.'*(N+2)] + ['.'+input()+'.' for _ in range(N)] + ['.'*(N+2)]
    ans = solve(arr)
    print(f'#{test_case} {ans}')