# 풀이중
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # 화덕 크기, 피자 개수
    cheese = list(map(int, input().split()))  # 피자에 뿌려진 치즈의 양
