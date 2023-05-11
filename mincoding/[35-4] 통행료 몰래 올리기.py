from heapq import heappush, heappop
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

heap = []
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            heappush(heap, (arr[i][j], i, j))

for _ in range(20):  # 양방향 고려해야하므로 10*2 회 확인
    cost, y, x = heappop(heap)
    heappush(heap, (cost*2, y, x))

print(f'{cost*2}만원')