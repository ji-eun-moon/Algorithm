N = int(input())  # 방 개수
P = list(map(int, input().split()))  # 각 숫자의 가격
M = int(input())  # 비용

dp = [0] * (M+1)  # 각 금액으로 살 수 있는 가장 큰 방 번호
for i in range(N-1, -1, -1):
    price = P[i]
    for j in range(price, M+1):
        dp[j] = max(dp[j], int(str(dp[j-price])+str(i)))

print(dp[M])