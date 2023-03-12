from collections import deque

N, M, V = map(int, input().split())  # 정점개수, 간선개수, 탐색 시작할 정점 번호

# dfs
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    st, ed = map(int, input().split())
    arr[st][ed] = 1
    arr[ed][st] = 1

result_dfs = []
def dfs(now):
    result_dfs.append(now)
    for i in range(N+1):
        if arr[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
visited[V] = 1
dfs(V)
print(*result_dfs)

# bfs

visited = [0]*(N+1)
result_bfs = []
def bfs(st):
    global result_bfs
    q = deque()
    q.append(st)
    visited[st] = 1
    while q:
        now = q.popleft()
        result_bfs.append(now)
        for i in range(N+1):
            if arr[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)

visited[V] = 1
bfs(V)
print(*result_bfs)