def getsum(y, x):
    sum = 0
    for i in range(M):
        for j in range(M):
            sum += arr[y+i][x+j]
    return sum

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            ret = getsum(i, j)
            if Max < ret:
                Max = ret

    print(f'#{test_case} {Max}')