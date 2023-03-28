T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    direct_y = [1, 0]
    direct_x = [0, 1]
    Min = 21e8
    def dfs(y, x, Sum):
        global Min
        if Sum > Min:
            return
        if y == N-1 and x == N-1:
            Min = min(Sum, Min)
        for i in range(2):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < N and 0 <= dx < N and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                dfs(dy, dx, Sum + arr[dy][dx])
                visited[dy][dx] = 0

    
    dfs(0, 0, arr[0][0])
    print(f'#{test_case} {Min}')