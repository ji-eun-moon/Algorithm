import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

i, j = 0, 0
Min = 21e8
while i < N and j < N:
    ret = lst[j] - lst[i]
    if ret < M:
        j += 1
    elif ret > M:
        i += 1
        Min = min(Min, ret)
    else:
        Min = M
        break

print(Min)