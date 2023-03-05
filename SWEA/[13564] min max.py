T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input().split()))

    Max = lst[0]
    for i in range(N):
        if Max < lst[i]:
            Max = lst[i]

    Min = lst[0]
    for j in range(N):
        if Min > lst[j]:
            Min = lst[j]

    print(f'#{test_case} {Max - Min}')