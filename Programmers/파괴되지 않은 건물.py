def solution(board, skill):
    answer = 0
    m = len(board[0])
    n = len(board)
    acc = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # 누적합 기록
    for option, r1, c1, r2, c2, degree in skill:
        effect = degree if option == 2 else -degree
        acc[r1][c1] += effect
        acc[r1][c2+1] -= effect
        acc[r2+1][c1] -= effect
        acc[r2+1][c2+1] += effect

    # 행 기준 누적합
    for i in range(n):
        for j in range(m):
            acc[i][j+1] += acc[i][j]

    # 열 기준 누적합
    for j in range(m):
        for i in range(n):
            acc[i+1][j] += acc[i][j]

    # board에 반영, 정답 체크
    for i in range(n):
        for j in range(m):
            board[i][j] += acc[i][j]
            if board[i][j] >= 0:
                answer += 1

    return answer