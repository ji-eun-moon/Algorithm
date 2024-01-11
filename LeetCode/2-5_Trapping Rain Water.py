class Solution:
    def trap(self, height):

        N = len(height)
        max_idx = height.index(max(height))  # 높은 인덱스

        def cal_water(start, end):
            cnt = 0

            # 시작점 인덱스가 끝 인덱스보다 크다면 뒤집어 주기
            if start > end:
                lst = height[end:start+1][::-1]
            else:
                lst = height[start:end + 1]

            # 작은 -> 큰 방향으로 이동하며 높이차 계산
            cur_max = 0
            for h in lst:
                cur_max = max(cur_max, h)
                if h < cur_max:
                    cnt += (cur_max - h)

            return cnt

        # 가장 큰 높이가 왼쪽 끝인 경우
        if max_idx == 0:
            return cal_water(N-1, 0)
        # 가장 큰 높이가 오른쪽 끝인 경우
        elif max_idx == N - 1:
            return cal_water(0, N-1)
        # 가장 큰 높이가 가운데에 있을 경우
        else:
            return cal_water(0, max_idx) + cal_water(N-1, max_idx)

solve = Solution()
print('#1', solve.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print('#2', solve.trap(height = [4,2,0,3,2,5]))

class Solution:
    def trap(self, height):

        trapped = height[:]
        stack = []
        prev_height = [0, 0]
        for idx, h in enumerate(trapped):
            while stack and stack[-1][1] <= h:
                prev_height = stack.pop()

            # 스택이 안비어 있으면 h 가 더 낮다.
            if stack:
                left = stack[-1]
                for j in range(left[0] + 1, idx):
                    trapped[j] = h
            # 비어 있으면 prev 가 더 낮다.
            else:
                left = prev_height
                for j in range(left[0] + 1, idx):
                    trapped[j] = left[1]

            stack.append([idx, h])

        return sum(trapped) - sum(height)

solve = Solution()
print('#1', solve.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print('#2', solve.trap(height = [4,2,0,3,2,5]))

# 투 포인터
class Solution(object):
    def trap(self, height):
        trapped = height[:]
        N = len(height)
        left, right = 0, N-1
        left_height, right_height = height[0], height[N-1]
        while left < right:
            # 왼쪽이 오른쪽보다 낮은 경우
            if left_height <= right_height:
                # 왼쪽 포인터 한칸 이동
                left += 1
                # 높이가 낮아졌으면 물 채우기
                if height[left] < left_height:
                    trapped[left] = left_height
                # 높아졌으면 높이 갱신
                else:
                    left_height = height[left]
            # 오른쪽이 왼쪽보다 낮은 경우
            else:
                # 오른쪽 포인터 이동
                right -= 1
                # 높이가 낮아졌으면 물 채우기
                if height[right] < right_height:
                    trapped[right] = right_height
                # 높아졌으면 높이 갱신
                else:
                    right_height = trapped[right]

        return sum(trapped) - sum(height)

solve = Solution()
print('#1', solve.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print('#2', solve.trap(height = [4,2,0,3,2,5]))