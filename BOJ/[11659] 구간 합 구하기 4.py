import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 숫자 개수, 합 구해야 하는 횟수
lst = list(map(int, input().split()))
# 시간 초과
# for _ in range(M):
#     sum = 0
#     a, b = map(int, input().split())
#     for i in range(a-1, b):
#         sum += lst[i]
#     print(sum)

# 시간 초과 2
Sumlst = [0]*(N+1)
for i in range(1, N+1):
    Sumlst[i] = Sumlst[i-1] + lst[i-1]

for _ in range(M):
    a, b = map(int, input().split())
    print(Sumlst[b] - Sumlst[a-1])