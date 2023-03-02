N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for paper in range(1, N+1):
    y, x, a, b = map(int, input().split())
    for i in range(b):
        for j in range(a):
            arr[x+i][y+j] = paper

for paper in range(1, N+1):
    cnt = 0
    for n in range(1001):
        cnt += arr[n].count(paper)
    print(cnt)