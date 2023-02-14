def findG(y, x):  # 가로에서 회문 찾아 길이 반환하는 함수
    word = ''
    ret = 0
    for i in range(x, 100):
        word += arr[y][i]
        if word == word[::-1]:
            if len(word) > ret:
                ret = len(word)
    return ret

def findS(y, x):  # 세로에서 회문 찾아 길이 반환하는 함수
    word = ''
    ret = 0
    for i in range(y, 100):
        word += arr[i][x]
        if word == word[::-1]:
            if word == word[::-1]:
                if len(word) > ret:
                    ret = len(word)
    return ret

T = 10
for test_case in range(1, T + 1):
    tc = int(input())

    arr = [list(input()) for _ in range(100)]

    ans = 0
    for i in range(100):
        for j in range(100):
            if ans < findG(i, j):  # 가로줄에서 제일 긴 회문 찾기
                ans = findG(i, j)
            if ans < findS(j, i):  # 세로줄에서 제일 긴 회문 찾기
                ans = findS(j, i)

    print(f'#{tc} {ans}')