# 풀이중
import sys
sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for test_case in range(1, T+1):
#     V, E = map(int, input().split())
#
#     arr = [[0]*V for _ in range(V)]
#
#     for _ in range(E):
#         A, B = map(int, input().split())
#         arr[A-1][B-1] = 1
#         arr[B-1][A-1] = 1
#
#     S, G = map(int, input().split())
#     used = [0]*V
#     cnt = 0
#     Min = 21e8
#     def abc(now):
#         global cnt, Min
#         if now == G-1:
#             if Min > cnt:
#                 Min = cnt
#             return
#         for i in range(V):
#             if arr[now][i] == 1 and used[i] == 0:
#                 used[i] = 1
#                 cnt += 1
#                 abc(i)
#                 cnt -= 1
#                 used[i] = 0
#                 if cnt > Min:
#                     return
#
#     abc(S-1)
#     print(f'#{test_case} {Min}')

from collections import deque

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0]*V for _ in range(V)]

    for _ in range(E):
        A, B = map(int, input().split())
        arr[A-1][B-1] = 1
        # arr[B-1][A-1] = 1

    S, G = map(int, input().split())
    used = [0]*V
    cnt = 0
    answer = 0
    def bfs(st):
        global cnt, answer
        q = deque()
        q.append(st)
        used[st] = 1
        while q:
            now = q.popleft()
            if now == G-1:
                return
            for i in range(V):
                if arr[now][i] == 1 and used[i] == 0:
                    used[i] = 1
                    cnt += 1
                    q.append(i)

    bfs(S-1)
    print(f'#{test_case} {cnt}')