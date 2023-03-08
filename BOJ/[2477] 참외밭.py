K = int(input())  # 1 면적에 자라는 참외의 개수
xlst = []  # 1, 2 동 서
ylst = []  # 3, 4 남 북
for _ in range(6):
    d, l = map(int, input().split())
    if d == 1 or d == 2:
        xlst.append(l)
    else:
        ylst.append(l)

Max = max(xlst)*max(ylst)

print(K*area)
