# 둘레인지 확인하는 함수
def check(y, x):
    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < 100 and 0 <= dx < 100:
            # 주위에 0이 한개라도 있으면 둘레
            if arr[dy][dx] == 0:
                return 1

N = int(input())
arr = [[0]*100 for _ in range(100)]
lst = []

# 색종이 좌표 입력
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])

# 색종이 칠하기
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
            if check(i, j):
                cnt += 1

print(cnt)