T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input()))
    lst.append(0)
    cnt_lst = []

    for i in range(N + 1):
        cnt = 0
        for j in range(i, N + 1):
            if lst[j] == 1:
                cnt += 1
            else:
                cnt_lst.append(cnt)
                break

    Max = cnt_lst[0]
    for i in range(len(cnt_lst)):
        if Max < cnt_lst[i]:
            Max = cnt_lst[i]

    print(f'#{test_case} {Max}')