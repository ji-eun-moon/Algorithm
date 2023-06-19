import sys
input = sys.stdin.readline

N = int(input())
rope = []

for _ in range(N):
    rope.append(int(input()))
rope.sort()

Max = 0
for i in range(N-1):
    n = N - i
    w = rope[i] * n
    Max = max(Max, w)

print(max(Max, rope[-1]))
