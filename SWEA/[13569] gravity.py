T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input().split()))

    Hmax = lst[0]
    for i in range(N):
        if Hmax < lst[i]:
            Hmax = lst[i]

    rot_lst = [[0] * Hmax for _ in range(N)]

    for i in range(N):
        for j in range(0, lst[i]):
            rot_lst[i][j] = 1

    H_idx = []
    for j in range(Hmax):
        for i in range(N):
            if rot_lst[i][j] == 1:
                idx = i
                break
        H_idx.append(idx)

    cnt_lst = []
    for j in range(Hmax):
        cnt = 0
        for i in range(H_idx[j], N):
            if rot_lst[i][j] == 0:
                cnt += 1
        cnt_lst.append(cnt)

    Max = cnt_lst[0]
    for i in range(Hmax):
        if Max < cnt_lst[i]:
            Max = cnt_lst[i]

    print(f'#{test_case} {Max}')