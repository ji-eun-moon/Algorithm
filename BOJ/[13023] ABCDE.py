import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N)]  # 친구 관계 인접리스트

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

result = 0
visited = [0]*N
def dfs(now, d):
    global result
    if d == 5:
        result = 1
        return
    else:
        visited[now] = 1
        for friend in arr[now]:
            if visited[friend] == 0:
                dfs(friend, d+1)
        visited[now] = 0

for i in range(N):
    dfs(i, 1)
    if result == 1:
        break

print(result)