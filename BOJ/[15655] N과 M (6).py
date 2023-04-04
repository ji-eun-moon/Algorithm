N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
path = [0]*M

def dfs(level, start):
    if level == M:
        print(*path)
        return
    for i in range(start, N):
        path[level] = num[i]
        dfs(level+1, i+1)
        path[level] = 0

dfs(0, 0)
