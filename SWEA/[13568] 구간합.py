T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_lst = []
    for i in range(N - M + 1):
        sum = 0
        for j in range(i, i + M):
            sum += lst[j]
        sum_lst.append(sum)

    Max = sum_lst[0]
    for i in range(len(sum_lst)):
        if sum_lst[i] > Max:
            Max = sum_lst[i]

    Min = sum_lst[0]
    for i in range(len(sum_lst)):
        if sum_lst[i] < Min:
            Min = sum_lst[i]

    print(f'#{test_case} {Max - Min}')
