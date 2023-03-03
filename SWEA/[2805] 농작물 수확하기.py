T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    answer = 0

    for i in range(N//2):
        for j in range(N//2-i, N//2+i):
            answer += farm[i][j]

    for i in range(N//2+1, N):
        for j in range(N//2+1):
            answer += farm[i][j]

    print(f'#{test_case} {answer}')