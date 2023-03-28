T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    number = list(range(2, N+1))
    used = [0]*(N+1)
    # 2 ~ N 숫자 조합을 담을 리스트
    path = [0]*(N+1)
    # 맨 앞 뒤는 사무실(1)
    path[0], path[-1] = 1, 1

    result = []
    def dfs(level):
        global result
        # 조합 끝까지 생성하면
        if level == N:
            # 배터리 소비량 계산하여 result에 담기
            Sum = 0
            for j in range(N):
                Sum += arr[path[j]-1][path[j+1]-1]
            result.append(Sum)
            return
        # 2부터 N까지 조합 생성
        for i in range(2, N+1):
            if used[i] == 0:
                used[i] = 1
                path[level] = i
                dfs(level+1)
                used[i] = 0
                path[level] = 0

    dfs(1)
    # result의 최소값 출력
    print(f'#{test_case} {min(result)}')