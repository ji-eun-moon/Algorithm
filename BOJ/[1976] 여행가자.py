# Solution 1 - BFS

from collections import deque

N = int(input())  # 도시의 수
M = int(input())  # 여행계획에 속한 도시의 수
cities = [list(map(int, input().split())) for _ in range(N)]  # 도시 연결 정보
plan = list(map(int, input().split()))  # 여행 계획
result = "YES"

# 여행 계획 순서대로 갈 수 있는지 BFS 탐색
def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [0] * N
    visited[start] = 1

    while q:
        current = q.popleft()

        # 다음 여행 계획지로 이동하면 True
        if current == end:
            return True

        for i in range(N):
            # 이동할 수 있는 다음 도시로 이동
            if cities[current][i] == 1 and not visited[i]:
                visited[i] = 1
                q.append(i)

    # 다음 여행 계획지로 이동하지 못하면 False
    return False

for i in range(M-1):
    canTravel = bfs(plan[i]-1, plan[i+1]-1)  # 도시의 번호는 1부터 시작
    if not canTravel:
        result = "NO"
        break

print(result)

# Solution 2 - Union Find
# 여행 계획이 모두 한 분리 집합 내에 속하면 YES, 아니면 NO 출력

N = int(input())  # 도시의 수
M = int(input())  # 여행계획에 속한 도시의 수
parent = [i for i in range(N)]  # 부모 테이블 초기화

# 부모 찾기
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    pa, pb = find(a), find(b)
    # 이미 같은 집합이면 리턴
    if pa == pb:
        return
    parent[b] = a

for y in range(N):
    maps = list(map(int, input().split()))
    for x in range(N):
        if maps[x] == 1:
            union(parent[y], parent[x])

plan = list(map(int, input().split()))  # 여행 계획
for i in range(M):
    plan[i] -= 1

result = set([find(i) for i in plan])
if len(result) == 1:
    print("YES")
else:
    print("NO")