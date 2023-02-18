lst = []  # 난쟁이 키 리스트

for _ in range(9):  # 난쟁이 키 입력받기
      lst.append(int(input()))

sum = 0  # 아홉 난쟁이 키 합을 구하고
for i in range(9):
      sum += lst[i]

target = sum - 100  # 합에서 100을 빼면 스파이 난쟁이 키의 합이 나온다.

for i in range(9):
      a = lst[i]
      for j in range(i+1, 9):
            b = lst[j]
            if a + b == target:  # 두 난쟁이 합이 타겟과 같으면
                  lst.remove(a)  # 난쟁이 리스트에서 제거하고
                  lst.remove(b)
                  break
      if len(lst) == 7:  # 일곱 난쟁이가 되었으면
            break  # 더이상 반복문 실행 x


lst.sort(reverse=True)
for a in lst:
      print(a)