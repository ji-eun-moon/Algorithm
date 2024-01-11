# https://leetcode.com/problems/keys-and-rooms/description/

class Solution:
    def canVisitAllRooms(self, rooms):

        N = len(rooms)
        visited = [0] * N

        def dfs(cur_room):
            visited[cur_room] = 1
            for next_room in rooms[cur_room]:
                if not visited[next_room]:
                    dfs(next_room)

        dfs(0)

        return all(visited)

solve = Solution()
print('#1', solve.canVisitAllRooms(rooms = [[1],[2],[3],[]]))
print('#2', solve.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))

from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms):

        N = len(rooms)
        visited = [0] * N

        def bfs(cur_room):
            q = deque()
            visited[cur_room] = 1
            q.append(cur_room)

            while q:
                cur_room = q.popleft()
                for next_room in rooms[cur_room]:
                    if not visited[next_room]:
                        visited[next_room] = 1
                        q.append(next_room)

        bfs(0)

        return all(visited)


solve = Solution()
print('#1', solve.canVisitAllRooms(rooms = [[1],[2],[3],[]]))
print('#2', solve.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))