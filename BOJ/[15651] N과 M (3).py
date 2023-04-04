N, M = map(int, input().split())
path = [0]*M

def dfs(level):
    if level == M:
        print(*path)
        return
    for i in range(1, N+1):
        path[level] = i
        dfs(level+1)
        path[level] = 0

dfs(0)