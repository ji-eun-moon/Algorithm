from collections import deque

N, M = map(int, input().split())  # 노드, 노드 쌍 개수
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

def bfs(st, ed):
    q = deque()
    q.append(st)
    visited = [0]*(N+1)
    visited[st] = 1
    while q:
        now = q.popleft()
        if now == ed:
            return visited[ed] - 1
        for (nxt, w) in arr[now]:
            if visited[nxt] == 0:
                visited[nxt] = visited[now] + w
                q.append(nxt)

for _ in range(M):
    st, ed = map(int, input().split())
    print(bfs(st, ed))