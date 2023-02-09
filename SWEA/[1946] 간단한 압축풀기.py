T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')

    N = int(input())
    lst = [list(input().split()) for _ in range(N)]
    file = []

    # 압축 풀어 file 리스트에 프린트할 알파벳 전부 담기
    for i in range(N):
        file.extend(lst[i][0]*int(lst[i][1]))

    # 반복문 수행할 횟수
    cnt = len(file)//10 + bool(len(file)%10)

    for i in range(cnt):
        if len(file) > 10:  # 파일 길이가 10보다 클 경우
            for _ in range(10):  # 10개씩 프린트하고 프린트한 알파벳 삭제
                print(file[0], end='')
                file.pop(0)
            print()
        elif len(file) <= 10:  # 파일 길이가 10 이하일 경우
            for i in file:  # 그대로 프린트
                print(i, end='')
    print()