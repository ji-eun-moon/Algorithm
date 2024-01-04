# https://leetcode.com/problems/n-queens/submissions/
class Solution:
    def solveNQueens(self, n):

        # arr[r] = c -> r행 c열에 퀸이 있음
        arr = [0] * n
        result = []
        board = [["."] * n for _ in range(n)]

        # 퀸 자리가 유효한지 체크하는 함수
        def queen(r):
            for i in range(r):
                # 세로 체크(열이 같을 때)
                if arr[i] == arr[r]:
                    return 0
                # 대각선 체크(행 차이와 열 차이가 같을 때)
                if abs(r - i) == abs(arr[r] - arr[i]):
                    return 0
            return 1

        # r 행에 퀸을 놓는 함수
        def dfs(r):
            if r == n:
                temp = ["".join(row) for row in board]
                result.append(temp)
                return
            for i in range(n):
                arr[r] = i  # r행 i열에 퀸을 놓기
                if queen(r) == 1:  # 해당 자리에 놓을 수 있다면
                    # 퀸을 놓기
                    board[r][i] = 'Q'
                    dfs(r + 1)  # 다음행으로 넘어가기
                    board[r][i] = '.'

        dfs(0)

        return result


solve = Solution()
print(solve.solveNQueens(1))
print(solve.solveNQueens(4))