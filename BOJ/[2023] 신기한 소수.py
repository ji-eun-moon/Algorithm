import math

N = int(input())

# 소수 판별하기
def is_prime_number(num):
    # 2부터 num의 제곱근까지 확인
    for i in range(2, int(math.sqrt(num))+1):
        # num이 해당 수로 나누어 떨어지면
        if num % i == 0:
            return False  # 소수가 아님
    return True

def dfs(number):
    # 자리수가 N이 되면 출력
    if len(str(number)) == N:
        print(number)
        return
    # 1 ~ 10 까지 반복
    for i in range(1, 10):
        new_number = number * 10 + i
        # 자리수 추가한 숫자가 소수이면 dfs 탐색
        if is_prime_number(new_number):
            dfs(new_number)

# 한자리 소수에 대하여 dfs 진행
for i in range(2, 10):
    if is_prime_number(i):
        dfs(i)