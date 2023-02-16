N, M = map(int, input().split())
y, x, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
used = [[0]*M for _ in range(N)]  # 방문 체크 배열

def check(y, x):  # y, x 좌표로 갈 수 있는지 확인하는 함수
    if arr[y][x] == 0 and used[dy][dx] == 0:
        return 1
    else:
        return 0

cnt = 0  # 캐릭터가 방문한 칸 수

# 북(0), 동(1), 남(2), 서(3) 차례대로 왼쪽 방향을 가리키는 배열
left_y = [0, -1, 0, 1]
left_x = [-1, 0, 1, 0]

# 뒤를 가리키는 배열
behind_y = [1, 0, 1, 0]
behind_x = [0, -1, 0, 1]

flag = 0  # 회전 수 체크
while True:
    dy = y + left_y[d]
    dx = x + left_x[d]
    if check(dy, dx) == 1:  # 갈 수 있는 칸이면
        y = dy  # 좌표 변경하고
        x = dx
        d = d - 1 if d-1 >= 0 else d + 3  # 왼쪽으로 회전
        cnt += 1  # 이동 수 카운트 추가
        used[dy][dx] = 1  # 방문 체트
    else:  # 못가면
        if flag == 4:  # 네번 회전했는데도 못갔으면
            y = y + behind_y[d]  # 뒤로 한칸 가고
            x = x + behind_x[d]
            cnt += 1  # 이동수 카운트 추가
            if arr[y][x] == 1:  # 뒤도 바다가 있으면
                break  # stop
            continue  # 그렇지 않으면 1단계로 가기
        d = d - 1 if d - 1 >= 0 else d + 3  # 회전만
        flag += 1  # 회전 수 추가

print(cnt)