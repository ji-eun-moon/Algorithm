T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = []
    # 리스트 선택 정렬
    for i in range(N):
        for j in range(i+1,N):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    # 정렬한 리스트에서 가장 큰 값, 작은 값을 순서대로 제거 후 ans 리스트에 append
    for i in range(5):
        Max = lst.pop(-1)
        Min = lst.pop(0)
        ans.append(Max)
        ans.append(Min)

    print(f'#{test_case}', end=' ')
    print(*ans)