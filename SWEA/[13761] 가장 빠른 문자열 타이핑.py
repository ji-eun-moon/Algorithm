def check(idx):  # B가 있는지 확인하는 함수
    for i in range(len(B)):
        if A[idx+i] != B[i]:
            return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    A, B = input().split()

    cnt = 0  # 타이핑 횟수
    j = 0  # 타이핑 위치
    while j < len(A):  # 끝까지 타이핑하면 반복문 종료
        if j < (len(A)-len(B)+1):  # B가 존재할수 있는 범위 내에서
            if check(j):
                j += len(B)  # B가 존재하면 타이핑 위치를 B길이 만큼 뒤로 이동
            else:
                j += 1  # 존재하지 않으면 한칸만 이동
        else:
            j += 1  # B가 존재할수 없는 경우 한칸씩만 이동
        cnt += 1  # 이동할 때마다 카운트 추가

    print(f'#{test_case} {cnt}')
