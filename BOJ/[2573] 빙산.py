N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]

# 빙하 녹이는 함수
def melt():
    # 빙하가 '동시에' 녹기 때문에 깊은 복사해서 0의 개수 확인
    temp = [a[:] for a in arr]
    for y in range(N):
        for x in range(M):
            cnt = 0
            if temp[y][x] != 0:
                for i in range(4):
                    dy = y + direct_y[i]
                    dx = x + direct_x[i]
                    if 0 <= dy < N and 0 <= dx < M:
                        # 음수일 경우도 확인하는 이유 - 이전에 빙하 녹을 때 음수가 될 수 있다.
                        if temp[dy][dx] <= 0:
                            cnt += 1
            arr[y][x] -= cnt


# 빙하 존재 확인
def bfs(y, x):
    cnt = 0
    q = []
    q.append((y, x))
    while q:
        cnt += 1
        y, x = q.pop(0)
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] > 0 and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    q.append((dy, dx))
    return cnt

flag = 0
time = 0
while True:
    visited = [[0]*M for _ in range(N)]
    result = []
    for y in range(N):
        for x in range(M):
            if arr[y][x] > 0 and visited[y][x] == 0:
                visited[y][x] = 1
                result.append(bfs(y, x))
    # 빙하 개수가 2개 이상이면 flag 켜고 break
    if len(result) >= 2:
        flag = 1
        break
    # 빙하 개수가 0이면 더이상 확인할 필요가 없으므로 break
    if len(result) == 0:
        break
    time += 1
    melt()

if flag == 0:
    time = 0

print(time)