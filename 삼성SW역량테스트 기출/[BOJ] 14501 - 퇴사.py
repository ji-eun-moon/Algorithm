# 풀이 1 - 완전 탐색
N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())
def dfs(n, sm):
    global answer
    # 종료 조건
    if n >= N:
        answer = max(answer, sm)
        return
    # 하부 호출
    # 상담하는 경우(퇴사일 전 완료할 경우만 가능)
    if n + T[n] <= N:
        dfs(n+T[n], sm+P[n])
    # 상담하는 경우 (항상 가능)
    dfs(n+1, sm)

answer = 0
dfs(0, 0)
print(answer)

# 풀이 2 - DP
N = int(input())

T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

DP = [0]*(N+1)

for i in range(N-1, -1, -1):  # 뒤에서 앞으로
    if i + T[i] <= N:  # 기간 내 상담 완료 가능한 경우
        DP[i] = max(DP[i+T[i]]+P[i], DP[i+1])  # 상담 선택한 경우와 상담 선택하지 않은 경우의 최대 수익
    else:
        DP[i] = DP[i+1]

print(DP[0])