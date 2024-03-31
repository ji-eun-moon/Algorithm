import math

N = int(input())  # 시험장의 개수
A = list(map(int, input().split()))  # 각 시험장에 있는 응시자의 수
B, C = map(int, input().split())  # 총 감독관이 한 시험장에서 감시할 수 있는 응시자 수, 부감독관이 한 시험장에서 감시할 수 있는 응시자 수
answer = N  # 필요한 감독관 수의 최솟값

'''
총 감독관은 각 반에 1명 => N
남은 학생수에 대해서 부감독관이 필요
'''

for a in A:
    if a - B > 0:  # 부감독관이 필요한 경우에만
        # # 올림 처럼 계산 하기 : C - 1 을 더한 다음 C 로 나누면 됨
        # tmp = a - B + C - 1
        # answer += (tmp // C)
        answer += math.ceil((a-B)/C)

print(answer)

