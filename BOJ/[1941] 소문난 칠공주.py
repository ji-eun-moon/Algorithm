from collections import deque

arr = [list(input()) for _ in range(5)]
direct_y = [0, -1, 1, 0, 0]
direct_x = [0, 0, 0, -1, 1]
used = [[0]*5 for _ in range(5)]
path = [0]*7
cnt = 0
def dfs(level, y, x):
    global cnt
    if level == 7:
        if path.count('S') >= 4:
            cnt += 1
            return
        else:
            return
    for i in range(5):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < 5 and 0 <= dx < 5:
            if used[dy][dx] == 0:
                path[level] = arr[dy][dx]
                used[dy][dx] = 1
                dfs(level+1, dy, dx)
                used[dy][dx] = 0
                path[level] = 0

dfs(0, 0, 0)
print(cnt)




