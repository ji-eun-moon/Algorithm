T = int(input())
for test_case in range(1, T+1):

    lst = list(input())

    while True:
        flag = 0
        for i in range(0, len(lst)-1):
            if lst[i] == lst[i+1]:  # 연속된 문자의 경우
                flag = 1  # flag 1 켜두고
                lst[i], lst[i+1] = 0, 0   # 인덱스 번호에 영향주지 않기 위해 삭제 대신 둘다 0으로 바꾼다.
                lst = [a for a in lst if a != 0]  # 0을 제외한 나머지 원소가 새로운 리스트
                break  # 한번 문자열 삭제했으면 다시 처음부터 비교 시작
        if flag == 0 or len(lst) == 1:  # 리스트 순회 했는데도 flag가 0이면 연속된 문자가 없는 것이므로 반복문 종료
            break

    answer = len(lst)

    print(f'#{test_case} {answer}')