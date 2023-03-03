def check(y, x):
    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]
    flag = 0
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < 102 and 0 <= dx < 102:
            if arr[dy][dx] == 0:
                flag += 1
    return flag

N = int(input())
arr = [[0]*102 for _ in range(102)]
lst = []

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[y+i][x+j] = 1

cnt = 0
for i in range(102):
    for j in range(102):
        if arr[i][j] == 1:
            cnt += check(i, j)

print(cnt)