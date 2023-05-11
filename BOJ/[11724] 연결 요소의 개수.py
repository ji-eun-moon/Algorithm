N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

def dfs(now):
    visited[now] = 1
    for i in range(1, N+1):
        if arr[now][i] == 1 and visited[i] == 0:
            dfs(i)


for i in range(1, N+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)