# https://leetcode.com/problems/trapping-rain-water-ii/description/

'''
1. `heap = []`
    1-1. 테두리 리스트에 (높이, 행, 열) 형태로 저장
2. 우선순위 큐를 통해 가장 높이가 낮은 테두리부터 확인
    2-1. 인접한 칸의 높이가 낮으면 높이 차만큼 물 저장 하고 테두리가 됨
    2-2. 인접한 칸의 높이가 높으면 물 저장하지 못하고 테두리가 됨
'''

import heapq

class Solution:
    def trapRainWater(self, heightMap):
        answer = 0
        m = len(heightMap)
        n = len(heightMap[0])
        heap = []  # 테두리 리스트 - (높이, 행, 열)
        visited = set()  # 방문한 칸

        # 테두리 칸 정보 저장
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
                if j == 0 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))

        while heap:
            # 테두리 리스트에서 가장 높이가 낮은 칸 확인
            h, y, x = heapq.heappop(heap)

            for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                dy = y + iy
                dx = x + ix
                if 0 <= dy < m and 0 <= dx < n:
                    if (dy, dx) not in visited:
                        dh = heightMap[dy][dx]
                        visited.add((dy, dx))
                        # 인접한 칸이 낮으면 물을 채우고, 채운 칸은 테두리가 됨
                        if dh < h:
                            answer += (h-dh)
                            heapq.heappush(heap, (h, dy, dx))
                        # 인접한 칸이 높으면 물을 채우지 못하고, 테두리가 됨
                        else:
                            heapq.heappush(heap, (dh, dy, dx))

        return answer

solve = Solution()
print(solve.trapRainWater(heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(solve.trapRainWater(heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))