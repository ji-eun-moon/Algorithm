T = int(input())

for test_case in range(1, T + 1):

    arr = [[0]*10 for _ in range(10)]
    N = int(input())

    for i in range(N):
        a1, a2, b1, b2, color = map(int, input().split())
        for i in range(a1, b1+1):
            for j in range(a2, b2+1):
                arr[i][j] += color

    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{test_case} {cnt}')