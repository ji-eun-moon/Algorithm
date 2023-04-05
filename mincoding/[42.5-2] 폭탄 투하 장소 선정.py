map = [list(input()) for _ in range(4)]
N = int(input())


def bomb(y, x):
    cnt = 0
    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < 4 and 0 <= dx < 4:
            if used[dy][dx] == 0 and map[dy][dx] != '_':
                used[dy][dx] = 1
                cnt += 1
    return cnt


used = [[0]*4 for _ in range(4)]
path = [0]*N
Max = 0
def dfs(level, cnt):
    global Max, answer
    if level == N:
        if Max < cnt:
            Max = cnt
            answer = path[:]
        return
    for i in range(4):
        for j in range(4):
            if used[i][j] == 0 and map[i][j] != '_':
                used[i][j] = 1
                path[level] = map[i][j]
                dfs(level+1, cnt + bomb(i, j) + 1)
                used[i][j] = 0


dfs(0, 0)
answer.sort()
print(*answer)