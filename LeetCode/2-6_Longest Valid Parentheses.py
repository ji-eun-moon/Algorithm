class Solution:
    def longestValidParentheses(self, s):
        answer = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    answer = max(answer, i - stack[-1])
                else:
                    stack.append(i)

        return answer

solve = Solution()
print('#1', solve.longestValidParentheses("(()"))
print('#2', solve.longestValidParentheses(")()())"))
print('#3', solve.longestValidParentheses(""))