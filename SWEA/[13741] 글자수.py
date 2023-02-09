T = int(input())
for test_case in range(1, T + 1):
    str1 = list(set(input()))  # str1 알파벳 중복 제거
    str2 = list(input())
    Max = 0
    for i in range(len(str1)):
        cnt = str2.count(str1[i])  # str1 알파벳을 str2에서 찾고
        if Max < cnt:  # 그 수가 Max 값보다 크면
            Max = cnt  # Max 갱신
    print(f'#{test_case} {Max}')