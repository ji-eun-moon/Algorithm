N, M = map(int, input().split())  # 패의 개수, 뽑아야하는 개수
lst = list(map(int, input().split()))
Min = 21e8
used = [0]*N
path = []
result = [0]*M
def dfs(level, gop):
    global Min, result
    if level == M:
        if gop < Min:
            Min = gop
            for i in range(M):
                result[i] = path[i]
        return
    for i in range(N):
        if used[i] == 0:
            path.append(lst[i])
            used[i] = 1
            dfs(level+1, gop*lst[i])
            path.pop()
            used[i] = 0

dfs(0, 1)
result.sort()
print(*result)