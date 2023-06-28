N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]  # [출발, 종료, 가중치]
INF = 21e9
D = [INF]*(N+1)

def bf(start):
    D[start] = 0
    for i in range(N):
        for j in range(M):
            st = arr[j][0]
            ed = arr[j][1]
            v = arr[j][2]
            if D[st] != INF and D[ed] > D[st] + v:
                D[ed] = D[st] + v
                if i == N-1:
                    return 0
    return 1

result = bf(1)

if result:
    for i in range(2, N+1):
        if D[i] != INF:
            print(D[i])
        else:
            print(-1)
else:
    print(-1)



