N, K = map(int, input().split())
coins = [0]
for _ in range(N):
    coins.append(int(input()))
coins.sort()
dp = [[10001]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j % coins[i] == 0:
            dp[i][j] = j//coins[i]
        else:
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i]])

if dp[N][K] == 10001:
    print(-1)
else:
    print(dp[N][K])