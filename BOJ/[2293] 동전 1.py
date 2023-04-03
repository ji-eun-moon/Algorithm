N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort()

dp = [0]*(K+1)
dp[0] = 1
for coin in coins:
    for i in range(1, K+1):
        if i >= coin:
            dp[i] += dp[i-coin]

print(dp[K])
