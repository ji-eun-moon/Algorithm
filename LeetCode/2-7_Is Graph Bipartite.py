class Solution:
    def isBipartite(self, graph):
        N = len(graph)
        color = [0]*N

        def dfs(cur_node, next_color):
            color[cur_node] = next_color
            for next_node in graph[cur_node]:
                if color[next_node]:
                    if color[next_node] == color[cur_node]:
                        return False
                else:
                    if not dfs(next_node, (color[cur_node] + 1) % 2):
                        return False
            return True

        for i in range(N):
            if color[i] == 0:
                if not dfs(i, 0):
                    return False

        return True

from collections import deque
class Solution:
    def isBipartite(self, graph):
        N = len(graph)
        color = [0]*N

        def bfs(start, c):
            q = deque()
            q.append(start)
            color[start] = c

            while q:
                cur_node = q.popleft()
                for next_node in graph[cur_node]:
                    if color[next_node]:
                        if color[next_node] == color[cur_node]:
                            return False
                    else:
                        q.append(next_node)
                        color[next_node] = (color[cur_node] + 1) % 2

            return True

        for i in range(N):
            if color[i] == 0:
                if not bfs(i, 0):
                    return False

        return True

solve = Solution()
print('#1', solve.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print('#2', solve.isBipartite([[1,3],[0,2],[1,3],[0,2]]))