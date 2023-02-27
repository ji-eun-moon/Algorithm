N, K = map(int, input().split())  # 전체 날짜 수, 연속적인 날짜 수
temp = list(map(int, input().split()))

# 시간초과
# Max = 0
# for i in range(N-K+1):
#     Sum = 0
#     for j in range(i, i+K):
#         Sum += temp[j]
#     if Max < Sum:
#         Max = Sum
# print(Max)

# 슬라이딩 윈도우 - 구간합
Sum = 0
for i in range(K):
    Sum += temp[i]

Max = Sum
for i in range(N-K):
    Sum -= temp[i]
    Sum += temp[i+K]
    if Max < Sum:
        Max = Sum

print(Max)
