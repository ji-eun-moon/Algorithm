T = int(input())
for test_case in range(1, T+1):
       N = int(input())
       arr = [list(map(int, input().split())) for _ in range(N)]

       used = [0]*N
       Sum = 0
       Min = 21e8
       def abc(level):
              global Min, Sum
              if level == N:  # 마지막 행까지 가면
                     if Min > Sum:  # 최소값 갱신
                            Min = Sum
                     return
              for i in range(N):
                     if used[i] == 0:  # 사용한적 없는 세로줄이면
                            used[i] = 1  # 사용 체크
                            Sum += arr[level][i]  # 합 구하기
                            abc(level+1)
                            used[i] = 0
                            Sum -= arr[level][i]
                            if Min < Sum:
                                   return

       abc(0)

       print(f'#{test_case} {Min}')