T = 10
for test_case in range(1, T+1):
       N, st = input().split()
       lst = list(st)

       while True:
              a = -1
              for i in range(len(lst)-1):
                     if lst[i] == lst[i+1]:  # 연속해서 같은 숫자 있으면
                            a = lst.pop(i)  # 제거하고 a에 값 저장
                            a = lst.pop(i)
                            break
              if a == -1:  # a 값 변화 없으면 같은 숫자 없는 것이므로 반복문 종료
                     break

       result = ''.join(lst)
       print(f'#{test_case} {result}')