while True:
    K, *lst = map(int, input().split())
    if K == 0:
        break
    path = [0]*6
    def dfs(level, start):
        if level == 6:
            print(*path)
            return
        for i in range(start, K):
            path[level] = lst[i]
            dfs(level+1, i+1)
    dfs(0, 0)
    print()