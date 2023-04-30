N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

direct_y = [-1, 1, 0, 0]
direct_x = [ 0, 0, -1, 1]
def dfs(y, x):
    max_y, max_x, min_y, min_x = y, x, y, x
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                new_max_y, new_max_x, new_min_y, new_min_x = dfs(dy, dx)
                max_y = max(max_y, new_max_y)
                min_y = min(min_y, new_min_y)
                max_x = max(max_x, new_max_x)
                min_x = min(min_x, new_min_x)
    return max_y, max_x, min_y, min_x

Max = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            max_y, max_x, min_y, min_x = dfs(i, j)
            rec = ((max_y - min_y + 1) + (max_x - min_x + 1))*2 + 4
            Max = max(Max, rec)

print(Max)