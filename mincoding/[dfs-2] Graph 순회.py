N, K = map(int, input().split())
S = int(input())
tree = dict()

for _ in range(K):
    a, b = map(int, input().split())
    # a - root, b - 자식 노드
    if a in tree:
        tree[a].append(b)
    else:
        tree[a] = [b]

# value를 내림 차순 정렬
for value in tree.values():
    value.sort(reverse=True)


visited = [0]*(N+1)
def preorder(root):
    if root in tree and visited[root] == 0:
        visited[root] = 1
        print(root, end=' ')
        for i in range(len(tree[root])):
            preorder(tree[root][i])
    else:
        if visited[root] == 0:
            visited[root] = 1
            print(root, end=' ')
preorder(S)
print()

visited = [0]*(N+1)
# 후위 순회 : left - right - root
def postorder(root):
    if root in tree and visited[root] == 0:
        visited[root] = 1
        for i in range(len(tree[root])):
            postorder(tree[root][i])
        print(root, end=' ')
        return
    else:
        if visited[root] == 0:
            visited[root] = 1
            print(root, end=' ')
            return
postorder(S)