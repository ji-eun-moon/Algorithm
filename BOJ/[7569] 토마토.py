from collections import deque

direct_h = [0, 0, 0, 0, -1, 1]
direct_y = [-1, 1, 0, 0, 0, 0]
direct_x = [0, 0, -1, 1, 0, 0]

def bfs():
    # [1] q 생성, v 생성
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]

    # [2] q에 초기 데이터 삽입, 안익은 토마토 카운트
    cnt = 0
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if arr[h][y][x] == 1 :  # 익은 토마토인 경우
                    q.append((h, y, x))
                    v[h][y][x] = 1
                elif arr[h][y][x] == 0:  # 안익은 토마토인 경우
                    cnt += 1

    while q:
        h, y, x = q.popleft()
        # 6 방향 범위 내, 미방문, arr[] == 0
        for i in range(6):
            dh = h + direct_h[i]
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dh < H and 0 <= dy < N and 0 <= dx < M:
                if v[dh][dy][dx] == 0:
                    if arr[dh][dy][dx] == 0:
                        q.append((dh, dy, dx))
                        v[dh][dy][dx] = v[h][y][x] + 1
                        cnt -= 1  # 안익은 토마토 1개 익음

    if cnt == 0:  # 모든 토마토가 익음
        return v[h][y][x] - 1
    else:
        return -1


M, N, H = map(int, input().split())  # 가로, 세로, 높이

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

ans = bfs()
print(ans)