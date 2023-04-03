N, M = map(int, input().split())
path = [0]*M
used = [0]*(N+1)
def dfs(level):
    if level == M:
        print(*path)
        return
    for i in range(1, N+1):
        if used[i] == 0:
            used[i] = 1
            path[level] = i
            dfs(level+1)
            used[i] = 0
            path[level] = 0

dfs(0)
