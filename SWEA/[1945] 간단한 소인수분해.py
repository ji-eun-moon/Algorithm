T = int(input())
for test_case in range(1, T + 1):
    num = [2, 3, 5, 7, 11]
    N = int(input())
    ans = [0]*5
    for i in range(5):
        if N % num[i] == 0:
            while True:
                N = N / num[i]
                ans[i] += 1
                if N % num[i] != 0:
                    break
    print(f'#{test_case}', end=' ')
    for i in ans:
        print(i, end=' ')
    print()