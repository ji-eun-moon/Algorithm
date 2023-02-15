st = list(input())
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # x 인덱스 찾기 위한 배열
y = int(st[1]) - 1  # 입력 값이 1~8 이므로 인덱스 구하기 위해서 1 빼기
for i in range(8):
    if st[0] == arr[i]:
        x = i  # x 인덱스 찾기

direct_y = [2, 2, -2, -2, -1, 1, -1, 1]
direct_x = [-1, 1, -1, 1, 2, 2, -2, -2]

cnt = 0  # 경우의 수 초기화
for i in range(8):
    dy = y + direct_y[i]
    dx = x + direct_x[i]
    if 0 <= dy < 8 and 0 <= dx < 8:  # 이동할 수 있는 경우
        cnt += 1  # 카운트 추가

print(cnt)