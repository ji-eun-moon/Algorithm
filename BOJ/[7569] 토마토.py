# 풀이중

M, N, H = map(int, input().split())  # 가로, 세로, 높이

arr = []

# 토마토 담기
for _ in range(H):
    temp = [list(map(int, input().split())) for _ in range(N)]
    arr.append(temp)

# 토마토 개수
tomato = 0
for a in arr:
    for b in a:
        for c in b:
            if c != -1:
                tomato += 1

# 토마토 모두 익었는지 확인
def tomato_count():
    Sum = 0
    for a in arr:
        for b in a:
            for c in b:
                if c == 1:
                    Sum += 1
    if Sum == tomato:
        return 1

# 주위에 익은 토마토가 있는지 확인하고 익히기
def check_tomato(h, y, x):
    direct_h = [0, 0, 0, 0, -1, 1]
    direct_y = [-1, 1, 0, 0, 0, 0]
    direct_x = [0, 0, -1, 1, 0, 0]
    for i in range(6):
        dh = h + direct_h[i]
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dh < H and 0 <= dy < N and 0 <= dx < M:
            if arr[dh][dy][dx] == 1:
                return 1
    return 0

# 토마토가 모두 익지 못하는 상황 ? - 주위에 -1만 있는 경우 (0이나 1이 0개인 경우)
def tomato(h, y, x):
    direct_h = [0, 0, 0, 0, -1, 1]
    direct_y = [-1, 1, 0, 0, 0, 0]
    direct_x = [0, 0, -1, 1, 0, 0]
    cnt = 0
    for i in range(6):
        dh = h + direct_h[i]
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dh < H and 0 <= dy < N and 0 <= dx < M:
            if arr[dh][dy][dx] == 0 or arr[dh][dy][dx] == 1:
                cnt += 1
    if cnt == 0:
        return 1

def problem():
    time = 0
    while True:
        # 토마토가 전부 익으면 break
        if tomato_count():
            return time
        for h in range(H):
            for y in range(N):
                for x in range(M):
                    if arr[h][y][x] == 0:
                        if check_tomato(h, y, x):
                            arr[h][y][x] = 1
                        if tomato(h, y, x):
                            return -1
        time += 1

time = problem()
print(time)


