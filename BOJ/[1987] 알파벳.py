# 풀이 중

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]

def dfs(y, x):

    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < R and 0 <= dx < C:
            if arr[dy][dx] not in path:
                path.append(arr[dy][dx])
                dfs(dy, dx)


path = [arr[1][1]]
dfs(1, 1)