T = int(input())
for test_case in range(1, T+1):
       N = int(input())
       arr = [list(input()) for _ in range(N)]

       for i in range(N):
              if arr[N-1][i] == '2':
                     sty = N-1
                     stx = i

       used = [[0]*N for _ in range(N)]
       direct_y = [-1, 1, 0, 0]
       direct_x = [0, 0, -1, 1]
       result = 0
       def miro(y, x):
              global result
              if arr[y][x] == '3':
                     result = 1
                     return
              for i in range(4):
                     dy = y + direct_y[i]
                     dx = x + direct_x[i]
                     if 0 <= dy < N and 0 <= dx < N:
                            if arr[dy][dx] != '1' and used[dy][dx] == 0:
                                   used[dy][dx] = 1
                                   miro(dy, dx)
                                   used[dy][dx] = 0
       miro(sty, stx)
       print(f'#{test_case} {result}')