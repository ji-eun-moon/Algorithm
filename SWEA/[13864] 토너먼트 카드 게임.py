# 풀이중
# 가위바위보 승자가리기
def RSP(A, B):
    # 1 가위 2 바위 3 보
    if lst[A] == lst[B]:  # 무승부일경우
        winner = A  # 앞 인덱스가 승자
    elif abs(lst[A] - lst[B]) == 1:  # 1 차이 나면
        if lst[A] > lst[B]:  # 숫자 큰사람이 이김
            winner = A
        else:
            winner = B
    else:  # 2차이 나면
        if lst[A] < lst[B]:  # 숫자 작은 사람이 이김
            winner = A
        else:
            winner = B
    return winner

def game(start, end):
    if start == end:
        return

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    print(f'#{test_case} {winner}')