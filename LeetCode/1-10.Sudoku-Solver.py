class Solution:
    def solveSudoku(self, board):
        # 가로 확인
        def checkW(x, n):
            for i in range(9):
                if str(n) == board[x][i]:
                    return False
            return True


        # 세로 확인
        def checkH(y, n):
            for i in range(9):
                if str(n) == board[i][y]:
                    return False
            return True

        # 3*3 사각형 확인
        def checkRect(y, x, n):
            ny = y // 3 * 3
            nx = x // 3 * 3
            for i in range(3):
                for j in range(3):
                    if str(n) == board[ny+i][nx+j]:
                        return False
            return True

        def dfs(n):
            # 스도쿠의 빈 칸을 전부 채웠다면 함수 종료
            if n == len(blank):
                return True

            # 빈칸에 1부터 9까지 넣어본다.
            for i in range(1, 10):
                y = blank[n][0]  # 빈칸의 y좌표
                x = blank[n][1]  # 빈칸의 x좌표

                if checkW(y, i) and checkH(x, i) and checkRect(y, x, i):
                    board[y][x] = str(i)
                    if dfs(n + 1):
                        return True
                    board[y][x] = '.'

        blank = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blank.append([i, j])  # 빈 칸의 [y, x] 좌표

        dfs(0)

        print(board)


solve = Solution()
print(solve.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))