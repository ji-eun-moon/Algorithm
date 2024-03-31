N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N // 2

# 두 팀의 능력치 차이를 계산하는 함수
def cal(alst, blst):
    aSum, bSum = 0, 0
    for i in range(M):
        for j in range(M):
            aSum += arr[alst[i]][alst[j]]
            bSum += arr[blst[i]][blst[j]]
    return abs(aSum - bSum)

def dfs(n, alst, blst):
    global answer

    if n == N:  # 종료 조건
        # 같은 인원으로 팀을 구성했을 경우
        if len(alst) == len(blst):
            answer = min(answer, cal(alst, blst))
        return

    # a 팀을 선택하는 경우
    dfs(n+1, alst+[n], blst)

    # b 팀을 선택하는 경우
    dfs(n+1, alst, blst+[n])


answer = float("inf")
dfs(0, [], [])
print(answer)