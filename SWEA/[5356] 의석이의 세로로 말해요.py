# 내 풀이
T = int(input())
for test_case in range(1, T+1):
    text = [list(input()) for _ in range(5)]

    for a in text:
        if len(a) < 15:
            for i in range(15-len(a)):
                a.insert(len(a), -1)

    text = list(map(list, zip(*text)))

    print(f'#{test_case}', end=' ')
    for a in text:
        for b in a:
            if b != -1:
                print(b, end='')
    print()

# 교수님 풀이
T = int(input())
for test_case in range(1, T+1):

    arr = [input() for _ in range(5)]
    ans = ''
    for j in range(15):  # 문자열 최대 길이
        for i in range(5):  # 단어 5개 탐색 - arr[i] : 단어
            if j < len(arr[i]):  # j 인덱스가 단어 길이보다 짧은 경우에만
                ans += arr[i][j]  # 정답에 더하기
    print(f'#{test_case} {ans}')

# try - except 사용하기
T = int(input())
for test_case in range(1, T+1):

    arr = [input() for _ in range(5)]
    ans = ''
    for j in range(15):  # 문자열 최대 길이
        for i in range(5):  # 단어 5개 탐색
            try:
                ans += arr[i][j]  # 정답에 더하기
            except:
                pass
    print(f'#{test_case} {ans}')