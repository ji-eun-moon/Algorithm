# DFS
N, M, X = map(int, input().split())  # N - 학생 수, M - 정보 개수, X - 등수를 알고 싶은 학생

up = [[] for _ in range(N+1)]
down = [[] for _ in range(N+1)]

arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())  # A가 B보다 잘했다.
    down[A].append(B)  # A 보다 못하는 친구들
    up[B].append(A)  # B 보다 잘하는 친구들

visited = [0]*(N+1)
U, V = 1, N

# num 보다 높거나 낮은 학생이 몇 명 있는지 세는 함수
def dfs(num, arr):
    cnt = 1
    visited[num] = 1  # dfs 진입 시 방문 체크
    for nextNum in arr[num]:  # 나보다 낮은/높은 학생이 있고
        if not visited[nextNum]:  # 아직 방문한 적이 없으면
            cnt += dfs(nextNum, arr)  # dfs 진입
    return cnt

U += dfs(X, up) - 1
V -= dfs(X, down) - 1

print(U)
print(V)

# BFS

from collections import deque

def bfs(num, arr):
    cnt = 0
    q = deque()
    q.append(num)
    visited[num] = 1
    while q:
        num = q.popleft()
        for next in arr[num]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1
                cnt += 1
    return cnt

N, M, X = map(int, input().split())  # N - 학생 수, M - 정보 개수, X - 등수를 알고 싶은 학생

up = [[] for _ in range(N+1)]
down = [[] for _ in range(N+1)]

arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())  # A가 B보다 잘했다.
    down[A].append(B)  # A 보다 못하는 친구들
    up[B].append(A)  # B 보다 잘하는 친구들

visited = [0]*(N+1)
U, V = 1, N

U += bfs(X, up)
V -= bfs(X, down)

print(U)
print(V)

# DFS - 전역 변수 사용
N, M, X = map(int, input().split())  # N - 학생 수, M - 정보 개수, X - 등수를 알고 싶은 학생

up = [[] for _ in range(N+1)]
down = [[] for _ in range(N+1)]

arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())  # A가 B보다 잘했다.
    down[A].append(B)  # A 보다 못하는 친구들
    up[B].append(A)  # B 보다 잘하는 친구들

visited = [0]*(N+1)
U, V = 1, N

# num 보다 높거나 낮은 학생이 몇 명 있는지 세는 함수
def dfs(num, arr):
    global cnt
    visited[num] = 1  # dfs 진입 시 방문 체크
    for nextNum in arr[num]:  # 나보다 낮은/높은 학생이 있고
        if not visited[nextNum]:  # 아직 방문한 적이 없으면
            cnt += 1
            dfs(nextNum, arr)  # dfs 진입

cnt = 0
dfs(X, up)
U += cnt

cnt = 0
dfs(X, down)
V -= cnt

print(U)
print(V)