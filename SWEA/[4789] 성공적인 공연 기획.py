T = int(input())

for test_case in range(1, T+1):

    lst = list(map(int, input()))

    emp = 0  # 고용한 사람수
    clap = lst[0]  # 박수 치고 있는 사람 수

    idx = 1  # 인덱스 1 부터 확인
    while True:
        if idx == len(lst):  # 끝까지 다 확인했으면 break
            break
        if clap >= idx:  # 박수치고 있는 사람이 충분하면
            clap += lst[idx]  # 박수칠 사람 수 더하기
            idx += 1  # 다음 인덱스로 넘어감
        else:  # 충분하지 않으면
            emp += 1  # 고용인 + 1
            clap += 1  # 박수치는 사람 + 1

    print(f'#{test_case} {emp}')