T = 10

for test_case in range(1, T + 1):

    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_lst = []

    D1sum = 0
    D2sum = 0
    for i in range(100):
        D1sum += arr[i][i]
        D2sum += arr[99-i][i]
        Hsum = 0
        Vsum = 0
        for j in range(100):
            Hsum += arr[i][j]
            Vsum += arr[j][i]
        sum_lst.append(Hsum)
        sum_lst.append(Vsum)
    sum_lst.append(D1sum)
    sum_lst.append(D2sum)

    ans = max(sum_lst)

    print(f'#{T} {ans}')