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

    def bfs():
        q = deque()
        v = [0]*N
        q.append((sty, stx))

        while q:
            y, x = q.popleft()
            if abs(edy-y) + abs(edx-x) <= 1000:
                return 'happy'
            for i in range(N):
                if v[i] == 0:
                    sy, sx = store[i]
                    # 50 미터 당 1 병 -> 20병은 1000미터 갈 수 있음
                    if abs(sy-y) + abs(sx-x) <= 1000:
                        q.append((sy, sx))
                        v[i] = 1

        return 'sad'

    print(bfs())

