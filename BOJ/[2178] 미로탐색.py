# dfs - 시간초과
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]

cnt = 1
Min = 21e8
def miro(y, x):
    global cnt, Min
    if y == N-1 and x == M-1:
        if Min > cnt:
            Min = cnt
        return
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                cnt += 1
                miro(dy, dx)
                visited[dy][dx] = 0
                cnt -= 1

visited[0][0] = 1
miro(0, 0)
print(Min)

# bfs - 정답

N, M = map(int, input().split())  # 세로, 가로
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]

sty, stx = 0, 0
edy, edx = N-1, M-1

def bfs(sty, stx):
    q = []
    q.append((sty, stx))
    visited[sty][stx] = 1
    while q:
        y, x = q.pop(0)
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                    visited[dy][dx] += visited[y][x] + 1
                    q.append((dy, dx))
                if dy == edy and dx == edx:
                    return visited[y][x] + 1

print(bfs(sty,stx))