# 내 풀이
N, K = map(int, input().split())

cnt = 0
while N != 1:
    if N % K == 0:
        N = N // K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)

# 점답 풀이 1
N, K = map(int, input().split())

cnt = 0
# N이 K 이상이라면 K로 계속 나누기
while N >= K:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while N % K != 0:
        N -= 1
        cnt += 1
    # K로 나누기
    N //= K
    cnt += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while N > 1:
    N -= 1
    cnt += 1

print(cnt)

# 정답 풀이 2 - N이 K의 배수가 되도록 한번에 빼는 방법
# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)