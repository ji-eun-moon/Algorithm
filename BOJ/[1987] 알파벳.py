R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]
ans = 0
cnt = 1
def dfs(y, x):
    global ans, cnt
    ans = max(ans, cnt)
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < R and 0 <= dx < C:
            if arr[dy][dx] not in path:
                path.append(arr[dy][dx])
                cnt += 1
                dfs(dy, dx)
                cnt -= 1
                path.remove(arr[dy][dx])

path = [arr[0][0]]
dfs(0, 0)
print(ans)

# 교수님 풀이 - 1 : pypy로 풀이시 정답

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]

def dfs(ci, cj, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        dy = ci + direct_y[i]
        dx = cj + direct_x[i]
        if 0 <= dy < R and 0 <= dx < C:
            if visited[ord(arr[dy][dx])] == 0:
                visited[ord(arr[dy][dx])] = 1
                dfs(dy, dx, cnt+1)
                visited[ord(arr[dy][dx])] = 0

ans = 1
visited = [0]*128
visited[ord(arr[0][0])] = 1
dfs(0, 0, 1)
print(ans)

# 교수님 풀이 - 2 : bfs
from collections import deque

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

def bfs():
    q = deque()
    # list는 O(N), set은 O(1)
    v = [[set() for _ in range(C)] for _ in range(R)]
    ans = 1

    # q에 초기 데이터 삽입
    q.append((0, 0, arr[0][0]))
    v[0][0].add(arr[0][0])

    while q:
        ci, cj, cv = q.popleft()  # y좌표, x좌표, 시퀀스
        ans = max(ans, len(cv))
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            # 범위 확인
            if 0 <= ni < R and 0 <= nj < C:
                # 알파벳이 중복되지 않아야 함
                if arr[ni][nj] not in cv:
                    # 시퀀스가 중복되지 않아야 함 (HAJ랑 HFJ랑 경로가 다르다)
                    if cv + arr[ni][nj] not in v[ni][nj]:
                        q.append((ni, nj, cv+arr[ni][nj]))
                        v[ni][nj].add((cv+arr[ni][nj]))
    return ans

print(bfs())