K = int(input())  # 1 면적에 자라는 참외의 개수
xlst = []  # 1, 2 동 서
ylst = []  # 3, 4 남 북
lst = []  # 전체
for _ in range(6):
    d, l = map(int, input().split())
    lst.append(l)
    if d == 1 or d == 2:
        xlst.append(l)
    else:
        ylst.append(l)

small_lst=[]
for i in range(6):
    if lst[(i-1)%6] + lst[(i+1)%6] == max(xlst) or lst[(i-1)%6] + lst[(i+1)%6] == max(ylst):
        small_lst.append(lst[i])

big = max(xlst)*max(ylst)
small = small_lst[0]*small_lst[1]
area = big - small
print(K*area)
