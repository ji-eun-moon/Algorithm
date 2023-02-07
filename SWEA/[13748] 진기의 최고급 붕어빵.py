import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time = sorted(arrive_time)

    result = 'Possible'
    # 손님이 도착한 시간에 만들 수 있는 붕어빵 개수가 필요한 붕어빵개수보다 작을 경우 Impossible
    for i in range(N):
        make = (arrive_time[i]//M) * K
        if make - (i+1) < 0:
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')