T = int(input())
for test_case in range(1, T+1):
       result = 1
       S = input()
       stack = []
       for s in S:
              if s == '(' or s == '{':
                     stack.append(s)
              elif s == ')':
                     if len(stack) == 0 or stack[-1] != '(':
                            result = 0
                            break
                     else:
                            stack.pop()
              elif s == '}':
                     if len(stack) == 0 or stack[-1] != '{':
                            result = 0
                            break
                     else:
                            stack.pop()

       if stack:
              result = 0

       print(f'#{test_case} {result}')