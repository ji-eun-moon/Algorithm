N = int(input())  # 컴퓨터의 수
M = int(input())  # 연결할 수 있는 선의 수

edges = []
for _ in range(M):
    tmp = list(map(int, input().split()))  # a, b, c
    edges.append(tmp)

edges.sort(key = lambda x: x[2])

root = [i for i in range(N+1)]
def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return 1
    root[fb] = fa

cost = 0
for a, b, c in edges:
    if union(a, b):
        continue
    cost += c

print(cost)