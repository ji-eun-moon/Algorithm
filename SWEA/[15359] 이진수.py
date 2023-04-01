T = int(input())

for test_case in range(1, T+1):
    N, num = input().split()
    N = int(N)
    num = list(num)

    n_16 = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
            '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}


    def binary(decimal):
        if decimal == 0:
            return '0'
        elif decimal == 1:
            return '1'

        if decimal % 2 == 0:
            return binary(decimal//2) + '0'
        else:
            return binary(decimal//2) + '1'

    answer = ''
    for i in range(N):
        temp = binary(n_16[num[i]])
        while len(temp) < 4:
            temp = '0' + temp
        answer += temp


    print(f'#{test_case} {answer}')
