N = int(input())  # 재료의 개수
arr = [[] for _ in range(N)]  # 인접 리스트 - 배수 관계 저장
visited = [0]*N
D = [0]*N
lcm = 1

# 최대 공약수 구하는 함수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(N-1):
    a, b, p, q = map(int, input().split())
    arr[a].append((b, p, q))
    arr[b].append((a, q, p))
    lcm *= (p * q // gcd(p,q))  # 최소 공배수

D[0] = lcm  # 노드 첫번째 값 최소 공배수로 초기화


def dfs(v):
    visited[v] = 1
    for i in arr[v]:
        n = i[0]
        if visited[n] == 0:
            D[n] = D[v] * i[2] // i[1]  # 비율 관계에 따라 노드 값 업데이트
            dfs(n)

dfs(0)

GCD = D[0]  # 최대공약수 구하기
for i in range(1, N):
    GCD = gcd(GCD, D[i])

D = list(map(lambda x: x//GCD, D))  # 최대공약수로 나누기
print(*D)
