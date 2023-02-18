T = int(input())

for test_case in range(1, T+1):

      V, E = map(int, input().split())

      arr = [[0]*V for _ in range(V)]

      for i in range(E):
            A, B = map(int, input().split())
            arr[A-1][B-1] = 1

      S, G = map(int, input().split())
      used = [0]*V
      flag = 0
      def dfs(now):
            global flag
            if now == G-1:
                  flag = 1
                  return
            for i in range(V):
                  if arr[now][i] == 1 and used[i]==0:
                        used[i] = 1
                        dfs(i)
                        used[i] = 0
      used[S-1] = 0
      dfs(S-1)
      if flag == 1:
            result = 1
      else:
            result = 0

      print(f'#{test_case} {result}')