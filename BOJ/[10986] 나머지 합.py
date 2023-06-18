import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 원본 배열

arr_sum = [0] * (N+1)  # 구간합 배열
for i in range(1, N+1):
    arr_sum[i] = arr_sum[i-1] + arr[i]

C = [0]*M  # 같은 나머지의 인덱스 카운트하기
answer = 0
for i in range(1, N+1):
    ret = arr_sum[i] % M
    if ret == 0:
        answer += 1
    C[ret] += 1

for i in range(M):
    # 니머지가 같은 인덱스 중에서 2개를 뽑는 경우의 수
    if C[i] > 1:
        answer += (C[i]*(C[i]-1)//2)

print(answer)
