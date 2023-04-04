N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
path = [0]*M

def dfs(level):
    if level == M:
        print(*path)
        return
    for i in range(N):
        path[level] = num[i]
        dfs(level+1)
        path[level] = 0

dfs(0)
