# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s, t):
        answer = ""

        # t 길이가 s 길이보다 긴 경우 답을 찾을 수 없음
        if len(s) < len(t):
            return answer

        need_alpha = {}  # 필요한 알파벳의 종류와 개수
        for w in t:
            need_alpha.setdefault(w, 0)
            need_alpha[w] += 1
        required_chars = len(need_alpha)

        start, end = 0, 0
        Min = float('inf')

        while end < len(s):
            # 필요한 알파벳 업데이트
            if s[end] in need_alpha:
                need_alpha[s[end]] -= 1
                if need_alpha[s[end]] == 0:
                    required_chars -= 1

            # 알파벳 모두 찾은 경우
            while required_chars == 0:
                # 부분 문자열 갱신
                word = s[start:end+1]
                if len(word) < Min:
                    Min = len(word)
                    answer = word

                # start 포인터가 필요한 알파벳인 경우
                if s[start] in need_alpha:
                    need_alpha[s[start]] += 1
                    if need_alpha[s[start]] > 0:
                        required_chars += 1

                # start 포인터 이동
                start += 1

            # end 포인터 이동
            end += 1

        return answer

solve = Solution()
print(solve.minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(solve.minWindow(s = "a", t = "a"))
print(solve.minWindow(s = "aa", t = "aa"))
