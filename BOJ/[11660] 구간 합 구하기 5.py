import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 표의 크기, 합을 구해야 하는 횟수
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]  # 원본 배열
arr_sum = [[0] * (N+1) for _ in range(N+1)]  # 합 배열

# 합 배열 만들기
for i in range(1, N+1):
    for j in range(1, N+1):
        arr_sum[i][j] = arr_sum[i][j-1] + arr_sum[i-1][j] - arr_sum[i-1][j-1] + arr[i][j]

# 구간합 구하기
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = arr_sum[x2][y2] - arr_sum[x2][y1-1] - arr_sum[x1-1][y2] + arr_sum[x1-1][y1-1]
    print(result)
