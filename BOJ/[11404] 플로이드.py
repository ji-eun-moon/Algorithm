import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
arr = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    arr[a][b] = min(c, arr[a][b])  # 노선이 하나가 아닐 수 있음 -> 최소값 넣기

# 플로이드 워셜 알고리즘
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:  # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
                arr[a][b] = 0
            else:
                arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if arr[a][b] == 1e9:
            print(0, end=' ')
        else:
            print(arr[a][b], end=' ')
    print()