N, K = map(int, input().split())
S = int(input())
tree = dict()

for _ in range(K):
    a, b = input().split()
    # a - root, b - 자식 노드
    if a in tree:
        tree[a].append(b)
    else:
        tree[a] = [b]

print(tree)

# 전위 순회

# 후위 순회
