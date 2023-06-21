N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

def solution():
    stack = []
    now = 1
    answer = ''
    for i in range(N):
        # 현재 수열 값이 자연수보다 크거나 같으면
        if A[i] >= now:
            # 자연수 1씩 증가시키며 자연수를 스택에 push
            while A[i] >= now:
                stack.append(now)
                now += 1
                answer += '+\n'
            # 마지막 숫자 pop
            stack.pop()
            answer += '-\n'
        # 현재 수열 값이 자연수 보다 작으면
        else:
            # 스택에 있는 값 꺼내고
            n = stack.pop()
            # 그 값이 수열 값보다 크면 NO
            if n > A[i]:
                return 'NO'
            else:
                answer += '-\n'
    return answer

print(solution())

