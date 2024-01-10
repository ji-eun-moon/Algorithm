# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures):
        N = len(temperatures)
        answer = [0] * N

        stack = []
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day = stack.pop()[0]
                answer[prev_day] = day - prev_day
            stack.append((day, temp))

        return answer

solve = Solution()
print('#1', solve.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
print('#2', solve.dailyTemperatures(temperatures = [30,40,50,60]))
print('#3', solve.dailyTemperatures(temperatures = [30,60,90]))