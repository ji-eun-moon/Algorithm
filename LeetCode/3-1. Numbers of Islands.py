# https://leetcode.com/problems/number-of-islands/description/
from collections import deque

class Solution:
    def numIslands(self, grid):
        num = 0

        m = len(grid)  # 세로
        n = len(grid[0])  # 가로

        visited = [[False] * n for _ in range(m)]

        def bfs(y, x):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            visited[y][x] = True
            q = deque()
            q.append((y, x))
            while q:
                cur_y, cur_x = q.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if 0 <= next_x < n and 0 <= next_y < m:
                        if grid[next_y][next_x] == "1" and not visited[next_y][next_x]:
                            visited[next_y][next_x] = True
                            q.append((next_y, next_x))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    num += 1

        return num