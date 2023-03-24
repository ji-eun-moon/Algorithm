N, M = map(int, input().split())  # 방의 크기
R, C, d = map(int, input().split())  # 로봇청소기 좌표, 방향 (0-북, 1-동, 2-남, 3-서)

# 뒤를 확인하는 딕셔너리
back = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}
# 앞을 확인하는 딕셔너리
front = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

arr = [list(map(int, input().split())) for _ in range(N)]  # 장소의 상태
cnt = 0
def clean(y, x):
    global d, cnt
    if arr[y][x] == 0:
        arr[y][x] = 2
        cnt += 1
    # 주위 4칸 확인
    for _ in range(4):
        # 반시계 방향 회전
        d = (d-1) % 4
        # 앞의 좌표
        fy = y + front[d][0]
        fx = x + front[d][1]
        # 앞이 청소 되지 않은 빈칸인 경우
        if 0 <= fy < N and 0 <= fx < M:  # 범위 확인
            if arr[fy][fx] == 0:
                # 전진 하고 좌표 갱신
                return clean(fy, fx)
    # for문 다 돌았는데도 return 안됐다면 4칸 중에 청소 되지 않은 빈칸이 없는 경우
    # 뒤의 좌표
    by = y + back[d][0]
    bx = x + back[d][1]
    # 뒤가 벽이 아니라면
    if arr[by][bx] != 1:
        # 후진 하고 좌표 갱신
        return clean(by, bx)
    # 후진할 수 없다면 함수 종료
    else:
        return cnt

answer = clean(R, C)
print(answer)