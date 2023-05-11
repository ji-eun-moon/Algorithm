from heapq import heappush, heappop

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
alphabet = [chr(n) for n in range(ord('A'), ord('Z')+1)]

heap = []
for i in range(N):
    for j in range(N):
        heappush(heap, (-arr[i][j], alphabet[i], alphabet[j]))

for _ in range(3):
    cost, st, ed = heappop(heap)
    print(f'{st}-{ed} {-cost}')