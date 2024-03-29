'''
1. 그래프 간선들을 가중치 기준 오름차순으로 정렬
2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선 선택
  2-1. 가장 낮은 가중치 먼저 선택
  2-2. 사이클 형성하는 간선은 제외 (Union Find)
3. 해당 간선을 MST 집합에 추가
'''

V, E = map(int, input().split())  # 정점 개수, 간선 개수

# [노드1, 노드2, 가중치] 리스트
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# 1. 그래프 간선들을 가중치 기준 오름차순으로 정렬
edges.sort(key=lambda x:x[2])

parent = [i for i in range(V+1)]

# find 연산
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# union 연산
def union(a, b):
    global answer, cnt
    fa, fb = find(a), find(b)
    # 사이클 형성하는 간선은 제외
    if fa == fb:
        return 1
    parent[fb] = fa


cost = 0  # 다리개수, 최소비용
for a, b, c in edges:
    if union(a, b):
        continue
    cost += c

print(cost)