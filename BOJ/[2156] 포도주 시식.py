N = int(input())
wine = [0]

for _ in range(N):
    wine.append(int(input()))

# dp 테이블 초기화
dp = [0]*(N+1)
dp[1] = wine[1]
if N > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], wine[i]+wine[i-1]+dp[i-3])

print(dp[N])