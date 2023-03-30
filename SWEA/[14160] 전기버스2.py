T = int(input())
for test_case in range(1, T+1):
    N, *M = map(int, input().split())
    Min = 21e8
    def dfs(now, cnt):
        global Min
        if cnt >= Min:
            return
        if now >= N-1:
            Min = min(Min, cnt)
            return
        V = M[now]  # now에서 충전하면 최대 갈 수 있는 거리
        for j in range(1, V+1):  # 충전했을 때 갈 수 있는 칸 모두 확인
            dfs(now+j, cnt+1)
    dfs(0, 0)
    print(f'#{test_case} {Min-1}')  # 처음 충전하는 것은 충전횟수에 포함하지 않으므로 -1