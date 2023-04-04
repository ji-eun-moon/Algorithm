N, M = map(int, input().split())
num = list(map(int, input().split()))

num.sort()

path = [0]*M
used = [0]*N
result = []

def dfs(level):
    if level == M:
        result.append(path[:])
        return
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            path[level] = num[i]
            dfs(level+1)
            path[level] = 0
            used[i] = 0

dfs(0)

result.sort()

for i in range(len(result)):
    if i == 0:
        print(*result[i])
    else:
        if result[i] != result[i-1]:
            print(*result[i])
