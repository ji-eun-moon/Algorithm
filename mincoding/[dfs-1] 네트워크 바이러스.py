N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

visited = [0]*(N+1)
cnt = 0
def dfs(now):
    global cnt
    for i in range(N+1):
        if arr[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfs(i)

visited[1] = 1
dfs(1)
print(cnt)