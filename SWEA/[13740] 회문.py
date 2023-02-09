# M 길이 만큼의 단어가 뒤집었을 때와 같을 경우 그 단어를 반환
# 가로줄에서 회문 찾는 함수
def Hcheck(a, b):
    word = ''
    for k in range(M):
        word += lst[a][b+k]
    if word == word[::-1]:
        return word
    else:
        return 0

# 세로줄에서 회문 찾는 함수
def Vcheck(a, b):
    word = ''
    for k in range(M):
        word += lst[a+k][b]
    if word == word[::-1]:
        return word
    else:
        return 0

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    lst = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            if Hcheck(i, j) != 0:
                ans = Hcheck(i, j)
                break
            if Vcheck(j, i) != 0:
                ans = Vcheck(j, i)
                break

    print(f'#{test_case} {ans}')