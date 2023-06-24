N = int(input())
k = int(input())

start = 1
end = N * N

while start <= end:
    # 중간 값
    mid = (start + end) // 2

    # 중간 값보다 작거나 같은 숫자 세기
    cnt = 0
    for i in range(1, N + 1):  # 각 행의 첫 번째 숫자

        # 중간 값을 행의 첫 번째 숫자로 나눈 몫이 중간 값보다 작은 숫자의 개수
        # 각 행마다 N개보다 많을 수 없으므로 최대는 N개
        cnt += min(mid // i, N)

    if cnt < k:  # mid 보다 작거나 같은 수의 개수가 k보다 적음
        start = mid + 1
    else:  # mid 보다 작거나 같은 수의 개수가 k보다 많거나 같음
        end = mid - 1

# 반복문 종료 후 start가 k번째 숫자
print(start)
