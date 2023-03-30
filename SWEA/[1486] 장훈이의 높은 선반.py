T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())  # 점원 수
    H = list(map(int, input().split()))  # 점원의 키
    Min = 21e8
    def dfs(level, start, Sum):
        global Min
        if Sum >= B:
            cha = Sum - B
            Min = min(cha, Min)
            return
        if level == N:
            return
        for i in range(start, N):
            dfs(level+1, i+1, Sum+H[i])

    dfs(0, 0, 0)
    print(f'#{test_case} {Min}')