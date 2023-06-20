N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
for i in range(N):
    a = A.pop(A.index(min(A)))
    b = B.pop(B.index(max(B)))
    S += a * b

print(S)