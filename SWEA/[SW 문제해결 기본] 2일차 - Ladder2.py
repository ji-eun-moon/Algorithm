T = 10
for test_case in range(1, T + 1):
   tc = int(input())
   ladder = [list(map(int, input().split())) for _ in range(100)]

   st = []  # 시작점 리스트
   for i in range(100):
       if ladder[0][i] == 1:
           st.append(i)

   direct_y = [0, 0, 1]
   direct_x = [-1, 1, 0]
   cnt_lst = []
   for i in range(len(st)):
       arr = [lst[:] for lst in ladder]  # 사다리 배열 깊은 복사
       cnt = 0
       y = 0
       x = st[i]
       while True:
           if y == 99:
               cnt_lst.append(cnt)
               break
           flag = 0
           for k in range(3):
               dy = y + direct_y[k]
               dx = x + direct_x[k]
               if 0 <= dy < 100 and 0 <= dx < 100:
                   if arr[dy][dx] == 1:
                       y = dy
                       x = dx
                       arr[dy][dx] = 0  # 지나온 자리 다시 가지 않도록 0으로 바꾸기
                       cnt += 1
                       flag = 1
                       break
           if flag == 0:  # 주위에 1이 없을 경우 break
               cnt_lst.append(0)
               break

   Min = 21e8
   for i in range(len(cnt_lst)):  # cnt 리스트에서 최소값 인덱스 찾고
       if cnt_lst[i] != 0 and cnt_lst[i] <= Min:
           Min = cnt_lst[i]
           Minst = st[i]  # 찾은 인덱스로 시작점 좌표 찾기

   print(f'#{tc} {Minst}')