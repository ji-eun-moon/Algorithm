# 풀이중

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())  # 노드개수, 간선개수

    arr = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):  # 간선 정보
        A, B = map(int, input().split())
        arr[A][B] = 1
        arr[B][A] = 1

    S, G = map(int, input().split())  # 출발, 도착 노드

    cnt = 0
    def bfs(st):
        global cnt
        q = []
        visited = [0] * (V + 1)
        q.append(st)
        visited[st] = 1
        while q:
            now = q.pop(0)
            if now == G:
                return visited[G]-1
            for i in range(V+1):
                if arr[now][i] == 1 and visited[i] == 0:
                    visited[i] += visited[now] + 1
                    q.append(i)
        return 0


    print(f'#{test_case} {bfs(S)}')