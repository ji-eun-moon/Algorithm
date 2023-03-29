T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())  # 노드 수, 리프 노드 수, 출력할 노드 번호
    lst = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        lst[a] = b


    for i in range(N):
        lst[(N-i)//2] += lst[N-i]

    print(f'#{test_case} {lst[L]}')