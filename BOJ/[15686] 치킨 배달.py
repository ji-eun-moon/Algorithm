N, M = map(int, input().split())  # 도시 개수, 치킨집 최대 개수(나머지는 모두 폐업)
arr = [list(map(int, input().split())) for _ in range(N)]  # 0-빈칸, 1-집, 2-치킨집
answer = float("inf")


# 집과 치킨집의 좌표를 각각 저장
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:    # 집
            home.append((i, j))
        elif arr[i][j]==2:  # 치킨집
            chicken.append((i, j))
cnt = len(chicken)

# 치킨거리 계산 함수
def cal(remain):
    total = 0
    for hi, hj in home:
        Min = 2*N
        for ri, rj in remain:
            Min = min(Min, abs(hi-ri) + abs(hj-rj))
        total += Min
    return total

def dfs(n, remain):
    global answer

    if n == cnt:  # 종료 조건: 마지막 치킨집까지 확인했을 경우
        if len(remain) <= M:  # M개 이하 치킨집을 유지했을 경우
            answer = min(answer, cal(remain))
        return

    dfs(n+1, remain+[chicken[n]])  # 폐업하지 않는 경우
    dfs(n+1, remain)  # 폐업하는 경우

dfs(0, [])

print(answer)