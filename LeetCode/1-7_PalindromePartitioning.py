# https://leetcode.com/problems/palindrome-partitioning/description/
# 922 ms
class Solution:
    def partition(self, s):

        # 회문인지 확인하는 함수 - O(n)
        def check(word):
            return word == word[::-1]

        result = []  # 회문으로만 구성된 리스트들을 담을 결과 리스트
        part = []  # 회문으로만 구성된 리스트
        N = len(s)
        def dfs(start):
            # 단어 끝까지 확인했으면 전부 다 회문인 것이므로, 결과 리스트에 넣기
            if start == N:
                result.append(part[:])
                return
            for end in range(start, N):
                # 단어 자르기
                word = s[start:end+1]
                # 회문인 경우에만 추가
                if check(word):
                    part.append(word)
                    # 앞에서 확인한 글자의 다음 글자부터 확인
                    dfs(end+1)
                    part.pop()

        dfs(0)
        return result

solve = Solution()
print(solve.partition(s = "aab"))
print(solve.partition(s = "a"))

# 474 ms
class Solution:
    def partition(self, s):

        # 회문인지 확인하는 함수 - O(n)
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        result = []  # 회문으로만 구성된 리스트들을 담을 결과 리스트
        part = []  # 회문으로만 구성된 리스트
        N = len(s)
        def dfs(start):
            # 단어 끝까지 확인했으면 전부 다 회문인 것이므로, 결과 리스트에 넣기
            if start == N:
                result.append(part[:])
                return
            for end in range(start, N):
                # 단어 자르기
                word = s[start:end+1]
                # 회문인 경우에만 추가
                if check(start, end):
                    part.append(word)
                    # 앞에서 확인한 글자의 다음 글자부터 확인
                    dfs(end+1)
                    part.pop()

        dfs(0)
        return result

solve = Solution()
print(solve.partition(s = "aab"))
print(solve.partition(s = "a"))