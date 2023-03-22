from collections import deque

floor, st, ed, up, down = map(int, input().split())  # 건물 층수, 현재 위치, 도착 위치, 위로, 아래로
visited = [0]*(floor+1)
flag = 0
def bfs():
    global flag
    q = deque()
    q.append(st)  # 시작 위치 담고
    visited[st] = 1  # 방문 체크
    while q:
        now = q.popleft()
        if now == ed:  # 도착하면
            flag = 1  # flag 켜기
            return visited[now] - 1  # 시작할 때 1부터 시작했으므로
        for d in (up, -down):  # 위로, 아래로 2방향 탐색
            Next = now + d
            if 1 <= Next <= floor:  # 범위 확인
                if visited[Next] == 0:
                    visited[Next] = visited[now] + 1
                    q.append(Next)

answer = bfs()

if flag == 1:
    print(answer)
else:
    print('use the stairs')

# 교수님 풀이

from collections import deque

floor, st, ed, up, down = map(int, input().split())  # 건물 층수, 현재 위치, 도착 위치, 위로, 아래로
visited = [0]*(floor+1)

def bfs():
    q = deque()
    q.append(st)  # 시작 위치 담고
    visited[st] = 1  # 방문 체크
    while q:
        now = q.popleft()
        if now == ed:  # 도착하면
            return visited[now] - 1  # 시작할 때 1부터 시작했으므로
        for d in (up, -down):  # 위로, 아래로 두 방향 탐색
            Next = now + d
            if 1 <= Next <= floor:
                if visited[Next] == 0:
                    visited[Next] = visited[now] + 1
                    q.append(Next)

    return 'use the stairs'

print(bfs())


