N = int(input())
arr = [[0]*100 for _ in range(100)]
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])

for a in lst:
    for i in range(10):
        for j in range(10):
            arr[a[1]+j][a[0]+i] = 1

for a in lst:
    for i in range(1, 9):
        for j in range(1, 9):
            arr[a[1]+j][a[0]+i] = 0

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)