from collections import deque

N = int(input())  # 학생의 수

hate = {}  # 싫어하는 사람 정보

for i in range(N):
    hate[i+1] = set(map(int, input().split()))  # i+1 가 싫어하는 사람들

blue, white = [], []
visited = [0]*(N+1)
result = ["blue"] * (N+1)

def bfs(cur, team):
    q = deque()
    q.append((cur, team))

    while q:
        cur, team = q.popleft()
        for nxt in range(1, N+1):
            # 싫어하는 사람이면 다른 팀에 배정
            if nxt in hate[cur] and not visited[nxt]:
                visited[nxt] = 1
                result[nxt] = "white"
                q.append((nxt, "blue"))

for i in range(1, N+1):
    if not visited[i]:
        bfs(i, "blue")

for i in range(1, N+1):
    if result[i] == "blue":
        blue.append(i)
    elif result[i] == "white":
        white.append(i)

# 각 팀 오름차순 정렬
blue.sort()
white.sort()

print(len(blue))
print(*blue)
print(len(white))
print(*white)
print(hate)