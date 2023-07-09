from sys import stdin
input = stdin.readline
from collections import deque

N, K = map(int, input().split())
visited = [0]*1000001
cnt = 0
def bfs(st):
    global cnt
    q = deque()
    q.append(st)
    visited[st] = 1
    while q:
        x = q.popleft()
        if x == K:
            cnt += 1
        move = [-1, 1, x]
        for i in range(3):
            dx = x + move[i]
            if 0 <= dx < 100001:
                # 첫 방문 또는 방믄 시간이 같은 경우
                if visited[dx] == 0 or visited[dx] == visited[x] + 1:
                    visited[dx] = visited[x] + 1
                    q.append(dx)

bfs(N)
print(visited[K] - 1)
print(cnt)