G, S = map(int, input().split())
N = int(input())

Glst = [0, G]
Slst = [0, S]

for _ in range(N):
    d, idx = map(int, input().split())
    if d == 0:
        Slst.append(idx)
    elif d == 1:
        Glst.append(idx)

Glst.sort()
Slst.sort()

Max = 0
for i in range(1, len(Glst)):
    for j in range(1, len(Slst)):
        tmp = (Glst[i] - Glst[i-1])*(Slst[j] - Slst[j-1])
        if Max < tmp:
            Max = tmp

print(Max)