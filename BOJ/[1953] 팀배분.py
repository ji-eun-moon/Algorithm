# DFS
def dfs(cur, team):
    visited[cur] = 1
    result[cur] = team
    for nxt in range(1, N+1):
        if nxt in hate[cur] and not visited[nxt]:
            dfs(nxt, -team)

N = int(input())  # 학생의 수

hate = {}  # 싫어하는 사람 정보

for i in range(1, N+1):
    hate[i] = set(list(map(int, input().split()))[1:])  # i가 싫어하는 사람 수, 사람들

# A가 B를 싫어하면 B도 A를 싫어한다.
for i in range(1, N+1):
    for j in hate[i]:
        hate[j].add(i)

blue, white = [], []
visited = [0] * (N+1)
result = [0] * (N+1)

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i, 1)

for i in range(1, N+1):
    if result[i] == -1:
        blue.append(i)
    elif result[i] == 1:
        white.append(i)

# 각 팀 오름차순 정렬
blue.sort()
white.sort()

print(len(blue))
print(*blue)
print(len(white))
print(*white)


# BFS
from collections import deque

N = int(input())  # 학생의 수

hate = {} # 싫어하는 사람 정보

for i in range(1, N+1):
    hate[i] = set(list(map(int, input().split()))[1:])  # i+1 가 싫어하는 사람 수, 사람들

# A가 B를 싫어하면 B도 A를 싫어한다.
for i in range(1, N+1):
    for j in hate[i]:
        hate[j].add(i)

blue, white = [], []
visited = [0] * (N+1)
result = [0] * (N+1)

def bfs(cur, team):

    q = deque()
    q.append((cur, team))
    visited[cur] = 1
    result[cur] = team

    while q:
        cur, team = q.popleft()
        for nxt in range(1, N+1):
            # 싫어하는 사람이면 다른 팀에 배정
            if nxt in hate[cur] and not visited[nxt]:
                visited[nxt] = 1
                result[nxt] = -team
                q.append((nxt, -team))

for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i, 1)

for i in range(1, N+1):
    if result[i] == -1:
        blue.append(i)
    elif result[i] == 1:
        white.append(i)

# 각 팀 오름차순 정렬
blue.sort()
white.sort()

print(len(blue))
print(*blue)
print(len(white))
print(*white)
print(hate)