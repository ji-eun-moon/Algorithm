import heapq

N = int(input())

heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

Sum = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    Sum += (a+b)
    heapq.heappush(heap, a+b)

print(Sum)