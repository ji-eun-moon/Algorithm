# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s):

        if len(s) % 2:
            return False

        open_par = { "{" : "}", "(":")", "[": "]"}
        close_par = {"}":"{", ")":"(", "]":"["}

        stack = []
        for w in s:
            # 열린 괄호이면 스택에 담기
            if w in open_par:
                stack.append(w)
            # 닫힌 괄호이면 짝 검사
            else:
                if stack and close_par[w] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True

solve = Solution()
print('#1', solve.isValid("()"))
print('#2', solve.isValid("()[]{}"))
print('#3', solve.isValid("(]"))
print('#4', solve.isValid("([}}])"))