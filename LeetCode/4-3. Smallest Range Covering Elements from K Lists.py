# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
'''
1. nums 배열에서 각 원소의 리스트 인덱스를 함께 저장하는 배열을 만든다.
2. 초기 힙 구성하기 → 범위 리스트
    1. 각 리스트의 최솟값으로 이루어진 리스트 (heappush)
3. 힙에서 최솟 값을 꺼내서 해당 값이 들어있던 리스트에서 다음 값 꺼내기
'''
import heapq
class Solution:
    def smallestRange(self, nums):

        # 각 원소의 인덱스 정보를 함께 저장하는 배열 만들기
        nums_lst = []
        for lst_idx, num in enumerate(nums):
            temp = []
            for val_idx, n in enumerate(num):
                temp.append([n, lst_idx, val_idx])  # [값, 리스트 인덱스, 값 인덱스]
            nums_lst.append(temp)

        # 초기 힙 구성
        heap = []
        Max, Min = -float("inf"), float("inf")
        for num in nums_lst:
            heapq.heappush(heap, num[0])
            Max = max(num[0][0], Max)  # 최댓값 초기화
            Min = min(num[0][0], Min)  # 최솟값 초기화

        Range = Max - Min  # 범위 초기화
        answer = [Min, Max]  # 정답리스트 초기화

        # 힙에서 최솟 값을 꺼내서 해당 값이 들어있던 리스트에서 다음 값 꺼내기
        while True:
            val, lst_idx, val_idx = heapq.heappop(heap)  # 최솟값 꺼내기

            # 다음 값을 꺼낼 수 없으면 반복문 종료
            if val_idx + 1 >= len(nums_lst[lst_idx]):
                return answer

            # 다음 값 꺼내서 넣기
            new_num = nums_lst[lst_idx][val_idx+1]
            heapq.heappush(heap, new_num)
            Max = max(Max, new_num[0])  # 최댓값 갱신

            # 범위 계산하기
            Min = heap[0][0]
            new_Range = Max - Min

            # 범위가 더 작아졌으면 정답 리스트 갱신
            if new_Range < Range:
                Range = new_Range
                answer = [heap[0][0], Max]


solve = Solution()
print(solve.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(solve.smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]]))