# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)

        # 작업의 수가 일수보다 적으면 일정을 완료할 수 없음
        if n < d:
            return -1

        # dp 배열 초기화
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # 아무 작업도 없는 경우 난이도는 0

        # 현재 날짜에서 수행할 작업의 범위
        for i in range(1, n + 1):
            for j in range(1, d + 1):
                max_difficulty = 0  # 현재까지 작업 중에서 최대 난이도
                dp[i][j] = float('inf')  # 최소 난이도를 나타내는 dp 배열 초기화

                # i 번째 작업부터 역순으로 이전 작업들을 확인
                for k in range(i - 1, j - 2, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[k])
                    # 최소 난이도 갱신
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + max_difficulty)

        # 최종 결과 반환
        result = dp[n][d]
        print(dp)

        # 결과가 무한대인 경우 작업을 완료할 수 없으므로 -1 반환
        return result if result != float('inf') else -1

# import itertools
#
# class Solution:
#     def minDifficulty(self, jobDifficulty, d):
#         n = len(jobDifficulty)
#
#         # 작업의 수가 일수보다 적으면 일정을 완료할 수 없음
#         if n < d:
#             return -1
#
#         # 각 구간의 최대 난이도의 합 계산하기
#         def cal_max(combi):
#             Sum = 0
#             start, end = 0, 0
#
#             for end in combi:
#                 Sum += max(jobDifficulty[start:end])
#                 start = end
#
#             Sum += max(jobDifficulty[end:])
#             return Sum
#
#         # 구간을 나눌 지점의 조합
#         combis = list(itertools.combinations(range(1, n), d - 1))
#
#         result = float('inf')
#
#         # 각 조합의 결과 최소값 구하기
#         for combi in combis:
#             result = min(result, cal_max(combi))
#
#         # 결과가 무한대인 경우 작업을 완료할 수 없으므로 -1 반환
#         return result if result != float('inf') else -1

solve = Solution()
print(solve.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))
print(solve.minDifficulty(jobDifficulty = [9,9,9], d = 4))
print(solve.minDifficulty(jobDifficulty = [1,1,1], d = 3))