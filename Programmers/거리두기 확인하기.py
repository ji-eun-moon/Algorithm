from collections import deque
def solution(places):

    answer = []
    def bfs(place):
        people = []
        # 사람 위치 담기
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))

        for p in people:
            q = deque()
            visited = [[0]*5 for _ in range(5)]
            q.append(p)
            visited[p[0]][p[1]] = 1

            while q:
                y, x = q.popleft()

                # 거리가 3 이상인 곳은 확인할 필요 없음
                if visited[y][x] > 3:
                    break

                for iy, ix in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny = y + iy
                    nx = x + ix

                    if 0 <= ny < 5 and 0 <= nx < 5:
                        if not visited[ny][nx]:
                            # 빈 칸이면 거리 갱신
                            if place[ny][nx] == 'O':
                                q.append((ny, nx))
                                visited[ny][nx] = visited[y][x] + 1
                            # 거리 2 이내에 사람이 있으면 실패
                            if place[ny][nx] == 'P' and visited[y][x] <= 2:
                                return 0
        return 1

    for place in places:
        ret = bfs(place)
        answer.append(ret)

    return answer