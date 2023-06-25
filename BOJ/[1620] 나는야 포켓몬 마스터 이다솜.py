import sys
input=sys.stdin.readline

N, M = map(int, input().split())

dic = dict()

for i in range(1, N+1):
    name = input().rstrip()
    dic[i] = name
    dic[name] = i

for _ in range(M):
    problem = input().rstrip()
    if problem.isalpha():
        print(dic[problem])
    else:
        print(dic[int(problem)])
