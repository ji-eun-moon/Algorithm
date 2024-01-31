# https://leetcode.com/problems/course-schedule/description/
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        visited = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # 진입 차수 배열 생성
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        # 위상 정렬 수행
        q = deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)

        while q:
            cur_v = q.popleft()
            visited.append(cur_v)

            # 현재 정점과 연결된 노드들의 진입 차수 -1
            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                # 진입 차수가 0이 되면 q에 넣기
                if indegree[next_v] == 0:
                    q.append(next_v)

        # 최종 방문한 과목 수가 numCourses 와 같으면 모두 수강할 수 있는 것
        return len(visited) == numCourses

solve = Solution()
print(solve.canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(solve.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))