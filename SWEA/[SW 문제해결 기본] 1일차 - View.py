T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    d = [-2, -1, 1, 2]
    for i in range(2, N-2):
        flag = 0
        Min = 21e8
        for j in range(4):
            dj = i + d[j]
            if lst[i] - lst[dj] > 0:
                flag += 1
                Min = min(Min, lst[i] - lst[dj])
            else:
                continue
        if flag == 4:
            answer += Min
    print(f'#{test_case} {answer}')
