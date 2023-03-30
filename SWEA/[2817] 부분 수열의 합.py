T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))  # N 개의 자연수

    cnt = 0
    def dfs(level, start, Sum):
        global cnt
        if Sum > K:
            return
        if level == N:
            return
        if Sum == K:
            cnt += 1
            return
        for i in range(start, N):
            dfs(level, i+1, Sum + A[i])

    dfs(0, 0, 0)

    print(f'#{test_case} {cnt}')
