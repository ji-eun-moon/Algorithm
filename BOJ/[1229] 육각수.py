'''
N 을 만들기 위해 필요한 육각수 개수의 최솟값
육각수 : 육각형을 점 하나만 겹치게 그렸을 때 존재하는 서로 다른 점의 개수
h1 = 1
h2 = 6
h3 = 15
h4 = 28
...
-> hn = n(2n -1)
'''
N = int(input())
INF = float("inf")

# 1~N 사이의 육각수
hex_number = {}
for i in range(1, N+1):
    tmp = i * (2*i - 1)
    hex_number[tmp] = True

# DP[i] = i 를 만들 수 있는 육각수의 최소 개수
dp = [0, 1, 2, 3, 4, 5] + [INF] * N

for i in range(6, N+1):
    # 육각수로 이루어진 값인 경우
    if i in hex_number:
        dp[i] = 1
    else:
        for hex in hex_number:
            if hex > i:
                break
            dp[i] = min(dp[i], dp[i-hex] + 1)

print(dp[N])
