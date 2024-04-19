T = int(input())


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    parent[fb] = fa
    network[fa] += network[fb]

for _ in range(T):
    F = int(input())

    parent = {}
    network = {}
    for _ in range(F):
        a, b = input().split()

        parent.setdefault(a, a)
        parent.setdefault(b, b)
        network.setdefault(a, 1)
        network.setdefault(b, 1)

        union(a, b)

        print(network[find(a)])