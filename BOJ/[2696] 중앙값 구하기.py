from heapq import heappop, heappush

T = int(input())

for _ in range(T):
    N = int(input())

    lst = []
    n = N // 10 + bool(N % 10)
    for _ in range(n):
        temp = list(map(int, input().split()))
        lst += temp

    max_heap = []
    min_heap = []
    result = []
    def push(num):

        # 같은 개수라면 무조건 최대 힙에 넣기
        if len(max_heap) == len(min_heap):
            heappush(max_heap, -num)
        # 개수가 다르면 이전에 최대 힙에 넣은 것이기 때문에 개수 맞춰주기 위해 최소 힙에 넣기
        else:
            heappush(min_heap, num)

        # 대소 조건 비교
        # 최소 힙의 top이 최대 힙의 top보다 작다면 두수를 바꿔주기
        if min_heap and -max_heap[0] > min_heap[0]:
            temp_min = heappop(min_heap)
            temp_max = heappop(max_heap)
            heappush(max_heap, -temp_min)
            heappush(min_heap, -temp_max)

    for i in range(len(lst)):
        push(lst[i])
        if i % 2 == 0:
            result.append(-max_heap[0])

    print(len(result))
    m = len(result)//10 + bool(len(result)%10)
    for i in range(m):
        start = i * 10
        end = min((i + 1) * 10, len(result))
        print(*result[start:end])