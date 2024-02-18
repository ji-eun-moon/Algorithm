# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

class Solution:
    def findSubstring(self, s, words):
        answer = []
        word_len = len(words[0])
        total_len = word_len * len(words)

        # 단어 개수
        words_count = {}
        for word in words:
            words_count.setdefault(word, 0)
            words_count[word] += 1

        for i in range(word_len):
            left = i
            right = i
            current_count = {}

            while right + word_len <= len(s):
                # 현재 단어는 오른쪽 기준으로 구분
                current_word = s[right:right+word_len]
                # 현재 단어 만들고 right은 단어 크기만큼 이동
                right += word_len

                # 현재 윈도우 내 단어 수 업데이트
                current_count.setdefault(current_word, 0)
                current_count[current_word] += 1

                # 현재 단어가 전체 words 내의 단어 수보다 많으면
                # left 를 오른쪽으로 이동하며 윈도우 축소
                # 없는 키 값에 대해서는 0 반환하도록 get 사용
                while current_count.get(current_word, 0) > words_count.get(current_word, 0):
                    left_word = s[left:left+word_len]
                    left += word_len
                    current_count[left_word] -= 1

                # 현재 윈도우의 총 길이가 모든 단어들의 총 길이와 같다면
                # 현재 윈도우의 시작 인덱스를 결과 리스트에 추가
                if right - left == total_len:
                    answer.append(left)

        return answer

class Solution:
    def findSubstring(self, s, words):
        answer = []
        word_len = len(words[0])
        total_len = word_len * len(words)

        # 단어 개수
        words_count = {}
        for word in words:
            words_count.setdefault(word, 0)
            words_count[word] += 1

        # 현재 윈도우 내 단어 카운트 확인
        # left = 시작점
        for left in range(0, len(s)-total_len+1):
            current_count = {}

            for right in range(left, left+total_len, word_len):
                current_word = s[right: right+word_len]

                current_count.setdefault(current_word, 0)
                current_count[current_word] += 1

            # 카운트 횟수가 같으면 시작 인덱스를 정답 리스트에 추가
            if current_count == words_count:
                answer.append(left)

        return answer



solve = Solution()
print(solve.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(solve.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
print(solve.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))