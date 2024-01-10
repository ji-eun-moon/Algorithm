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

class Solution:
    def isValid(self, s):
        stack = []
        for p in s:  # O(n)
            if p == "{":
                stack.append("}")
            elif p == "[":
                stack.append("]")
            elif p == "(":
                stack.append(")")
            elif stack and stack[-1] == p:
                stack.pop()
            else:
                return False
        # 마지막에는 스택이 비어있어야 한다.
        return not stack

solve = Solution()
print('#1', solve.isValid("()"))
print('#2', solve.isValid("()[]{}"))
print('#3', solve.isValid("(]"))
print('#4', solve.isValid("([}}])"))