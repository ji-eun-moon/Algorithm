# https://leetcode.com/problems/number-of-islands/description/

# DFS
class Solution:
    def numIslands(self, grid):
        cnt = 0

        n, m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]

        def dfs(y, x):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and grid[ny][nx] == "1":
                        visited[ny][nx] = 1
                        dfs(ny, nx)

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = 1
                    dfs(i, j)
                    cnt += 1

        return cnt

# BFS

from collections import deque
class Solution:
    def numIslands(self, grid):
        cnt = 0

        n, m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]

        def bfs(y, x):
            q = deque()
            q.append((y, x))

            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < n and 0 <= nx < m:
                        if not visited[ny][nx] and grid[ny][nx] == "1":
                            visited[ny][nx] = 1
                            q.append((ny, nx))

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = 1
                    bfs(i, j)
                    cnt += 1

        return cnt

solve = Solution()
print(solve.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(solve.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))