
# def fibo(x):
#     global zero, one
#     if x == 0:
#         zero += 1
#         return 0
#     elif x == 1:
#         one += 1
#         return 1
#     return fibo(x-1) + fibo(x-2)
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     zero, one = 0, 0
#     fibo(n)
#     print(zero, one)


T = int(input())
for _ in range(T):
    n = int(input())

    # 호출되는 0과 1의 개수를 저장하는 리스트 초기화
    count = [[0, 0] for _ in range(max(n + 1, 2))]

    # 초기값 설정
    count[0] = [1, 0]  # f(0) 호출 개수
    count[1] = [0, 1]  # f(1) 호출 개수

    # 동적 계획법을 사용하여 f(0)과 f(1) 호출 개수 계산
    for i in range(2, n + 1):
        count[i][0] = count[i - 1][0] + count[i - 2][0]  # f(i) = f(i-1) + f(i-2)
        count[i][1] = count[i - 1][1] + count[i - 2][1]

    print(count[n][0], count[n][1])

