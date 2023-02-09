# str2에서 str1 찾는 함수
def find(idx):
    for k in range(N):
        if str2[idx+k] != str1[k]:
            return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    cnt = 0
    for i in range(M-N+1):
        if find(i):
            cnt += 1

    print(f'#{test_case} {cnt}')