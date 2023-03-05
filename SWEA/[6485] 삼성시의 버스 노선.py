T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    P = int(input())
    c = [0] * P
    for i in range(P):
        c[i] = int(input())
    cnt_lst = []
    for i in range(P):
        cnt = 0
        for j in range(N):
            if a[j] <= c[i] <= b[j]:
                cnt += 1
        cnt_lst.append(cnt)

    print(f'#{test_case}', end=' ')
    for i in cnt_lst:
        print(i, end=' ')
    print()