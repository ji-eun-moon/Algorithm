class Solution:
    def updateBoard(self, board, click):
        N = len(board)
        M = len(board[0])
        y, x = click
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]

        # 누른 곳이 지뢰일 경우
        if board[y][x] == 'M':
            board[y][x] = 'X'
            return board

        # 8방향의 지뢰를 카운트 하는 함수
        def getMinesCount(y, x):
            cnt = 0
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if board[ny][nx] == 'M':
                        cnt += 1
            return cnt

        def dfs(y, x):

            if board[y][x] == 'E':
                minesCount = getMinesCount(y, x)
                # 주변에 지뢰가 없는 E를 누를 경우
                if minesCount == 0:
                    # B로 바꾸고 인접한 칸 재귀적으로 확인
                    board[y][x] = 'B'
                    for i in range(8):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= ny < N and 0 <= nx < M:
                            dfs(ny, nx)
                else:
                    # 주번에 지뢰가 있는 E를 누를 경우 - 지뢰 수로 값 변경
                    board[y][x] = str(minesCount)

        dfs(y, x)

        return board


solve = Solution()
print(solve.updateBoard(board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]))
print(solve.updateBoard(board=[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))