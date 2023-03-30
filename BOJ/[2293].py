N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0
Min = 21e8
def abc(changes):
    global cnt
    if changes < 0:
        return
    if changes == 0:
        cnt += 1
        return
    for i in range(3):
        abc(changes-coins[i])

abc(K)
print(cnt)