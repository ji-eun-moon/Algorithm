st = list(input())
Min = 21e8
temp = []
for i in range(1, len(st)+1):
    for j in range(len(st)//i):
        temp.append(st[i*j:i*(j+1)])
    ans = len(st)
    for k in range(len(st)//i):
        cnt = 1
        while True:
            if len(temp) == 1:
                break
            if temp[0] == temp[1]:
                temp.pop(0)
                cnt += 1
            else:
                temp.pop(0)
                break
        if cnt > 1:
            ans -= (i*cnt-(1+i))
    if Min > ans:
        Min = ans

print(Min)