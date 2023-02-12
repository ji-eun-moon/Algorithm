def color(y, x):
    for a in range(10):
        for b in range(10):
            arr[y-a][x+b] += 1

arr = [[0]*100 for _ in range(100)]

T = int(input())
for _ in range(T):
    dy, dx = map(int, input().split())
    color(dy, dx)

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > 0:
            ans += 1

print(ans)