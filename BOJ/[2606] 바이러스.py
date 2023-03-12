N = int(input())  # 정점 수
M = int(input())  # 간선 수

# 양방향 그래프 그리기
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    st, ed = map(int, input().split())
    arr[st][ed] = 1
    arr[ed][st] = 1

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