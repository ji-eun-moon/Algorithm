import sys
input = sys.stdin.readline

N = int(input())
lst = [0]+list(map(int, input().split()))

# dp 테이블 초기화
dp = [0]*(N+1)

for i in range(1, N+1):
    Max = 0
    for j in range(0, i):
        if lst[i] > lst[j]:
            Max = max(Max, dp[j])
    dp[i] = Max + 1

# 중간에 최댓값이 있을 수 있으므로
print(max(dp))