from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        answer = 0
        N = len(grid)
        visited = [[0] * N for _ in range(N)]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]

        if grid[0][0] == 1:
            return -1

        q = deque()
        q.append((0, 0))
        visited[0][0] = 1
        while q:
            y, x = q.popleft()
            if y == N-1 and x == N-1:
                return visited[y][x]
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx] and grid[ny][nx] == 0:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((ny, nx))

        return -1

solve = Solution()
print(solve.shortestPathBinaryMatrix(grid = [[0,1],[1,0]]))
print(solve.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))
print(solve.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]))
