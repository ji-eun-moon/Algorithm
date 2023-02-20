T = 10
for test_case in range(1, T+1):
       tc = int(input())
       A, B = map(int, input().split())

       result = 1
       def gop(A, now):
              global result
              if now == B:
                     return
              result *= A
              gop(A, now+1)

       gop(A, 0)

       print(f'#{test_case} {result}')