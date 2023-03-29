N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
used = [[0]*N for _ in range(N)]

direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]

result = '불가능'

def dfs(y, x):
    global result
    if y == N-1 and x == N-1:
        result = '가능'
        return
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < N and 0 <= dx < N:
            if arr[dy][dx] == 0 and used[dy][dx] == 0:
                used[dy][dx] = 1
                dfs(dy, dx)
                used[dy][dx] = 0

dfs(0, 0)
print(result)