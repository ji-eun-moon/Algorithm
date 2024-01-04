class Solution:
    def getPermutation(self, n, k) -> str:

        path = []
        used = [0]*n
        nums = list(range(1, n+1))
        result = []
        def dfs(level):
            if level == n:
                result.append(path[:])
                return
            for i in range(n):
                if used[i] == 0:
                    used[i] = 1
                    path.append(nums[i])
                    dfs(level + 1)
                    used[i] = 0
                    path.pop()

        dfs(0)

        answer = ''
        for w in result[k-1]:
            answer += str(w)

        return answer

class Solution:
    def getPermutation(self, n, k) -> str:

        # factorial 배열 생성
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        # k 값 조정 - k 번째 숫자를 찾기 위해
        k -= 1

        result = []
        nums = list(range(1, n + 1))

        for i in range(n - 1, -1, -1):  # 가장 큰 자리 숫자(첫번째 숫자)부터 차례대로 찾기
            index = k // factorial[i]  # 현재 자리에 올 숫자의 인덱스 구하기
            k %= factorial[i]  # 남은 경우의 수
            result.append(nums.pop(index))  # 현재 자리에 올 숫자 추가 하기

        answer = ''.join(map(str, result))

        return answer

solve = Solution()
print(solve.getPermutation(n = 3, k = 3))
print(solve.getPermutation(n = 4, k = 9))
print(solve.getPermutation(n = 3, k = 1))