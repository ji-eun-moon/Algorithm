T = 10

for test_case in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input().split()))

    Maxidx = 0
    Minidx = 0
    for i in range(N):  # 덤프 횟수만큼 평탄화 수행
        # 리스트 안에서 최댓값, 최소값을 찾아 덤프를 수행
        for i in range(100):
            if lst[Maxidx] < lst[i]:
                Maxidx = i
            if lst[Minidx] > lst[i]:
                Minidx = i
        lst[Maxidx] -= 1
        lst[Minidx] += 1
        if (lst[Maxidx]-lst[Minidx]) <= 1:  # 덤프 횟수 이내에 평탄화 완료되면 break
            break
    # 평탄화 이후 최고점과 최저점 높이 차이 계산
    Max = lst[0]
    Min = lst[0]
    for i in range(100):
        if Max < lst[i]:
            Max = lst[i]
        if Min > lst[i]:
            Min = lst[i]
    ans = Max - Min
    print(f'#{test_case} {ans}')