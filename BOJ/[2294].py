N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

dp = [[0]*(K+1) for _ in range(N)]

for i in range(N):
    for j in range(K+1):
        if j % coins[i] == 0:
            dp[i][j] = j//coins[i]
        else:
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], j//coins[i] + dp[i][j%coins[i]])

print(dp[N-1][K])