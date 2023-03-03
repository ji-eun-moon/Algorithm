T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    Max = 0
    for i in range(N-2):  # 흰색이 색칠될수 있는 범위
        for j in range(i+1, N-1):  # 파란색이 색칠될 수 있는 범위
            cnt = 0
            for s in range(i+1):
                cnt += arr[s].count('W')
            for s in range(i+1, j+1):
                cnt += arr[s].count('B')
            for s in range(j+1, N):
                cnt += arr[s].count('R')
            Max = max(Max, cnt)

    answer = N*M - Max
    print(f'#{test_case} {answer}')
