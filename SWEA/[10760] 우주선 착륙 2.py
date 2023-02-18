def check(y, x):
    direct_y = [-1, -1, -1, 0, 0, 1, 1, 1]
    direct_x = [1, 0, -1, -1, 1, -1, 0, 1]
    flag = 0
    for i in range(8):  # 방향 배열 돌며
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] < arr[y][x]:  # 착륙지 높이보다 낮은 지역이 있을경우
                flag += 1  # flag + 1
    if flag >= 4:  # flag 4 이상이면 최적 착륙 장소
        return 1
    else:
        return 0

T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if check(i, j):  # 최적 착륙장소일경우
                cnt += 1  # cnt + 1

    print(f'#{test_case} {cnt}')


