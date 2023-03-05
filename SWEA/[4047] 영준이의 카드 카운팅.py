# 내 풀이
T = int(input())
for test_case in range(1, T+1):
    # S, D, H, C
    S = {}
    D = {}
    H = {}
    C = {}
    flag = 0
    answer = [13, 13, 13, 13]
    lst = list(input())
    N = len(lst)
    for i in range(N//3):
        card = lst.pop(0)
        number = int(lst.pop(0))*10 + int(lst.pop(0))
        if card == 'S':
            S.setdefault(number, 0)
            if S[number] != 0:
                flag = 1
                break
            S[number] += 1
            answer[0] -= 1
        elif card == 'D':
            D.setdefault(number, 0)
            if D[number] != 0:
                flag = 1
                break
            D[number] += 1
            answer[1] -= 1
        elif card == 'H':
            H.setdefault(number, 0)
            if H[number] != 0:
                flag = 1
                break
            H[number] += 1
            answer[2] -= 1
        elif card == 'C':
            C.setdefault(number, 0)
            if C[number] != 0:
                flag = 1
                break
            C[number] += 1
            answer[3] -= 1

    print(f'#{test_case}', end=' ')
    if flag == 1:
        print('ERROR')
    else:
        print(*answer)

# 교수님 풀이
dic = {'S':0, 'D':1, 'H':2, 'C':3}
T = int(input())
for test_case in range(1, T+1):
    st = input()
    arr = [[] for _ in range(4)]

    for i in range(0, len(st), 3):
        arr[dic[st[i]]].append(int(st[i+1:i+3]))

    ans = []
    for lst in arr:
        if len(lst) != len(set(lst)):  # 오류
            print(f'#{test_case} ERROR')
            break
        ans.append(13-len(lst))
    else:
        print(f'#{test_case}', *ans)