def change(a, b, color):
    cnt = 0
    for i in range(a, b+1):
        cnt += (M-arr[i].count(color))
    return cnt

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]




    print(f'#{test_case} {answer}')
