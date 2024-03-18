N = int(input())
data = list(map(int, input().split()))  # 주어진 수열을 저장하는 변수

if N == 1:  # 숫자가 1개만 주어지면 뒤에 올 수는 모든 숫자가 가능
    print('A')

elif N == 2:
    if data[0] == data[1]:  # 숫자가 2개만 주어졌을 때, 두 숫자가 같으면 다음 숫자는 무조건 같음.
        print(data[0])
    else:  # 숫자가 2개만 주어졌을 때, 두 숫자가 다르다면 뒤에 올 수는 모든 숫자가 가능.
        print('A')

else:  # 숫자가 3개 이상 주어졌을 때
    if data[0] == data[1]:  # 기울기의 분모가 0이 되버리는 경우 예외처리
        a = 0
    else:
        a = (data[2] - data[1]) // (data[1] - data[0])  # 기울기

    b = data[1] - data[0] * a  # y절편

    # a와 b를 통해 예측값과 실제값을 비교
    for i in range(N - 1):
        expect = data[i] * a + b  # 다음 예측값
        if (data[i + 1] != expect):  # 예측값과 다르다면 구할 수 없는 경우
            print('B')
            exit()

    print(data[-1] * a + b)  # 다음 예측값