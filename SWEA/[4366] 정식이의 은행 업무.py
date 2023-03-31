# 2진수를 10진수로 변경하기
def bin_to_dec(num):
    decimal = 0
    for i in range(len(num)):
        decimal += num[i]*(2**i)
    return decimal

# 3진수를 10진수로 변경하기
def tri_to_dec(num):
    decimal = 0
    for i in range(len(num)):
        decimal += num[i]*(3**i)
    return decimal

T = int(input())

for test_case in range(1, T+1):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))

    # 10진수로 바꿀때 편하게 하기 위해서 리스트 뒤집기
    binary = binary[::-1]
    trinary = trinary[::-1]

    # 2진수 숫자 하나씩 바꾸면서 가능한 10진수 숫자 리스트에 담기
    lst1 = []
    b = [0, 1]
    for i in range(len(binary)):
        temp = binary[:]
        for j in range(2):
            temp[i] = b[j]
            lst1.append(bin_to_dec(temp))

    # 3진수 숫자 하나씩 바꾸면서 가능한 10진수 숫자 리스트에 담기
    lst2 = []
    t = [0, 1, 2]
    for i in range(len(trinary)):
        temp = trinary[:]
        for j in range(3):
            temp[i] = t[j]
            lst2.append(tri_to_dec(temp))

    # lst1, lst2 비교하면서 같은 숫자가 있는지 확인 -> 있다면 그것이 답
    for num in lst1:
        if num in lst2:
            answer = num
            break

    print(f'#{test_case} {answer}')