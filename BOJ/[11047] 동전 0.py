N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0
i = 0
while True:
    if K == 0:
        break
    if K >= coins[i]:
        n = K//coins[i]
        K = K - n*coins[i]
        cnt += n  # 동전 개수 더하기
        i += 1
    else:
        i += 1

print(cnt)
