# T = int(input())
#
# for test_case in range(1, T+1):
#     N, L = map(int, input().split())  # 재료 수, 제한 칼로리
#     used = [0]*N
#     food = []
#     for _ in range(N):
#         T, K = map(int, input().split())  # 맛 점수, 칼로리
#         food.append([T, K])
#
#     Max = 0
#     def dfs(level, T_sum, K_sum):
#         global Max
#         if K_sum > L:
#             return
#         if level == N:
#             return
#         Max = max(Max, T_sum)
#         for i in range(N):
#             if used[i] == 0:
#                 used[i] = 1
#                 dfs(level+1, T_sum+food[i][0], K_sum+food[i][1])
#                 used[i] = 0
#
#     dfs(0, 0, 0)
#     print(f'#{test_case} {Max}')
#

T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())  # 재료 수, 제한 칼로리

    food = []
    for _ in range(N):
        T, K = map(int, input().split())  # 맛 점수, 칼로리
        food.append([T, K])
    T = [0]*N  # 점수 부분집합
    K = [0]*N  # 칼로리 부분집합
    Max = 0
    def dfs(level, start):
        global Max
        if level == N:  # 전부다 확인하면 return
            return
        for i in range(start, N):
            T[level] = food[i][0]
            K[level] = food[i][1]
            # 부분집합 만들 때마다 확인하고 제한 칼로리 이하이면 맛 최대 점수 갱신
            if sum(K) <= L:
                Max = max(Max, sum(T))
            # 다른 집합 만들러 가기
            dfs(level+1, i+1)
            T[level] = 0
            K[level] = 0

    dfs(0, 0)
    print(f'#{test_case} {Max}')