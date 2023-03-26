from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 편의점 개수
    sty, stx = map(int, input().split())  # 집
    store = []
    for _ in range(N):
        by, bx = map(int, input().split())  # 편의점
        store.append([by, bx])
    edy, edx = map(int, input().split())  # 페스티벌
    visited = [0] * N  # 편의점 방문 확인
    def bfs():
        q = deque()
        q.append((sty, stx))

        while q:
            nowy, nowx = q.popleft()  # 현재 위치
            # 현재 위치로부터 페스티벌 위치가 1000미터 이내라면 행복하게 도착 가능
            if abs(edy-nowy) + abs(edx-nowx) <= 1000:
                return 'happy'
            for i in range(N):
                if visited[i] == 0:  # 아직 방문하지 않은 편의점일때
                    sy, sx = store[i]  # 편의점 위치
                    # 현재 위치로부터 편의점 위치가 1000미터 이내라면 그 편의점까지 갈 수 있음
                    if abs(sy-nowy) + abs(sx-nowx) <= 1000:
                        q.append((sy, sx))
                        visited[i] = 1
        # while문 다 돌때까지 리턴하지 않으면 도착하지 않은 것
        return 'sad'

    print(bfs())

