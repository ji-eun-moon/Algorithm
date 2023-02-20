def calc(a, b, sign):
    if sign == '+':
        result = a + b
    elif sign == '*':
        result = a * b
    elif sign == '/':
        result = a // b
    elif sign == '-':
        result = a - b
    return result


T = int(input())
for test_case in range(1, T + 1):
    lst = list(input().split())
    stack = []
    sign = ['/', '*', '+', '-']
    answer = 'error'
    for s in lst:
        if s.isdigit():
            stack.append(s)
        elif s in sign:
            if len(stack) == 0 or len(stack) == 1:
                break
            b = stack.pop()
            a = stack.pop()
            if a in sign or b in sign:
                break
            result = calc(int(a), int(b), s)
            stack.append(result)
        elif s == '.':
            if len(stack) == 1:
                answer = stack[-1]
            else:
                break

    print(f'#{test_case} {answer}')