T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())  # 상자 개수, 변경 횟수
    box = [0]*N
    for i in range(1, Q+1):
        L, R = map(int, input().split())  # 상자 변경 범위
        for j in range(L-1, R):
            box[j] = i
    print(f'#{test_case}', end=' ')
    print(*box)