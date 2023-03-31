N, K = map(int, input().split())
coins = [0]
for _ in range(N):
    coins.append(int(input()))
coins.sort()
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        continue

