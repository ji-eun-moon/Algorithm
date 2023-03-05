import sys
input = sys.stdin.readline

N = int(input())
cnt = N

for i in range(2, N//2+1):
    for j in range(i, N):
        if i*j <= N:
            cnt += 1

print(cnt)
