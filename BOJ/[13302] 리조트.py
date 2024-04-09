'''
하루 이용권 - 10000원
연속 3일권 - 25000원 -> 쿠폰 1장
연속 5일권 - 37000원 -> 쿠폰 2장
쿠폰 3장 = 하루 이용권
'''

N, M = map(int, input().split())  # 여름방학 일수, 리조트에 갈 수 없는 날 수

if M == 0:
    holidays = {}
else:
    holidays = set(map(int, input().split()))  # 리조트에 갈 수 없는 날

INF = float("inf")
# dp[i][j] = i 번째 날에 j 개의 쿠폰을 가지고 있는 경우
dp = [[INF] * 110 for _ in range(110)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(40):
        if dp[i][j] == INF:
            continue

        tmp = dp[i][j]

        # 리조트에 가지 못하는 경우
        if i+1 in holidays:
            # 쿠폰 개수 그대로 다음 날로
            dp[i+1][j] = min(tmp, dp[i+1][j])

        # 쿠폰이 3장 이상 있는 경우
        if j >= 3:
            # 금액 증가 없이 1일 이용
            dp[i+1][j-3] = min(tmp, dp[i+1][j-3])

        # 1일권 구매
        dp[i+1][j] = min(tmp + 10000, dp[i+1][j])

        # 연속 3일권 - 25000원 -> 쿠폰 1장
        for k in range(1, 4):
            dp[i+k][j+1] = min(tmp + 25000, dp[i+k][j+1])

        # 연속 5일권 - 37000원 -> 쿠폰 2장
        for k in range(1, 6):
            dp[i+k][j+2] = min(tmp+37000, dp[i+k][j+2])


print(min(dp[N]))
