T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 제품 수
    arr = [list(map(int, input().split())) for _ in range(N)]  # 공장별 생산 비용
    used = [0]*N  # 이미 생산한 공장인지 확인
    Sum = 0
    Min = 21e8
    def dfs(level):
        global Min, Sum
        if Sum > Min:
            return
        if level == N:
            Min = min(Min, Sum)
            return
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                Sum += arr[level][i]
                dfs(level+1)
                used[i] = 0
                Sum -= arr[level][i]

    dfs(0)
    print(f'#{test_case} {Min}')