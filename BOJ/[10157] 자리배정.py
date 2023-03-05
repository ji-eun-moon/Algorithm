C, R = map(int, input().split())  # 공연장 크기 x, y
K = int(input())  # 관객 번호
arr = [[0]*C for _ in range(R)]

# 상 우 하 좌 순서대로
direct_y = [-1, 0, 1, 0]
direct_x = [0, 1, 0, -1]
i = 0
num = 1
flag = 0
stx, sty = 0, R-1
arr[sty][stx] = num
while True:
    if num == K:
        flag = 1
        x = stx + 1
        y = R - sty
        break
    if num == C*R:
        break
    dy = sty + direct_y[i]
    dx = stx + direct_x[i]
    if 0 > dy or dy >= R or 0 > dx or dx >= C or arr[dy][dx] != 0:  # 벽을 만나면
        i = (i + 1) % 4  # 방향 전환
        continue
    num += 1
    arr[dy][dx] = num
    stx = dx
    sty = dy

if flag == 1:
    print(x, y)
else:
    print(0)