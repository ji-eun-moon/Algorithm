T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())  # 마지막 연결지점 번호, 도로의 개수

    arr = [[0]*(N+1) for _ in range(N+1)]
    used = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w

    Min = 21e8
    def dfs(now, Sum):
        global Min
        if Sum > Min:
            return
        if now == N:
            Min = min(Sum, Min)
            return
        for i in range(N+1):
            if used[now][i] == 0 and arr[now][i] != 0:
                used[now][i] = 1
                dfs(i, Sum + arr[now][i])
                used[now][i] = 0

    dfs(0, 0)
    print(f'#{test_case} {Min}')
