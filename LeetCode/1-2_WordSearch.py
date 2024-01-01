# https://leetcode.com/problems/word-search/

# 4213 ms
class Solution:
    def exist(self, board, word):
        N = len(board)  # 가로
        M = len(board[0])  # 세로

        def wordSearch(y, x, level, new_word):

            # word 글자 수 만큼 단어를 만들었으면, 단어가 같은지 확인
            if level == len(word) - 1:
                return word == new_word

            # level 번째 글자가 다르면 가지치기
            if word[level] != board[y][x]:
                return False

            # DFS로 단어 만들기
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        if wordSearch(ny, nx, level+1, new_word+board[ny][nx]):
                            return True
                        visited[ny][nx] = False

        for i in range(N):
            for j in range(M):
                # 첫 글자가 같은 경우에만 dfs 실행
                if board[i][j] == word[0]:
                    visited = [[False]*M for _ in range(N)]
                    visited[i][j] = True
                    if wordSearch(i, j, 0, board[i][j]):
                        return True

        # True 리턴하지 못했으면 False 리턴
        return False

result = Solution()
print(result.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(result.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
print(result.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))


