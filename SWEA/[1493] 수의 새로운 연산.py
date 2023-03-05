dic = {}
r_dic = {}
i, j = 1, 1
for n in range(1, 10002):
    dic[n] = (i, j)
    r_dic[(i, j)] = n
    i, j = i-1, j+1
    if i < 1:
        i, j = j, 1

T = int(input())
for test_case in range(1, T+1):
    p, q = map(int, input().split())

    # p, q 값을 좌표로 변환
    pi, pj = dic[p]
    qi, qj = dic[q]

    answer = r_dic[(pi+qi, pj+qj)]
    print(f'#{test_case} {answer}')

