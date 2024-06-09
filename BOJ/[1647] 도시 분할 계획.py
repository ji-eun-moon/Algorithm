N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
parent = [i for i in range(N+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

arr.sort(key= lambda x:x[2])

result = 0
max_cost = 0

for edge in arr:
    st, ed, cost = edge
    if find(st) != find(ed):
        union(st, ed)
        result += cost
        max_cost = max(cost, max_cost)

print(result - max_cost)