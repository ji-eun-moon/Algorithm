T = int(input())

for test_case in range(1, T + 1):

    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 찾을 패턴 만들기
    Klst = [1] * K
    pattern = [0, *Klst, 0]

    # 주어진 배열 0으로 둘러 싸기
    arr.insert(0, [0] * N)
    arr.insert(len(arr), [0] * N)
    for i in range(N + 2):
        arr[i].insert(0, 0)
        arr[i].insert(len(arr[i]), 0)

    # 가로줄에서 패턴 찾는 함수
    def Gcheck(i, j):
        for a in range(K + 2):
            if arr[i][j + a] != pattern[a]:
                return 0
        return 1

    # 세로줄에서 패턴 찾는 함수
    def Scheck(i, j):
        for a in range(K + 2):
            if arr[j + a][i] != pattern[a]:
                return 0
        return 1

    ans = 0
    # 가로줄에서 패턴 개수 세기
    for i in range(N + 2):
        for j in range(N - K + 1):
            if Gcheck(i, j):
                ans += 1

    # 세로줄에서 패턴 개수 세기
    for i in range(N + 2):
        for j in range(N - K + 1):
            if Scheck(i, j):
                ans += 1

    print(f'#{test_case} {ans}')
