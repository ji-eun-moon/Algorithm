N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
item = [[0, 0]]
for _ in range(1, N+1):
    W, V = map(int, input().split())
    item.append([W, V])

Max = 0
for i in range(1, N+1):
    for j in range(1, K+1):

        weight = item[i][0]
        value = item[i][1]

        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])

print(dp[N][K])