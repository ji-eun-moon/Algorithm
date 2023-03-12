N = int(input())  # 정점 수
st, ed = map(int, input().split())
M = int(input())  # 간선 수

arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

# 양방향 연결 트리
for _ in range(M):
    x, y = map(int, input().split())  # 부모, 자식
    arr[x][y] = 1
    arr[y][x] = 1

flag = 0
cnt = 0
def dfs(now):
    global cnt, flag
    if now == ed:
        flag = 1
        print(cnt)
        return
    for i in range(N+1):
        if arr[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfs(i)
            cnt -= 1

visited[st] = 1
dfs(st)
if flag == 0:
    print(-1)

# bfs

def bfs(st):
    q = []
    visited = [0]*(N+1)
    q.append(st)
    visited[st] = 1
    while q:
        c = q.pop(0)
        if c == ed:
            return visited[ed]-1
        for i in range(N+1):
            if arr[c][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] += visited[c] + 1
    return -1

print(bfs(st))