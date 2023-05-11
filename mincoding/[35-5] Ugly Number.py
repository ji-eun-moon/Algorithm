from heapq import heappush, heappop

n = int(input())
nums = list(map(int, input().split()))
ugly = [1]

heap = []
heappush(heap, 2)
heappush(heap, 3)
heappush(heap, 5)

while len(ugly) < max(nums):
    num = heappop(heap)
    if num > ugly[-1]:  # 중복된 값 넣지 않기 위해서
        ugly.append(num)
        # 현재 큐에서 꺼낸 수에 2, 3, 5를 곱한 수를 push
        heappush(heap, 2*num)
        heappush(heap, 3*num)
        heappush(heap, 5*num)

for num in nums:
    print(ugly[num-1], end=' ')