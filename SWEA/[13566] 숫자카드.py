T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    a = list(map(int, input()))

    DAT = [0] * 10
    for i in range(N):
        DAT[a[i]] += 1

    max_idx = 0
    for i in range(10):
        if DAT[max_idx] < DAT[i]:
            max_idx = i
        if DAT[max_idx] == DAT[i]:
            if max_idx < i:
                max_idx = i

    print(f'#{test_case} {max_idx} {DAT[max_idx]}')