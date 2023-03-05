# Solution 1
T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 전치행렬로 변환해서 행단위로 처리
    arr = list(map(list, zip(*arr)))

    # 1 다음에 2 있으면 교착
    # 2번 찾고, 직전이 1번이면 ans += 1
    ans = 0
    for lst in arr:
        prev = 0
        for n in lst:
            if n != 0:
                if n == 2 and prev == 1:
                    ans += 1
                prev = n

    print(f'#{test_case} {ans}')

# Solution 2
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    # 전치행렬로 변환해서 행단위로 처리
    arr = list(map(list, zip(*arr)))

    ans = 0
    for st in arr:
        ans += "".join(st).replace('0', '').count('12')

    print(f'#{test_case} {ans}')

