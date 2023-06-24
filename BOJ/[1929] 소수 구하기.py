import math

M, N = map(int, input().split())
array = [True for i in range(N+1)]

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(N))+1):
    if array[i] == True:
        j = 2
        # i를 제외한 i의 모든 배수 지우기
        while i * j <= N:
            array[i * j] = False
            j += 1

for i in range(2, N+1):
    if array[i] and i >= M:
        print(i)