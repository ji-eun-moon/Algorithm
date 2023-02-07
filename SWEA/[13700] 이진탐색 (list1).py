T = int(input())

for test_case in range(1, T + 1):

    P, Pa, Pb = map(int, input().split())

    # target을 탐색할때 이진탐색을 수행한 횟수를 반환하는 함수
    def bs(st, ed, target):
        cnt = 1
        while True:
            mid = int((st+ed)/2)
            if target == mid:
                return cnt
            elif target > mid:
                st = mid
                cnt += 1
            elif target < mid:
                ed = mid
                cnt += 1
    # 함수를 이용하여 각각 탐색 수행 횟수를 변수에 저장
    A = bs(1, P, Pa)
    B = bs(1, P, Pb)
    # 횟수 적은 쪽이 win
    if A < B:
        ans = 'A'
    elif A > B:
        ans = 'B'
    else:
        ans = 0

    print(f'#{test_case} {ans}')