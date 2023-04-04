from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*N for _ in range(N)]
    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]

    result = []
    def bfs():
        q = deque()
        q.append([0, 0])  # 시작점
        while q:
            y, x = q.popleft()
            for i in range(4):
                dy = y + direct_y[i]
                dx = x + direct_x[i]
                if 0 <= dy < N and 0 <= dx < N:
                    # 높이 차 계산하기
                    if arr[dy][dx] > arr[y][x]:
                        extra = abs(arr[dy][dx] - arr[y][x])
                    else:
                        extra = 0

                    if used[dy][dx] == 0:  # 아직 방문하지 않은 곳이라면
                        used[dy][dx] += (used[y][x] + extra + 1)  # 높이차 + cnt
                        q.append((dy, dx))
                    else:  # 방문해 본 곳인데
                        if used[dy][dx] > (used[y][x] + extra + 1):  # 더 적은 비용으로 갈 수 있다면
                            used[dy][dx] = (used[y][x] + extra + 1)  # 값 갱신하고
                            q.append([dy, dx])  # 다시 q에 넣어주기

    bfs()

    print(f'#{test_case} {used[N-1][N-1]}')