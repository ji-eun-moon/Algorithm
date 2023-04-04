# 조합

N, M = map(int, input().split())
path = [0]*M

def dfs(level, start):
    if level == M:
        print(*path)
        return
    for i in range(start, N+1):
        path[level] = i
        dfs(level+1, i+1)
        path[level] = 0

dfs(0, 1)