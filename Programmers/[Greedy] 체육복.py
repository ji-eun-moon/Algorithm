def solution(n, lost, reserve):
    # 기본적으로 1개의 체육복을 가지고 있다.
    student = [1]*(n+2)

    # 인덱스 에러 방지
    student[0], student[n+1] = 0, 0

    # 여벌의 체육복을 가져온 사람
    for i in reserve:
        student[i] = 2

    # 잃어버린 사람
    for i in lost:
        student[i] -= 1

    for i in range(1, n+1):
        # 체육복이 없으면 빌릴 수 있는지 확인하고 빌리기
        if student[i] == 0:
            if student[i-1] == 2:
                student[i] = 1
                student[i-1] = 1
            elif student[i+1] == 2:
                student[i] = 1
                student[i+1] = 1

    answer = 0
    for s in student:
        if s > 0:
            answer += 1

    return answer
복