N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
st, ed = map(int, input().split())

used = [0]*N
Min = 21e8
Max = 0
Sum = 0

def dfs(now):
    global Min, Max, Sum
    if now == ed:  # 도착하면 최소, 최대 값 갱신하기
        if Sum < Min:
            Min = Sum
        if Sum > Max:
            Max = Sum
        return
    for i in range(N):
        if arr[now][i] > 0:  # 이동할 수 있고 한번도 방문한 적 없는 곳이라면
            if used[i] == 0:
                used[i] = 1  # 방문체크하고 비용 더하기
                Sum += arr[now][i]
                dfs(i)
                used[i] = 0
                Sum -= arr[now][i]

used[st] = 1
dfs(st)
print(Min)
print(Max)