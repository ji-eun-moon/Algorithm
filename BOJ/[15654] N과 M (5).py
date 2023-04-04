N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
path = [0]*M
used = [0]*N

def dfs(level):
    if level == M:
        print(*path)
        return
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            path[level] = num[i]
            dfs(level+1)
            path[level] = 0
            used[i] = 0

dfs(0)