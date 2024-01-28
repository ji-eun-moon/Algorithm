# from collections import deque
#
# def can_move(robo1, robo2, new_board):
#     y, x = 0, 1
#     temp = []
#     # 평행이동
#     for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
#         n_robo1 = (robo1[y] + iy, robo1[x] + ix)
#         n_robo2 = (robo2[y] + iy, robo2[x] + ix)
#         if new_board[n_robo1[y]][n_robo1[x]] == 0 and new_board[n_robo2[y]][n_robo2[x]] == 0:
#             temp.append((n_robo1, n_robo2))
#
#     # 회전
#     if robo1[y] == robo2[y]:  # 가로 방향
#         # 위 쪽이 비어있을 때
#         if new_board[robo1[y] - 1][robo1[x]] == 0 and new_board[robo2[y] - 1][robo2[x]] == 0:
#             temp.append((robo1, (robo1[y]-1, robo1[x])))
#             temp.append(((robo2[y]-1, robo2[x]), robo2))
#         # 아래쪽이 비어있을 때
#         if new_board[robo1[y]+1][robo1[x]] == 0 and new_board[robo2[y]+1][robo2[x]] == 0:
#             temp.append((robo1, (robo1[y]+1, robo1[x])))
#             temp.append(((robo2[y]+1, robo2[x]), robo2))
#     else:  # 세로 방향
#         # 왼쪽이 비었을 때
#         if new_board[robo1[y]][robo1[x] - 1] == 0 and new_board[robo2[y]][robo2[x] - 1] == 0:
#             temp.append((robo1, (robo1[y], robo1[x]-1)))
#             temp.append(((robo2[y], robo2[x]-1), robo2))
#         # 오른쪽이 비어있을 때
#         if new_board[robo1[y]][robo1[x] + 1] == 0 and new_board[robo2[y]][robo2[x] + 1] == 0:
#             temp.append((robo1, (robo1[y], robo1[x]+1)))
#             temp.append(((robo2[y], robo2[x]+1), robo2))
#
#     return temp
# def solution(board):
#     N = len(board)
#     # board 패딩 작업
#     new_board = [[1] * (N + 2) for _ in range(N + 2)]
#     for i in range(N):
#         for j in range(N):
#             new_board[i + 1][j + 1] = board[i][j]
#
#     q = deque()
#     visited = set()
#     q.append(((1, 1), (1, 2), 0))  # 로봇 각 위치, cnt
#     visited.add(((1, 1), (1, 2)))
#
#     while q:
#         robo1, robo2, cnt = q.popleft()
#         # 둘 중 하나라도 도착하면
#         if robo1 == (N, N) or robo2 == (N, N):
#             return cnt
#         for nxt in can_move(robo1, robo2, new_board):
#             if nxt not in visited:
#                 q.append((nxt[0], nxt[1], cnt + 1))
#                 visited.add(nxt)


from collections import deque

def can_move(robo1, robo2, new_board):
    y, x = 0, 1
    temp = []
    # 평행이동
    for iy, ix in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        n_robo1 = (robo1[y] + iy, robo1[x] + ix)
        n_robo2 = (robo2[y] + iy, robo2[x] + ix)
        if new_board[n_robo1[y]][n_robo1[x]] == 0 and new_board[n_robo2[y]][n_robo2[x]] == 0:
            temp.append((n_robo1, n_robo2))

    # 회전
    if robo1[y] == robo2[y]:  # 가로 방향
        for d in (-1, 1):
            if new_board[robo1[y] + d][robo1[x]] == 0 and new_board[robo2[y] +d][robo2[x]] == 0:
                temp.append((robo1, (robo1[y]+d, robo1[x])))
                temp.append(((robo2[y]+d, robo2[x]), robo2))
    else:  # 세로 방향
        for d in (-1, 1):
            if new_board[robo1[y]][robo1[x] + d] == 0 and new_board[robo2[y]][robo2[x] + d] == 0:
                temp.append((robo1, (robo1[y], robo1[x]+d)))
                temp.append(((robo2[y], robo2[x]+d), robo2))

    return temp
def solution(board):
    N = len(board)
    # board 패딩 작업
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = set()
    q.append(((1, 1), (1, 2), 0))  # 로봇 각 위치, cnt
    visited.add(((1, 1), (1, 2)))

    while q:
        robo1, robo2, cnt = q.popleft()
        # 둘 중 하나라도 도착하면
        if robo1 == (N, N) or robo2 == (N, N):
            return cnt
        for nxt in can_move(robo1, robo2, new_board):
            if nxt not in visited:
                q.append((nxt[0], nxt[1], cnt + 1))
                visited.add(nxt)
