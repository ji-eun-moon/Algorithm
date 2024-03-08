# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        max_length, start = 0, 0

        # 문자: 문자 인덱스 딕셔너리
        substr = {}

        for end in range(len(s)):
            # 끝점의 문자가 부분문자열에 포함되어 있으면
            if s[end] in substr:
                # 끝점 문자열의 이전 인덱스 앞으로 시작점을 옮김
                start = max(start, substr[s[end]]+1)

            # 인덱스 업데이트
            substr[s[end]] = end

            # 최대 길이 업데이트
            max_length = max(end - start + 1, max_length)

        return max_length