T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    dic = {}  # 숫자 담을 딕셔너리
    cnt = 1
    while True:
        if len(dic) == 10:  # 딕셔너리에 0~9 숫자가 모두 담기면 break
            break
        sheep = list(str(cnt * N))  # 양이 가지고 있는 숫자 리스트
        for i in range(len(sheep)):  # 숫자리스트를 딕셔너리에 담기
            dic.setdefault(sheep[i], 0)
            dic[sheep[i]] += 1
        cnt += 1
    answer = (cnt-1) * N  # 시작할떄 cnt가 1부터 시작했으므로 1빼고 곱해야함
    print(f'#{test_case} {answer}')
