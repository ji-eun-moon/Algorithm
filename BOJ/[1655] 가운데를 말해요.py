import sys
from heapq import heappop, heappush

max_heap = []
min_heap = []

def push_num(num):
    # max_heap과 min_heap의 크기가 같다면 max_heap에 값을 넣는다.
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)
    # max_heap과 min_heap의 크기가 다르면 이전에 최대 힙에 넣은 것이기 때문에
    # 개수를 맞춰주기 위해 최소 힙에 값을 넣는다.
    else:
        heappush(min_heap, num)

    # 대소 조건 비교하기
    # min_heap의 root 값이 max_heap의 root 값보다 작다면 두 수를 바꿔준다.
    if min_heap and -max_heap[0] > min_heap[0]:
        temp_min = heappop(min_heap)
        temp_max = heappop(max_heap)
        heappush(max_heap, -temp_min)
        heappush(min_heap, -temp_max)

def find_median():
    if len(max_heap) == len(min_heap):
        return min(-max_heap[0], min_heap[0])
    else:
        return -max_heap[0]

N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline())
    push_num(num)
    print(find_median())