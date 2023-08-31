import math

# 소수 판별 함수
def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

def solution(numbers):
    number_lst = list(numbers)
    N = len(number_lst)
    prime_dic = {}
    used = [0]*N
    def dfs(level, number):

        if level > 0:
            new_number = int(number)
            if new_number != 0 and new_number != 1:
                if isPrime(new_number):
                    prime_dic.setdefault(new_number, 0)
                    prime_dic[new_number] += 1

        if level == N:
            return

        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                dfs(level+1, number+number_lst[i])
                used[i] = 0
    dfs(0, '')
    return len(prime_dic)

