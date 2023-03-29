T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    lst = []
    for _ in range(N):
        st, ed = map(int, input().split())
        lst.append([st, ed])

    lst = sorted(lst, key=lambda x:x[1])

    result = [lst[0]]

    for i in range(1, N):
        if result[-1][1] <= lst[i][0]:
            result.append(lst[i])
        else:
            continue

    print(f'#{test_case} {len(result)}')