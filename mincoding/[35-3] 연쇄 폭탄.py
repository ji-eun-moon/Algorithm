from heapq import heappush, heappop

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

heap = []
for i in range(N):
    for j in range(N):
        heappush(heap, (arr[i][j], i, j))

time = 0
bombs = N * N
while bombs > 0:  # 남은 폭탄이 0개이면 반복문 종료
    time += 1  # 시간 증가 위치 중요... 이미 터진 폭탄이라 넘어가더라도 시간은 증가한다.
    n, y, x = heappop(heap)
    if visited[y][x] == 1:  # 이미 터진 폭탄이면 넘어가기
        continue
    visited[y][x] = 1
    bombs -= 1
    for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        dy = y + iy
        dx = x + ix
        if 0 <= dy < N and 0 <= dx < N:
            if visited[dy][dx] == 0:
                visited[dy][dx] = 1
                bombs -= 1

print(f'{time}초')
