# 시간 초과
# from heapq import heappop, heapify, heappush

# N = int(input())
# nums = [500]
# def mid_num(nums):
#     heapify(nums)
#     lst = nums[:]
#     n = (len(nums)+1)//2
#     for _ in range(n):
#         mid = heappop(lst)
#     return mid
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     nums.append(a)
#     nums.append(b)
#     print(mid_num(nums))

# maxh = [-500]
# minh = []
#
# def push_num(num):
#     mid = (maxh[-1])*-1
#     if len(maxh) > len(minh):
#         if num < mid:
#             heappush(minh, -heappop(maxh))
#             heappush(maxh, -num)
#         else:
#             heappush(minh, num)
#

####################################################################################

from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline())

# max_heap과 min_heap 초기화
max_heap = [-500]
min_heap = []

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

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    push(a)
    push(b)
    # 최대 힙의 top이 중앙값
    print(-max_heap[0])
