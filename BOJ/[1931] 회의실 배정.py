N = int(input())
lst = []

for _ in range(N):
    st, ed = map(int, input().split())
    lst.append([st, ed])

lst.sort(key=lambda x: (x[1], x[0]))

start = 0
cnt = 0
for i in range(N):
    if lst[i][0] >= start:
        cnt += 1
        start = lst[i][1]

print(cnt)