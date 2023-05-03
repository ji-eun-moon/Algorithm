import sys
input=sys.stdin.readline

from collections import deque

N, M, K, X = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)

visited = [0]*(N+1)
def bfs(st):
    q = deque()
    q.append(st)
    visited[st] = 1
    answer = []
    while q:
        now = q.popleft()
        if visited[now] == K+1:
            answer.append(now)
        for i in arr[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for a in answer:
            print(a)

bfs(X)
