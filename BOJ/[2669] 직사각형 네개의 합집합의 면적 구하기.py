arr = [[0]*100 for _ in range(100)]

def color(a, b, c, d):  # 주어진 좌표로 이루어진 사각형을 색칠하는 함수
    for i in range(b, d):
        for j in range(a, c):
            arr[i][j] = 1

for i in range(4):  # 좌표 입력 받고 색칠하기
    a, b, c, d = map(int, input().split())
    color(a, b, c, d)

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)