N = int(input())  # 아이들의 수
# 번호 순서대로 배치하기 위해 옮겨지는 아이의 최소 수?

# 아이들 배열
children = [0]
for i in range(N):
    children.append(int(input()))

# 가장 긴 증가하는 부분 수열
dp = [1]*(N+1)
for i in range(1, N+1):
    for j in range(1, i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))