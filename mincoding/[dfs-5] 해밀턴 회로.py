N = int(input())  # 정점 개수
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N  # 방문한 도시 배열
Min = 21e8  # 최소 이동 비용

def dfs(level, now, cost):
    global Min
    # 가지치기 - 없으면 시간 초과
    if cost > Min:
        return
    if level == N:  # 모든 정점을 방문한 경우
        if arr[now][1] > 0:  # 다시 처음 정점으로 돌아갈 수 있는 경우
            if Min > cost + arr[now][1]:  # 이동 비용이 최소 비용보다 작은 경우
                Min = cost + arr[now][1]  # 최소 비용을 갱신
    for i in range(N):
        if visited[i] == 0 and arr[now][i] > 0:  # 아직 방문하지 않은 정점이고 이동 가능한 경우
            visited[i] = 1 # 해당 정점을 방문한 것으로 표시
            dfs(level+1, i, cost+arr[now][i])  # 다음 정점으로 이동
            visited[i] = 0 # 이전 상태로 되돌리기

visited[1] = 1  # 첫 번째 정점을 방문한 것으로 표시
dfs(1, 1, 0)  # 첫 번째 정점에서 시작하므로 level은 1, 시작 정점은 1, 이동 비용은 0으로 설정
print(Min)  # 최소 이동 비용 출력
