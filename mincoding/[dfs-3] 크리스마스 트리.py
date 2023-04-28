N = int(input())

tree = dict()

for _ in range(N):
    a, *b = map(int, input().split())
    # a - root, b - 자식 노드
    tree[a] = b

# 중위 순회
def inorder(root):
    if root != -1:
        inorder(tree[root][0])
        print(root, end=' ')
        inorder(tree[root][1])
inorder(1)
print()

# 전위 순회
def preorder(root):
    if root != -1:
        print(root, end=' ')
        preorder(tree[root][0])
        preorder(tree[root][1])
preorder(1)
print()

# 후위 순회
def postorder(root):
    if root != -1:
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end=' ')
postorder(1)