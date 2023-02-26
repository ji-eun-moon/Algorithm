
# 가위바위보 승자가리기
def RSP(A, B):
    # 1 가위 2 바위 3 보
    if lst[A] == lst[B]:  # 무승부일경우
        return A  # 앞 인덱스가 승자
    elif abs(lst[A] - lst[B]) == 1:  # 1 차이 나면
        if lst[A] > lst[B]:  # 숫자 큰사람이 이김
            return A
        else:
            return B
    else:  # 2차이 나면
        if lst[A] < lst[B]:  # 숫자 작은 사람이 이김
            return A
        else:
            return B

def game(start, end):
    if start == end:  # 한명 남으면
        return start
    # 범위를 둘로 나누어 게임 진행
    a = game(start, (start+end)//2)
    b = game((start+end)//2+1, end)
    return RSP(a, b)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    winner = game(0, N-1) + 1  # 인덱스 번호가 1 부터 시작하므로 1 더하기
    print(f'#{test_case} {winner}')