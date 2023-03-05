T = int(input())

for test_case in range(1, T + 1):

    K, N, M = map(int, input().split())
    charge_lst = list(map(int, input().split()))


    def check():
        for i in range(M - 1):
            if charge_lst[i + 1] - charge_lst[i] > K:
                return 0


    a = check()
    cnt = K
    ans = 0
    i = 0
    while i < N:
        if a == 0:
            break
        if cnt != 0:
            cnt -= 1
            i += 1
        else:
            for j in range(K):
                if i in charge_lst:
                    ans += 1
                    cnt = K
                    break
                else:
                    i -= 1

    print(f'#{test_case} {ans}')
