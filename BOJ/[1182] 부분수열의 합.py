N, S = map(int, input().split())
num = list(map(int, input().split()))
path = []
cnt = 0
def dfs(level, start):
    global cnt
    if level == N:
        return
    for i in range(start, N):
        path.append(num[i])
        if sum(path) == S:
            cnt += 1
        dfs(level+1, i+1)
        path.pop()
dfs(0, 0)
print(cnt)