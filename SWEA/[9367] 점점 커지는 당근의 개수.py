T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 1

    def check(i):
        start = 1
        for j in range(i, N - 1):
            if lst[j + 1] == lst[j] + 1:
                start += 1
            else:
                break
        return start


    for i in range(5):
        start = check(i)
        if start > cnt:
            cnt = start

    print(f'#{test_case} {cnt}')