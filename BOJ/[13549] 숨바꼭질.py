import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())  # 수빈, 동생
visited = [0]*100001
def bfs(st):
    q = deque()
    q.append(st)
    visited[st] = 1
    while q:
        x = q.popleft()
        if x == K:
            return visited[x] - 1
        move = (x, -1, 1)  # 순서 중요
        for i in range(3):
            dx = x + move[i]
            if 0 <= dx < 100001:
                if visited[dx] == 0:
                    if i == 0:
                        visited[dx] = visited[x]
                        q.appendleft(dx)
                    else:
                        visited[dx] = visited[x] + 1
                        q.append(dx)
print(bfs(N))