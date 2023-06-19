# 입력 받기
N, M, K = map(int, input().split())  # 숫자 개수, 더할 수의 개수, 한 숫자당 더할 수 있는 최대 횟수
arr = list(map(int, input().split()))
arr.sort(reverse=True)  # 내림 차순 정렬
first = arr[0]  # 가장 큰 수
second = arr[1]  # 두 번째로 큰 수

# 풀이 1
Sum = 0
while True:
    for _ in range(K):
        if M == 0:
            break
        Sum += first
        M -= 1
    if M == 0:
        break
    Sum += second
    M -= 1

print(Sum)

# 풀이 2
# 큰 수가 더해지는 횟수
count = int(M/(K+1)) * K
count += M % (K+1)  # 반복 횟수가 나누어 떨어지지 않을 경우를 위해

Sum = 0
Sum += first * count
Sum += second * (M-count)
print(Sum)