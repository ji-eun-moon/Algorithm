import sys
input = sys.stdin.readline

G = int(input())  # 게이트 수
P = int(input())  # 비행기 수
planes = [int(input()) for _ in range(P)]  # planes[i] : 비행기 i가 도킹 시도하는 게이트 번호

parent = [i for i in range(G+1)]
answer = 0

# 도킹할 게이트 찾기
def find(m):
    if parent[m] == m:
        return m
    parent[m] = find(parent[m])
    return parent[m]

# 게이트 연결하기
def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    parent[fb] = fa

for plane in planes:
    x = find(plane)
    if x == 0:  # 도킹할 게이트가 0이면 모든 비행기 도킹 불가능
        break
    union(x-1, x)  # 이전 게이트와 연결
    answer += 1

print(answer)