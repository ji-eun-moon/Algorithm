# Solution 1 - 규칙 찾기
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(abs(N//2-i), N-abs(N//2-i)):
            answer += farm[i][j]

    print(f'#{test_case} {answer}')

# Solution 2 - 범위
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    answer = 0
    m = N//2
    st = ed = m
    for i in range(N):
        for j in range(st, ed+1):
            answer += farm[i][j]
        # st, ed 재조정
        if i < m:
            st -= 1
            ed += 1
        else:
            st += 1
            ed -= 1
    print(f'#{test_case} {answer}')

