N = int(input())
lst = list(map(int, input().split()))
Max = 0  # 최대 길이
d = [0]*len(lst)  # 오름차순 리스트 숫자 확인 표시
d2 = [0]*len(lst)  # 내림차순 리스트 숫자 확인 표시

# 오름차순인 수열 확인하기
for i in range(len(lst)):
    temp_A = [lst[i]]
    if d[i] != 0:  # 이미 확인했던 숫자 이면 continue
        continue
    for j in range(i, len(lst)-1):
        if lst[j+1] >= lst[j]:  # 뒤에 수가 앞의 수보다 크거나 같으면
            temp_A.append(lst[j+1])  # 오름차순 리스트에 append
            d[j] = 1  # 확인한 숫자는 표시
        else:  # 작은 숫자가 나오면 break
            break
    if Max < len(temp_A):  # 최대 길이 갱신
        Max = len(temp_A)

# 내림차순인 수열 확인하기
for i in range(len(lst)):
    temp_D = [lst[i]]
    if d2[i] != 0:  # 이미 확인했던 숫자 이면 continue
        continue
    for j in range(i, len(lst)-1):
        if lst[j+1] <= lst[j]:  # 뒤에 수가 앞의 수보다 작거나 같으면
            temp_D.append(lst[j+1])  # 오름차순 리스트에 append
            d2[j] = 1  # 확인한 숫자는 표시
        else:
            break
    if Max < len(temp_D):  # 최대 길이 갱신
        Max = len(temp_D)
print(Max)
